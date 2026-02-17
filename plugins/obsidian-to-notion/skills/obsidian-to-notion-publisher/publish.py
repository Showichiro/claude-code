#!/usr/bin/env python3
"""Obsidian → Notion 直接パブリッシュ

convert.py で Notion Markdown に変換後、Notion API で直接ページ作成/更新する。
LLM を介さず数秒で完了。

Usage:
    python publish.py <file> --parent <page_id_or_url>   # 新規作成
    python publish.py <file> --update <page_id_or_url>   # 置換更新
    python publish.py <file> --append <page_id_or_url>   # 末尾追記
    python publish.py <file> --parent <url> --dry-run     # JSON出力のみ
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from convert import convert

NOTION_API = "https://api.notion.com/v1"
NOTION_VER = "2022-06-28"
BATCH = 100


# ──────────────────────────────────────
# Notion API
# ──────────────────────────────────────


def api(method, path, body=None):
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        sys.exit("Error: NOTION_API_KEY が設定されていません")
    req = urllib.request.Request(
        f"{NOTION_API}{path}",
        data=json.dumps(body).encode() if body else None,
        method=method,
    )
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Notion-Version", NOTION_VER)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode()
        sys.exit(f"Notion API {e.code}: {body_text}")


# ──────────────────────────────────────
# ユーティリティ
# ──────────────────────────────────────


def page_id(url_or_id):
    """URL or ID → UUID形式に変換"""
    clean = url_or_id.split("?")[0].replace("-", "")
    m = re.search(r"([0-9a-f]{32})$", clean)
    if not m:
        sys.exit(f"Invalid page ID/URL: {url_or_id}")
    h = m.group(1)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"


def color_to_api(c):
    """convert.py の色名 → Notion API 形式"""
    if c and c.endswith("_bg"):
        return c.replace("_bg", "_background")
    return c or "default"


def extract_title(text, filepath):
    """H1見出しをタイトルとして抽出、本文から除去"""
    m = re.match(r'^#\s+(.+?)(?:\s*\{color="[^"]*"\})?\s*\n', text)
    if m:
        return m.group(1).strip(), text[m.end() :].lstrip("\n")
    return Path(filepath).stem, text


# ──────────────────────────────────────
# Rich Text パーサー
# ──────────────────────────────────────


def rt(content, bold=False, italic=False, code=False, strike=False, color=None, link=None):
    """Notion rich_text オブジェクト生成"""
    o = {
        "type": "text",
        "text": {"content": content[:2000]},
        "annotations": {
            "bold": bold,
            "italic": italic,
            "strikethrough": strike,
            "underline": False,
            "code": code,
            "color": color or "default",
        },
    }
    if link:
        o["text"]["link"] = {"url": link}
    return o


def parse_rt(text):
    """インラインマークダウン → Notion rich_text 配列"""
    if not text or not text.strip():
        return [rt("")]
    result = []
    pos = 0
    while pos < len(text):
        # <span color="x">**bold**</span>
        m = re.match(r'<span color="(\w+)">\*\*(.+?)\*\*</span>', text[pos:])
        if m:
            result.append(rt(m.group(2), bold=True, color=m.group(1)))
            pos += m.end()
            continue
        # **bold**
        m = re.match(r"\*\*(.+?)\*\*", text[pos:])
        if m:
            result.append(rt(m.group(1), bold=True))
            pos += m.end()
            continue
        # *italic* (not **)
        m = re.match(r"(?<!\*)\*([^*]+?)\*(?!\*)", text[pos:])
        if m:
            result.append(rt(m.group(1), italic=True))
            pos += m.end()
            continue
        # `code`
        m = re.match(r"`([^`]+?)`", text[pos:])
        if m:
            result.append(rt(m.group(1), code=True))
            pos += m.end()
            continue
        # ~~strike~~
        m = re.match(r"~~(.+?)~~", text[pos:])
        if m:
            result.append(rt(m.group(1), strike=True))
            pos += m.end()
            continue
        # [text](url)
        m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", text[pos:])
        if m:
            result.append(rt(m.group(1), link=m.group(2)))
            pos += m.end()
            continue
        # プレーンテキスト: 次のマーカーまで
        next_pos = len(text)
        for marker in ["<span", "**", "`", "~~", "["]:
            idx = text.find(marker, pos + 1)
            if 0 < idx < next_pos:
                next_pos = idx
        # 単独 * (italic) のチェック
        idx = pos + 1
        while idx < next_pos:
            if text[idx] == "*" and (idx + 1 >= len(text) or text[idx + 1] != "*"):
                if idx > 0 and text[idx - 1] != "*":
                    next_pos = idx
                    break
            idx += 1
        result.append(rt(text[pos:next_pos]))
        pos = next_pos
    return result or [rt("")]


# ──────────────────────────────────────
# Block パーサー
# ──────────────────────────────────────


def to_blocks(text):
    """Notion-flavored markdown → Notion API blocks"""
    lines = text.split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # 空行 → 空パラグラフとして保持
        if not line.strip():
            blocks.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": []},
                }
            )
            i += 1
            continue

        # コードブロック
        if line.startswith("```"):
            lang = line[3:].strip() or "plain text"
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # closing ```
            code_text = "\n".join(code_lines)
            segments = []
            for start in range(0, len(code_text), 2000):
                segments.append({"type": "text", "text": {"content": code_text[start : start + 2000]}})
            blocks.append(
                {
                    "object": "block",
                    "type": "code",
                    "code": {"rich_text": segments, "language": lang},
                }
            )
            continue

        # Callout
        m = re.match(r'^<callout color="(\w+)">', line)
        if m:
            clr = color_to_api(m.group(1))
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "</callout>":
                c = lines[i][1:] if lines[i].startswith("\t") else lines[i]
                body.append(c)
                i += 1
            if i < len(lines):
                i += 1  # </callout>
            first_line = body[0] if body else ""
            children = []
            for bl in body[1:]:
                if bl.strip():
                    children.append(
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {"rich_text": parse_rt(bl)},
                        }
                    )
            cb = {
                "object": "block",
                "type": "callout",
                "callout": {"rich_text": parse_rt(first_line), "color": clr},
            }
            if children:
                cb["callout"]["children"] = children
            blocks.append(cb)
            continue

        # テーブル
        if line.startswith("|"):
            table_rows = []
            while i < len(lines) and lines[i].startswith("|"):
                table_rows.append(lines[i])
                i += 1
            data_rows = [r for r in table_rows if not re.match(r"^\|[\s\-:|]+\|$", r)]
            if data_rows:
                parsed = []
                for row in data_rows:
                    cells = [c.strip() for c in row.strip("|").split("|")]
                    parsed.append(cells)
                width = max(len(r) for r in parsed)
                row_blocks = []
                for cells in parsed:
                    while len(cells) < width:
                        cells.append("")
                    row_blocks.append(
                        {
                            "object": "block",
                            "type": "table_row",
                            "table_row": {"cells": [parse_rt(c) for c in cells]},
                        }
                    )
                blocks.append(
                    {
                        "object": "block",
                        "type": "table",
                        "table": {
                            "table_width": width,
                            "has_column_header": True,
                            "children": row_blocks,
                        },
                    }
                )
            continue

        # 見出し (色付き)
        m = re.match(r'^(#{1,3})\s+(.+?)\s*\{color="(\w+)"\}\s*$', line)
        if m:
            lvl = len(m.group(1))
            key = f"heading_{lvl}"
            color = m.group(3)
            rich_texts = parse_rt(m.group(2))
            for r in rich_texts:
                r["annotations"]["color"] = color
            blocks.append(
                {
                    "object": "block",
                    "type": key,
                    key: {"rich_text": rich_texts, "color": color},
                }
            )
            i += 1
            continue

        # 見出し (色なし)
        m = re.match(r"^(#{1,3})\s+(.+)$", line)
        if m:
            lvl = len(m.group(1))
            key = f"heading_{lvl}"
            blocks.append(
                {
                    "object": "block",
                    "type": key,
                    key: {"rich_text": parse_rt(m.group(2)), "color": "default"},
                }
            )
            i += 1
            continue

        # To-do
        m = re.match(r"^[-*]\s+\[([ xX/])\]\s+(.*)", line)
        if m:
            blocks.append(
                {
                    "object": "block",
                    "type": "to_do",
                    "to_do": {
                        "rich_text": parse_rt(m.group(2)),
                        "checked": m.group(1).lower() == "x",
                    },
                }
            )
            i += 1
            continue

        # 番号付きリスト
        m = re.match(r"^\d+\.\s+(.*)", line)
        if m:
            blocks.append(
                {
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {"rich_text": parse_rt(m.group(1))},
                }
            )
            i += 1
            continue

        # 箇条書き
        m = re.match(r"^[-*]\s+(.*)", line)
        if m:
            blocks.append(
                {
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": parse_rt(m.group(1))},
                }
            )
            i += 1
            continue

        # 引用
        m = re.match(r"^>\s?(.*)", line)
        if m:
            blocks.append(
                {
                    "object": "block",
                    "type": "quote",
                    "quote": {"rich_text": parse_rt(m.group(1))},
                }
            )
            i += 1
            continue

        # 区切り線
        if re.match(r"^[-*_]{3,}\s*$", line):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            i += 1
            continue

        # パラグラフ
        blocks.append(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": parse_rt(line)},
            }
        )
        i += 1
    return blocks


# ──────────────────────────────────────
# ページ操作
# ──────────────────────────────────────


def create_page(parent, title, blocks):
    """新規ページ作成"""
    first, rest = blocks[:BATCH], blocks[BATCH:]
    r = api(
        "POST",
        "/pages",
        {
            "parent": {"page_id": parent},
            "properties": {"title": [{"text": {"content": title}}]},
            "children": first,
        },
    )
    pid = r["id"]
    while rest:
        batch, rest = rest[:BATCH], rest[BATCH:]
        api("PATCH", f"/blocks/{pid}/children", {"children": batch})
    return pid


def replace_page(target, blocks):
    """既存ページの内容を置換"""
    r = api("GET", f"/blocks/{target}/children?page_size=100")
    for b in r.get("results", []):
        api("DELETE", f"/blocks/{b['id']}")
    while r.get("has_more"):
        r = api(
            "GET",
            f"/blocks/{target}/children?page_size=100&start_cursor={r['next_cursor']}",
        )
        for b in r.get("results", []):
            api("DELETE", f"/blocks/{b['id']}")
    rem = blocks
    while rem:
        batch, rem = rem[:BATCH], rem[BATCH:]
        api("PATCH", f"/blocks/{target}/children", {"children": batch})
    return target


def append_page(target, blocks):
    """既存ページの末尾にブロックを追加"""
    rem = blocks
    while rem:
        batch, rem = rem[:BATCH], rem[BATCH:]
        api("PATCH", f"/blocks/{target}/children", {"children": batch})
    return target


# ──────────────────────────────────────
# メイン
# ──────────────────────────────────────


def main():
    p = argparse.ArgumentParser(description="Obsidian → Notion publisher")
    p.add_argument("file", help="Obsidian markdown ファイルパス")
    p.add_argument("--parent", help="親ページ ID/URL（新規作成）")
    p.add_argument("--update", help="更新先ページ ID/URL（置換）")
    p.add_argument("--append", help="追記先ページ ID/URL（末尾に追加）")
    p.add_argument("--dry-run", action="store_true", help="API呼び出しせずJSON出力")
    a = p.parse_args()

    if not a.parent and not a.update and not a.append:
        sys.exit("Error: --parent（新規）/ --update（置換）/ --append（追記）のいずれかが必要です")

    with open(a.file, encoding="utf-8") as f:
        raw = f.read()

    converted = convert(raw)
    title, content = extract_title(converted, a.file)
    blocks = to_blocks(content)

    print(f"Title: {title}")
    print(f"Blocks: {len(blocks)}")

    if a.dry_run:
        print(json.dumps(blocks[:3], ensure_ascii=False, indent=2))
        print(f"... ({len(blocks)} blocks total)")
        return

    if a.update:
        pid = page_id(a.update)
        replace_page(pid, blocks)
        print(f"Updated: https://notion.so/{pid.replace('-', '')}")
    elif a.append:
        pid = page_id(a.append)
        append_page(pid, blocks)
        print(f"Appended: https://notion.so/{pid.replace('-', '')}")
    else:
        pid = page_id(a.parent)
        new_id = create_page(pid, title, blocks)
        print(f"Created: https://notion.so/{new_id.replace('-', '')}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Obsidian Markdown → Notion Markdown 変換スクリプト

機械的な記法変換を処理し、LLMが解決すべき内部リンク等はプレースホルダーとして残す。

Usage:
    python convert.py <file_path>
    cat file.md | python convert.py
"""

import re
import sys

CALLOUT_COLORS = {
    "note": "blue_bg", "info": "blue_bg", "todo": "blue_bg",
    "abstract": "blue_bg", "summary": "blue_bg", "tldr": "blue_bg",
    "tip": "blue_bg", "hint": "blue_bg", "important": "blue_bg",
    "success": "green_bg", "check": "green_bg", "done": "green_bg",
    "question": "yellow_bg", "help": "yellow_bg", "faq": "yellow_bg",
    "warning": "orange_bg", "caution": "orange_bg", "attention": "orange_bg",
    "failure": "red_bg", "fail": "red_bg", "missing": "red_bg",
    "danger": "red_bg", "error": "red_bg", "bug": "red_bg",
    "example": "purple_bg",
    "quote": "gray_bg", "cite": "gray_bg",
}

HEADING_COLORS = {1: "red", 2: "yellow", 3: "green", 4: "blue", 5: "blue", 6: "purple"}


def remove_frontmatter(text: str) -> str:
    """YAML Frontmatter を削除"""
    return re.sub(r"\A---\n.*?\n---\n?", "", text, count=1, flags=re.DOTALL)


def remove_tags(text: str) -> str:
    """Obsidian タグを削除（行頭の # 見出しは除外）"""
    def replace_tag(m: re.Match) -> str:
        return m.group(1)

    return re.sub(r"(^|[ \t])#([^\s#][^\s]*)", replace_tag, text, flags=re.MULTILINE)


def convert_callouts(text: str) -> str:
    """Obsidian Callout を Notion callout に変換"""
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r"^>\s*\[!(\w+)\]\s*(.*)", lines[i])
        if m:
            callout_type = m.group(1).lower()
            title = m.group(2).strip()
            color = CALLOUT_COLORS.get(callout_type, "gray_bg")

            body_lines = []
            if title:
                body_lines.append(title)
            i += 1
            while i < len(lines) and re.match(r"^>\s?(.*)", lines[i]):
                content = re.match(r"^>\s?(.*)", lines[i]).group(1)
                body_lines.append(content)
                i += 1

            result.append(f'<callout color="{color}">')
            for line in body_lines:
                result.append(f"\t{line}")
            result.append("</callout>")
        else:
            result.append(lines[i])
            i += 1
    return "\n".join(result)


def convert_headings(text: str) -> str:
    """見出しに Tokyo Night テーマ色を適用。H4-H6 は H3 に変換"""

    def replace_heading(m: re.Match) -> str:
        hashes = m.group(1)
        content = m.group(2)
        level = len(hashes)
        color = HEADING_COLORS.get(level, "gray")
        notion_hashes = hashes if level <= 3 else "###"
        return f'{notion_hashes} {content} {{color="{color}"}}'

    return re.sub(r"^(#{1,6})\s+(.+)$", replace_heading, text, flags=re.MULTILINE)


def convert_bold(text: str) -> str:
    """太文字に blue 色を適用"""
    parts = re.split(r"(```[\s\S]*?```|`[^`]+`)", text)
    for i, part in enumerate(parts):
        if not part.startswith("`"):
            parts[i] = re.sub(
                r"\*\*(.+?)\*\*",
                r'<span color="blue">**\1**</span>',
                part,
            )
    return "".join(parts)


def convert_image_embeds(text: str) -> str:
    """画像埋め込みを注釈に変換"""
    return re.sub(
        r"!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|svg|webp|bmp))\]\]",
        r"[Image: \1]",
        text,
        flags=re.IGNORECASE,
    )


def convert_note_embeds(text: str) -> str:
    """ノート埋め込みをプレーンテキストに変換（画像以外の ![[xxx]]）"""
    return re.sub(
        r"!\[\[([^\]]+?)(?<!\.png)(?<!\.jpg)(?<!\.jpeg)(?<!\.gif)(?<!\.svg)(?<!\.webp)(?<!\.bmp)\]\]",
        r"[Embedded: \1]",
        text,
    )


def convert_internal_links(text: str) -> str:
    """内部リンクをプレーンテキストに変換"""
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    return text


def convert(text: str) -> str:
    """全変換を順番に適用"""
    text = remove_frontmatter(text)
    text = remove_tags(text)
    text = convert_callouts(text)
    text = convert_headings(text)
    text = convert_bold(text)
    text = convert_image_embeds(text)
    text = convert_note_embeds(text)
    text = convert_internal_links(text)
    return text


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    print(convert(text))


if __name__ == "__main__":
    main()

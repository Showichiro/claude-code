---
name: obsidian-to-notion-publisher
description: |-
  ObsidianファイルをNotionに直接パブリッシュする。
  「Notionに反映して」「Notionに同期して」「このページをNotionに」
  と言われたときに使用。Pythonスクリプトが変換からNotion API呼び出しまで
  一括処理するため、LLMはコマンド実行のみ。MCP不要・数秒で完了。
argument-hint: "[ファイルパス] [NotionページURL(省略可)]"
allowed-tools:
  - Read
  - Glob
  - Bash
  - AskUserQuestion
---

# Obsidian to Notion Publisher

ObsidianファイルをPythonスクリプトでNotionに直接パブリッシュする。
`publish.py` が変換からNotion API呼び出しまで一括処理するため、LLMはコマンド実行のみ。

## ワークフロー

```
1. ファイル特定
   └─ パス指定あり → 指定ファイルを使用
   └─ パス指定なし → 直前のRead対象を使用

2. 反映先特定
   └─ URL指定あり → そのまま使用
   └─ URL指定なし → ユーザーに確認

3. 反映方法を選択（AskUserQuestionで3択を提示）
   └─ 子ページとして新規作成 → --parent
   └─ 上書き（既存内容を置換） → --update
   └─ ページの下に挿入（末尾に追記） → --append

4. コマンド実行（1行で完了）
```

**重要: 反映方法は必ずユーザーに確認すること。勝手に上書きしない。**

## コマンド

```bash
SCRIPT_DIR="$(dirname "$0")"

# 子ページとして新規作成（親ページの子として）
python3 "$SCRIPT_DIR/publish.py" <ファイルパス> --parent <NotionページURL or ID>

# 上書き（既存ページの内容を置換）
python3 "$SCRIPT_DIR/publish.py" <ファイルパス> --update <NotionページURL or ID>

# ページの下に挿入（既存内容の末尾に追記）
python3 "$SCRIPT_DIR/publish.py" <ファイルパス> --append <NotionページURL or ID>

# dry-run（API呼び出しなし、ブロックJSON確認）
python3 "$SCRIPT_DIR/publish.py" <ファイルパス> --parent <URL> --dry-run
```

## 処理内容

`publish.py` は内部で以下を自動実行する:

1. `convert.py` でObsidian記法→Notion記法に変換
2. H1見出しをページタイトルとして抽出
3. Notion APIブロック形式にパース（見出し色、太文字色、Callout、テーブル等）
4. Notion APIで直接ページ作成/更新（100ブロック単位でバッチ処理）

### 対応する変換

| 変換 | 内容 |
|------|------|
| Frontmatter | 削除 |
| タグ (`#xxx`) | 削除 |
| Callout (`> [!type]`) | Notion calloutブロック（色はObsidian準拠） |
| 見出し (`#`〜`###`) | Tokyo Night色適用（H1:red, H2:yellow, H3:green）、H4-6はH3に変換 |
| 太文字 (`**xxx**`) | blue色の太字 |
| テーブル | Notion tableブロック |
| コードブロック | Notion codeブロック（言語指定対応） |
| 画像埋め込み | `[Image: xxx.png]` テキスト |
| 内部リンク | プレーンテキスト化 |

## 前提条件

- Python 3.8+（標準ライブラリのみ使用、追加パッケージ不要）
- 環境変数 `NOTION_API_KEY` が設定されていること
- 対象のNotionページにインテグレーションが接続されていること

## 既存コマンド版との違い

| 項目 | コマンド版（MCP方式） | スキル版（Python直接API方式） |
|------|----------------------|--------------------------|
| 変換 | LLMが記法変換を実行 | `convert.py`が機械的に変換 |
| API | Notion MCP経由 | `publish.py`が直接Notion API |
| 依存 | Notion MCPサーバー必須 | `NOTION_API_KEY`のみ |
| 速度 | LLMの推論が必要 | 数秒で完了 |
| 一貫性 | LLM依存で結果にばらつきあり | 決定論的で再現性が高い |

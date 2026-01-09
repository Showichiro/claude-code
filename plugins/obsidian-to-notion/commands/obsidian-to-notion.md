---
description: |-
  ObsidianのドキュメントをNotionに反映する。
  「Notionに反映して」「Notionに同期して」「このページをNotionに」
  と言われたときに使用。指定されたObsidianファイルを読み取り、
  Notion記法に変換して既存ページの更新または新規ページ作成を行う。
  プレビューを表示してから反映する。
allowed-tools:
  - Read
  - Glob
  - Grep
  - TodoRead
  - TodoWrite
  - AskUserQuestion
  - mcp__plugin_Notion_notion__notion-search
  - mcp__plugin_Notion_notion__notion-fetch
  - mcp__plugin_Notion_notion__notion-create-pages
  - mcp__plugin_Notion_notion__notion-update-page
---

# Obsidian to Notion

ObsidianファイルをNotion記法に変換してNotionに反映する。

## ワークフロー

```
1. ファイル特定
   └─ パス指定あり → 指定ファイルを使用
   └─ パス指定なし → 直前のRead対象を使用

2. 反映先特定
   └─ URL指定あり → 指定ページを使用
   └─ URL指定なし → Notionを検索 → 候補を提案

3. 新規 or 更新判定
   └─ 新規 → 親ページをユーザーに確認
   └─ 更新 → 「置換」or「追加」を選択

4. 記法変換
   └─ Obsidian記法 → Notion記法

5. 内部リンク解決
   └─ [[リンク]] → Notionで検索
       └─ 発見 → <mention-page>に変換
       └─ 未発見 → ユーザーに確認
           └─ 保存する → 再帰的に処理
           └─ 保存しない → プレーンテキスト化

6. プレビュー表示
   └─ 変換後のNotionコンテンツを表示

7. 反映実行
   └─ 新規 → notion-create-pages
   └─ 更新 → notion-update-page
```

## 記法変換ルール

| Obsidian | Notion | 備考 |
|----------|--------|------|
| `[[リンク]]` | `<mention-page url="...">` | 検索して対応ページがあればリンク化 |
| `[[リンク\|表示名]]` | `<mention-page url="...">表示名</mention-page>` | エイリアス対応 |
| `![[image.png]]` | `[Image: image.png]` | 画像は注釈として記載 |
| `![[note]]` | 内容を展開 or 注釈 | 埋め込みノートは確認後処理 |
| `#タグ` | 削除 | 完全削除 |
| Frontmatter | 削除 | YAML部分を完全削除 |

### Callout変換（色で区別）

| Obsidian | Notion |
|----------|--------|
| `> [!info]`, `> [!note]` | `<callout color="blue_bg">` |
| `> [!warning]`, `> [!caution]` | `<callout color="yellow_bg">` |
| `> [!danger]`, `> [!error]` | `<callout color="red_bg">` |
| `> [!tip]`, `> [!hint]` | `<callout color="green_bg">` |
| `> [!todo]`, `> [!success]`, `> [!check]` | `<callout color="green_bg">` |
| `> [!question]`, `> [!help]` | `<callout color="purple_bg">` |
| その他 | `<callout color="gray_bg">` |

### そのまま変換

| 記法 | 備考 |
|------|------|
| `# 見出し` | H1-H3はそのまま、H4-H6はH3に |
| `- [ ] タスク` | チェックボックスはそのまま |
| `- [ ] HH:MM - HH:MM タスク` | Day Planner形式もそのまま |
| `` ```language `` | コードブロック（言語指定含む） |
| `**太字**`, `*斜体*` | 基本書式はそのまま |
| `> 引用` | 通常の引用はそのまま |

## 変換関数

```
obsidian_to_notion(content):
  1. Frontmatterを削除（---で囲まれた部分）
  2. タグを削除（#xxx形式）
  3. Calloutを変換（> [!type] → <callout>）
  4. 内部リンクを抽出（[[xxx]]形式）
  5. 画像埋め込みを注釈に変換（![[xxx.png]]）
  6. ノート埋め込みを処理（![[xxx]]）
  7. 残りはそのまま出力
```

## MCPツール使用

### ページ検索
```
notion-search: {"query": "検索ワード"}
```

### ページ取得
```
notion-fetch: {"id": "ページURL or ID"}
```

### 新規ページ作成
```
notion-create-pages: {
  "parent": {"page_id": "親ページID"},
  "pages": [{
    "properties": {"title": "タイトル"},
    "content": "変換後のコンテンツ"
  }]
}
```

### ページ更新（置換）
```
notion-update-page: {
  "data": {
    "page_id": "ページID",
    "command": "replace_content",
    "new_str": "変換後のコンテンツ"
  }
}
```

### ページ更新（追加）
```
notion-update-page: {
  "data": {
    "page_id": "ページID",
    "command": "insert_content_after",
    "selection_with_ellipsis": "既存内容の末尾...",
    "new_str": "\n\n変換後のコンテンツ"
  }
}
```

## エラーハンドリング

- 変換できない要素はスキップして処理継続
- 最後にスキップした要素をリストアップして報告

## 参考資料

詳細なNotion Markdown仕様は [references/notion-markdown.md](../references/notion-markdown.md) を参照。

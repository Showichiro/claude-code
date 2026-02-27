---
description: |-
  ObsidianのVault内を検索する。
  「/obs-search <query> [options]」でノートを検索。
  query=, path=, limit=, total, case をサポート。
  search:context でマッチ行コンテキスト付き検索も可能。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-search

公式 Obsidian CLI を使用して Vault 内のノートを検索するコマンド。

## 使い方

```
/obs-search meeting                → "meeting" を含むファイルを検索
/obs-search meeting context        → マッチ行のコンテキスト付き
/obs-search meeting path=inbox     → inboxフォルダ内に限定
/obs-search meeting limit=5        → 5件まで
/obs-search meeting total          → 件数のみ
```

## 実行手順

```bash
# テキスト検索（ファイルパスを返す）
obsidian search query="検索ワード"

# フォルダ限定
obsidian search query="検索ワード" path=inbox

# 件数制限
obsidian search query="検索ワード" limit=5

# 件数のみ
obsidian search query="検索ワード" total

# 大文字小文字区別
obsidian search query="検索ワード" case

# コンテキスト付き検索（マッチ行を含む grep 形式出力）
obsidian search:context query="検索ワード"
obsidian search:context query="検索ワード" format=json

# 検索ビューを開く
obsidian search:open query="検索ワード"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| 結果なし | 検索ワードの変更を提案 |

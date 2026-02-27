---
description: |-
  Obsidianのノート内容を表示する。
  「/obs-print <note-name> [options]」でノート内容を標準出力に表示。
  file=, path=, vault= をサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-print

公式 Obsidian CLI を使用してノートの内容を標準出力に表示するコマンド。

## 使い方

```
/obs-print Recipe                 → ノート名で読む
/obs-print inbox/note.md          → パスで読む
/obs-print Recipe vault=MyVault   → 特定Vault
```

## 実行手順

1. ノート名が指定されていない場合は AskUserQuestion で確認

2. ノート内容を表示:

```bash
# 名前で読む（wikilink式解決）
obsidian read file="note-name"

# パスで読む
obsidian read path="folder/note.md"

# 特定Vault
obsidian vault=MyVault read file="note-name"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| ノートが見つからない | `obsidian search query="..."` で候補を検索して提示 |

---
description: |-
  Obsidianのノートを開く。
  「/obs-open <note-name> [options]」でノートを指定して開く。
  file=, path=, newtab, vault= をサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-open

公式 Obsidian CLI を使用してノートを Obsidian で開くコマンド。

## 使い方

```
/obs-open daily-log               → ノートを開く
/obs-open daily-log newtab        → 新しいタブで開く
/obs-open daily-log vault=Work    → 特定Vault
```

## 実行手順

1. ノート名が指定されていない場合は AskUserQuestion で確認

2. ノートを開く:

```bash
# 名前で開く
obsidian open file="note-name"

# パスで開く
obsidian open path="folder/note.md"

# 新しいタブで開く
obsidian open file="note-name" newtab

# 特定Vault
obsidian vault=MyVault open file="note-name"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| ノートが見つからない | `obsidian search query="..."` で候補を検索して提示 |

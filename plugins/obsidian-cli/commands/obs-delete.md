---
description: |-
  Obsidianのノートを削除する。
  「/obs-delete <note> [options]」でノートを削除。
  file=, path=, permanent, vault= をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-delete

公式 Obsidian CLI を使用してノートを削除するコマンド。

## 使い方

```
/obs-delete old-draft             → ゴミ箱へ移動
/obs-delete old-draft permanent   → 完全削除
/obs-delete old-draft vault=Work  → 特定Vault
```

## 実行手順

1. ノート名が指定されていない場合は AskUserQuestion で確認
2. **削除前に必ずユーザーに最終確認を行う**

```bash
# ゴミ箱へ移動（デフォルト）
obsidian delete file="note-name"
obsidian delete path="folder/note.md"

# 完全削除
obsidian delete file="note-name" permanent
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| ノートが見つからない | `obsidian search query="..."` で正しい名前を確認 |

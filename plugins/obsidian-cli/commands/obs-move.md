---
description: |-
  Obsidianのノートを移動・リネームする。
  「/obs-move <note> <destination>」で移動。
  「/obs-move rename <note> <new-name>」でリネーム。
  Vault内のリンクも自動更新される。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-move

公式 Obsidian CLI を使用してノートを移動・リネームするコマンド。内部リンクも自動的に更新される。

## 使い方

```
/obs-move Note archive/Note.md             → 移動
/obs-move rename Note "New Name"            → リネーム
/obs-move Note archive/Note.md vault=Work   → 特定Vault
```

## 実行手順

```bash
# ノートを移動
obsidian move file="note-name" to="archive/note.md"
obsidian move path="inbox/note.md" to="archive/note.md"

# ノートをリネーム（拡張子は自動保持）
obsidian rename file="note-name" name="new-name"
obsidian rename path="folder/note.md" name="new-name"

# 特定Vault
obsidian vault=MyVault move file="note-name" to="archive/note.md"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| 元ノートが見つからない | `obsidian search query="..."` で正しい名前を確認 |
| 移動先が既に存在 | ユーザーに確認して対応を決定 |

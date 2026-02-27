---
description: |-
  Obsidianにノートを作成する。
  「/obs-create <note-name> [options]」でノートを作成。
  name=, content=, template=, overwrite, open, vault= をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# obs-create

公式 Obsidian CLI を使用してノートを作成するコマンド。

## 使い方

```
/obs-create meeting-notes                              → 空のノート作成
/obs-create meeting-notes content="# 議事録\n内容"      → 内容付き
/obs-create meeting-notes template=Meeting              → テンプレート使用
/obs-create meeting-notes content="更新" overwrite       → 上書き
/obs-create meeting-notes content="内容" open            → 作成後に開く
```

## 実行手順

1. ノート名が指定されていない場合は AskUserQuestion で確認

2. ノート作成:

```bash
# 空のノートを作成
obsidian create name="note-name"

# 内容付きで作成（改行は \n で指定）
obsidian create name="note-name" content="# Title\n\nBody text"

# テンプレートを使用
obsidian create name="note-name" template=Meeting

# 既存ノートを上書き
obsidian create name="note-name" content="新しい内容" overwrite

# 作成後にObsidianで開く
obsidian create name="note-name" content="内容" open

# 特定Vault
obsidian vault=MyVault create name="note-name"
```

## 追記・先頭挿入

既存ノートへの追記は `append` / `prepend` コマンドを使う:

```bash
obsidian append file="note-name" content="追記内容"
obsidian prepend file="note-name" content="先頭に追加"
obsidian append file="note-name" content="..." inline   # 改行なし
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| 既存ノートとの競合 | `overwrite` フラグの使用を提案 |

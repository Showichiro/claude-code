---
description: |-
  Obsidianノートのプロパティ（Frontmatter）を操作する。
  「/obs-frontmatter <note> [options]」でプロパティの表示・編集・削除。
  property:read, property:set, property:remove をサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-frontmatter

公式 Obsidian CLI を使用してノートのプロパティ（YAML Frontmatter）を操作するコマンド。

## 使い方

```
/obs-frontmatter Recipe                             → プロパティ一覧
/obs-frontmatter Recipe read status                 → 特定プロパティの値
/obs-frontmatter Recipe set status done             → プロパティを設定
/obs-frontmatter Recipe remove draft                → プロパティを削除
```

## 実行手順

1. ノート名が指定されていない場合は AskUserQuestion で確認

2. プロパティ操作:

```bash
# プロパティ一覧
obsidian properties file="note-name"

# 特定プロパティの値を読む
obsidian property:read name=status file="note-name"

# プロパティを設定（存在しなければ作成）
obsidian property:set name=status value=done file="note-name"

# 型指定付きで設定
obsidian property:set name=tags value="tech, tutorial" type=list file="note-name"

# プロパティを削除
obsidian property:remove name=draft file="note-name"

# 特定Vault
obsidian vault=MyVault properties file="note-name"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| ノートが見つからない | `obsidian search query="..."` で正しい名前を確認 |
| プロパティが存在しない | `property:set` で新規作成を提案 |

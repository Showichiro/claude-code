---
description: |-
  ObsidianのVault内のファイル・フォルダ一覧を表示する。
  「/obs-list [options]」でVault内容を一覧表示。
  folder=, ext=, total フラグをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-list

公式 Obsidian CLI を使用して Vault 内のファイル・フォルダを一覧表示するコマンド。

## 使い方

```
/obs-list                         → Vaultルートのファイル一覧
/obs-list folder=inbox            → inboxフォルダのファイル一覧
/obs-list folders                 → フォルダ一覧
/obs-list folders folder=inbox    → inboxのサブフォルダ一覧
/obs-list total                   → ファイル数のみ
/obs-list ext=md                  → .mdファイルのみ
/obs-list vault=MyVault           → 特定Vault
```

## 実行手順

```bash
# ファイル一覧
obsidian files
obsidian files folder=inbox
obsidian files ext=md
obsidian files total

# フォルダ一覧
obsidian folders
obsidian folders folder=inbox
obsidian folders total

# フォルダ情報
obsidian folder path=inbox
obsidian folder path=inbox info=files

# 特定Vault
obsidian vault=MyVault files folder=inbox
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| フォルダが見つからない | `obsidian folders` でフォルダ一覧を表示 |

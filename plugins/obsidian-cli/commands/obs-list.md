---
description: |-
  ObsidianのVault内のファイル・フォルダ一覧を表示する。
  「/obs-list [path] [options]」でVault内容を一覧表示。
  --vault オプションをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-list

obsidian-cli を使用して Vault 内のファイル・フォルダを一覧表示するコマンド。

## ワークフロー

```
/obs-list [path] [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ パス確認
  │     ├─ 引数あり → 指定パスの内容を表示
  │     └─ 引数なし → Vaultルートの内容を表示
  │
  └─ obsidian-cli list 実行
        ├─ 成功 → 一覧を表示
        └─ エラー → 対処法を提案
```

## 実行手順

```bash
# Vaultルートの一覧
obsidian-cli list

# サブフォルダの一覧
obsidian-cli list "001 Notes"

# 指定Vault
obsidian-cli list --vault "{vault-name}"
obsidian-cli list "folder" --vault "{vault-name}"
```

## 使用例

```bash
# Vaultルートの一覧
/obs-list

# サブフォルダの一覧
/obs-list 001 Notes

# 指定Vaultの一覧
/obs-list --vault work
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| パスが見つからない | Vaultルートの内容を表示して正しいパスを案内 |

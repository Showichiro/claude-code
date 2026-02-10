---
description: |-
  Obsidianのノートを開く。
  「/obs-open <note-name> [options]」でノートを指定して開く。
  --vault, --section オプションをサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-open

obsidian-cli を使用してノートを Obsidian で開くコマンド。

## ワークフロー

```
/obs-open <note-name> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │     └─ 未インストール → brew install yakitrak/yakitrak/obsidian-cli を提案
  │
  ├─ デフォルトVault確認
  │     └─ 未設定 → obsidian-cli set-default を案内
  │
  ├─ ノート名確認
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → AskUserQuestion で確認
  │
  └─ obsidian-cli open 実行
        ├─ 成功 → ノートが Obsidian で開かれたことを報告
        └─ エラー → 対処法を提案
```

## 実行手順

1. **ノート名の確認**
   - 引数で指定されていない場合は AskUserQuestion で確認

2. **ノートを開く**

   ```bash
   # 基本
   obsidian-cli open "{note-name}"

   # 指定Vault
   obsidian-cli open "{note-name}" --vault "{vault-name}"

   # 特定セクション
   obsidian-cli open "{note-name}" --section "{heading-text}"
   ```

## 使用例

```bash
# ノートを開く
/obs-open daily-log

# 特定Vaultのノートを開く
/obs-open meeting-notes --vault work

# 特定セクションを開く
/obs-open project-plan --section "Next Steps"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| デフォルトVault未設定 | `obsidian-cli set-default` を案内 |
| ノートが見つからない | `obsidian-cli list` で候補を検索して提示 |

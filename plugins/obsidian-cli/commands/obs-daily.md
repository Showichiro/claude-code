---
description: |-
  Obsidianのデイリーノートを作成・開く。
  「/obs-daily [options]」でデイリーノートを作成/開く。
  --vault オプションをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-daily

obsidian-cli を使用してデイリーノートを作成または開くコマンド。存在しない場合はテンプレートから作成される。

## ワークフロー

```
/obs-daily [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  └─ obsidian-cli daily 実行
        ├─ 成功 → デイリーノートが開かれたことを報告
        └─ エラー → 対処法を提案
```

## 実行手順

```bash
# デフォルトVaultのデイリーノート
obsidian-cli daily

# 指定Vaultのデイリーノート
obsidian-cli daily --vault "{vault-name}"
```

## 使用例

```bash
# デイリーノートを開く
/obs-daily

# 指定Vaultのデイリーノートを開く
/obs-daily --vault work
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| デフォルトVault未設定 | `obsidian-cli set-default` を案内 |
| デイリーノートプラグイン未設定 | Obsidian の Daily Notes プラグイン設定を案内 |

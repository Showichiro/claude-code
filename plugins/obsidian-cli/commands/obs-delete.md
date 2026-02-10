---
description: |-
  Obsidianのノートを削除する。
  「/obs-delete <note-path> [options]」でノートを削除。
  --vault オプションをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-delete

obsidian-cli を使用してノートを削除するコマンド。

## ワークフロー

```
/obs-delete <note-path> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ ノートパス確認
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → AskUserQuestion で確認
  │
  ├─ 確認
  │     └─ ユーザーに削除の最終確認を行う
  │
  └─ obsidian-cli delete 実行
        ├─ 成功 → 削除完了を報告
        └─ エラー → 対処法を提案
```

## 実行手順

**重要**: 削除は取り消せないため、実行前に必ずユーザーに確認する。

```bash
# ノートを削除
obsidian-cli delete "{note-path}"

# 指定Vault
obsidian-cli delete "{note-path}" --vault "{vault-name}"
```

## 使用例

```bash
# ノートを削除
/obs-delete old-draft.md

# 指定Vaultのノートを削除
/obs-delete archive/old-note.md --vault work
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| ノートが見つからない | `obsidian-cli list` で正しいパスを確認 |

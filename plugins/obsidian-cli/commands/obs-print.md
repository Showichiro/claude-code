---
description: |-
  Obsidianのノート内容を表示する。
  「/obs-print <note-name> [options]」でノート内容を標準出力に表示。
  --vault オプションをサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-print

obsidian-cli を使用してノートの内容を標準出力に表示するコマンド。

## ワークフロー

```
/obs-print <note-name> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ ノート名確認
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → AskUserQuestion で確認
  │
  └─ obsidian-cli print 実行
        ├─ 成功 → ノート内容を表示
        └─ エラー → 対処法を提案
```

## 実行手順

```bash
# ノート内容を表示
obsidian-cli print "{note-name}"

# パス指定
obsidian-cli print "{note-path}"

# 指定Vault
obsidian-cli print "{note-name}" --vault "{vault-name}"
```

## 使用例

```bash
# ノート内容を表示
/obs-print meeting-notes

# パス指定で表示
/obs-print 001 Notes/project-plan

# 指定Vaultのノートを表示
/obs-print todo-list --vault work
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| ノートが見つからない | `obsidian-cli list` で候補を検索して提示 |

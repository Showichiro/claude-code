---
description: |-
  Obsidianのノートを移動・リネームする。
  「/obs-move <current-path> <new-path> [options]」で移動/リネーム。
  Vault内のリンクも自動更新される。--vault, --open オプションをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-move

obsidian-cli を使用してノートを移動・リネームするコマンド。Vault 内のリンクも自動的に更新される。

## ワークフロー

```
/obs-move <current-path> <new-path> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ パス確認
  │     ├─ 引数2つあり → そのまま使用
  │     └─ 引数不足 → AskUserQuestion で確認
  │
  └─ obsidian-cli move 実行
        ├─ 成功 → 移動完了とリンク更新を報告
        └─ エラー → 対処法を提案
```

## 実行手順

```bash
# ノートを移動/リネーム
obsidian-cli move "{current-note-path}" "{new-note-path}"

# 指定Vault
obsidian-cli move "{current-note-path}" "{new-note-path}" --vault "{vault-name}"

# 移動後にObsidianで開く
obsidian-cli move "{current-note-path}" "{new-note-path}" --open
```

## 使用例

```bash
# リネーム
/obs-move old-name.md new-name.md

# フォルダ間の移動
/obs-move inbox/note.md archive/note.md

# 移動後に開く
/obs-move draft.md published/article.md --open
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| 元ノートが見つからない | `obsidian-cli list` で正しいパスを確認 |
| 移動先が既に存在 | ユーザーに確認して対応を決定 |

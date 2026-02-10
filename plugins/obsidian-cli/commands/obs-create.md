---
description: |-
  Obsidianにノートを作成する。
  「/obs-create <note-name> [options]」でノートを作成。
  --content, --overwrite, --append, --open, --vault オプションをサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# obs-create

obsidian-cli を使用してノートを作成・更新するコマンド。

## ワークフロー

```
/obs-create <note-name> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ ノート名確認
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → AskUserQuestion で確認
  │
  ├─ 内容確認
  │     ├─ --content 指定あり → そのまま使用
  │     ├─ 標準入力/パイプ → パイプの内容を使用
  │     └─ 指定なし → 空ノートとして作成
  │
  ├─ 既存ノート処理
  │     ├─ --overwrite → 上書き
  │     ├─ --append → 追記
  │     └─ なし → 別名で作成
  │
  └─ obsidian-cli create 実行
        ├─ 成功 → 作成結果を報告
        └─ エラー → 対処法を提案
```

## 実行手順

1. **ノート名の確認**
   - 引数がない場合は AskUserQuestion で確認
   - パスを含む場合（例: `folder/note.md`）はそのまま使用

2. **ノート作成**

   ```bash
   # 空のノートを作成
   obsidian-cli create "{note-name}"

   # 内容付きで作成
   obsidian-cli create "{note-name}" --content "内容テキスト"

   # 既存ノートを上書き
   obsidian-cli create "{note-name}" --content "新しい内容" --overwrite

   # 既存ノートに追記
   obsidian-cli create "{note-name}" --content "追記内容" --append

   # 作成後にObsidianで開く
   obsidian-cli create "{note-name}" --content "内容" --open

   # 指定Vault
   obsidian-cli create "{note-name}" --vault "{vault-name}"
   ```

## 使用例

```bash
# 空のノートを作成
/obs-create meeting-2024-01-15

# 内容付きで作成して開く
/obs-create todo-list --content "# TODO\n- [ ] タスク1" --open

# 既存ノートに追記
/obs-create daily-log --content "\n## 追記メモ\n内容" --append

# 上書き更新
/obs-create project-status --content "# Status\n完了" --overwrite
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| デフォルトVault未設定 | `obsidian-cli set-default` を案内 |
| 既存ノートとの競合 | `--overwrite` または `--append` の使用を提案 |

---
description: |-
  ObsidianノートのYAML Frontmatterを操作する。
  「/obs-frontmatter <note-name> [options]」でFrontmatterの表示・編集・削除。
  --print, --edit, --delete, --key, --value, --vault オプションをサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# obs-frontmatter

obsidian-cli を使用してノートの YAML Frontmatter を操作するコマンド。エイリアス: `fm`

## ワークフロー

```
/obs-frontmatter <note-name> [options] 実行
  │
  ├─ obsidian-cli インストール確認
  │
  ├─ ノート名確認
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → AskUserQuestion で確認
  │
  ├─ 操作の判定
  │     ├─ --print → Frontmatter を表示
  │     ├─ --edit --key --value → フィールドを編集（なければ作成）
  │     └─ --delete --key → フィールドを削除
  │
  └─ obsidian-cli frontmatter 実行
        ├─ 成功 → 結果を表示
        └─ エラー → 対処法を提案
```

## 実行手順

```bash
# Frontmatterを表示
obsidian-cli frontmatter "{note-name}" --print

# フィールドを編集（存在しなければ作成）
obsidian-cli frontmatter "{note-name}" --edit --key "status" --value "done"

# フィールドを削除
obsidian-cli frontmatter "{note-name}" --delete --key "draft"

# 指定Vault
obsidian-cli frontmatter "{note-name}" --print --vault "{vault-name}"
```

## 使用例

```bash
# Frontmatterを表示
/obs-frontmatter project-plan --print

# ステータスを更新
/obs-frontmatter meeting-notes --edit --key status --value reviewed

# タグを追加
/obs-frontmatter article --edit --key tags --value "tech, tutorial"

# 不要なフィールドを削除
/obs-frontmatter draft --delete --key wip
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| obsidian-cli 未インストール | `brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| ノートが見つからない | `obsidian-cli list` で正しいパスを確認 |
| Frontmatterが存在しない | `--edit` で新規作成を提案 |

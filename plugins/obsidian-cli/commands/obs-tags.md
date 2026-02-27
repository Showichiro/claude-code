---
description: |-
  Obsidianのタグを管理する。
  「/obs-tags [options]」でタグ一覧・情報取得。
  counts, sort=count, total, file= をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-tags

公式 Obsidian CLI を使用して Vault 内のタグを管理するコマンド。

## 使い方

```
/obs-tags                         → タグ一覧
/obs-tags counts                  → カウント付き
/obs-tags sort=count              → カウント順ソート
/obs-tags total                   → タグ数のみ
/obs-tags file=Recipe             → 特定ファイルのタグ
/obs-tags info todo               → 特定タグの情報
```

## 実行手順

```bash
# タグ一覧
obsidian tags
obsidian tags counts                # カウント付き
obsidian tags sort=count            # カウント順ソート
obsidian tags total                 # タグ数のみ
obsidian tags active                # アクティブファイルのタグ
obsidian tags file="note-name"      # 特定ファイルのタグ

# タグ情報
obsidian tag name=todo              # タグ情報
obsidian tag name=todo verbose      # ファイルリスト付き
obsidian tag name=todo total        # 使用回数のみ
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| タグが見つからない | `obsidian tags` で利用可能なタグを確認 |

---
description: |-
  gog CLI で Google Contacts を操作する。
  「/gog-contacts [操作] [オプション]」で連絡先の検索・作成・更新・削除を実行。
  list, search, create, update, delete, directory 等をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-contacts

gog CLI を使って Google Contacts を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `list` | 連絡先一覧 |
| `search` | 連絡先検索 |
| `get` | 連絡先詳細 |
| `create` | 連絡先作成 |
| `update` | 連絡先更新 |
| `delete` | 連絡先削除 |
| `other list` | その他の連絡先一覧 |
| `other search` | その他の連絡先検索 |
| `directory list` | Workspace ディレクトリ一覧 |
| `directory search` | Workspace ディレクトリ検索 |

## 実行手順

```bash
# 一覧・検索
gog contacts list --max 50
gog contacts search "名前" --max 50
gog contacts get people/<resourceName>
gog contacts get user@example.com

# 作成
gog contacts create \
  --given-name "太郎" --family-name "田中" \
  --email "taro@example.com" --phone "+81901234567"

# 更新
gog contacts update people/<resourceName> --given-name "更新名"

# 削除
gog contacts delete people/<resourceName>

# その他の連絡先
gog contacts other list --max 50
gog contacts other search "John"

# Workspace ディレクトリ
gog contacts directory list --max 50
gog contacts directory search "Jane"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| 権限エラー | `gog auth add --services contacts --force-consent` を案内 |
| リソース名不正 | `people/<id>` 形式を案内 |

## 使用例

```bash
/gog-contacts search "田中"
/gog-contacts create --given-name "太郎" --family-name "田中" --email "taro@example.com"
```

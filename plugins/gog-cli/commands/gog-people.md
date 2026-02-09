---
description: |-
  gog CLI で Google People（プロフィール）を操作する。
  「/gog-people [操作] [オプション]」でプロフィール情報・検索・リレーションを取得。
  me, get, search, relations をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-people

gog CLI を使って Google People API でプロフィール情報を取得するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `me` | 自分のプロフィール |
| `get` | 指定ユーザーのプロフィール |
| `search` | Workspace ディレクトリ検索 |
| `relations` | リレーション（マネージャー等） |

## 実行手順

```bash
# 自分のプロフィール
gog people me

# 特定ユーザー
gog people get people/<userId>

# Workspace ディレクトリ検索
gog people search "Ada Lovelace" --max 5

# リレーション
gog people relations
gog people relations people/<userId> --type manager
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| 権限エラー | `gog auth add --services people --force-consent` を案内 |

## 使用例

```bash
/gog-people me
/gog-people search "田中" --max 10
/gog-people relations --type manager
```

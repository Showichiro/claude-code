---
description: |-
  gog CLI で Google Keep を操作する（Workspace + サービスアカウント必須）。
  「/gog-keep [操作] [オプション]」でノートの一覧・取得・検索・添付ファイルダウンロードを実行。
  list, get, search, attachment をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-keep

gog CLI を使って Google Keep を操作するコマンド。Workspace + ドメイン委任のサービスアカウントが必要。

## 前提条件

Keep API は Workspace 限定で、サービスアカウント（ドメイン委任）が必要:

```bash
gog auth service-account set you@yourdomain.com --key ~/Downloads/service-account.json
```

## サポートする操作

| 操作 | 説明 |
|------|------|
| `list` | ノート一覧 |
| `get` | ノート詳細 |
| `search` | ノート検索 |
| `attachment` | 添付ファイルダウンロード |

## 実行手順

```bash
# ノート一覧
gog keep list --account you@yourdomain.com

# ノート取得
gog keep get <noteId> --account you@yourdomain.com

# ノート検索
gog keep search <query> --account you@yourdomain.com

# 添付ファイルダウンロード
gog keep attachment <attachmentName> --account you@yourdomain.com --out ./attachment.bin
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| サービスアカウント未設定 | `gog auth service-account set` の手順を案内 |
| Workspace アカウントなし | Keep は Workspace + ドメイン委任が必要であることを案内 |

## 使用例

```bash
/gog-keep list --account you@yourdomain.com
/gog-keep search "買い物リスト" --account you@yourdomain.com
```

---
description: |-
  gog CLI で Google Chat を操作する（Workspace のみ）。
  「/gog-chat [操作] [オプション]」でスペース・メッセージ・DM を操作。
  spaces, messages, threads, dm 等をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-chat

gog CLI を使って Google Chat を操作するコマンド。Workspace アカウントが必要。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `spaces list` | スペース一覧 |
| `spaces find` | スペース検索 |
| `spaces create` | スペース作成 |
| `messages list` | メッセージ一覧 |
| `messages send` | メッセージ送信 |
| `threads list` | スレッド一覧 |
| `dm space` | DM スペース取得 |
| `dm send` | DM 送信 |

## 実行手順

### スペース

```bash
gog chat spaces list
gog chat spaces find "Engineering"
gog chat spaces create "Engineering" --member alice@company.com --member bob@company.com
```

### メッセージ

```bash
# 一覧
gog chat messages list spaces/<spaceId> --max 5
gog chat messages list spaces/<spaceId> --thread <threadId>
gog chat messages list spaces/<spaceId> --unread

# 送信
gog chat messages send spaces/<spaceId> --text "メッセージ"

# スレッドへ返信
gog chat messages send spaces/<spaceId> --text "返信" --thread spaces/<spaceId>/threads/<threadId>
```

### スレッド

```bash
gog chat threads list spaces/<spaceId>
```

### DM

```bash
gog chat dm space user@company.com
gog chat dm send user@company.com --text "ping"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| Workspace アカウントなし | Google Workspace アカウントが必要であることを案内 |
| 権限エラー | `gog auth add --services chat --force-consent` を案内 |

## 使用例

```bash
/gog-chat spaces list
/gog-chat messages list spaces/<spaceId> --max 10
/gog-chat dm send user@company.com --text "確認お願いします"
```

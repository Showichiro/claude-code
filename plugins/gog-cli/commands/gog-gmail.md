---
description: |-
  gog CLI で Gmail を操作する。
  「/gog-gmail [操作] [オプション]」で検索・送信・ラベル管理・追跡・Watch等を実行。
  search, messages, send, thread, labels, drafts, filters, batch, track, watch, delegation, vacation, forwarding, sendas 等をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-gmail

gog CLI を使って Gmail を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `search` | スレッド単位でメール検索 |
| `messages search` | メッセージ単位で検索（`--include-body` 対応） |
| `send` | メール送信（`--track` で開封追跡） |
| `thread get/modify` | スレッド詳細取得・ラベル変更・添付ダウンロード |
| `get` | メッセージ取得 |
| `attachment` | 添付ファイル取得 |
| `url` | Gmail Web URL 取得 |
| `labels` | ラベル一覧・作成・変更 |
| `drafts` | 下書きの作成・更新・送信 |
| `filters` | フィルタの作成・削除 |
| `batch` | バッチ操作（削除・ラベル変更） |
| `vacation` | 不在設定 |
| `sendas` | 送信元アドレス管理 |
| `forwarding` | 転送設定 |
| `autoforward` | 自動転送の有効化/無効化 |
| `delegates` | 委任管理（Workspace） |
| `track` | メール開封追跡 |
| `watch` | Pub/Sub push 通知 |
| `history` | メールボックス変更履歴 |

## ワークフロー

```text
/gog-gmail [操作] [引数...] 実行
  │
  ├─ gog インストール確認
  │     └─ 未インストール → brew install steipete/tap/gogcli を提案
  │
  ├─ 操作の判定
  │     ├─ search → 検索クエリを確認して実行
  │     ├─ messages search → メッセージ単位検索
  │     ├─ send → 宛先・件名・本文を確認して実行
  │     ├─ thread → スレッドIDを確認して実行
  │     └─ その他 → 必要な引数を確認
  │
  └─ gog gmail [操作] 実行
        ├─ 成功 → 結果を表示
        └─ エラー → エラーメッセージを表示し対処法を案内
```

## 実行手順

### 検索（スレッド単位）

```bash
gog gmail search 'newer_than:7d' --max 10
gog gmail search 'from:alice@example.com' --max 20
gog gmail search 'is:unread' --max 20
gog gmail search 'has:attachment newer_than:30d' --max 10
gog gmail search 'newer_than:7d' --max 10 --json
```

### 検索（メッセージ単位）

```bash
gog gmail messages search 'newer_than:7d' --max 10
gog gmail messages search 'newer_than:7d' --include-body --json
```

### 送信

**注意**: 送信前に必ずユーザーに確認を取る。

```bash
gog gmail send --to recipient@example.com --subject "件名" --body "本文"
gog gmail send --to recipient@example.com --subject "件名" --body-html "<p>HTML本文</p>"
gog gmail send --to recipient@example.com --subject "件名" --body-file ./message.txt
gog gmail send --to recipient@example.com --subject "件名" --body-file -  # stdin から

# 開封追跡付き送信（HTML body 必須、宛先1名のみ）
gog gmail send --to recipient@example.com --subject "件名" --body-html "<p>本文</p>" --track
```

### スレッド操作

```bash
gog gmail thread get <threadId>
gog gmail thread get <threadId> --download --out-dir ./attachments
gog gmail thread modify <threadId> --add STARRED --remove INBOX
gog gmail url <threadId>
```

### メッセージ・添付ファイル

```bash
gog gmail get <messageId>
gog gmail get <messageId> --format metadata
gog gmail attachment <messageId> <attachmentId>
gog gmail attachment <messageId> <attachmentId> --out ./attachment.bin
```

### ラベル管理

```bash
gog gmail labels list
gog gmail labels get INBOX --json
gog gmail labels create "My Label"
```

### 下書き

```bash
gog gmail drafts list
gog gmail drafts create --to a@b.com --subject "件名" --body "本文"
gog gmail drafts update <draftId> --subject "更新" --body "更新"
gog gmail drafts send <draftId>
```

### バッチ操作

```bash
gog gmail batch delete <msgId1> <msgId2>
gog gmail batch modify <msgId1> <msgId2> --add STARRED --remove INBOX
```

### フィルタ

```bash
gog gmail filters list
gog gmail filters create --from 'noreply@example.com' --add-label 'Notifications'
gog gmail filters delete <filterId>
```

### メール開封追跡

```bash
# セットアップ（Cloudflare Worker のデプロイが必要）
gog gmail track setup --worker-url https://gog-email-tracker.<acct>.workers.dev

# 追跡付き送信
gog gmail send --to recipient@example.com --subject "件名" --body-html "<p>本文</p>" --track

# 開封確認
gog gmail track opens <tracking_id>
gog gmail track opens --to recipient@example.com

# ステータス
gog gmail track status
```

### 設定

```bash
# 不在設定
gog gmail vacation get
gog gmail vacation enable --subject "Out of office" --message "..."
gog gmail vacation disable

# 送信元管理
gog gmail sendas list
gog gmail sendas create --email alias@example.com

# 転送
gog gmail forwarding list
gog gmail forwarding add --email forward@example.com
gog gmail autoforward get
gog gmail autoforward enable --email forward@example.com
gog gmail autoforward disable
```

### 委任（Workspace）

```bash
gog gmail delegates list
gog gmail delegates add --email delegate@example.com
gog gmail delegates remove --email delegate@example.com
```

### Watch（Pub/Sub push）

```bash
gog gmail watch start --topic projects/<p>/topics/<t> --label INBOX
gog gmail watch serve --bind 127.0.0.1 --token <shared> --hook-url http://127.0.0.1:18789/hooks/agent
gog gmail history --since <historyId>
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| 認証エラー | `gog auth add <email>` を案内 |
| 操作未指定 | 利用可能な操作一覧を表示 |
| 送信先未指定 | AskUserQuestion で確認 |

## 使用例

```bash
/gog-gmail search 'newer_than:7d' --max 10
/gog-gmail messages search 'is:unread' --include-body --json --max 20
/gog-gmail send --to alice@example.com --subject "Hello" --body "Hi!"
/gog-gmail labels list
/gog-gmail track opens --to recipient@example.com
```

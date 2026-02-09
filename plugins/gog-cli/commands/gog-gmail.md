---
description: |-
  gog CLI で Gmail を操作する。
  「/gog-gmail [操作] [オプション]」で検索・送信・ラベル管理等を実行。
  search, send, thread, labels, drafts, filters 等をサポート。
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
| `search` | メールを検索 |
| `send` | メールを送信 |
| `thread` | スレッドの詳細取得・ラベル変更 |
| `get` | メッセージ取得 |
| `labels` | ラベル一覧・作成・変更 |
| `drafts` | 下書きの作成・更新・送信 |
| `filters` | フィルタの作成・削除 |
| `batch` | バッチ操作（削除・ラベル変更） |
| `vacation` | 不在設定 |

## ワークフロー

```
/gog-gmail [操作] [引数...] 実行
  │
  ├─ gog インストール確認
  │     └─ 未インストール → brew install steipete/tap/gogcli を提案
  │
  ├─ 操作の判定
  │     ├─ search → 検索クエリを確認して実行
  │     ├─ send → 宛先・件名・本文を確認して実行
  │     ├─ thread → スレッドIDを確認して実行
  │     └─ その他 → 必要な引数を確認
  │
  └─ gog gmail [操作] 実行
        ├─ 成功 → 結果を表示
        └─ エラー → エラーメッセージを表示し対処法を案内
```

## 実行手順

### 検索

```bash
# 最近のメール
gog gmail search 'newer_than:7d' --max 10

# 特定の送信者から
gog gmail search 'from:alice@example.com' --max 20

# 未読メール
gog gmail search 'is:unread' --max 20

# 添付ファイル付き
gog gmail search 'has:attachment newer_than:30d' --max 10

# JSON 出力
gog gmail search 'newer_than:7d' --max 10 --json
```

### 送信

**注意**: 送信前に必ずユーザーに確認を取る。

```bash
gog gmail send --to recipient@example.com --subject "件名" --body "本文"

# HTML メール
gog gmail send --to recipient@example.com --subject "件名" --body-html "<p>HTML本文</p>"

# ファイルから本文
gog gmail send --to recipient@example.com --subject "件名" --body-file ./message.txt
```

### スレッド操作

```bash
# スレッド詳細
gog gmail thread get <threadId>

# 添付ファイルダウンロード
gog gmail thread get <threadId> --download --out-dir ./attachments

# ラベル変更
gog gmail thread modify <threadId> --add STARRED --remove INBOX
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
gog gmail drafts send <draftId>
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
# 最近7日のメールを確認
/gog-gmail search 'newer_than:7d' --max 10

# メール送信
/gog-gmail send --to alice@example.com --subject "Hello" --body "Hi!"

# 未読メールを JSON で取得
/gog-gmail search 'is:unread' --json --max 20

# ラベル一覧
/gog-gmail labels list
```

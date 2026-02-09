# Gmail リファレンス

## 検索（スレッド単位）

```bash
gog gmail search '<query>' --max <n>
gog gmail search '<query>' --max <n> --json
```

よく使うクエリ:
- `newer_than:7d` — 直近7日
- `from:alice@example.com` — 特定の送信者
- `is:unread` — 未読
- `has:attachment` — 添付ファイル付き
- `subject:invoice` — 件名検索
- `older_than:1y` — 1年以上前

## 検索（メッセージ単位）

```bash
gog gmail messages search '<query>' --max <n>
gog gmail messages search '<query>' --include-body --json
```

## スレッド操作

```bash
gog gmail thread get <threadId>
gog gmail thread get <threadId> --download                    # 添付ダウンロード
gog gmail thread get <threadId> --download --out-dir ./dir
gog gmail thread modify <threadId> --add STARRED --remove INBOX
gog gmail url <threadId>                                      # Web URL
```

## メッセージ・添付ファイル

```bash
gog gmail get <messageId>
gog gmail get <messageId> --format metadata
gog gmail attachment <messageId> <attachmentId>
gog gmail attachment <messageId> <attachmentId> --out ./file.bin
```

## 送信

```bash
gog gmail send --to a@b.com --subject "件名" --body "本文"
gog gmail send --to a@b.com --subject "件名" --body-file ./message.txt
gog gmail send --to a@b.com --subject "件名" --body-file -         # stdin
gog gmail send --to a@b.com --subject "件名" --body "fallback" --body-html "<p>HTML</p>"
gog gmail send --to a@b.com --subject "件名" --body-html "<p>本文</p>" --track   # 追跡付き
```

## 下書き

```bash
gog gmail drafts list
gog gmail drafts create --subject "件名" --body "本文"
gog gmail drafts create --to a@b.com --subject "件名" --body "本文"
gog gmail drafts update <draftId> --subject "件名" --body "本文"
gog gmail drafts update <draftId> --to a@b.com --subject "件名" --body "本文"
gog gmail drafts send <draftId>
```

## ラベル

```bash
gog gmail labels list
gog gmail labels get INBOX --json           # メッセージ数を含む
gog gmail labels create "My Label"
gog gmail thread modify <threadId> --add STARRED --remove INBOX
```

## バッチ操作

```bash
gog gmail batch delete <msgId1> <msgId2>
gog gmail batch modify <msgId1> <msgId2> --add STARRED --remove INBOX
```

## フィルタ

```bash
gog gmail filters list
gog gmail filters create --from 'noreply@example.com' --add-label 'Notifications'
gog gmail filters delete <filterId>
```

## 設定

```bash
# 不在
gog gmail vacation get
gog gmail vacation enable --subject "Out of office" --message "..."
gog gmail vacation disable

# 送信元
gog gmail sendas list
gog gmail sendas create --email alias@example.com

# 転送
gog gmail forwarding list
gog gmail forwarding add --email forward@example.com
gog gmail autoforward get
gog gmail autoforward enable --email forward@example.com
gog gmail autoforward disable
```

## 委任（Workspace）

```bash
gog gmail delegates list
gog gmail delegates add --email delegate@example.com
gog gmail delegates remove --email delegate@example.com
```

## メール追跡

```bash
gog gmail track setup --worker-url https://gog-email-tracker.<acct>.workers.dev
gog gmail send --to a@b.com --subject "件名" --body-html "<p>本文</p>" --track
gog gmail track opens <tracking_id>
gog gmail track opens --to recipient@example.com
gog gmail track status
```

注意: `--track` は宛先1名・HTML body 必須。`--track-split` で個別追跡ID付き一斉送信。

## Watch（Pub/Sub push）

```bash
gog gmail watch start --topic projects/<p>/topics/<t> --label INBOX
gog gmail watch serve --bind 127.0.0.1 --token <shared> --hook-url http://127.0.0.1:18789/hooks/agent
gog gmail watch serve --bind 0.0.0.0 --verify-oidc --oidc-email <svc@...> --hook-url <url>
gog gmail history --since <historyId>
```

## スクリプト例

```bash
# 特定送信者のメールをまとめてラベル付け
gog --json gmail search 'from:noreply@example.com' --max 200 | \
  jq -r '.threads[].id' | \
  xargs -n 50 gog gmail labels modify --add IMPORTANT

# 古いメールをアーカイブ
gog --json gmail search 'older_than:1y' --max 200 | \
  jq -r '.threads[].id' | \
  xargs -n 50 gog gmail labels modify --remove INBOX

# 最近のメールを検索して添付ダウンロード
gog gmail search 'newer_than:7d has:attachment' --max 10
gog gmail thread get <threadId> --download --out-dir ./attachments
```

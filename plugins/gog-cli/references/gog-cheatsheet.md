# gog CLI チートシート

Google Suite CLI (gogcli) のクイックリファレンス。
Gmail, Calendar, Drive, Contacts, Tasks, Sheets, Docs, Slides, Chat, Classroom, People, Groups, Keep をターミナルから操作可能。

詳細リファレンス:
- `references/auth-reference.md` — 認証・設定・環境変数
- `references/gmail-reference.md` — Gmail の全コマンド
- `references/calendar-reference.md` — Calendar の全コマンド
- `references/classroom-reference.md` — Classroom の全コマンド

## インストール

```bash
brew install steipete/tap/gogcli
```

## 認証セットアップ

```bash
gog auth credentials ~/Downloads/client_secret_....json
gog auth add you@gmail.com
export GOG_ACCOUNT=you@gmail.com
```

## グローバルフラグ

| フラグ | 説明 |
|--------|------|
| `--account <email\|alias>` | 使用するアカウント |
| `--json` | JSON 出力 |
| `--plain` | TSV 出力（パイプ向け） |
| `--verbose` | 詳細ログ |
| `--force` | 確認スキップ |
| `--no-input` | 非対話モード（CI用） |

## Gmail

```bash
gog gmail search 'newer_than:7d' --max 10
gog gmail messages search 'is:unread' --include-body --json
gog gmail thread get <threadId> --download --out-dir ./attachments
gog gmail send --to a@b.com --subject "件名" --body "本文"
gog gmail send --to a@b.com --subject "件名" --body-html "<p>本文</p>" --track
gog gmail labels list
gog gmail drafts list / create / send
gog gmail batch modify <msgId1> <msgId2> --add STARRED
gog gmail filters list / create / delete
gog gmail vacation get / enable / disable
gog gmail delegates list / add / remove
gog gmail track setup / opens / status
gog gmail watch start / serve
```

## Calendar

```bash
gog calendar events primary --today
gog calendar events --all --week
gog calendar search "meeting" --days 30
gog calendar create primary --summary "会議" --from ... --to ... --attendees "..."
gog calendar create primary --summary "定例" --from ... --to ... --rrule "RRULE:FREQ=WEEKLY" --reminder "popup:10m"
gog calendar update <calId> <eventId> --add-attendee "alice@example.com"
gog calendar respond <calId> <eventId> --status accepted
gog calendar propose-time <calId> <eventId> --open
gog calendar freebusy --calendars primary --from ... --to ...
gog calendar conflicts --calendars primary --today
gog calendar focus-time --from ... --to ...
gog calendar out-of-office --from ... --to ... --all-day
gog calendar working-location --type office --office-label "HQ" --from ... --to ...
gog calendar team <group-email> --today
gog calendar calendars / acl / colors / users
gog time now --timezone UTC
```

## Drive

```bash
gog drive ls --max 20
gog drive ls --parent <folderId>
gog drive search "invoice" --max 20
gog drive get <fileId>
gog drive url <fileId>
gog drive upload ./file --parent <folderId>
gog drive download <fileId> --out ./file.bin
gog drive download <fileId> --format pdf --out ./exported.pdf
gog drive mkdir "Folder" --parent <parentId>
gog drive rename <fileId> "New Name"
gog drive move <fileId> --parent <destId>
gog drive copy <fileId> "Copy Name"
gog drive delete <fileId>
gog drive permissions <fileId>
gog drive share <fileId> --to user --email user@example.com --role reader
gog drive unshare <fileId> --permission-id <permId>
gog drive drives --max 100
```

## Contacts

```bash
gog contacts list --max 50
gog contacts search "名前" --max 50
gog contacts get people/<resourceName>
gog contacts get user@example.com
gog contacts create --given-name "太郎" --family-name "田中" --email "taro@example.com" --phone "+81901234567"
gog contacts update people/<resourceName> --given-name "更新"
gog contacts delete people/<resourceName>
gog contacts other list / search
gog contacts directory list / search
```

## Tasks

```bash
gog tasks lists --max 50
gog tasks lists create <title>
gog tasks list <tasklistId> --max 50
gog tasks get <tasklistId> <taskId>
gog tasks add <tasklistId> --title "タスク名"
gog tasks add <tasklistId> --title "定例" --due 2025-02-01 --repeat weekly --repeat-count 4
gog tasks update <tasklistId> <taskId> --title "新しい名前"
gog tasks done <tasklistId> <taskId>
gog tasks undo <tasklistId> <taskId>
gog tasks delete <tasklistId> <taskId>
gog tasks clear <tasklistId>
```

## Sheets

```bash
gog sheets metadata <spreadsheetId>
gog sheets get <spreadsheetId> 'Sheet1!A1:B10'
gog sheets update <spreadsheetId> 'A1' 'val1|val2,val3|val4'
gog sheets update <spreadsheetId> 'A1' --values-json '[["a","b"],["c","d"]]'
gog sheets update <spreadsheetId> 'Sheet1!A1:C1' 'data' --copy-validation-from 'Sheet1!A2:C2'
gog sheets append <spreadsheetId> 'Sheet1!A:C' 'new|row|data'
gog sheets clear <spreadsheetId> 'Sheet1!A1:B10'
gog sheets format <spreadsheetId> 'Sheet1!A1:B2' --format-json '{"textFormat":{"bold":true}}' --format-fields '...'
gog sheets create "新しいシート" --sheets "Sheet1,Sheet2"
gog sheets export <spreadsheetId> --format pdf --out ./sheet.pdf
gog sheets copy <spreadsheetId> "コピー名"
```

## Docs

```bash
gog docs info <docId>
gog docs cat <docId> --max-bytes 10000
gog docs create "My Doc"
gog docs copy <docId> "Copy"
gog docs export <docId> --format pdf --out ./doc.pdf
gog docs export <docId> --format docx --out ./doc.docx
gog docs export <docId> --format txt --out ./doc.txt
```

## Slides

```bash
gog slides info <presentationId>
gog slides create "My Deck"
gog slides copy <presentationId> "Copy"
gog slides export <presentationId> --format pdf --out ./deck.pdf
gog slides export <presentationId> --format pptx --out ./deck.pptx
```

## Chat (Workspace のみ)

```bash
gog chat spaces list
gog chat spaces find "Engineering"
gog chat spaces create "Engineering" --member alice@company.com
gog chat messages list spaces/<spaceId> --max 5
gog chat messages list spaces/<spaceId> --unread
gog chat messages list spaces/<spaceId> --thread <threadId>
gog chat messages send spaces/<spaceId> --text "メッセージ"
gog chat threads list spaces/<spaceId>
gog chat dm space user@company.com
gog chat dm send user@company.com --text "ping"
```

## Classroom (Workspace for Education)

```bash
gog classroom courses list / get / create / update / archive / url
gog classroom roster <courseId>
gog classroom coursework list / get / create / update / assignees
gog classroom materials list / create
gog classroom submissions list / get / grade / return / turn-in / reclaim
gog classroom announcements list / create / update / assignees
gog classroom topics list / create / update
gog classroom invitations list / create / accept
gog classroom guardians list / get / delete
gog classroom profile get
```

## People

```bash
gog people me
gog people get people/<userId>
gog people search "名前" --max 5
gog people relations
gog people relations people/<userId> --type manager
```

## Groups (Workspace のみ)

```bash
gog groups list
gog groups members engineering@company.com
```

## Keep (Workspace + サービスアカウント)

```bash
gog keep list --account you@yourdomain.com
gog keep get <noteId>
gog keep search <query>
gog keep attachment <attachmentName> --out ./attachment.bin
```

## 設定

```bash
gog config path / list / keys
gog config get <key>
gog config set <key> <value>
gog config unset <key>
```

## 環境変数

| 変数 | 説明 |
|------|------|
| `GOG_ACCOUNT` | デフォルトアカウント |
| `GOG_CLIENT` | OAuth クライアント名 |
| `GOG_JSON` | デフォルト JSON 出力 |
| `GOG_PLAIN` | デフォルト plain 出力 |
| `GOG_COLOR` | カラーモード (auto/always/never) |
| `GOG_TIMEZONE` | デフォルトタイムゾーン |
| `GOG_ENABLE_COMMANDS` | コマンド許可リスト |
| `GOG_KEYRING_BACKEND` | キーリングバックエンド |
| `GOG_KEYRING_PASSWORD` | ファイルキーリングのパスワード |

## スクリプト例

```bash
# メール → 添付ダウンロード
gog gmail search 'newer_than:7d has:attachment' --max 10
gog gmail thread get <threadId> --download --out-dir ./attachments

# 今日のカレンダーを JSON で
gog calendar events primary --today --json

# Drive から PDF 一括ダウンロード
gog --json drive search "invoice filetype:pdf" --max 20 | \
  jq -r '.files[] | .id' | while read fileId; do gog drive download "$fileId"; done

# 送信者のメールをまとめてラベル付け
gog --json gmail search 'from:noreply@example.com' --max 200 | \
  jq -r '.threads[].id' | xargs -n 50 gog gmail labels modify --add IMPORTANT

# CSV → スプレッドシート更新
cat data.csv | tr ',' '|' | gog sheets update <spreadsheetId> 'Sheet1!A1'
```

## 関連リンク

- [gogcli GitHub](https://github.com/steipete/gogcli)
- [Gmail API](https://developers.google.com/gmail/api)
- [Calendar API](https://developers.google.com/calendar)
- [Drive API](https://developers.google.com/drive)
- [Sheets API](https://developers.google.com/sheets)
- [Tasks API](https://developers.google.com/tasks)
- [People API](https://developers.google.com/people)
- [Cloud Identity API](https://cloud.google.com/identity/docs/reference/rest)
- [Classroom API](https://developers.google.com/classroom)
- [Chat API](https://developers.google.com/workspace/chat)
- [Keep API](https://developers.google.com/keep)

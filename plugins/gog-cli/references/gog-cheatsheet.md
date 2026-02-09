# gog CLI チートシート

Google Suite CLI (gogcli) のクイックリファレンス。
Gmail, Calendar, Drive, Contacts, Tasks, Sheets, Chat, Docs, Slides, Classroom, Groups, Keep をターミナルから操作可能。

## インストール

```bash
# Homebrew
brew install steipete/tap/gogcli

# ソースからビルド
git clone https://github.com/steipete/gogcli.git
cd gogcli && make
```

## 認証セットアップ

### 1. OAuth2 クレデンシャルの保存

```bash
gog auth credentials ~/Downloads/client_secret_....json
```

複数 OAuth クライアント:
```bash
gog --client work auth credentials ~/Downloads/work-client.json
gog auth credentials list
```

### 2. アカウント認可

```bash
gog auth add you@gmail.com
```

### 3. 動作確認

```bash
export GOG_ACCOUNT=you@gmail.com
gog gmail labels list
```

### アカウント管理

```bash
gog auth list                    # アカウント一覧
gog auth list --check            # トークン検証
gog auth status                  # 現在のアカウント状態
gog auth remove <email>          # アカウント削除
gog auth alias set work work@company.com  # エイリアス設定
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

### 検索・閲覧

```bash
gog gmail search 'newer_than:7d' --max 10
gog gmail thread get <threadId>
gog gmail thread get <threadId> --download --out-dir ./attachments
gog gmail get <messageId>
gog gmail url <threadId>
```

### メッセージ検索（メッセージ単位）

```bash
gog gmail messages search 'newer_than:7d' --max 10
gog gmail messages search 'newer_than:7d' --include-body --json
```

### 送信

```bash
gog gmail send --to a@b.com --subject "件名" --body "本文"
gog gmail send --to a@b.com --subject "件名" --body-file ./message.txt
gog gmail send --to a@b.com --subject "件名" --body-html "<p>HTML本文</p>"
```

### 下書き

```bash
gog gmail drafts list
gog gmail drafts create --to a@b.com --subject "件名" --body "本文"
gog gmail drafts update <draftId> --subject "更新" --body "更新"
gog gmail drafts send <draftId>
```

### ラベル管理

```bash
gog gmail labels list
gog gmail labels get INBOX --json
gog gmail labels create "My Label"
gog gmail thread modify <threadId> --add STARRED --remove INBOX
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

### 設定

```bash
gog gmail vacation get
gog gmail vacation enable --subject "Out of office" --message "..."
gog gmail vacation disable
gog gmail sendas list
gog gmail forwarding list
gog gmail autoforward get
```

### メール追跡

```bash
gog gmail track setup --worker-url https://gog-email-tracker.<acct>.workers.dev
gog gmail send --to a@b.com --subject "件名" --body-html "<p>本文</p>" --track
gog gmail track opens <tracking_id>
gog gmail track opens --to recipient@example.com
gog gmail track status
```

## Calendar

### イベント一覧

```bash
gog calendar events <calId> --today
gog calendar events <calId> --tomorrow
gog calendar events <calId> --week
gog calendar events <calId> --days 3
gog calendar events <calId> --from today --to friday
gog calendar events --all                    # 全カレンダー
```

### イベント検索

```bash
gog calendar search "meeting" --today
gog calendar search "meeting" --days 365
```

### イベント作成

```bash
gog calendar create <calId> \
  --summary "ミーティング" \
  --from 2025-01-15T10:00:00Z \
  --to 2025-01-15T11:00:00Z \
  --attendees "alice@example.com,bob@example.com" \
  --location "Zoom"
```

### イベント更新・削除

```bash
gog calendar update <calId> <eventId> --summary "更新" --send-updates all
gog calendar delete <calId> <eventId>
```

### 招待応答

```bash
gog calendar respond <calId> <eventId> --status accepted
gog calendar respond <calId> <eventId> --status declined
gog calendar respond <calId> <eventId> --status tentative
```

### 空き時間確認

```bash
gog calendar freebusy --calendars "primary" \
  --from 2025-01-15T00:00:00Z --to 2025-01-16T00:00:00Z
gog calendar conflicts --calendars "primary" --today
```

### 特殊イベント

```bash
gog calendar focus-time --from ... --to ...
gog calendar out-of-office --from ... --to ... --all-day
gog calendar working-location --type office --office-label "HQ" --from ... --to ...
```

### チームカレンダー

```bash
gog calendar team <group-email> --today
gog calendar team <group-email> --week
gog calendar team <group-email> --freebusy
```

### その他

```bash
gog calendar calendars                # カレンダー一覧
gog calendar colors                   # 利用可能な色
gog time now                          # 現在時刻
gog time now --timezone UTC
```

## Drive

### ファイル一覧・検索

```bash
gog drive ls --max 20
gog drive ls --parent <folderId>
gog drive search "invoice" --max 20
gog drive get <fileId>
gog drive url <fileId>
```

### アップロード・ダウンロード

```bash
gog drive upload ./path/to/file --parent <folderId>
gog drive download <fileId> --out ./file.bin
gog drive download <fileId> --format pdf --out ./exported.pdf
```

### ファイル管理

```bash
gog drive mkdir "New Folder" --parent <parentId>
gog drive rename <fileId> "New Name"
gog drive move <fileId> --parent <destId>
gog drive copy <fileId> "Copy Name"
gog drive delete <fileId>
```

### 権限

```bash
gog drive permissions <fileId>
gog drive share <fileId> --to user --email user@example.com --role reader
gog drive unshare <fileId> --permission-id <permId>
```

### 共有ドライブ

```bash
gog drive drives --max 100
```

## Contacts

```bash
gog contacts list --max 50
gog contacts search "名前" --max 50
gog contacts get people/<resourceName>
gog contacts get user@example.com

gog contacts create --given-name "太郎" --family-name "田中" --email "taro@example.com"
gog contacts update people/<resourceName> --given-name "更新"
gog contacts delete people/<resourceName>

# その他の連絡先
gog contacts other list --max 50
gog contacts other search "John" --max 50

# Workspace ディレクトリ
gog contacts directory list --max 50
gog contacts directory search "Jane" --max 50
```

## Tasks

```bash
# タスクリスト
gog tasks lists --max 50
gog tasks lists create <title>

# タスク操作
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
# 読み取り
gog sheets metadata <spreadsheetId>
gog sheets get <spreadsheetId> 'Sheet1!A1:B10'

# 書き込み
gog sheets update <spreadsheetId> 'A1' 'val1|val2,val3|val4'
gog sheets update <spreadsheetId> 'A1' --values-json '[["a","b"],["c","d"]]'
gog sheets append <spreadsheetId> 'Sheet1!A:C' 'new|row|data'
gog sheets clear <spreadsheetId> 'Sheet1!A1:B10'

# フォーマット
gog sheets format <spreadsheetId> 'Sheet1!A1:B2' \
  --format-json '{"textFormat":{"bold":true}}' \
  --format-fields 'userEnteredFormat.textFormat.bold'

# 作成・エクスポート
gog sheets create "新しいスプレッドシート" --sheets "Sheet1,Sheet2"
gog sheets export <spreadsheetId> --format pdf --out ./sheet.pdf
gog sheets copy <spreadsheetId> "コピー名"
```

## Docs / Slides

```bash
# Docs
gog docs info <docId>
gog docs cat <docId> --max-bytes 10000
gog docs create "My Doc"
gog docs copy <docId> "Copy"
gog docs export <docId> --format pdf --out ./doc.pdf

# Slides
gog slides info <presentationId>
gog slides create "My Deck"
gog slides copy <presentationId> "Copy"
gog slides export <presentationId> --format pptx --out ./deck.pptx
```

## Chat (Workspace のみ)

```bash
gog chat spaces list
gog chat spaces find "Engineering"
gog chat spaces create "Engineering" --member alice@company.com

gog chat messages list spaces/<spaceId> --max 5
gog chat messages list spaces/<spaceId> --unread
gog chat messages send spaces/<spaceId> --text "メッセージ"

gog chat dm space user@company.com
gog chat dm send user@company.com --text "ping"
```

## Groups (Workspace のみ)

```bash
gog groups list
gog groups members engineering@company.com
```

## People

```bash
gog people me
gog people get people/<userId>
gog people search "名前" --max 5
gog people relations
```

## Keep (Workspace のみ)

```bash
gog keep list --account you@yourdomain.com
gog keep get <noteId>
gog keep search <query>
gog keep attachment <attachmentName> --out ./attachment.bin
```

## 設定

```bash
gog config path                      # 設定ファイルパス
gog config list                      # 設定一覧
gog config get default_timezone      # 値取得
gog config set default_timezone UTC  # 値設定
gog config unset default_timezone    # 値削除
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

### 最近のメールを検索して添付ファイルをダウンロード

```bash
gog gmail search 'newer_than:7d has:attachment' --max 10
gog gmail thread get <threadId> --download --out-dir ./attachments
```

### 今日のカレンダーイベントを JSON で取得

```bash
gog calendar events primary --today --json
```

### Drive から PDF を一括ダウンロード

```bash
gog --json drive search "invoice filetype:pdf" --max 20 | \
  jq -r '.files[] | .id' | \
  while read fileId; do gog drive download "$fileId"; done
```

### 特定の送信者のメールをまとめてラベル付け

```bash
gog --json gmail search 'from:noreply@example.com' --max 200 | \
  jq -r '.threads[].id' | \
  xargs -n 50 gog gmail labels modify --add IMPORTANT
```

### CSV からスプレッドシートを更新

```bash
cat data.csv | tr ',' '|' | gog sheets update <spreadsheetId> 'Sheet1!A1'
```

## 関連リンク

- [gogcli GitHub リポジトリ](https://github.com/steipete/gogcli)
- [Gmail API](https://developers.google.com/gmail/api)
- [Calendar API](https://developers.google.com/calendar)
- [Drive API](https://developers.google.com/drive)
- [Sheets API](https://developers.google.com/sheets)
- [Tasks API](https://developers.google.com/tasks)
- [People API](https://developers.google.com/people)

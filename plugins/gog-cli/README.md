# gog-cli プラグイン

Google Suite CLI ([gogcli](https://github.com/steipete/gogcli)) の操作を支援する Claude Code プラグイン。

Gmail, Calendar, Drive, Contacts, Tasks, Sheets, Docs, Slides, Chat, Classroom, People, Groups, Keep の全サービスをカバーします。

## 前提条件

- [gog CLI](https://github.com/steipete/gogcli) がインストール済みであること
- OAuth2 クレデンシャルが設定済みであること

```bash
brew install steipete/tap/gogcli
gog auth credentials ~/Downloads/client_secret_....json
gog auth add you@gmail.com
```

## コマンド

| コマンド | 説明 |
|----------|------|
| `/gog-auth` | 認証・アカウント管理（サービスアカウント含む） |
| `/gog-gmail` | Gmail 操作（検索・送信・ラベル・追跡・Watch等） |
| `/gog-calendar` | Calendar 操作（イベント・繰り返し・特殊イベント・チーム等） |
| `/gog-drive` | Drive 操作（ファイル検索・アップロード・ダウンロード・共有等） |
| `/gog-sheets` | Sheets 操作（読み書き・作成・フォーマット・エクスポート等） |
| `/gog-tasks` | Tasks 操作（タスク一覧・追加・完了・繰り返し等） |
| `/gog-contacts` | Contacts 操作（検索・作成・更新・ディレクトリ等） |
| `/gog-docs` | Docs 操作（情報取得・テキスト取得・作成・エクスポート） |
| `/gog-slides` | Slides 操作（情報取得・作成・エクスポート） |
| `/gog-chat` | Chat 操作（スペース・メッセージ・DM / Workspace のみ） |
| `/gog-classroom` | Classroom 操作（コース・課題・成績 / Workspace for Education） |
| `/gog-people` | People 操作（プロフィール・検索・リレーション） |
| `/gog-groups` | Groups 操作（グループ一覧・メンバー / Workspace のみ） |
| `/gog-keep` | Keep 操作（ノート一覧・検索 / Workspace + サービスアカウント） |

## スキル

### gog-helper

自然言語のリクエストを検知して自動的に gog CLI コマンドに変換するスキル。

**トリガー例:**
- 「メールを確認して」→ `gog gmail search`
- 「今日の予定を教えて」→ `gog calendar events primary --today`
- 「ファイルを検索して」→ `gog drive search`
- 「タスクを追加して」→ `gog tasks add`
- 「ドキュメントをPDFにして」→ `gog docs export --format pdf`
- 「チャットでメッセージを送って」→ `gog chat messages send`
- 「コースの一覧を見せて」→ `gog classroom courses list`

## リファレンス

| ファイル | 内容 |
|----------|------|
| `references/gog-cheatsheet.md` | 全コマンドのクイックリファレンス |
| `references/auth-reference.md` | 認証・設定・環境変数の詳細 |
| `references/gmail-reference.md` | Gmail の全コマンド詳細 |
| `references/calendar-reference.md` | Calendar の全コマンド詳細 |
| `references/classroom-reference.md` | Classroom の全コマンド詳細 |

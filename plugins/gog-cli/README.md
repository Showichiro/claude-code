# gog-cli プラグイン

Google Suite CLI ([gogcli](https://github.com/steipete/gogcli)) の操作を支援する Claude Code プラグイン。

Gmail, Calendar, Drive, Contacts, Tasks, Sheets の操作コマンドを提供します。Chat, Docs, Slides はチートシート経由で参照可能です。

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
| `/gog-auth` | 認証・アカウント管理 |
| `/gog-gmail` | Gmail 操作（検索・送信・ラベル管理等） |
| `/gog-calendar` | Calendar 操作（イベント表示・作成・更新等） |
| `/gog-drive` | Drive 操作（ファイル検索・アップロード・ダウンロード等） |
| `/gog-sheets` | Sheets 操作（読み書き・作成・エクスポート等） |
| `/gog-tasks` | Tasks 操作（タスク一覧・追加・完了等） |
| `/gog-contacts` | Contacts 操作（検索・作成・更新等） |

## スキル

### gog-helper

自然言語のリクエストを検知して自動的に gog CLI コマンドに変換するスキル。

**トリガー例:**
- 「メールを確認して」→ `gog gmail search`
- 「今日の予定を教えて」→ `gog calendar events primary --today`
- 「ファイルを検索して」→ `gog drive search`
- 「タスクを追加して」→ `gog tasks add`

## リファレンス

- `references/gog-cheatsheet.md` — 全コマンドのクイックリファレンス

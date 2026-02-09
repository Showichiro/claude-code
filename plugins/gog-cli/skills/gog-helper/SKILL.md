---
description: |-
  Google Suite CLI (gog) の操作を支援。
  「メール」「Gmail」「カレンダー」「予定」「Drive」「スプレッドシート」
  「gog」「連絡先」「タスク」「Google」などのキーワードで自動トリガー。
  gog コマンドを使用して Google サービスを操作。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-helper

ユーザーの自然言語リクエストを検知して gog CLI (Google Suite CLI) の操作を支援するスキル。

## トリガーキーワード

### 明示的キーワード
- `gog`, `gogcli`
- `Gmail`, `Google Calendar`, `Google Drive`
- `Google Sheets`, `Google Tasks`, `Google Chat`
- `Google Docs`, `Google Slides`

### 意図推定キーワード（メール系）
- `メールを確認`, `メールを検索`, `メールを送って`
- `未読メール`, `最近のメール`
- `メールの添付ファイル`, `メールをダウンロード`
- `下書きを作成`, `下書きを送信`

### 意図推定キーワード（カレンダー系）
- `今日の予定`, `明日の予定`, `今週の予定`
- `予定を作成`, `ミーティングを入れて`
- `空き時間を確認`, `スケジュール`
- `予定を更新`, `予定を削除`

### 意図推定キーワード（Drive / ファイル系）
- `ファイルを検索`, `ファイルをアップロード`
- `ファイルをダウンロード`, `共有設定`
- `フォルダを作成`, `ファイルを移動`

### 意図推定キーワード（その他）
- `スプレッドシート`, `シートを読む`, `シートに書き込む`
- `連絡先を検索`, `連絡先を追加`
- `タスクを追加`, `タスク一覧`, `タスク完了`
- `ドキュメントをエクスポート`, `PDF に変換`

## ワークフロー

```
キーワード検出
  │
  ├─ gog インストール確認
  │     └─ 未インストール → brew install steipete/tap/gogcli を提案
  │
  ├─ アカウント設定確認
  │     ├─ GOG_ACCOUNT 環境変数あり → そのまま使用
  │     └─ なし → gog auth list で確認、必要なら --account 指定
  │
  ├─ 意図の分類
  │     ├─ メール操作 → Gmail コマンド群
  │     ├─ 予定操作 → Calendar コマンド群
  │     ├─ ファイル操作 → Drive コマンド群
  │     ├─ シート操作 → Sheets コマンド群
  │     ├─ タスク操作 → Tasks コマンド群
  │     ├─ 連絡先操作 → Contacts コマンド群
  │     ├─ チャット → Chat コマンド群
  │     └─ 不明 → AskUserQuestion で確認
  │
  └─ gog コマンド実行
        ├─ 成功 → 結果を表示
        ├─ 認証エラー → gog auth add を案内
        └─ スコープ不足 → gog auth add --services ... --force-consent を案内
```

## 意図の推定ロジック

| ユーザーの発言例 | 推定される操作 |
|-----------------|---------------|
| 「最近のメールを確認して」 | `gog gmail search 'newer_than:7d' --max 10` |
| 「○○にメールを送って」 | `gog gmail send --to ... --subject ... --body ...` |
| 「未読メールを見せて」 | `gog gmail search 'is:unread' --max 20` |
| 「添付ファイルをダウンロード」 | `gog gmail thread get <id> --download` |
| 「今日の予定を教えて」 | `gog calendar events primary --today` |
| 「明日ミーティングを入れて」 | `gog calendar create primary --summary ... --from ... --to ...` |
| 「空いてる時間を確認」 | `gog calendar freebusy --calendars primary --from ... --to ...` |
| 「Drive でファイルを探して」 | `gog drive search "..." --max 20` |
| 「ファイルをアップロードして」 | `gog drive upload ./path --parent <folderId>` |
| 「スプレッドシートを読んで」 | `gog sheets get <id> 'Sheet1!A1:Z100'` |
| 「シートにデータを書き込んで」 | `gog sheets update <id> 'A1' 'data'` |
| 「連絡先を検索して」 | `gog contacts search "名前"` |
| 「タスクを追加して」 | `gog tasks add <listId> --title "タスク名"` |
| 「タスクを完了にして」 | `gog tasks done <listId> <taskId>` |
| 「ドキュメントを PDF にして」 | `gog docs export <docId> --format pdf` |

## 実行コマンド

### インストール確認

```bash
which gog
```

未インストールの場合:
```bash
brew install steipete/tap/gogcli
```

### アカウント確認

```bash
gog auth list
gog auth status
```

### 出力形式

スクリプト連携や後続処理が必要な場合は `--json` を付ける:
```bash
gog gmail search 'newer_than:7d' --max 10 --json
gog calendar events primary --today --json
```

## エラーハンドリング

| エラー状況 | 対応 |
|-----------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| アカウント未設定 | `gog auth credentials <path>` → `gog auth add <email>` を案内 |
| 認証エラー / トークン期限切れ | `gog auth add <email> --force-consent` を案内 |
| スコープ不足 (403) | `gog auth add <email> --services <service> --force-consent` を案内 |
| API レートリミット | 少し待ってからリトライを提案 |
| アカウント指定なし | `gog auth list` で確認し `--account` 指定を案内 |

## 破壊的操作の確認

以下の操作は実行前に必ずユーザーに確認:

- メール送信 (`gog gmail send`)
- メール削除 (`gog gmail batch delete`)
- イベント削除 (`gog calendar delete`)
- ファイル削除 (`gog drive delete`)
- 連絡先削除 (`gog contacts delete`)
- タスク削除 / クリア (`gog tasks delete`, `gog tasks clear`)

## 補足

- 曖昧なリクエストの場合は AskUserQuestion で確認
- JSON 出力が後続処理に便利な場合は自動で `--json` を付与
- 大量のデータを取得する際は `--max` で件数を制限
- カレンダーの時刻指定は ISO 8601 形式（例: `2025-01-15T10:00:00Z`）
- `GOG_ACCOUNT` 環境変数でデフォルトアカウントを設定可能

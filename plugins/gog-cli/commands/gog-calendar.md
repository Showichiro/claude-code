---
description: |-
  gog CLI で Google Calendar を操作する。
  「/gog-calendar [操作] [オプション]」でイベントの表示・作成・更新・削除等を実行。
  events, create, update, delete, freebusy, search 等をサポート。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# gog-calendar

gog CLI を使って Google Calendar を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `events` | イベント一覧取得 |
| `search` | イベント検索 |
| `create` | イベント作成 |
| `update` | イベント更新 |
| `delete` | イベント削除 |
| `respond` | 招待に応答 |
| `freebusy` | 空き時間確認 |
| `conflicts` | 予定の競合確認 |
| `calendars` | カレンダー一覧 |
| `team` | チームカレンダー |

## ワークフロー

```text
/gog-calendar [操作] [引数...] 実行
  │
  ├─ gog インストール確認
  │
  ├─ 操作の判定
  │     ├─ events → 日付範囲を確認して実行
  │     ├─ create → summary, from, to を確認して実行
  │     ├─ update → eventId と変更内容を確認
  │     ├─ delete → eventId を確認（確認必須）
  │     └─ freebusy → カレンダーと日付範囲を確認
  │
  └─ gog calendar [操作] 実行
```

## 実行手順

### イベント一覧

```bash
gog calendar events primary --today
gog calendar events primary --tomorrow
gog calendar events primary --week
gog calendar events primary --days 3
gog calendar events primary --from today --to friday
gog calendar events --all                    # 全カレンダー
```

### イベント検索

```bash
gog calendar search "meeting" --today
gog calendar search "meeting" --days 30
```

### イベント作成

```bash
gog calendar create primary \
  --summary "ミーティング" \
  --from 2025-01-15T10:00:00Z \
  --to 2025-01-15T11:00:00Z

# 参加者付き
gog calendar create primary \
  --summary "Team Sync" \
  --from 2025-01-15T14:00:00Z \
  --to 2025-01-15T15:00:00Z \
  --attendees "alice@example.com,bob@example.com" \
  --location "Zoom" \
  --send-updates all
```

### イベント更新

```bash
gog calendar update <calId> <eventId> \
  --summary "Updated Meeting" \
  --from 2025-01-15T11:00:00Z \
  --to 2025-01-15T12:00:00Z \
  --send-updates all
```

### 空き時間確認

```bash
gog calendar freebusy --calendars "primary" \
  --from 2025-01-15T00:00:00Z --to 2025-01-16T00:00:00Z

gog calendar conflicts --calendars "primary" --today
```

### 招待応答

```bash
gog calendar respond <calId> <eventId> --status accepted
gog calendar respond <calId> <eventId> --status declined
gog calendar respond <calId> <eventId> --status tentative
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| カレンダーID 未指定 | `primary` をデフォルトで使用 |
| 時刻フォーマットエラー | ISO 8601 形式を案内 |
| 権限エラー | `gog auth add --services calendar --force-consent` を案内 |

## 使用例

```bash
# 今日の予定
/gog-calendar events primary --today

# 予定を作成
/gog-calendar create primary --summary "会議" --from 2025-01-15T10:00:00Z --to 2025-01-15T11:00:00Z

# 空き時間確認
/gog-calendar freebusy --calendars primary --from 2025-01-15T00:00:00Z --to 2025-01-16T00:00:00Z
```

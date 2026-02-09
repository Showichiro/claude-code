---
description: |-
  gog CLI で Google Calendar を操作する。
  「/gog-calendar [操作] [オプション]」でイベントの表示・作成・更新・削除・チーム・特殊イベント等を実行。
  events, create, update, delete, respond, propose-time, freebusy, conflicts, team, focus-time, out-of-office, working-location 等をサポート。
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
| `events` | イベント一覧（`--today`, `--week`, `--days`, `--all`） |
| `event` / `get` | イベント詳細 |
| `search` | イベント検索 |
| `create` | イベント作成（繰り返し・リマインダー対応） |
| `update` | イベント更新（`--add-attendee` 対応） |
| `delete` | イベント削除 |
| `respond` | 招待に応答（accepted/declined/tentative） |
| `propose-time` | 新しい時間を提案 |
| `freebusy` | 空き時間確認 |
| `conflicts` | 予定の競合確認 |
| `calendars` | カレンダー一覧 |
| `acl` | アクセス制御ルール |
| `colors` | 利用可能な色一覧 |
| `users` | Workspace ユーザー一覧 |
| `team` | チームカレンダー（Workspace） |
| `focus-time` | 集中時間イベント作成 |
| `out-of-office` | 不在イベント作成 |
| `working-location` | 勤務場所イベント作成 |

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
  │     ├─ respond → eventId とステータスを確認
  │     └─ freebusy → カレンダーと日付範囲を確認
  │
  └─ gog calendar [操作] 実行
```

## 実行手順

### イベント一覧

```bash
gog calendar events <calId> --today
gog calendar events <calId> --tomorrow
gog calendar events <calId> --week
gog calendar events <calId> --days 3
gog calendar events <calId> --from today --to friday
gog calendar events <calId> --from today --to friday --weekday   # 曜日列を追加
gog calendar events --all                    # 全カレンダー
```

### イベント詳細

```bash
gog calendar event <calId> <eventId>
gog calendar get <calId> <eventId>
gog calendar get <calId> <eventId> --json    # ローカル時刻・曜日フィールド付き
```

### イベント検索

```bash
gog calendar search "meeting" --today
gog calendar search "meeting" --tomorrow
gog calendar search "meeting" --days 365
gog calendar search "meeting" --from 2025-01-01T00:00:00Z --to 2025-01-31T00:00:00Z --max 50
```

### イベント作成

```bash
gog calendar create <calId> \
  --summary "ミーティング" \
  --from 2025-01-15T10:00:00Z \
  --to 2025-01-15T11:00:00Z

# 参加者・場所・通知付き
gog calendar create <calId> \
  --summary "Team Sync" \
  --from 2025-01-15T14:00:00Z \
  --to 2025-01-15T15:00:00Z \
  --attendees "alice@example.com,bob@example.com" \
  --location "Zoom" \
  --send-updates all

# 繰り返し + リマインダー
gog calendar create <calId> \
  --summary "Payment" \
  --from 2025-02-11T09:00:00-03:00 \
  --to 2025-02-11T09:15:00-03:00 \
  --rrule "RRULE:FREQ=MONTHLY;BYMONTHDAY=11" \
  --reminder "email:3d" \
  --reminder "popup:30m"
```

### イベント更新

```bash
gog calendar update <calId> <eventId> \
  --summary "Updated Meeting" \
  --from 2025-01-15T11:00:00Z \
  --to 2025-01-15T12:00:00Z \
  --send-updates all

# 既存参加者を保持して追加
gog calendar update <calId> <eventId> \
  --add-attendee "alice@example.com,bob@example.com"
```

### イベント削除

```bash
gog calendar delete <calId> <eventId>
```

### 招待応答

```bash
gog calendar respond <calId> <eventId> --status accepted
gog calendar respond <calId> <eventId> --status declined
gog calendar respond <calId> <eventId> --status tentative
gog calendar respond <calId> <eventId> --status declined --send-updates externalOnly
```

### 新しい時間を提案

```bash
gog calendar propose-time <calId> <eventId>
gog calendar propose-time <calId> <eventId> --open          # ブラウザで開く
gog calendar propose-time <calId> <eventId> --decline --comment "Can we do 5pm?"
```

### 空き時間・競合確認

```bash
gog calendar freebusy --calendars "primary,work@example.com" \
  --from 2025-01-15T00:00:00Z --to 2025-01-16T00:00:00Z

gog calendar conflicts --calendars "primary,work@example.com" --today
```

### 特殊イベント

```bash
# 集中時間
gog calendar focus-time --from 2025-01-15T13:00:00Z --to 2025-01-15T14:00:00Z

# 不在
gog calendar out-of-office --from 2025-01-20 --to 2025-01-21 --all-day

# 勤務場所
gog calendar working-location --type office --office-label "HQ" --from 2025-01-22 --to 2025-01-23

# --event-type フラグでも作成可能
gog calendar create primary --event-type focus-time --from ... --to ...
gog calendar create primary --event-type out-of-office --from ... --to ... --all-day
gog calendar create primary --event-type working-location \
  --working-location-type office --working-office-label "HQ" --from ... --to ...
```

### チームカレンダー（Workspace）

```bash
gog calendar team <group-email> --today
gog calendar team <group-email> --week
gog calendar team <group-email> --freebusy      # 忙しい/空きブロックのみ
gog calendar team <group-email> --query "standup"
```

### その他

```bash
gog calendar calendars                # カレンダー一覧
gog calendar acl <calendarId>         # アクセス制御ルール
gog calendar colors                   # 利用可能な色
gog calendar users                    # Workspace ユーザー一覧
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| カレンダーID 未指定 | `primary` をデフォルトで使用 |
| 時刻フォーマットエラー | ISO 8601 形式を案内 |
| 権限エラー | `gog auth add --services calendar --force-consent` を案内 |
| チーム機能エラー | Cloud Identity API の有効化を案内 |

## 使用例

```bash
/gog-calendar events primary --today
/gog-calendar create primary --summary "会議" --from 2025-01-15T10:00:00Z --to 2025-01-15T11:00:00Z
/gog-calendar team engineering@company.com --week
/gog-calendar focus-time --from 2025-01-15T13:00:00Z --to 2025-01-15T14:00:00Z
```

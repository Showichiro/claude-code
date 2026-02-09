# Calendar リファレンス

## カレンダー管理

```bash
gog calendar calendars                        # カレンダー一覧
gog calendar acl <calendarId>                 # アクセス制御ルール
gog calendar colors                           # 利用可能な色
gog calendar users                            # Workspace ユーザー一覧
```

## イベント一覧

```bash
gog calendar events <calId> --today
gog calendar events <calId> --tomorrow
gog calendar events <calId> --week                           # 月-日（--week-start で変更可）
gog calendar events <calId> --days 3
gog calendar events <calId> --from today --to friday
gog calendar events <calId> --from today --to friday --weekday  # 曜日列
gog calendar events <calId> --from 2025-01-01T00:00:00Z --to 2025-01-08T00:00:00Z
gog calendar events --all                                    # 全カレンダー
```

ヒント: `GOG_CALENDAR_WEEKDAY=1` で `--weekday` をデフォルト化。

## イベント詳細

```bash
gog calendar event <calId> <eventId>
gog calendar get <calId> <eventId>
gog calendar get <calId> <eventId> --json     # startDayOfWeek, startLocal 等を含む
```

## イベント検索

```bash
gog calendar search "meeting" --today
gog calendar search "meeting" --tomorrow
gog calendar search "meeting" --days 365
gog calendar search "meeting" --from ... --to ... --max 50
```

デフォルト: 30日前〜90日先。`--from`/`--to`/`--today`/`--week`/`--days` で上書き。

## イベント作成

```bash
gog calendar create <calId> \
  --summary "Meeting" \
  --from 2025-01-15T10:00:00Z \
  --to 2025-01-15T11:00:00Z

# 参加者・場所・通知
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

## イベント更新

```bash
gog calendar update <calId> <eventId> \
  --summary "Updated" \
  --from ... --to ... \
  --send-updates all

# 参加者追加（既存を維持）
gog calendar update <calId> <eventId> \
  --add-attendee "alice@example.com,bob@example.com"
```

## イベント削除

```bash
gog calendar delete <calId> <eventId>
```

## 招待応答

```bash
gog calendar respond <calId> <eventId> --status accepted
gog calendar respond <calId> <eventId> --status declined
gog calendar respond <calId> <eventId> --status tentative
gog calendar respond <calId> <eventId> --status declined --send-updates externalOnly
```

## 新しい時間を提案

```bash
gog calendar propose-time <calId> <eventId>
gog calendar propose-time <calId> <eventId> --open
gog calendar propose-time <calId> <eventId> --decline --comment "Can we do 5pm?"
```

## 空き時間・競合

```bash
gog calendar freebusy --calendars "primary,work@example.com" \
  --from 2025-01-15T00:00:00Z --to 2025-01-16T00:00:00Z

gog calendar conflicts --calendars "primary,work@example.com" --today
```

## 特殊イベント

```bash
# 集中時間
gog calendar focus-time --from ... --to ...

# 不在
gog calendar out-of-office --from ... --to ... --all-day

# 勤務場所
gog calendar working-location --type office --office-label "HQ" --from ... --to ...

# --event-type フラグでも可
gog calendar create primary --event-type focus-time --from ... --to ...
gog calendar create primary --event-type out-of-office --from ... --to ... --all-day
gog calendar create primary --event-type working-location \
  --working-location-type office --working-office-label "HQ" --from ... --to ...
```

## チームカレンダー（Workspace）

Cloud Identity API が必要。

```bash
gog calendar team <group-email> --today
gog calendar team <group-email> --week
gog calendar team <group-email> --freebusy       # 忙しい/空きブロックのみ
gog calendar team <group-email> --query "standup"
```

## 時刻

```bash
gog time now
gog time now --timezone UTC
gog calendar time --timezone America/New_York
```

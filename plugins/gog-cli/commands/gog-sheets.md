---
description: |-
  gog CLI で Google Sheets を操作する。
  「/gog-sheets [操作] [オプション]」でスプレッドシートの読み書き・作成・エクスポートを実行。
  get, update, append, clear, create, export, format 等をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-sheets

gog CLI を使って Google Sheets を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `metadata` | メタデータ取得 |
| `get` | セル範囲の読み取り |
| `update` | セル範囲の書き込み |
| `append` | 行の追加 |
| `clear` | セル範囲のクリア |
| `format` | セルのフォーマット |
| `create` | 新規スプレッドシート作成 |
| `export` | エクスポート (PDF/XLSX) |
| `copy` | コピー |

## 実行手順

### 読み取り

```bash
gog sheets metadata <spreadsheetId>
gog sheets get <spreadsheetId> 'Sheet1!A1:B10'
```

### 書き込み

```bash
# パイプ区切り (| で列区切り、, で行区切り)
gog sheets update <spreadsheetId> 'A1' 'val1|val2,val3|val4'

# JSON 形式
gog sheets update <spreadsheetId> 'A1' --values-json '[["a","b"],["c","d"]]'

# 行の追加
gog sheets append <spreadsheetId> 'Sheet1!A:C' 'new|row|data'
```

### クリア・フォーマット

```bash
gog sheets clear <spreadsheetId> 'Sheet1!A1:B10'
gog sheets format <spreadsheetId> 'Sheet1!A1:B2' \
  --format-json '{"textFormat":{"bold":true}}' \
  --format-fields 'userEnteredFormat.textFormat.bold'
```

### 作成・エクスポート

```bash
gog sheets create "新しいスプレッドシート" --sheets "Sheet1,Sheet2"
gog sheets export <spreadsheetId> --format pdf --out ./sheet.pdf
gog sheets export <spreadsheetId> --format xlsx --out ./sheet.xlsx
gog sheets copy <spreadsheetId> "コピー名"
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| シート名エラー | メタデータで正しいシート名を確認 |
| 範囲指定エラー | `Sheet1!A1:B10` 形式を案内 |
| 権限エラー | `gog auth add --services sheets --force-consent` を案内 |

## 使用例

```bash
# シートの内容を読む
/gog-sheets get <spreadsheetId> 'Sheet1!A1:Z100'

# データを書き込む
/gog-sheets update <spreadsheetId> 'Sheet1!A1' 'name|age,Alice|30,Bob|25'

# PDF エクスポート
/gog-sheets export <spreadsheetId> --format pdf --out ./report.pdf
```

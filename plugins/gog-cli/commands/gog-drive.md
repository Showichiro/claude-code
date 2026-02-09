---
description: |-
  gog CLI で Google Drive を操作する。
  「/gog-drive [操作] [オプション]」でファイルの検索・アップロード・ダウンロード・管理を実行。
  ls, search, upload, download, mkdir, share 等をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-drive

gog CLI を使って Google Drive を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `ls` | ファイル一覧 |
| `search` | ファイル検索 |
| `get` | ファイルメタデータ取得 |
| `upload` | アップロード |
| `download` | ダウンロード / エクスポート |
| `mkdir` | フォルダ作成 |
| `rename` | リネーム |
| `move` | 移動 |
| `copy` | コピー |
| `delete` | ゴミ箱へ移動 |
| `share` / `unshare` | 共有管理 |
| `permissions` | 権限確認 |
| `url` | Web URL 取得 |
| `drives` | 共有ドライブ一覧 |

## 実行手順

### ファイル一覧・検索

```bash
gog drive ls --max 20
gog drive ls --parent <folderId> --max 20
gog drive search "invoice" --max 20
gog drive get <fileId>
gog drive url <fileId>
```

### アップロード・ダウンロード

```bash
gog drive upload ./path/to/file --parent <folderId>
gog drive download <fileId> --out ./file.bin
gog drive download <fileId> --format pdf --out ./exported.pdf
gog drive download <fileId> --format docx --out ./doc.docx
```

### ファイル管理

```bash
gog drive mkdir "New Folder" --parent <parentId>
gog drive rename <fileId> "New Name"
gog drive move <fileId> --parent <destId>
gog drive copy <fileId> "Copy Name"
gog drive delete <fileId>
```

### 共有

```bash
gog drive permissions <fileId>
gog drive share <fileId> --to user --email user@example.com --role reader
gog drive share <fileId> --to user --email user@example.com --role writer
gog drive unshare <fileId> --permission-id <permId>
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| ファイル未発見 | fileId を確認 |
| 権限エラー | `gog auth add --services drive --force-consent` を案内 |
| アップロードサイズ超過 | 分割またはリサイズを提案 |

## 使用例

```bash
# ファイル一覧
/gog-drive ls --max 20

# ファイル検索
/gog-drive search "報告書" --max 10

# ダウンロード
/gog-drive download <fileId> --out ./report.pdf

# アップロード
/gog-drive upload ./data.csv --parent <folderId>
```

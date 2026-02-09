---
description: |-
  gog CLI で Google Docs を操作する。
  「/gog-docs [操作] [オプション]」でドキュメントの情報取得・作成・コピー・エクスポートを実行。
  info, cat, create, copy, export をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-docs

gog CLI を使って Google Docs を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `info` | ドキュメント情報取得 |
| `cat` | テキスト内容取得 |
| `create` | 新規ドキュメント作成 |
| `copy` | ドキュメントコピー |
| `export` | エクスポート（PDF/DOCX/TXT） |

## 実行手順

```bash
# 情報取得
gog docs info <docId>

# テキスト取得
gog docs cat <docId> --max-bytes 10000

# 作成・コピー
gog docs create "My Doc"
gog docs copy <docId> "My Doc Copy"

# エクスポート
gog docs export <docId> --format pdf --out ./doc.pdf
gog docs export <docId> --format docx --out ./doc.docx
gog docs export <docId> --format txt --out ./doc.txt
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| 権限エラー | `gog auth add --services docs --force-consent` を案内 |

## 使用例

```bash
/gog-docs info <docId>
/gog-docs cat <docId>
/gog-docs export <docId> --format pdf --out ./report.pdf
```

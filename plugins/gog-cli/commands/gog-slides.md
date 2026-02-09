---
description: |-
  gog CLI で Google Slides を操作する。
  「/gog-slides [操作] [オプション]」でプレゼンテーションの情報取得・作成・コピー・エクスポートを実行。
  info, create, copy, export をサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# gog-slides

gog CLI を使って Google Slides を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `info` | プレゼンテーション情報取得 |
| `create` | 新規プレゼンテーション作成 |
| `copy` | プレゼンテーションコピー |
| `export` | エクスポート（PDF/PPTX） |

## 実行手順

```bash
# 情報取得
gog slides info <presentationId>

# 作成・コピー
gog slides create "My Deck"
gog slides copy <presentationId> "My Deck Copy"

# エクスポート
gog slides export <presentationId> --format pdf --out ./deck.pdf
gog slides export <presentationId> --format pptx --out ./deck.pptx
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| 権限エラー | `gog auth add --services docs --force-consent` を案内（Slides は Docs API 経由） |

## 使用例

```bash
/gog-slides info <presentationId>
/gog-slides export <presentationId> --format pptx --out ./slides.pptx
```

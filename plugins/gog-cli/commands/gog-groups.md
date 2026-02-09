---
description: |-
  gog CLI で Google Groups を操作する（Workspace のみ）。
  「/gog-groups [操作] [オプション]」でグループ一覧・メンバー確認を実行。
  list, members をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-groups

gog CLI を使って Google Groups を操作するコマンド。Workspace アカウントが必要。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `list` | 所属グループ一覧 |
| `members` | グループメンバー一覧 |

## 実行手順

```bash
# 所属グループ一覧
gog groups list

# メンバー一覧
gog groups members engineering@company.com
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| Workspace アカウントなし | Cloud Identity API と Workspace が必要であることを案内 |
| 権限エラー | `gog auth add --services groups --force-consent` を案内 |

## 使用例

```bash
/gog-groups list
/gog-groups members engineering@company.com
```

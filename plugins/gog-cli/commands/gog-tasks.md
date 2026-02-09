---
description: |-
  gog CLI で Google Tasks を操作する。
  「/gog-tasks [操作] [オプション]」でタスクの一覧・追加・完了・削除を実行。
  lists, list, add, done, undo, update, delete, clear 等をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-tasks

gog CLI を使って Google Tasks を操作するコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `lists` | タスクリスト一覧 |
| `lists create` | タスクリスト作成 |
| `list` | タスク一覧 |
| `get` | タスク詳細 |
| `add` | タスク追加 |
| `update` | タスク更新 |
| `done` | タスク完了 |
| `undo` | タスク未完了に戻す |
| `delete` | タスク削除 |
| `clear` | 完了済みタスクをクリア |

## 実行手順

### タスクリスト

```bash
gog tasks lists --max 50
gog tasks lists create "新しいリスト"
```

### タスク操作

```bash
# 一覧
gog tasks list <tasklistId> --max 50

# 追加
gog tasks add <tasklistId> --title "タスク名"
gog tasks add <tasklistId> --title "定例" --due 2025-02-01 --repeat weekly --repeat-count 4

# 更新
gog tasks update <tasklistId> <taskId> --title "新しい名前"

# 完了 / 未完了
gog tasks done <tasklistId> <taskId>
gog tasks undo <tasklistId> <taskId>

# 削除
gog tasks delete <tasklistId> <taskId>
gog tasks clear <tasklistId>
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| タスクリストID 未指定 | `gog tasks lists` で確認を案内 |
| 権限エラー | `gog auth add --services tasks --force-consent` を案内 |

## 使用例

```bash
# タスクリスト一覧
/gog-tasks lists

# タスク一覧
/gog-tasks list <tasklistId>

# タスク追加
/gog-tasks add <tasklistId> --title "レポート作成"

# タスク完了
/gog-tasks done <tasklistId> <taskId>
```

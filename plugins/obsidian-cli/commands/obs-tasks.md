---
description: |-
  Obsidianのタスクを管理する。
  「/obs-tasks [options]」でタスク一覧・操作。
  todo, done, daily, file=, verbose, total をサポート。
  タスクのトグル・完了・未完了への変更も可能。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-tasks

公式 Obsidian CLI を使用して Vault 内のタスクを管理するコマンド。

## 使い方

```
/obs-tasks                        → 全タスク一覧
/obs-tasks todo                   → 未完了タスク一覧
/obs-tasks done                   → 完了タスク一覧
/obs-tasks daily                  → デイリーノートのタスク
/obs-tasks file=Recipe            → 特定ファイルのタスク
/obs-tasks total                  → タスク数のみ
/obs-tasks toggle Recipe:8        → タスクをトグル
/obs-tasks done Recipe:8          → タスクを完了に
```

## 実行手順

```bash
# タスク一覧
obsidian tasks
obsidian tasks todo                 # 未完了のみ
obsidian tasks done                 # 完了のみ
obsidian tasks daily                # デイリーノートのタスク
obsidian tasks file="note-name"     # 特定ファイル
obsidian tasks total                # タスク数のみ
obsidian tasks verbose              # ファイルパス・行番号付き

# タスク操作
obsidian task ref="path/note.md:8" toggle    # トグル
obsidian task ref="path/note.md:8" done      # 完了
obsidian task ref="path/note.md:8" todo      # 未完了に戻す
obsidian task daily line=3 toggle             # デイリーノートのタスクをトグル
obsidian task daily line=3 done               # デイリーノートのタスクを完了
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| タスクが見つからない | `obsidian tasks verbose` でファイル・行番号を確認 |

---
description: |-
  Obsidianのデイリーノートを操作する。
  「/obs-daily [options]」でデイリーノートを開く・読む・追記・パス取得。
  read, append, prepend, path をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# obs-daily

公式 Obsidian CLI を使用してデイリーノートを操作するコマンド。

## 使い方

```
/obs-daily                        → デイリーノートを開く
/obs-daily read                   → デイリーノートの内容を読む
/obs-daily path                   → デイリーノートのパスを取得
/obs-daily append タスク内容       → デイリーノートに追記
/obs-daily prepend 朝メモ         → デイリーノートの先頭に挿入
```

## 実行手順

```bash
# デイリーノートを開く
obsidian daily

# デイリーノートのパスを取得
obsidian daily:path

# デイリーノートの内容を読む
obsidian daily:read

# デイリーノートに追記
obsidian daily:append content="- [ ] タスク"

# デイリーノートの先頭に挿入
obsidian daily:prepend content="# 朝メモ"

# 特定Vault
obsidian vault=MyVault daily
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| `obsidian` 未検出 | CLI セットアップを案内 |
| デイリーノートプラグイン未設定 | Obsidian の Daily Notes プラグイン設定を案内 |

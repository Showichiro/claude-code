---
description: |-
  Git worktree操作を支援（wtp連携）。
  「worktree作成」「別ブランチで作業」「並行開発」「wtp」「作業終了」
  などのキーワードで自動トリガー。
  worktree の一覧表示、作成、削除、移動案内を提供。
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
---

# wtp-helper

ユーザーの自然言語リクエストを検知して Git worktree 操作を支援するスキル。

## トリガーキーワード

### 明示的キーワード
- `worktree`, `ワークツリー`
- `wtp`

### 意図推定キーワード
- `別ブランチで作業`, `別のブランチで`
- `並行開発`, `並列で開発`, `同時に作業`
- `ブランチを分けて`

### 作業終了キーワード
- `作業終了`, `作業完了`
- `ブランチ削除`, `cleanup`
- `マージ済み`

## ワークフロー

```
キーワード検出
  │
  ├─ wtp インストール確認
  │     └─ 未インストール → brew install satococoa/tap/wtp を提案
  │
  ├─ worktree 作成の意図
  │     └─ 既存ブランチか新規か確認
  │           ├─ 既存 → wtp add <branch>
  │           └─ 新規 → wtp add -b <branch>
  │     └─ 成功時 → パス + 移動コマンド例を表示
  │
  ├─ worktree 削除の意図
  │     └─ wtp list で一覧表示
  │     └─ 対象を確認
  │     └─ wtp remove --with-branch <worktree>
  │
  └─ worktree 確認の意図
        └─ wtp list 実行・結果表示
```

## 意図の推定ロジック

| ユーザーの発言例 | 推定される操作 |
|-----------------|---------------|
| 「worktreeを見せて」「一覧表示」 | wtp list |
| 「feature/xxx で作業したい」 | wtp add または wtp add -b |
| 「別ブランチで並行開発したい」 | wtp add -b（ブランチ名を確認） |
| 「作業が終わったのでブランチを削除」 | wtp remove --with-branch |
| 「worktree の設定を確認」 | .wtp.yml を表示 |

## 実行コマンド

### インストール確認

```bash
which wtp
```

未インストールの場合:
```bash
brew install satococoa/tap/wtp
```

### 一覧表示

```bash
wtp list
```

### worktree 作成（既存ブランチ）

```bash
wtp add <branch>
```

### worktree 作成（新規ブランチ）

```bash
wtp add -b <branch> [base]
```

### worktree 削除

```bash
wtp remove --with-branch <worktree>
```

## 成功時の案内

worktree 作成後は以下の移動方法を案内:

```bash
# シェルで移動
cd $(wtp cd <branch>)

# Claude Code を起動
cd $(wtp cd <branch>) && claude
```

## エラーハンドリング

| エラー状況 | 対応 |
|-----------|------|
| wtp 未インストール | brew install を提案 |
| ブランチが存在しない | 新規作成を提案 |
| worktree が dirty | --force オプションを提案 |
| ブランチが未マージ | --force-branch オプションを確認 |

## 補足

- 曖昧なリクエストの場合は AskUserQuestion で確認
- 破壊的な操作（削除）は必ず確認を取る
- Claude Code ではディレクトリ変更が永続しないため、移動方法を案内

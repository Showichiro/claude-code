# wtp (Worktree Plus) チートシート

Git worktree 管理ツール wtp のクイックリファレンス。

## インストール

```bash
# Homebrew
brew install satococoa/tap/wtp

# Go
go install github.com/satococoa/wtp/v2/cmd/wtp@latest
```

## 基本コマンド

### 一覧表示

```bash
wtp list              # すべての worktree を表示
```

出力例:
```
PATH                      BRANCH           HEAD
----                      ------           ----
@ (main worktree)*        main             c72c7800
feature/auth              feature/auth     def45678
```

### worktree 作成

```bash
# 既存ブランチから作成
wtp add feature/auth

# 新規ブランチで作成
wtp add -b feature/new

# 特定のベースから新規ブランチで作成
wtp add -b hotfix/urgent main

# 特定のコミットから作成
wtp add -b bugfix/issue-123 abc1234
```

### worktree 削除

```bash
# worktree のみ削除
wtp remove feature-old

# worktree とブランチを削除
wtp remove --with-branch feature-done

# dirty でも強制削除
wtp remove --force feature-dirty

# 未マージブランチも強制削除
wtp remove --with-branch --force-branch feature-abandoned
```

### パス取得

```bash
# worktree のパスを取得
wtp cd feature/auth

# シェルで移動
cd $(wtp cd feature/auth)

# main worktree に移動
cd $(wtp cd @)
# または
cd $(wtp cd)
```

## Claude Code での利用

### 新しい worktree で作業開始

1. worktree を作成
   ```bash
   wtp add -b feature/new-feature
   ```

2. 表示されたパスをコピー

3. 新しいターミナルで Claude Code を起動
   ```bash
   cd $(wtp cd feature/new-feature) && claude
   ```

### 既存 worktree に移動

1. 一覧を確認
   ```bash
   wtp list
   ```

2. パスを取得
   ```bash
   wtp cd <worktree>
   ```

3. 新しいターミナルで移動
   ```bash
   cd $(wtp cd <worktree>)
   ```

### 現在のセッションで別 worktree を操作

絶対パスを使用すれば、現在のセッションからも別 worktree のファイルを操作可能:

```bash
# 別 worktree のファイルを読む
cat $(wtp cd feature/auth)/src/auth.ts
```

## 設定ファイル (.wtp.yml)

リポジトリルートに配置:

```yaml
version: "1.0"
defaults:
  base_dir: "../worktrees"

hooks:
  post_create:
    # 環境変数ファイルをコピー
    - type: copy
      from: ".env"
      to: ".env"

    # Claude Code 設定をコピー
    - type: copy
      from: ".claude"
      to: ".claude"

    # 依存関係インストール
    - type: command
      command: "npm ci"
```

## ディレクトリ構造

```
<project-root>/
├── .git/
├── .wtp.yml
└── src/

../worktrees/
├── feature/
│   ├── auth/
│   └── payment/
└── hotfix/
    └── bug-123/
```

ブランチ名のスラッシュがディレクトリ構造として保持される。

## よくあるエラーと対処

| エラー | 原因 | 対処 |
|--------|------|------|
| branch not found | ブランチが存在しない | `-b` オプションで新規作成 |
| exists in multiple remotes | 複数リモートに同名ブランチ | リモートを明示的に指定 |
| uncommitted changes | 未コミットの変更あり | `--force` で強制削除 |
| branch is not merged | 未マージのブランチ | `--force-branch` で強制削除 |

## 関連リンク

- [wtp GitHub リポジトリ](https://github.com/satococoa/wtp)
- [Git worktree 公式ドキュメント](https://git-scm.com/docs/git-worktree)

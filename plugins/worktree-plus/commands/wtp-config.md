---
description: |-
  .wtp.yml 設定ファイルの表示・作成・編集を行う。
  「/wtp-config」で設定を管理。
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# wtp-config

wtp の設定ファイル `.wtp.yml` を管理する。

## ワークフロー

```
/wtp-config 実行
  │
  ├─ .wtp.yml の存在確認
  │     ├─ 存在する → 内容を表示
  │     │     └─ 編集するか確認
  │     │           ├─ はい → 編集内容を確認して適用
  │     │           └─ いいえ → 終了
  │     │
  │     └─ 存在しない → 作成するか確認
  │           ├─ はい → テンプレートから作成
  │           └─ いいえ → 終了
```

## 設定ファイルの場所

`.wtp.yml` はリポジトリのルートディレクトリに配置する。

## 汎用テンプレート

```yaml
version: "1.0"
defaults:
  # worktree の作成先ディレクトリ
  base_dir: "../worktrees"

hooks:
  post_create:
    # 環境変数ファイルをコピー
    - type: copy
      from: ".env"
      to: ".env"

    # Claude Code の設定をコピー
    - type: copy
      from: ".claude"
      to: ".claude"

    # 依存関係のインストール（プロジェクトに合わせて変更）
    # - type: command
    #   command: "npm ci"
    #   env:
    #     NODE_ENV: "development"
```

## 設定オプション

### defaults

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `base_dir` | worktree の作成先 | `../worktrees` |

### hooks.post_create

worktree 作成後に実行されるフック。

#### type: copy

```yaml
- type: copy
  from: ".env"      # main worktree からの相対パス
  to: ".env"        # 新しい worktree への相対パス
```

- gitignore されているファイルもコピー可能
- ディレクトリのコピーも対応

#### type: command

```yaml
- type: command
  command: "npm ci"
  work_dir: "."           # オプション: 作業ディレクトリ
  env:                    # オプション: 環境変数
    NODE_ENV: "development"
```

## 編集例

### Node.js プロジェクト用

```yaml
hooks:
  post_create:
    - type: copy
      from: ".env"
      to: ".env"
    - type: command
      command: "npm ci"
```

### Python プロジェクト用

```yaml
hooks:
  post_create:
    - type: copy
      from: ".env"
      to: ".env"
    - type: command
      command: "pip install -r requirements.txt"
```

### Go プロジェクト用

```yaml
hooks:
  post_create:
    - type: copy
      from: ".env"
      to: ".env"
    - type: command
      command: "go mod download"
```

## 使用例

```bash
# 設定を表示または作成
/wtp-config
```

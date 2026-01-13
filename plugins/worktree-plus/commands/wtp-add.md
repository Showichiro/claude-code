---
description: |-
  既存ブランチから worktree を作成する。
  「/wtp-add <branch>」で指定ブランチの worktree を作成。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# wtp-add

既存のローカルまたはリモートブランチから worktree を作成する。

## ワークフロー

```
/wtp-add [branch] 実行
  │
  ├─ wtp インストール確認
  │     └─ 未インストール → brew install satococoa/tap/wtp を提案
  │
  ├─ ブランチ名取得
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → ユーザーに確認
  │
  └─ wtp add <branch> 実行
        ├─ 成功 → パスと移動方法を表示
        └─ 失敗 → エラーメッセージを表示
```

## 実行手順

1. **wtp インストール確認**
   ```bash
   which wtp
   ```
   - 未インストールの場合、以下を提案:
     ```bash
     brew install satococoa/tap/wtp
     ```

2. **ブランチ名の取得**
   - 引数で指定されていない場合は AskUserQuestion で確認

3. **worktree 作成**
   ```bash
   wtp add <branch>
   ```

4. **成功時の案内**
   - 作成されたパスを表示
   - 移動方法を案内:
     ```bash
     # シェルで移動
     cd $(wtp cd <branch>)

     # Claude Code を起動
     cd $(wtp cd <branch>) && claude
     ```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| ブランチが存在しない | `/wtp-new` で新規作成を提案 |
| 複数リモートに同名ブランチ | リモート指定を案内 |
| worktree が既に存在 | 既存パスを表示 |

## 使用例

```bash
# feature/auth ブランチの worktree を作成
/wtp-add feature/auth

# リモートブランチを追跡して作成
/wtp-add origin/feature/remote-branch
```

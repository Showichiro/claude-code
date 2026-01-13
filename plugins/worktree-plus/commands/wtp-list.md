---
description: |-
  Git worktree の一覧を表示する。
  「/wtp-list」で現在のworktree一覧を確認。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# wtp-list

現在のリポジトリの Git worktree 一覧を表示する。

## ワークフロー

```
/wtp-list 実行
  │
  ├─ wtp インストール確認
  │     └─ 未インストール → brew install satococoa/tap/wtp を提案
  │
  └─ wtp list 実行
        └─ 結果を整形して表示
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

2. **worktree 一覧表示**
   ```bash
   wtp list
   ```

## 出力例

```
PATH                      BRANCH           HEAD
----                      ------           ----
@ (main worktree)*        main             c72c7800
feature/auth              feature/auth     def45678
../project-hotfix         hotfix/urgent    abc12345
```

## 補足

- `@` は現在の main worktree を示す
- `*` は現在アクティブな worktree を示す

---
description: |-
  新規ブランチで worktree を作成する。
  「/wtp-new <branch> [base]」で新規ブランチを作成して worktree を作成。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# wtp-new

新規ブランチを作成し、同時に worktree を作成する。

## ワークフロー

```
/wtp-new [branch] [base] 実行
  │
  ├─ wtp インストール確認
  │     └─ 未インストール → brew install satococoa/tap/wtp を提案
  │
  ├─ ブランチ名取得
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → ユーザーに確認
  │
  ├─ ベースブランチ確認（オプション）
  │     └─ 指定なし → 現在のブランチから作成
  │
  └─ wtp add -b <branch> [base] 実行
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
   - 推奨形式: `feature/xxx`, `hotfix/xxx`, `bugfix/xxx`

3. **ベースブランチの確認**
   - 第2引数がある場合はそれを使用
   - なければ現在のブランチ（HEAD）から分岐

4. **worktree 作成**
   ```bash
   # ベース指定なし
   wtp add -b <branch>

   # ベース指定あり
   wtp add -b <branch> <base>
   ```

5. **成功時の案内**
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
| ブランチ名が既に存在 | `/wtp-add` を提案 |
| ベースブランチが存在しない | 正しいブランチ名を確認 |

## 使用例

```bash
# 新しい feature ブランチを作成
/wtp-new feature/new-feature

# main から新しい hotfix ブランチを作成
/wtp-new hotfix/urgent-fix main

# 特定のコミットから作成
/wtp-new bugfix/issue-123 abc1234
```

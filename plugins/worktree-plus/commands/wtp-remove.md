---
description: |-
  worktree とブランチを削除する。
  「/wtp-remove <worktree>」で worktree とブランチを削除。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# wtp-remove

worktree とそれに関連するブランチを削除する。

## ワークフロー

```
/wtp-remove [worktree] 実行
  │
  ├─ wtp インストール確認
  │     └─ 未インストール → brew install satococoa/tap/wtp を提案
  │
  ├─ worktree 名取得
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → wtp list を表示して選択
  │
  ├─ 削除確認
  │     └─ ユーザーに確認（ブランチも削除される旨を通知）
  │
  └─ wtp remove --with-branch <worktree> 実行
        ├─ 成功 → 完了メッセージを表示
        ├─ dirty → --force オプションを提案
        └─ unmerged → --force-branch オプションを提案
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

2. **worktree 名の取得**
   - 引数で指定されていない場合:
     ```bash
     wtp list
     ```
     を実行して選択肢を提示

3. **削除確認**
   - AskUserQuestion で確認
   - 「worktree とブランチの両方が削除されます」と明示

4. **worktree 削除**
   ```bash
   wtp remove --with-branch <worktree>
   ```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| 未コミットの変更あり | `--force` オプションの使用を提案 |
| ブランチが未マージ | `--force-branch` オプションの使用を提案 |
| worktree が存在しない | `wtp list` で一覧を表示 |

## 強制削除オプション

```bash
# dirty な worktree を強制削除
wtp remove --force --with-branch <worktree>

# 未マージのブランチも強制削除
wtp remove --with-branch --force-branch <worktree>

# 両方
wtp remove --force --with-branch --force-branch <worktree>
```

## 使用例

```bash
# feature/auth worktree とブランチを削除
/wtp-remove feature/auth

# 引数なしで実行すると一覧から選択
/wtp-remove
```

## 注意事項

- デフォルトで `--with-branch` が適用されるため、ブランチも削除される
- ブランチを残したい場合は手動で `wtp remove <worktree>` を実行

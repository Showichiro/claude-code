---
description: |-
  OpenAI Codex CLI の実行を支援。
  「codex」「Codex」「OpenAI Codex」「Codexで実行」「Codexに任せ」
  などのキーワードで自動トリガー。
  プロンプトを確認してから非対話モードで実行。
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# codex-helper

ユーザーの自然言語リクエストを検知して OpenAI Codex CLI の実行を支援するスキル。

## トリガーキーワード

### 明示的キーワード
- `codex`, `Codex`, `CODEX`
- `OpenAI Codex`

### 意図推定キーワード
- `Codexで実行`, `Codexで`
- `Codexに任せ`, `Codexにやらせ`
- `Codexを使って`

## ワークフロー

```
キーワード検出
  │
  ├─ codex インストール確認
  │     └─ 未インストール → npm install -g @openai/codex を提案
  │
  ├─ プロンプト内容をユーザーに確認（AskUserQuestion）
  │     └─ 何を実行するか明確にする
  │
  ├─ オプションの確認（必要に応じて）
  │     ├─ モデル指定が必要か
  │     ├─ JSON出力が必要か
  │     └─ サンドボックス設定が必要か
  │
  └─ codex exec 実行
        ├─ 成功 → 結果を表示
        └─ 認証エラー → codex login を案内
```

## 意図の推定ロジック

| ユーザーの発言例 | 推定される操作 |
|-----------------|---------------|
| 「Codexでこのコードを説明して」 | codex exec "コードを説明" |
| 「Codexに任せてリファクタリング」 | codex exec "リファクタリング" |
| 「OpenAI Codexでテストを書いて」 | codex exec "テストを書く" |
| 「Codexで検索して調べて」 | codex exec --search "調査" |

## 実行コマンド

### インストール確認

```bash
which codex
```

未インストールの場合:
```bash
npm install -g @openai/codex
```

### 基本実行

```bash
codex exec "プロンプト"
```

### オプション付き実行

```bash
# モデル指定
codex exec -m gpt-5 "プロンプト"

# JSON出力
codex exec --json "プロンプト"

# サンドボックス指定
codex exec -s workspace-write "プロンプト"

# Web検索有効
codex exec --search "プロンプト"
```

## プロンプト確認のフロー

1. **キーワード検出**
   - ユーザーの発言から Codex 関連のキーワードを検出

2. **プロンプト抽出**
   - 発言からプロンプト部分を抽出
   - 曖昧な場合は AskUserQuestion で確認

3. **確認**
   - 抽出したプロンプトをユーザーに確認
   - 「このプロンプトで実行しますか？」

4. **実行**
   - 確認後に codex exec を実行

## エラーハンドリング

| エラー状況 | 対応 |
|-----------|------|
| codex 未インストール | `npm install -g @openai/codex` を提案 |
| 認証エラー | `codex login` を実行するよう案内 |
| プロンプトが不明確 | AskUserQuestion で詳細を確認 |
| 実行エラー | エラーメッセージを表示し対処法を提案 |

## 認証エラー時の対応

認証エラーが発生した場合:

```
認証が必要です。以下のコマンドでログインしてください:

codex login

ログイン後、再度実行してください。
```

## 補足

- 曖昧なリクエストの場合は必ず AskUserQuestion で確認
- 破壊的な操作（ファイル書き換え等）は実行前に確認
- 長時間実行される可能性がある場合は事前に案内
- 結果が大きい場合は要約して表示

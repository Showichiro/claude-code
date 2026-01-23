---
description: |-
  OpenAI Codex CLI を非対話モードで実行する。
  「/codex-exec [prompt] [options]」でプロンプトを指定して実行。
  --model, --json, --sandbox, --search オプションをサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# codex-exec

OpenAI Codex CLI の非対話モード（`codex exec`）を実行するコマンド。

## サポートするオプション

| オプション | 短縮形 | 説明 |
|-----------|--------|------|
| `--model` | `-m` | モデル指定（gpt-5-codex, gpt-5等） |
| `--json` | | JSON形式で出力 |
| `--sandbox` | `-s` | サンドボックスポリシー（read-only, workspace-write等） |
| `--search` | | Web検索を有効化 |

## ワークフロー

```
/codex-exec [prompt] [--model X] [--json] [--sandbox Y] [--search] 実行
  │
  ├─ codex インストール確認
  │     └─ 未インストール → npm install -g @openai/codex を提案
  │
  ├─ プロンプト取得
  │     ├─ 引数あり → そのまま使用
  │     └─ 引数なし → ユーザーに確認
  │
  ├─ オプション解析
  │     └─ 指定あれば利用、なければデフォルト
  │
  └─ codex exec "プロンプト" [オプション] 実行
        ├─ 成功 → 結果を表示
        └─ 認証エラー → codex login を案内
```

## 実行手順

1. **codex インストール確認**
   ```bash
   which codex
   ```
   - 未インストールの場合、以下を提案:
     ```bash
     npm install -g @openai/codex
     ```

2. **プロンプトの取得**
   - 引数で指定されていない場合は AskUserQuestion で確認
   - プロンプトは引用符で囲んで渡す

3. **オプションの解析**
   - 指定されたオプションをそのまま使用
   - 指定がなければデフォルト動作（オプションなし）

4. **codex exec 実行**
   ```bash
   # 基本実行
   codex exec "プロンプト"

   # モデル指定
   codex exec -m gpt-5 "プロンプト"

   # JSON出力
   codex exec --json "プロンプト"

   # サンドボックス指定
   codex exec -s read-only "プロンプト"

   # 複合オプション
   codex exec -m gpt-5-codex --json -s workspace-write --search "プロンプト"
   ```

5. **結果表示**
   - 通常出力: そのまま表示
   - JSON出力（--json指定時）: 整形して表示

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| codex 未インストール | `npm install -g @openai/codex` を提案 |
| 認証エラー | `codex login` を実行するよう案内 |
| プロンプト未指定 | AskUserQuestion で確認 |
| 無効なオプション | 有効なオプションを案内 |

## 使用例

```bash
# シンプルな実行
/codex-exec "現在のディレクトリの構造を説明して"

# モデル指定
/codex-exec "このコードをリファクタリングして" --model gpt-5

# JSON出力
/codex-exec "ファイル一覧を取得" --json

# サンドボックス指定
/codex-exec "README.mdを更新して" --sandbox workspace-write

# Web検索付き
/codex-exec "最新のReact 19の機能を調べて" --search

# 複合オプション
/codex-exec "テストを書いて" -m gpt-5-codex -s workspace-write
```

## 注意事項

- プロンプトにダブルクォートが含まれる場合はエスケープが必要
- 長いプロンプトは一時ファイル経由での実行を検討
- 認証が必要な場合は `codex login` で事前にログイン

---
description: |-
  Obsidianのノート操作を支援（obsidian-cli連携）。
  「ノートを開いて」「ノートを作成」「Obsidianに書いて」「Vault」「ノート検索」
  「デイリーノート」「Frontmatter」「obsidian-cli」「obs」
  などのキーワードで自動トリガー。
  obsidian-cliでノートの作成・表示・検索・移動・削除等を実行。
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---

# obs-helper

ユーザーの自然言語リクエストを検知して Obsidian ノートの操作を支援するスキル。

## トリガーキーワード

### 明示的キーワード
- `obsidian-cli`, `obs`
- `Obsidian`（アプリケーションとしてのObsidianへの言及）
- `Vault`, `ボルト`

### 意図推定キーワード
- `ノートを開いて`, `ノートを開く`, `ノート開いて`
- `ノートを作成`, `ノートを書いて`, `メモを作成`, `メモを書いて`
- `ノートに追記`, `ノートに書き足し`, `メモに追加`
- `ノートを表示`, `ノートの内容`, `メモを見せて`
- `ノートを検索`, `ノートを探して`, `メモを検索`
- `ノートを削除`, `メモを削除`
- `ノートを移動`, `ノートをリネーム`, `ノート名を変更`
- `デイリーノート`, `日報`, `今日のノート`
- `Frontmatter`, `フロントマター`, `メタデータ`
- `Vault内の`, `Vault一覧`

### 後続処理キーワード
- `Obsidianに保存して`, `ノートとして保存`
- `ノートの内容を要約`, `ノートを読んで`
- `ノートの内容を更新`, `ノートを書き換えて`

## ワークフロー

```
キーワード検出
  │
  ├─ obsidian-cli インストール確認
  │     └─ 未インストール → brew install yakitrak/yakitrak/obsidian-cli を提案
  │
  ├─ デフォルトVault確認
  │     └─ 未設定 → obsidian-cli set-default を案内
  │
  ├─ 意図の判定
  │     ├─ ノートを開く → obsidian-cli open
  │     ├─ ノートを作成/更新 → obsidian-cli create
  │     ├─ ノート内容表示 → obsidian-cli print
  │     ├─ ノート検索 → obsidian-cli list / search-content
  │     ├─ ノート移動/リネーム → obsidian-cli move
  │     ├─ ノート削除 → obsidian-cli delete（要確認）
  │     ├─ デイリーノート → obsidian-cli daily
  │     ├─ Frontmatter操作 → obsidian-cli frontmatter
  │     └─ Vault一覧 → obsidian-cli list
  │
  └─ コマンド実行
        ├─ 成功 → 結果を報告
        │     ├─ 後続処理あり → 要約・翻訳等を実行
        │     └─ 後続処理なし → 結果のみ表示
        └─ エラー → 対処法を案内
```

## 意図の推定ロジック

| ユーザーの発言例 | 推定される操作 |
|-----------------|---------------|
| 「Obsidianでノートを開いて」 | obsidian-cli open（ノート名を確認） |
| 「meeting-notesを見せて」 | obsidian-cli print "meeting-notes" |
| 「新しいメモを作って」 | obsidian-cli create（名前と内容を確認） |
| 「このテキストをObsidianに保存して」 | obsidian-cli create --content "..." |
| 「ノートに追記して」 | obsidian-cli create --append --content "..." |
| 「デイリーノートを開いて」 | obsidian-cli daily |
| 「Vaultの中身を見せて」 | obsidian-cli list |
| 「ノートを検索して」 | obsidian-cli list / search-content |
| 「ノートを移動して」 | obsidian-cli move（パスを確認） |
| 「不要なノートを消して」 | obsidian-cli delete（要確認） |
| 「Frontmatterを確認して」 | obsidian-cli frontmatter --print |
| 「ステータスをdoneに変更」 | obsidian-cli frontmatter --edit --key status --value done |
| 「Obsidianの○○を読んで要約して」 | obsidian-cli print → 内容を要約 |

## 実行コマンド

### インストール確認

```bash
which obsidian-cli
```

未インストールの場合:
```bash
brew tap yakitrak/yakitrak && brew install yakitrak/yakitrak/obsidian-cli
```

### デフォルトVault確認

```bash
obsidian-cli print-default
```

### ノートを開く

```bash
obsidian-cli open "{note-name}"
obsidian-cli open "{note-name}" --section "{heading}"
obsidian-cli open "{note-name}" --vault "{vault-name}"
```

### デイリーノート

```bash
obsidian-cli daily
obsidian-cli daily --vault "{vault-name}"
```

### ノート内容表示

```bash
obsidian-cli print "{note-name}"
obsidian-cli print "{note-name}" --vault "{vault-name}"
```

### ノート作成・更新

```bash
# 空のノート作成
obsidian-cli create "{note-name}"

# 内容付き作成
obsidian-cli create "{note-name}" --content "内容"

# 上書き
obsidian-cli create "{note-name}" --content "内容" --overwrite

# 追記
obsidian-cli create "{note-name}" --content "追記" --append

# 作成後に開く
obsidian-cli create "{note-name}" --content "内容" --open
```

### Vault一覧

```bash
obsidian-cli list
obsidian-cli list "subfolder"
```

### ノート内容検索

```bash
obsidian-cli search-content "検索語"
```

注意: `search` と `search-content` は対話的UIを使用するため、Claude から直接呼び出す場合は `list` + `print` の組み合わせで代替する。
Vault内のファイルを探す場合は `obsidian-cli list` でフォルダを辿るか、`obsidian-cli print-default --path-only` でVaultパスを取得して Glob/Grep ツールで検索する。

### ノート移動・リネーム

```bash
obsidian-cli move "{current-path}" "{new-path}"
obsidian-cli move "{current-path}" "{new-path}" --open
```

### ノート削除

```bash
obsidian-cli delete "{note-path}"
```

### Frontmatter操作

```bash
# 表示
obsidian-cli frontmatter "{note-name}" --print

# 編集
obsidian-cli frontmatter "{note-name}" --edit --key "key" --value "value"

# 削除
obsidian-cli frontmatter "{note-name}" --delete --key "key"
```

## Vault内ファイル検索の補助

`search` / `search-content` は対話的UIのため、ファイル検索には以下を使用:

```bash
# Vaultパスを取得
VAULT_PATH=$(obsidian-cli print-default --path-only)

# Glob ツールでノートを検索
# パターン: ${VAULT_PATH}/**/*.md

# Grep ツールでノート内容を検索
# パス: ${VAULT_PATH}
```

## エラーハンドリング

| エラー状況 | 対応 |
|-----------|------|
| obsidian-cli 未インストール | `brew tap yakitrak/yakitrak && brew install yakitrak/yakitrak/obsidian-cli` を提案 |
| デフォルトVault未設定 | `obsidian-cli set-default "{vault-name}"` を案内 |
| ノートが見つからない | `obsidian-cli list` で候補を表示、Glob で検索 |
| 権限エラー | ファイル権限の確認を案内 |
| Obsidianアプリが起動していない | `open` コマンドがObsidianを起動することを案内 |

## 補足

- 曖昧なリクエストの場合は AskUserQuestion で確認
- 削除操作は必ずユーザーに確認を取ってから実行
- `obsidian-cli print` でノート内容を取得→後続処理（要約、翻訳、分析等）に活用可能
- `search` / `search-content` は対話的UIのため、Claudeからの直接実行には向かない。代わりに `list` + `print` または Glob/Grep で代替
- Vault のパスは `obsidian-cli print-default --path-only` で取得可能

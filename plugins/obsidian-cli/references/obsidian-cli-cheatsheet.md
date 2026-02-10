# obsidian-cli チートシート

Obsidian CLI（`obsidian-cli`）のコマンドリファレンス。

## Vault 設定

```bash
# デフォルトVaultを設定（名前のみ、パスは不要）
obsidian-cli set-default "{vault-name}"

# デフォルトVaultの名前とパスを表示
obsidian-cli print-default

# Vaultパスのみ表示
obsidian-cli print-default --path-only
```

## ノートを開く

```bash
# デフォルトVaultでノートを開く
obsidian-cli open "{note-name}"

# 指定Vaultでノートを開く
obsidian-cli open "{note-name}" --vault "{vault-name}"

# 特定の見出しセクションを開く（大文字小文字区別あり）
obsidian-cli open "{note-name}" --section "{heading-text}"
```

## デイリーノート

```bash
# デイリーノートを作成/開く
obsidian-cli daily

# 指定Vaultのデイリーノート
obsidian-cli daily --vault "{vault-name}"
```

## ノート検索

```bash
# ファジー検索（対話的に選択→Obsidianで開く）
obsidian-cli search

# 指定Vaultで検索
obsidian-cli search --vault "{vault-name}"

# エディタで開く（$EDITOR を使用、デフォルトは vim）
obsidian-cli search --editor
```

## ノート内容検索

```bash
# 内容にマッチするノートを検索
obsidian-cli search-content "search term"

# 指定Vaultで内容検索
obsidian-cli search-content "search term" --vault "{vault-name}"

# 結果をエディタで開く
obsidian-cli search-content "search term" --editor
```

## Vault内容一覧

```bash
# Vaultルートの一覧
obsidian-cli list

# サブフォルダの一覧
obsidian-cli list "001 Notes"

# 指定Vaultのフォルダ一覧
obsidian-cli list "folder" --vault "{vault-name}"
```

## ノート表示

```bash
# ノート内容を標準出力に表示
obsidian-cli print "{note-name}"

# パス指定でも可
obsidian-cli print "{note-path}"

# 指定Vault
obsidian-cli print "{note-name}" --vault "{vault-name}"
```

## ノート作成・更新

```bash
# 空のノートを作成
obsidian-cli create "{note-name}"

# 内容付きで作成
obsidian-cli create "{note-name}" --content "内容テキスト"

# 既存ノートを上書き
obsidian-cli create "{note-name}" --content "新しい内容" --overwrite

# 既存ノートに追記
obsidian-cli create "{note-name}" --content "追記内容" --append

# 作成後にObsidianで開く
obsidian-cli create "{note-name}" --content "内容" --open

# 作成後にエディタで開く
obsidian-cli create "{note-name}" --content "内容" --open --editor

# 指定Vaultで作成
obsidian-cli create "{note-name}" --vault "{vault-name}"
```

## ノート移動・リネーム

```bash
# ノートを移動/リネーム（Vault内のリンクも自動更新）
obsidian-cli move "{current-note-path}" "{new-note-path}"

# 指定Vault
obsidian-cli move "{current-note-path}" "{new-note-path}" --vault "{vault-name}"

# 移動後にObsidianで開く
obsidian-cli move "{current-note-path}" "{new-note-path}" --open
```

## ノート削除

```bash
# ノートを削除
obsidian-cli delete "{note-path}"

# 指定Vault
obsidian-cli delete "{note-path}" --vault "{vault-name}"
```

## Frontmatter 操作

```bash
# Frontmatterを表示
obsidian-cli frontmatter "{note-name}" --print

# フィールドを編集（存在しなければ作成）
obsidian-cli frontmatter "{note-name}" --edit --key "status" --value "done"

# フィールドを削除
obsidian-cli frontmatter "{note-name}" --delete --key "draft"

# 指定Vault
obsidian-cli frontmatter "{note-name}" --print --vault "{vault-name}"
```

## 共通フラグ

| フラグ | 短縮形 | 説明 |
|--------|--------|------|
| `--vault` | | Vault名を指定（set-default未設定時は必須） |
| `--editor` | `-e` | デフォルトエディタで開く（search, search-content, create, move） |
| `--open` | | 操作後にObsidianで開く（create, move） |
| `--overwrite` | | 既存ノートを上書き（create） |
| `--append` | | 既存ノートに追記（create） |
| `--content` | | ノート内容を指定（create） |
| `--section` | | 特定の見出しを開く（open） |
| `--path-only` | | パスのみ表示（print-default） |
| `--print` | | Frontmatter表示（frontmatter） |
| `--edit` | | Frontmatter編集（frontmatter） |
| `--delete` | | Frontmatterフィールド削除（frontmatter） |
| `--key` | | Frontmatterキー指定（frontmatter） |
| `--value` | | Frontmatter値指定（frontmatter） |

## 注意事項

- `open` 等のコマンドはデフォルトVaultのベースディレクトリを作業ディレクトリとして使用する（ターミナルのカレントディレクトリではない）
- `--editor` フラグは `$EDITOR` 環境変数を参照。未設定時は vim がデフォルト
- GUI エディタ（VSCode, Sublime Text 等）は自動的に `--wait` フラグが付与される
- `move` コマンドはVault内の全リンクを自動更新する

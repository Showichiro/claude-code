# Obsidian CLI チートシート

公式 Obsidian CLI（`obsidian` コマンド）のリファレンス。
Obsidian アプリが起動している必要がある。

## 構文

```
obsidian <command> [parameters] [flags]
```

- **パラメータ**: `key=value` 形式。スペースを含む場合はクォート: `name="My Note"`
- **フラグ**: 値なしのブール指定。例: `open`, `overwrite`, `total`
- **Vault指定**: `vault=<name>` を最初のパラメータとして指定
- **ファイル指定**: `file=<name>`（wikilink式の名前解決）または `path=<path>`（Vaultルートからの正確なパス）
- **改行**: `\n`、タブ: `\t`
- **出力コピー**: `--copy` を付けるとクリップボードにコピー

## Vault

```bash
obsidian vault                        # Vault情報
obsidian vault info=name              # 名前のみ
obsidian vault info=path              # パスのみ
obsidian vaults                       # Vault一覧
obsidian vaults verbose               # パス付き
```

## ファイル・フォルダ一覧

```bash
obsidian files                        # ファイル一覧
obsidian files folder=inbox           # フォルダ指定
obsidian files ext=md                 # 拡張子フィルタ
obsidian files total                  # ファイル数のみ
obsidian folders                      # フォルダ一覧
obsidian folders folder=inbox         # サブフォルダ
obsidian folder path=inbox            # フォルダ情報
obsidian folder path=inbox info=files # ファイル数のみ
```

## ノートの読み書き

```bash
# 読む（デフォルト: アクティブファイル）
obsidian read
obsidian read file=Recipe
obsidian read path="inbox/note.md"

# 作成
obsidian create name=Note
obsidian create name=Note content="# Title\n\nBody"
obsidian create name=Note template=Meeting
obsidian create name=Note content="..." overwrite
obsidian create name=Note content="..." open

# 追記（デフォルト: アクティブファイル）
obsidian append content="追記テキスト"
obsidian append file=Note content="追記テキスト"
obsidian append file=Note content="..." inline   # 改行なし

# 先頭に挿入（Frontmatter の後）
obsidian prepend file=Note content="先頭テキスト"

# 開く
obsidian open file=Note
obsidian open file=Note newtab

# 移動
obsidian move file=Note to="archive/Note.md"

# リネーム
obsidian rename file=Note name="New Name"

# 削除（デフォルトはゴミ箱へ）
obsidian delete file=Note
obsidian delete file=Note permanent
```

## デイリーノート

```bash
obsidian daily                        # デイリーノートを開く
obsidian daily:path                   # デイリーノートのパスを取得
obsidian daily:read                   # デイリーノートを読む
obsidian daily:append content="- [ ] タスク"   # 追記
obsidian daily:prepend content="# 朝メモ"      # 先頭挿入
```

## 検索

```bash
obsidian search query="検索ワード"                # テキスト検索
obsidian search query="検索ワード" path=inbox     # フォルダ限定
obsidian search query="検索ワード" limit=5        # 件数制限
obsidian search query="検索ワード" total          # 件数のみ
obsidian search query="検索ワード" case           # 大文字小文字区別
obsidian search:context query="検索ワード"        # マッチ行コンテキスト付き
obsidian search:context query="検索ワード" format=json
```

## タグ

```bash
obsidian tags                         # タグ一覧
obsidian tags counts                  # カウント付き
obsidian tags sort=count              # カウント順
obsidian tags total                   # タグ数のみ
obsidian tags active                  # アクティブファイルのタグ
obsidian tags file=Note               # 特定ファイルのタグ
obsidian tag name=todo                # タグ情報
obsidian tag name=todo verbose        # ファイルリスト付き
```

## タスク

```bash
obsidian tasks                        # 全タスク一覧
obsidian tasks todo                   # 未完了のみ
obsidian tasks done                   # 完了のみ
obsidian tasks daily                  # デイリーノートのタスク
obsidian tasks file=Note              # 特定ファイルのタスク
obsidian tasks total                  # タスク数のみ
obsidian tasks verbose                # ファイル・行番号付き
obsidian task ref="Recipe.md:8" toggle  # トグル
obsidian task ref="Recipe.md:8" done    # 完了
obsidian task ref="Recipe.md:8" todo    # 未完了に戻す
obsidian task daily line=3 toggle       # デイリーのタスクをトグル
```

## プロパティ (Frontmatter)

```bash
obsidian properties                   # Vault内プロパティ一覧
obsidian properties active            # アクティブファイル
obsidian properties file=Note         # 特定ファイル
obsidian properties format=json
obsidian property:read name=status file=Note    # 値を読む
obsidian property:set name=status value=done file=Note  # 設定
obsidian property:set name=tags value="tech, tutorial" type=list file=Note
obsidian property:remove name=draft file=Note   # 削除
obsidian aliases                      # エイリアス一覧
```

## リンク

```bash
obsidian backlinks                    # バックリンク
obsidian backlinks file=Note
obsidian links                        # アウトゴーイングリンク
obsidian links file=Note
obsidian unresolved                   # 未解決リンク
obsidian orphans                      # 孤立ファイル
obsidian deadends                     # 行き止まりファイル
```

## テンプレート

```bash
obsidian templates                    # テンプレート一覧
obsidian template:read name=Meeting
obsidian template:read name=Meeting resolve    # 変数展開
```

## アウトライン・ワードカウント

```bash
obsidian outline                      # 見出し一覧
obsidian outline file=Note format=md
obsidian wordcount                    # アクティブファイル
obsidian wordcount file=Note words    # 単語数のみ
```

## ブックマーク

```bash
obsidian bookmarks                    # ブックマーク一覧
obsidian bookmark file=Note.md
obsidian bookmark url="https://example.com" title="Example"
```

## プラグイン

```bash
obsidian plugins                      # プラグイン一覧
obsidian plugins filter=community versions
obsidian plugin:enable id=my-plugin
obsidian plugin:disable id=my-plugin
obsidian plugin:install id=my-plugin enable
obsidian plugin:reload id=my-plugin   # 開発用
```

## ファイル履歴

```bash
obsidian diff file=Note               # バージョン一覧
obsidian diff file=Note from=1        # 最新 vs 現在
obsidian diff file=Note from=2 to=1   # 2バージョン比較
obsidian history:read file=Note version=1
obsidian history:restore file=Note version=1
```

## ワークスペース

```bash
obsidian workspace                    # ワークスペースツリー
obsidian workspaces                   # 保存済み一覧
obsidian workspace:save name=coding
obsidian workspace:load name=coding
obsidian tabs                         # 開いているタブ
obsidian recents                      # 最近のファイル
```

## 開発者コマンド

```bash
obsidian devtools
obsidian eval code="app.vault.getFiles().length"
obsidian dev:screenshot path=screenshot.png
obsidian dev:console limit=10
obsidian dev:errors
```

## Bases

```bash
obsidian bases                        # .baseファイル一覧
obsidian base:views                   # ビュー一覧
obsidian base:create file=MyBase name="New Item"
obsidian base:query file=MyBase format=json
```

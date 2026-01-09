# Notion-flavored Markdown仕様

## 基本ルール
- インデントはタブを使用
- 空行を追加する場合は `<empty-block/>` を単独行で出力
- エスケープが必要な文字: `\ * ~ ` $ [ ] < > { } | ^`

## ブロックタイプ

### 見出し
```
# H1 {color="Color"}
## H2 {color="Color"}
### H3 {color="Color"}
```
H4-H6はH3に変換される

### リスト
```
- 箇条書き {color="Color"}
	子要素（タブでインデント）

1. 番号付き {color="Color"}
	子要素
```

### To-do
```
- [ ] 未完了タスク {color="Color"}
- [x] 完了タスク {color="Color"}
```

### 引用
```
> 引用テキスト {color="Color"}
```
複数行は `<br>` で区切る:
```
> 行1<br>行2<br>行3 {color="Color"}
```

### トグル
```
▶ トグルタイトル {color="Color"}
	トグル内容（タブでインデント）

▶# トグル見出し1 {color="Color"}
▶## トグル見出し2 {color="Color"}
▶### トグル見出し3 {color="Color"}
```

### コードブロック
````
```language
コード内容
```
````

### 数式
```
$$
数式
$$
```

### 区切り線
```
---
```

## リッチテキスト

### 基本書式
- 太字: `**テキスト**`
- 斜体: `*テキスト*`
- 取り消し線: `~~テキスト~~`
- 下線: `<span underline="true">テキスト</span>`
- インラインコード: `` `コード` ``
- リンク: `[表示テキスト](URL)`

### 色指定
```
<span color="Color">テキスト</span>
```

### インライン数式
```
$数式$ または $`数式`$
```
開始`$`の前と終了`$`の後に空白が必要

## メンション

### ユーザー
```
<mention-user url="{{URL}}">ユーザー名</mention-user>
<mention-user url="{{URL}}"/>
```

### ページ
```
<mention-page url="{{URL}}">ページタイトル</mention-page>
```

### データベース
```
<mention-database url="{{URL}}">データベース名</mention-database>
```

### 日付
```
<mention-date start="YYYY-MM-DD" end="YYYY-MM-DD"/>
<mention-date start="YYYY-MM-DDThh:mm:ssZ"/>
```

## 色一覧

### テキスト色（透明背景）
gray, brown, orange, yellow, green, blue, purple, pink, red

### 背景色
gray_bg, brown_bg, orange_bg, yellow_bg, green_bg, blue_bg, purple_bg, pink_bg, red_bg

## 特殊ブロック

### Callout
```
<callout icon="emoji" color="Color">
	内容（タブでインデント）
	子ブロックも追加可能
</callout>
```

### テーブル
```
<table fit-page-width="true|false" header-row="true|false" header-column="true|false">
	<colgroup>
		<col color="Color">
		<col color="Color">
	</colgroup>
	<tr color="Color">
		<td>セル内容</td>
		<td color="Color">セル内容</td>
	</tr>
</table>
```

### カラム
```
<columns>
	<column>
		左カラム内容
	</column>
	<column>
		右カラム内容
	</column>
</columns>
```

### 画像
```
<image source="{{URL}}" color="Color">キャプション</image>
```

### ファイル
```
<file source="{{URL}}" color="Color">キャプション</file>
```

### PDF
```
<pdf source="{{URL}}" color="Color">キャプション</pdf>
```

### 埋め込みページ
```
<page url="{{URL}}" color="Color">タイトル</page>
```
新規サブページ作成: `<page>新しいページ</page>`

### 埋め込みデータベース
```
<database url="{{URL}}" inline="true|false" icon="Emoji" color="Color">タイトル</database>
```

### 目次
```
<table_of_contents color="Color"/>
```

## MCPツール

### 検索 (notion-search)
ページやユーザーを検索
```json
{"query": "検索クエリ", "query_type": "internal|user"}
```

### 取得 (notion-fetch)
ページまたはデータベースの詳細を取得
```json
{"id": "ページURL or ID"}
```

### ページ作成 (notion-create-pages)
```json
{
  "parent": {"page_id": "親ページID"},
  "pages": [{
    "properties": {"title": "ページタイトル"},
    "content": "Notion Markdown形式のコンテンツ"
  }]
}
```
親を省略するとプライベートページとして作成

### ページ更新 (notion-update-page)
```json
{
  "data": {
    "page_id": "ページID",
    "command": "replace_content",
    "new_str": "新しいコンテンツ"
  }
}
```
コマンド:
- `replace_content`: 全体置換
- `replace_content_range`: 部分置換
- `insert_content_after`: 挿入
- `update_properties`: プロパティ更新

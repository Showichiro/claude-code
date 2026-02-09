---
description: |-
  音声・動画ファイルの文字起こしを支援（yap連携）。
  「文字起こし」「書き起こし」「音声をテキストに」「字幕を作成」「yap」
  などのキーワードで自動トリガー。
  yapでオンデバイス文字起こしを実行し結果を活用。
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
  - mcp__yap__transcribe
---

# yap-helper

ユーザーの自然言語リクエストを検知して音声・動画ファイルの文字起こしを支援するスキル。

## トリガーキーワード

### 明示的キーワード
- `yap`
- `文字起こし`, `書き起こし`
- `transcribe`, `transcription`

### 意図推定キーワード
- `音声をテキストに`, `音声からテキスト`
- `動画をテキストに`, `動画からテキスト`
- `字幕を作成`, `字幕を付け`, `字幕生成`, `キャプション`
- `SRTを作成`, `SRTファイル`
- `会議の音声を`, `録音を`
- `ポッドキャストを`, `講義を`
- `音声ファイル`, `動画ファイル`
- `mp3`, `mp4`, `wav`, `m4a` （ファイル拡張子への言及）

### 後続処理キーワード
- `文字起こしして要約`, `書き起こして翻訳`
- `音声の内容を`, `動画の内容を`

## ワークフロー

```
キーワード検出
  │
  ├─ yap インストール確認
  │     └─ 未インストール → brew install yap を提案
  │
  ├─ 文字起こしの意図
  │     ├─ ファイルパスが明示 → そのまま使用
  │     └─ ファイルパスが不明 → AskUserQuestion で確認
  │           └─ Glob で音声/動画ファイルを検索して候補を提示
  │
  ├─ オプション推定
  │     ├─ 字幕が必要 → --srt
  │     ├─ 日本語の会話 → --locale ja-JP
  │     ├─ 出力先の指定 → --output-file
  │     └─ その他 → デフォルト
  │
  └─ yap transcribe 実行
        ├─ 成功 → 結果を表示
        │     ├─ 後続処理あり → 要約・翻訳等を実行
        │     └─ 後続処理なし → 結果のみ表示
        └─ エラー → 対処法を案内
```

## 意図の推定ロジック

| ユーザーの発言例 | 推定される操作 |
|-----------------|---------------|
| 「この音声を文字起こしして」 | yap transcribe（ファイルパスを確認） |
| 「meeting.mp4 を書き起こして」 | yap transcribe meeting.mp4 |
| 「動画に日本語字幕を付けて」 | yap transcribe --srt -l ja-JP |
| 「録音をテキストにして保存して」 | yap transcribe -o transcript.txt |
| 「この音声を文字起こしして要約して」 | yap transcribe → 結果を要約 |
| 「mp3ファイルの内容を教えて」 | yap transcribe（結果を表示） |
| 「講義動画をSRTにして」 | yap transcribe --srt -o lecture.srt |

## 実行方法

### 優先: MCP ツール経由（mcp__yap__transcribe）

MCP サーバーが利用可能な場合は `mcp__yap__transcribe` ツールを優先的に使用する。

```
mcp__yap__transcribe:
  file: "/absolute/path/to/file.mp3"    # 必須: 絶対パス
  locale: "ja-JP"                        # 任意: BCP 47 ロケール
  format: "txt"                          # 任意: "txt" or "srt"（デフォルト: "txt"）
  censor: false                          # 任意: マスク（デフォルト: false）
  maxLength: 40                          # 任意: SRT最大文字数（デフォルト: 40）
```

### フォールバック: CLI 経由（Bash）

MCP ツールが利用できない場合は Bash で yap CLI を直接実行する。

#### インストール確認

```bash
which yap
```

未インストールの場合:
```bash
brew install yap
```

#### 基本的な文字起こし

```bash
yap transcribe "file.mp3"
```

#### 日本語ロケール指定

```bash
yap transcribe -l ja-JP "file.mp3"
```

#### SRT字幕出力

```bash
yap transcribe --srt "video.mp4"
```

#### ファイルに保存

```bash
yap transcribe -o transcript.txt "file.mp3"
```

#### SRT字幕をファイルに保存

```bash
yap transcribe --srt -o captions.srt "video.mp4"
```

## ファイル検索の補助

ユーザーがファイルパスを明示しない場合、以下のパターンで検索:

```bash
# 音声・動画ファイルの検索（Glob ツールを使用）
# パターン: **/*.{mp3,mp4,wav,m4a,mov,aac,caf,webm,ogg,flac}
```

候補が見つかった場合はリストを提示してユーザーに選択を促す。

## 後続処理の対応

文字起こし結果に対する後続処理:

| 要求 | 対応 |
|------|------|
| 要約 | 文字起こし結果をそのまま要約 |
| 翻訳 | 文字起こし結果を翻訳 |
| 議事録作成 | 文字起こし結果を構造化して議事録にまとめる |
| テキスト保存 | Write ツールでファイルに保存 |
| 検索 | 文字起こし結果から特定のキーワードを検索 |

## エラーハンドリング

| エラー状況 | 対応 |
|-----------|------|
| yap 未インストール | `brew install yap` を提案 |
| ファイルが存在しない | パスを再確認、Glob で候補を検索 |
| サポートされないファイル形式 | 対応形式を案内 |
| 権限エラー | システム環境設定での許可手順を案内 |
| 文字起こし結果が空 | ロケール変更や音声品質の確認を提案 |
| タイムアウト | 長時間ファイルの場合、timeout を延長して再実行 |

## 補足

- 曖昧なリクエストの場合は AskUserQuestion で確認
- 長時間の音声ファイルは実行に時間がかかることを事前に案内
- オンデバイス処理のためプライバシーが保たれることを案内
- 文字起こし後の後続処理（要約、翻訳等）も積極的に提案

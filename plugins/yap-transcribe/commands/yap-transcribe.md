---
description: |-
  音声・動画ファイルをオンデバイスで文字起こしする。
  「/yap-transcribe <file> [options]」でファイルを指定して実行。
  --locale, --srt, --censor, --output-file, --max-length オプションをサポート。
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - AskUserQuestion
  - mcp__yap__transcribe
---

# yap-transcribe

yap CLI を使用して音声・動画ファイルをオンデバイスで文字起こしするコマンド。
macOS の Speech.framework を利用するため、インターネット接続不要・プライバシー安全。

## サポートするオプション

| オプション | 短縮形 | 説明 |
|-----------|--------|------|
| `--locale` | `-l` | 言語ロケール指定（ja-JP, en-US 等） |
| `--srt` | | SRT字幕形式で出力（デフォルトはテキスト） |
| `--txt` | | テキスト形式で出力（デフォルト） |
| `--censor` | | 不適切な語句をマスク |
| `--output-file` | `-o` | 出力ファイルパスを指定 |
| `--max-length` | `-m` | 1文の最大文字数（デフォルト: 40） |

## ワークフロー

```
/yap-transcribe <file> [options] 実行
  │
  ├─ yap インストール確認
  │     └─ 未インストール → brew install yap を提案
  │
  ├─ 入力ファイル確認
  │     ├─ 引数あり → ファイル存在を確認
  │     └─ 引数なし → ユーザーに確認
  │
  ├─ オプション解析
  │     ├─ --locale: 言語指定（デフォルト: システムロケール）
  │     ├─ --srt / --txt: 出力形式
  │     ├─ --censor: マスク有無
  │     ├─ --output-file: 出力先
  │     └─ --max-length: 最大文字数
  │
  └─ yap transcribe 実行
        ├─ 成功 → 文字起こし結果を表示
        └─ エラー → エラーメッセージを表示し対処法を提案
```

## 実行手順

1. **入力ファイルの確認**
   - 引数で指定されていない場合は AskUserQuestion で確認
   - ファイルが存在するか確認

2. **オプションの解析**
   - 指定されたオプションをそのまま使用
   - 日本語ファイルの場合、`--locale ja-JP` を自動付与（ユーザーの指定がなければ推定）

3. **文字起こし実行（MCP ツール優先）**

   MCP サーバーが利用可能な場合は `mcp__yap__transcribe` ツールを優先的に使用する:

   ```
   mcp__yap__transcribe:
     file: "/absolute/path/to/audio.mp3"   # 必須: 絶対パス
     locale: "ja-JP"                        # 任意: BCP 47 ロケール
     format: "txt"                          # 任意: "txt" or "srt"
     censor: false                          # 任意: マスク
     maxLength: 40                          # 任意: SRT最大文字数
   ```

4. **フォールバック: CLI 経由（MCP ツールが使えない場合）**

   ```bash
   # yap インストール確認
   which yap
   # 未インストールの場合: brew install yap

   # 基本実行（テキスト出力）
   yap transcribe "audio.mp3"

   # 日本語ロケール指定
   yap transcribe -l ja-JP "audio.mp3"

   # SRT字幕形式で出力
   yap transcribe --srt "video.mp4"

   # ファイルに保存
   yap transcribe -o transcript.txt "audio.mp3"

   # SRT字幕をファイルに保存
   yap transcribe --srt -o captions.srt "video.mp4"

   # マスク付き + 最大文字数指定
   yap transcribe --censor -m 80 "audio.mp3"

   # 複合オプション
   yap transcribe -l ja-JP --srt -o captions.srt -m 60 "video.mp4"
   ```

5. **結果の活用**
   - テキスト出力: そのまま表示、または後続の処理（要約、翻訳等）に利用
   - SRT出力: 字幕ファイルとして保存
   - 出力ファイル指定時: ファイルパスを案内

## 言語ロケールの推定

ユーザーが `--locale` を指定しない場合、以下のロジックで推定する:

| 条件 | 推定ロケール |
|------|-------------|
| ユーザーが日本語で会話 | `ja-JP` |
| ファイル名に日本語が含まれる | `ja-JP` |
| ユーザーが英語で会話 | `en-US` |
| 明示的に指定あり | そのまま使用 |
| 判断不能 | 指定なし（システムデフォルト） |

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| yap 未インストール | `brew install yap` を提案 |
| ファイルが存在しない | パスを再確認、Glob で候補を検索 |
| サポートされないファイル形式 | 対応形式を案内（mp3, mp4, wav, m4a, mov 等） |
| 権限エラー（マイク/Speech） | システム環境設定での許可手順を案内 |
| 文字起こし結果が空 | ロケール変更や音声品質の確認を提案 |

## 使用例

```bash
# 音声ファイルの文字起こし
/yap-transcribe recording.mp3

# 動画に日本語字幕を作成
/yap-transcribe meeting.mp4 --srt -o meeting.srt --locale ja-JP

# 英語の音声を文字起こし
/yap-transcribe podcast.mp3 --locale en-US -o transcript.txt

# 不適切表現をマスク
/yap-transcribe audio.wav --censor

# 長文対応（1文最大80文字）
/yap-transcribe lecture.mp4 -m 80 -o lecture.txt
```

## 注意事項

- macOS 26 以降が必要（Speech.framework を使用）
- オンデバイス処理のため、インターネット接続不要
- 対応ファイル形式: mp3, mp4, wav, m4a, mov, aac, caf 等（AVFoundation がサポートする形式）
- 長時間の音声はタイムアウトに注意（必要に応じて timeout を延長）

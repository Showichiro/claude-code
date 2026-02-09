# yap チートシート

## インストール

```bash
brew install yap
```

## 基本コマンド

```bash
yap transcribe <file>           # テキスト出力（stdout）
yap transcribe <file> --srt     # SRT字幕出力（stdout）
```

## オプション一覧

| オプション | 短縮形 | デフォルト | 説明 |
|-----------|--------|-----------|------|
| `--locale` | `-l` | current | 言語ロケール |
| `--txt` | | ✓ | テキスト形式出力 |
| `--srt` | | | SRT字幕形式出力 |
| `--censor` | | off | 不適切語句マスク |
| `--output-file` | `-o` | stdout | 出力先ファイル |
| `--max-length` | `-m` | 40 | 1文の最大文字数 |

## よく使うパターン

```bash
# 日本語音声の文字起こし
yap transcribe -l ja-JP audio.mp3

# 英語音声の文字起こし
yap transcribe -l en-US audio.mp3

# 字幕ファイル作成
yap transcribe --srt -o captions.srt video.mp4

# テキストファイルに保存
yap transcribe -o transcript.txt audio.mp3

# 日本語字幕を長文対応で作成
yap transcribe -l ja-JP --srt -m 60 -o subtitles.srt video.mp4

# 不適切表現をマスクして文字起こし
yap transcribe --censor audio.mp3
```

## 対応ロケール例

| ロケール | 言語 |
|---------|------|
| `ja-JP` | 日本語 |
| `en-US` | 英語（米国） |
| `en-GB` | 英語（英国） |
| `zh-CN` | 中国語（簡体字） |
| `ko-KR` | 韓国語 |
| `fr-FR` | フランス語 |
| `de-DE` | ドイツ語 |
| `es-ES` | スペイン語 |

## 応用: パイプライン

```bash
# YouTube動画を文字起こし（yt-dlp連携）
yt-dlp "https://www.youtube.com/watch?v=xxx" -x --exec yap

# 文字起こし → 要約（llm連携）
yap transcribe audio.mp3 | uvx llm 'この内容を要約して:'
```

## MCP サーバー

```bash
# Claude Code に MCP サーバーとして追加
claude mcp add yap -- yap mcp
```

## トラブルシューティング

| 問題 | 対処 |
|------|------|
| `command not found: yap` | `brew install yap` |
| 文字起こし結果が空 | `--locale` で正しい言語を指定 |
| 権限エラー | システム環境設定 > プライバシーとセキュリティ > 音声認識 を許可 |
| タイムアウト | 長時間ファイルの場合は分割を検討 |

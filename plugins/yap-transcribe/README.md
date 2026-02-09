# yap-transcribe

音声・動画ファイルのオンデバイス文字起こしを支援する Claude Code プラグイン。

[yap](https://github.com/finnvoor/yap) CLI を利用して、macOS の Speech.framework によるオンデバイス文字起こしを実行します。

## 前提条件

- macOS 26 以降
- yap CLI (`brew install yap`)

## 機能

- **スラッシュコマンド**: `/yap-transcribe <file> [options]` で直接実行
- **自然言語トリガー**: 「文字起こしして」「字幕を作成して」等のキーワードで自動検知
- **多言語対応**: `--locale` による言語ロケール指定
- **SRT字幕出力**: `--srt` で字幕ファイル生成
- **後続処理**: 文字起こし結果の要約・翻訳・議事録作成

## 使い方

### スラッシュコマンド

```
/yap-transcribe recording.mp3
/yap-transcribe meeting.mp4 --srt -o meeting.srt --locale ja-JP
```

### 自然言語

```
「この音声ファイルを文字起こしして」
「動画に日本語字幕を付けて」
「meeting.mp4 を書き起こして要約して」
```

## 構成

```
yap-transcribe/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/
│   └── yap-transcribe.md
├── skills/
│   └── yap-helper/
│       └── SKILL.md
└── references/
    └── yap-cheatsheet.md
```

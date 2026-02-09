---
description: |-
  gog CLI の認証・アカウント管理を行う。
  「/gog-auth [操作]」でクレデンシャル設定・アカウント追加・確認を実行。
  credentials, add, list, status, remove, alias, keyring 等をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-auth

gog CLI の認証とアカウント管理を行うコマンド。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `credentials <path>` | OAuth クレデンシャルを保存 |
| `credentials list` | 保存済みクレデンシャル一覧 |
| `add <email>` | アカウントを認可 |
| `list` | アカウント一覧 |
| `list --check` | トークン検証 |
| `status` | 現在のアカウント状態 |
| `remove <email>` | アカウント削除 |
| `alias set <name> <email>` | エイリアス設定 |
| `alias list` | エイリアス一覧 |
| `keyring [backend]` | キーリング設定 |
| `services` | 利用可能なサービス一覧 |

## 実行手順

### 初期セットアップ

```bash
# 1. クレデンシャル保存
gog auth credentials ~/Downloads/client_secret_....json

# 2. アカウント認可（ブラウザが開く）
gog auth add you@gmail.com

# 3. 動作確認
gog auth status
```

### 複数アカウント

```bash
# 複数 OAuth クライアント
gog --client work auth credentials ~/Downloads/work-client.json
gog --client work auth add you@company.com

# エイリアス設定
gog auth alias set work work@company.com
gog auth alias set personal me@gmail.com
```

### サービススコープ

```bash
# 特定サービスのみ認可
gog auth add you@gmail.com --services drive,calendar

# 読み取り専用
gog auth add you@gmail.com --services drive --readonly

# スコープ追加（再認可）
gog auth add you@gmail.com --services sheets --force-consent
```

### キーリング

```bash
gog auth keyring                  # 現在の設定
gog auth keyring file             # ファイルベースに変更
gog auth keyring keychain         # macOS Keychain に変更
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| クレデンシャル未設定 | Google Cloud Console でOAuth クライアントを作成し JSON をダウンロードする手順を案内 |
| トークン期限切れ | `gog auth add <email> --force-consent` を案内 |
| Keychain プロンプト多発 | `gog auth keyring file` を提案 |

## 使用例

```bash
# 初期セットアップ
/gog-auth credentials ~/Downloads/client_secret_xxx.json
/gog-auth add you@gmail.com

# 状態確認
/gog-auth status
/gog-auth list --check

# エイリアス
/gog-auth alias set work work@company.com
```

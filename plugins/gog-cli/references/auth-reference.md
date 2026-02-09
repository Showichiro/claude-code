# 認証リファレンス

## 初期セットアップ

```bash
# 1. OAuth クレデンシャル保存
gog auth credentials ~/Downloads/client_secret_....json

# 2. アカウント認可
gog auth add you@gmail.com

# 3. 動作確認
export GOG_ACCOUNT=you@gmail.com
gog gmail labels list
```

## アカウント管理

```bash
gog auth list                             # アカウント一覧
gog auth list --check                     # トークン検証
gog auth status                           # 現在のアカウント状態
gog auth remove <email>                   # アカウント削除
gog auth manage                           # ブラウザでアカウントマネージャー
gog auth tokens                           # リフレッシュトークン管理
```

## エイリアス

```bash
gog auth alias set work work@company.com
gog auth alias list
gog auth alias unset work
```

予約語: `auto`, `default`

## 複数 OAuth クライアント

```bash
gog --client work auth credentials ~/Downloads/work-client.json
gog --client work auth add you@company.com

# ドメインマッピング
gog --client work auth credentials ~/Downloads/work.json --domain example.com

# クレデンシャル一覧
gog auth credentials list
```

クライアント選択順序:
1. `--client` / `GOG_CLIENT`
2. `account_clients` 設定
3. `client_domains` 設定
4. ドメイン名のクレデンシャルファイル
5. `default`

## サービススコープ

```bash
gog auth add you@gmail.com --services drive,calendar
gog auth add you@gmail.com --services drive,calendar --readonly
gog auth add you@gmail.com --services drive --drive-scope full
gog auth add you@gmail.com --services drive --drive-scope readonly
gog auth add you@gmail.com --services drive --drive-scope file
gog auth add you@gmail.com --services sheets --force-consent
gog auth services                          # 利用可能なサービスとスコープ一覧
```

## サービスアカウント（Workspace ドメイン委任）

```bash
gog auth service-account set you@yourdomain.com --key ~/Downloads/service-account.json
gog auth service-account status you@yourdomain.com
gog auth service-account unset you@yourdomain.com
```

サービスアカウントが設定されていると OAuth トークンより優先される。

## キーリング

```bash
gog auth keyring                           # 現在の設定
gog auth keyring file                      # 暗号化ファイルベース
gog auth keyring keychain                  # macOS Keychain
gog auth keyring auto                      # 自動選択
```

バックエンド: `auto` (デフォルト), `keychain` (macOS), `file` (暗号化ディスク)

非対話環境:
```bash
export GOG_KEYRING_BACKEND=file
export GOG_KEYRING_PASSWORD='...'
gog --no-input auth status
```

## 環境変数

| 変数 | 説明 |
|------|------|
| `GOG_ACCOUNT` | デフォルトアカウント |
| `GOG_CLIENT` | OAuth クライアント名 |
| `GOG_JSON` | デフォルト JSON 出力 |
| `GOG_PLAIN` | デフォルト plain 出力 |
| `GOG_COLOR` | カラーモード (auto/always/never) |
| `GOG_TIMEZONE` | デフォルトタイムゾーン |
| `GOG_ENABLE_COMMANDS` | コマンド許可リスト |
| `GOG_KEYRING_BACKEND` | キーリングバックエンド (auto/keychain/file) |
| `GOG_KEYRING_PASSWORD` | ファイルキーリングのパスワード |

## 設定ファイル（JSON5）

パス: `gog config path` で確認

```json5
{
  keyring_backend: "file",
  default_timezone: "UTC",
  account_aliases: {
    work: "work@company.com",
    personal: "me@gmail.com",
  },
  account_clients: {
    "work@company.com": "work",
  },
  client_domains: {
    "example.com": "work",
  },
}
```

```bash
gog config path
gog config list
gog config keys
gog config get default_timezone
gog config set default_timezone UTC
gog config unset default_timezone
```

## コマンド許可リスト（サンドボックス）

```bash
gog --enable-commands calendar,tasks calendar events --today
export GOG_ENABLE_COMMANDS=calendar,tasks
```

## グローバルフラグ

| フラグ | 説明 |
|--------|------|
| `--account <email\|alias\|auto>` | 使用するアカウント |
| `--enable-commands <csv>` | コマンド許可リスト |
| `--json` | JSON 出力 |
| `--plain` | TSV 出力 |
| `--color <mode>` | カラーモード |
| `--force` | 確認スキップ |
| `--no-input` | 非対話モード |
| `--verbose` | 詳細ログ |

# claude-code

A collection of personal Claude Code utilities and custom skills.

## Overview

This repository contains a Claude Code plugin marketplace that provides custom skills to enhance your Claude Code workflow. The plugins are designed to help with document conversion and cross-platform content management.

## Installation

### From Claude Code (Recommended)

You can install plugins directly from Claude Code using the plugin management system:

1. Add this repository as a marketplace:
   ```
   /plugin marketplace add Showichiro/claude-code
   ```

2. Install the plugins:
   ```
   /plugin install obsidian-to-notion@Showichiro/claude-code
   ```

3. Restart Claude Code to activate the plugins.

### Manual Installation

Alternatively, you can clone this repository and use it as a local marketplace:

```bash
git clone https://github.com/Showichiro/claude-code.git
```

Then in Claude Code:
```
/plugin marketplace add ./claude-code
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [obsidian-to-notion](plugins/obsidian-to-notion/) | Convert Obsidian documents to Notion format |
| [worktree-plus](plugins/worktree-plus/) | Git worktree management with wtp CLI |
| [openai-codex](plugins/openai-codex/) | Run OpenAI Codex CLI in non-interactive mode |
| [gog-cli](plugins/gog-cli/) | Google Suite CLI (gog) for Gmail, Calendar, Drive, Sheets, Tasks, Contacts |
| [yap-transcribe](plugins/yap-transcribe/) | On-device speech transcription with yap CLI + MCP server |

## Skills

### `/obsidian-to-notion` - Obsidian to Notion Converter

Convert Obsidian documents to Notion format and sync them.

**Purpose:**
This skill helps convert Obsidian markdown files to Notion-compatible format, handling internal links, callouts, and other Obsidian-specific syntax.

**Features:**
- Converts `[[internal links]]` to Notion page mentions
- Transforms Obsidian callouts (`> [!info]`) to Notion callouts with appropriate colors
- Removes frontmatter and tags
- Supports both new page creation and existing page updates
- Preview before applying changes

**Usage:**
```
/obsidian-to-notion
```

Or simply say "Notionに反映して" while viewing an Obsidian file.

### `/wtp-*` - Git Worktree Management

Manage Git worktrees using the [wtp](https://github.com/satococoa/wtp) CLI tool.

**Prerequisites:**
```bash
# Homebrew (macOS)
brew install satococoa/tap/wtp

# Go
go install github.com/satococoa/wtp/v2/cmd/wtp@latest
```

**Available Commands:**
| Command | Description |
|---------|-------------|
| `/wtp-list` | List all worktrees |
| `/wtp-add <branch>` | Create worktree from existing branch |
| `/wtp-new <branch> [base]` | Create worktree with new branch |
| `/wtp-remove [worktree]` | Remove worktree and branch |
| `/wtp-config` | Manage .wtp.yml configuration |

**Usage:**
```
/wtp-list
/wtp-add feature/auth
/wtp-new feature/new-feature main
```

You can also use natural language (e.g., "I want to work on feature/auth branch").

### `/codex-exec` - OpenAI Codex CLI

Run [OpenAI Codex CLI](https://github.com/openai/codex) in non-interactive mode.

**Prerequisites:**
```bash
npm install -g @openai/codex
codex login
```

**Available Commands:**
| Command | Description |
|---------|-------------|
| `/codex-exec` | Run Codex CLI in non-interactive mode |

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--model` | `-m` | Specify model (gpt-5-codex, gpt-5, etc.) |
| `--json` | - | Output in JSON format |
| `--sandbox` | `-s` | Sandbox policy (read-only, workspace-write, etc.) |
| `--search` | - | Enable web search |

**Usage:**
```
/codex-exec "explain this code"
/codex-exec "refactor this" --model gpt-5
/codex-exec "update README.md" --sandbox workspace-write
```

You can also use natural language with keywords like "Codex", "Codexで実行", "Codexに任せて".

### `/gog-*` - Google Suite CLI

Operate Google services via [gog CLI (gogcli)](https://github.com/steipete/gogcli) from the terminal.

**Prerequisites:**
```bash
brew install steipete/tap/gogcli
gog auth credentials ~/Downloads/client_secret_....json
gog auth add you@gmail.com
```

**Available Commands:**
| Command | Description |
|---------|-------------|
| `/gog-auth` | Authentication & account management |
| `/gog-gmail` | Gmail (search, send, labels, drafts, filters) |
| `/gog-calendar` | Calendar (events, create, update, freebusy) |
| `/gog-drive` | Drive (list, search, upload, download, share) |
| `/gog-sheets` | Sheets (read, write, create, export) |
| `/gog-tasks` | Tasks (list, add, done, delete) |
| `/gog-contacts` | Contacts (search, create, update, delete) |

**Usage:**
```
/gog-gmail search 'newer_than:7d' --max 10
/gog-calendar events primary --today
/gog-drive search "report" --max 20
/gog-sheets get <spreadsheetId> 'Sheet1!A1:B10'
```

You can also use natural language (e.g., "メールを確認して", "今日の予定を教えて", "ファイルを検索して").

### `/yap-transcribe` - Speech Transcription

On-device speech transcription using [yap](https://github.com/finnvoor/yap) CLI and MCP server.

**Prerequisites:**
```bash
brew install yap
```

**Available Commands:**
| Command | Description |
|---------|-------------|
| `/yap-transcribe` | Transcribe audio/video files |

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--locale` | `-l` | Language locale (ja-JP, en-US, etc.) |
| `--srt` | - | Output in SRT subtitle format |
| `--censor` | - | Redact inappropriate words |
| `--output-file` | `-o` | Save output to file |
| `--max-length` | `-m` | Max sentence length for SRT (default: 40) |

**Usage:**
```
/yap-transcribe recording.mp3
/yap-transcribe meeting.mp4 --srt -o meeting.srt --locale ja-JP
```

You can also use natural language (e.g., "この音声を文字起こしして", "動画に字幕を付けて").

MCP server integration is also available — the `mcp__yap__transcribe` tool is preferred when the MCP server is running.

## Plugin Structure

This repository is organized as a plugin marketplace containing multiple plugins:

```
.claude-plugin/
└── marketplace.json    # Marketplace metadata

plugins/
└── obsidian-to-notion/         # obsidian-to-notion plugin
    ├── .claude-plugin/
    │   └── plugin.json
    ├── skills/
    │   └── obsidian-to-notion.md
    └── references/
        └── notion-markdown.md
```

## Contributing

Feel free to fork this repository and add your own custom commands, agents, or skills.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

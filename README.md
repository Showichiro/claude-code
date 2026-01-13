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

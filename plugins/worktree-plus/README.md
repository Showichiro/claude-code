# worktree-plus

A Claude Code plugin for Git worktree management with [wtp](https://github.com/satococoa/wtp).

## Overview

This plugin simplifies Git worktree management, enabling smooth parallel development and branch switching.

## Prerequisites

Install wtp:

```bash
# Homebrew (macOS)
brew install satococoa/tap/wtp

# Go
go install github.com/satococoa/wtp/v2/cmd/wtp@latest
```

## Installation

### From Marketplace

```
/plugin marketplace add Showichiro/claude-code
/plugin install worktree-plus@Showichiro/claude-code
```

### Manual Installation

```bash
git clone https://github.com/Showichiro/claude-code.git
```

```
/plugin marketplace add ./claude-code
/plugin install worktree-plus
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/wtp-list` | List all worktrees | `/wtp-list` |
| `/wtp-add` | Create worktree from existing branch | `/wtp-add feature/auth` |
| `/wtp-new` | Create worktree with new branch | `/wtp-new feature/new main` |
| `/wtp-remove` | Remove worktree and branch | `/wtp-remove feature/auth` |
| `/wtp-config` | Manage .wtp.yml configuration | `/wtp-config` |

Natural language is also supported (e.g., "I want to work on feature/auth").

## References

- [wtp-cheatsheet](references/wtp-cheatsheet.md) - Detailed command reference
- [wtp GitHub](https://github.com/satococoa/wtp)
- [Git worktree documentation](https://git-scm.com/docs/git-worktree)

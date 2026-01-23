# openai-codex

A Claude Code plugin for running [OpenAI Codex CLI](https://github.com/openai/codex) in non-interactive mode.

## Overview

This plugin enables seamless integration with OpenAI Codex CLI, providing two interfaces:

- **Commands**: Manual execution via `/codex-exec`
- **Skills**: Automatic trigger through natural language keywords

## Prerequisites

Install OpenAI Codex CLI:

```bash
npm install -g @openai/codex
```

Authenticate with OpenAI:

```bash
codex login
```

## Installation

### From Marketplace

```
/plugin marketplace add Showichiro/claude-code
/plugin install openai-codex@Showichiro/claude-code
```

### Manual Installation

```bash
git clone https://github.com/Showichiro/claude-code.git
```

```
/plugin marketplace add ./claude-code
/plugin install openai-codex
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/codex-exec` | Run Codex CLI in non-interactive mode | `/codex-exec "explain this code"` |

### Supported Options

| Option | Short | Description |
|--------|-------|-------------|
| `--model` | `-m` | Specify model (gpt-5-codex, gpt-5, etc.) |
| `--json` | - | Output in JSON format |
| `--sandbox` | `-s` | Sandbox policy (read-only, workspace-write, etc.) |
| `--search` | - | Enable web search |

### Usage Examples

```bash
# Basic execution
/codex-exec "explain the current directory structure"

# With model specification
/codex-exec "refactor this code" --model gpt-5

# JSON output
/codex-exec "list files" --json

# With sandbox policy
/codex-exec "update README.md" --sandbox workspace-write

# With web search
/codex-exec "research latest React 19 features" --search

# Combined options
/codex-exec "write tests" -m gpt-5-codex -s workspace-write
```

## Skills

| Skill | Description |
|-------|-------------|
| `codex-helper` | Assists Codex execution via natural language |

### Trigger Keywords

- `codex`, `Codex`, `CODEX`
- `OpenAI Codex`
- `Codexで実行`, `Codexで`
- `Codexに任せ`, `Codexにやらせ`
- `Codexを使って`

### Intent Inference Examples

| User Request | Inferred Action |
|--------------|-----------------|
| "Codexでこのコードを説明して" | `codex exec "explain this code"` |
| "Codexに任せてリファクタリング" | `codex exec "refactor"` |
| "OpenAI Codexでテストを書いて" | `codex exec "write tests"` |
| "Codexで検索して調べて" | `codex exec --search "research"` |

## References

- [OpenAI Codex CLI](https://github.com/openai/codex) - Official CLI repository

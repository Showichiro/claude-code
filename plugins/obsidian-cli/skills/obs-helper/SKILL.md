---
description: |-
  This skill should be used when the user asks to "ノートを開いて", "ノートを作成",
  "Obsidianに書いて", "Vault一覧", "ノートを検索", "デイリーノート", "日報",
  "Frontmatter", "プロパティ", "タスク一覧", "タグ一覧", "ブックマーク",
  "バックリンク", "obsidian", "obs", "open note", "create note", "daily note",
  "search notes", "vault list", or requests any Obsidian note read/write/search operation.
  Provides workflows for operating Obsidian notes via the official Obsidian CLI
  (the `obsidian` command), including read, create, search, move, delete,
  daily notes, properties, tasks, tags, and links.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---

# obs-helper

To operate Obsidian notes, detect the user's natural language intent and execute the appropriate official Obsidian CLI (`obsidian`) command. Respond in the same language the user used.

## Prerequisites

- Obsidian app must be running (first CLI command launches it if not)
- Settings → General → Command line interface must be enabled
- macOS: PATH must include `/Applications/Obsidian.app/Contents/MacOS`

## CLI Syntax

The official Obsidian CLI uses `parameter=value` syntax, NOT `--flag value`.

```
obsidian <command> [parameter=value ...] [flag ...]
```

- **Parameters**: `key=value` — quote values with spaces: `name="My Note"`
- **Flags**: boolean, no value — e.g. `open`, `overwrite`, `total`
- **Vault targeting**: prepend `vault=<name>` as the first parameter
- **File targeting**: `file=<name>` (wikilink-style resolution) or `path=<path>` (exact path from vault root)
- **Newlines**: `\n` — **Tabs**: `\t`

## Core Workflow

```
Keyword detection
  │
  ├─ Verify CLI availability: which obsidian
  │     └─ Not found → guide setup (Settings → General → CLI)
  │
  ├─ Determine intent
  │     ├─ Read note       → obsidian read file=<name>
  │     ├─ Open note       → obsidian open file=<name>
  │     ├─ Create note     → obsidian create name=<name> content="..."
  │     ├─ Append to note  → obsidian append file=<name> content="..."
  │     ├─ Search notes    → obsidian search query="..."
  │     ├─ Move note       → obsidian move file=<name> to=<path>
  │     ├─ Rename note     → obsidian rename file=<name> name=<new>
  │     ├─ Delete note     → obsidian delete file=<name> (confirm first)
  │     ├─ List files      → obsidian files / folders
  │     ├─ Daily notes     → obsidian daily / daily:read / daily:append
  │     ├─ Properties      → obsidian property:read / set / remove
  │     ├─ Tasks           → obsidian tasks / task
  │     ├─ Tags            → obsidian tags / tag
  │     ├─ Links           → obsidian backlinks / links / unresolved
  │     └─ Templates       → obsidian templates / create template=<name>
  │
  └─ Execute and report results
        └─ On follow-up request → summarize, translate, analyze, etc.
```

## Intent Mapping

| User says | Execute |
|-----------|---------|
| 「ノートを開いて」 | `obsidian open file=<name>` |
| 「○○を見せて」 | `obsidian read file="○○"` |
| 「メモを作って」 | `obsidian create name=<name> content="..."` |
| 「Obsidianに保存して」 | `obsidian create name=<name> content="..."` |
| 「ノートに追記」 | `obsidian append file=<name> content="..."` |
| 「デイリーノートを開いて」 | `obsidian daily` |
| 「デイリーにタスク追加」 | `obsidian daily:append content="- [ ] ..."` |
| 「Vaultの中身」 | `obsidian files` / `obsidian folders` |
| 「inboxの一覧」 | `obsidian files folder=inbox` |
| 「ノートを検索」 | `obsidian search query="..."` |
| 「○○を含むノート」 | `obsidian search:context query="..."` |
| 「ノートを移動」 | `obsidian move file=<name> to=<path>` |
| 「ノートを削除」 | `obsidian delete file=<name>` (confirm first) |
| 「プロパティを確認」 | `obsidian properties file=<name>` |
| 「ステータスをdoneに」 | `obsidian property:set name=status value=done file=<name>` |
| 「未完了タスク一覧」 | `obsidian tasks todo` |
| 「タスクを完了に」 | `obsidian task ref="path:line" done` |
| 「タグ一覧」 | `obsidian tags counts` |
| 「バックリンク確認」 | `obsidian backlinks file=<name>` |
| 「○○を読んで要約」 | `obsidian read file=<name>` → summarize content |

## Vault Path for Glob/Grep Fallback

Retrieve the Vault path and use Glob/Grep tools for more flexible file content searches:

```bash
obsidian vault info=path
```

## Error Handling

| Situation | Action |
|-----------|--------|
| `obsidian` command not found | Guide CLI setup (Settings → General → CLI) |
| Obsidian app not running | First command launches the app automatically |
| Note not found | Search with `obsidian search query="..."` and suggest candidates |
| Vault not found | Show vault list with `obsidian vaults verbose` |

## Important Rules

- Confirm with AskUserQuestion on ambiguous requests
- Always confirm before delete operations (default goes to trash, but confirm anyway)
- Use `obsidian read` to fetch note content, then apply follow-up processing (summarize, translate, analyze)
- Prepend `vault=<name>` when targeting a specific vault
- Choose `file=<name>` (name resolution) vs `path=<path>` (exact path) appropriately

## Additional Resources

### Reference Files

To look up exact parameters, flags, or usage examples for any command, read:
- **`references/obsidian-cli-cheatsheet.md`** — Full CLI cheatsheet covering vault, files, read/write, daily notes, search, tags, tasks, properties, links, templates, bookmarks, plugins, history, workspaces, and developer commands

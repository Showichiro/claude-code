---
description: |-
  gog CLI で Google Classroom を操作する（Workspace for Education）。
  「/gog-classroom [操作] [オプション]」でコース・課題・名簿・成績等を管理。
  courses, roster, coursework, submissions, announcements, topics 等をサポート。
allowed-tools:
  - Bash
  - AskUserQuestion
---

# gog-classroom

gog CLI を使って Google Classroom を操作するコマンド。Workspace for Education アカウントが必要。

## サポートする操作

| 操作 | 説明 |
|------|------|
| `courses list` | コース一覧 |
| `courses get` | コース詳細 |
| `courses create` | コース作成 |
| `courses update` | コース更新 |
| `courses archive/unarchive` | コースのアーカイブ |
| `courses url` | コースの Web URL |
| `roster` | 名簿表示 |
| `students add` | 生徒追加 |
| `teachers add` | 教師追加 |
| `coursework list/get/create/update` | 課題管理 |
| `coursework assignees` | 課題の割り当て |
| `materials list/create` | 教材管理 |
| `submissions list/get/grade/return/turn-in/reclaim` | 提出物管理 |
| `announcements list/create/update/assignees` | お知らせ管理 |
| `topics list/create/update` | トピック管理 |
| `invitations list/create/accept` | 招待管理 |
| `guardians list/get/delete` | 保護者管理 |
| `guardian-invitations list/create` | 保護者招待 |
| `profile get` | プロフィール表示 |

## 実行手順

### コース管理

```bash
gog classroom courses list
gog classroom courses list --role teacher
gog classroom courses get <courseId>
gog classroom courses create --name "Math 101"
gog classroom courses update <courseId> --name "Math 102"
gog classroom courses archive <courseId>
gog classroom courses unarchive <courseId>
gog classroom courses url <courseId>
```

### 名簿

```bash
gog classroom roster <courseId>
gog classroom roster <courseId> --students
gog classroom students add <courseId> <userId>
gog classroom teachers add <courseId> <userId>
```

### 課題

```bash
gog classroom coursework list <courseId>
gog classroom coursework get <courseId> <courseworkId>
gog classroom coursework create <courseId> --title "Homework 1" --type ASSIGNMENT --state PUBLISHED
gog classroom coursework update <courseId> <courseworkId> --title "Updated"
gog classroom coursework assignees <courseId> <courseworkId> --mode INDIVIDUAL_STUDENTS --add-student <studentId>
```

### 教材

```bash
gog classroom materials list <courseId>
gog classroom materials create <courseId> --title "Syllabus" --state PUBLISHED
```

### 提出物・成績

```bash
gog classroom submissions list <courseId> <courseworkId>
gog classroom submissions get <courseId> <courseworkId> <submissionId>
gog classroom submissions grade <courseId> <courseworkId> <submissionId> --grade 85
gog classroom submissions return <courseId> <courseworkId> <submissionId>
gog classroom submissions turn-in <courseId> <courseworkId> <submissionId>
gog classroom submissions reclaim <courseId> <courseworkId> <submissionId>
```

### お知らせ

```bash
gog classroom announcements list <courseId>
gog classroom announcements create <courseId> --text "Welcome!"
gog classroom announcements update <courseId> <announcementId> --text "Updated"
```

### トピック

```bash
gog classroom topics list <courseId>
gog classroom topics create <courseId> --name "Unit 1"
gog classroom topics update <courseId> <topicId> --name "Unit 2"
```

### 招待

```bash
gog classroom invitations list
gog classroom invitations create <courseId> <userId> --role student
gog classroom invitations accept <invitationId>
```

### 保護者

```bash
gog classroom guardians list <studentId>
gog classroom guardians get <studentId> <guardianId>
gog classroom guardians delete <studentId> <guardianId>
gog classroom guardian-invitations list <studentId>
gog classroom guardian-invitations create <studentId> --email parent@example.com
```

### プロフィール

```bash
gog classroom profile get
gog classroom profile get <userId>
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| gog 未インストール | `brew install steipete/tap/gogcli` を提案 |
| Workspace for Education アカウントなし | 対応アカウントが必要であることを案内 |
| 権限エラー | `gog auth add --services classroom --force-consent` を案内 |

## 使用例

```bash
/gog-classroom courses list
/gog-classroom coursework list <courseId>
/gog-classroom submissions grade <courseId> <courseworkId> <submissionId> --grade 90
```

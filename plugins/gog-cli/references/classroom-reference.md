# Classroom リファレンス

Google Workspace for Education アカウントが必要。

## コース

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

## 名簿

```bash
gog classroom roster <courseId>
gog classroom roster <courseId> --students
gog classroom students add <courseId> <userId>
gog classroom teachers add <courseId> <userId>
```

## 課題

```bash
gog classroom coursework list <courseId>
gog classroom coursework get <courseId> <courseworkId>
gog classroom coursework create <courseId> --title "Homework 1" --type ASSIGNMENT --state PUBLISHED
gog classroom coursework update <courseId> <courseworkId> --title "Updated"
gog classroom coursework assignees <courseId> <courseworkId> --mode INDIVIDUAL_STUDENTS --add-student <studentId>
```

## 教材

```bash
gog classroom materials list <courseId>
gog classroom materials create <courseId> --title "Syllabus" --state PUBLISHED
```

## 提出物・成績

```bash
gog classroom submissions list <courseId> <courseworkId>
gog classroom submissions get <courseId> <courseworkId> <submissionId>
gog classroom submissions grade <courseId> <courseworkId> <submissionId> --grade 85
gog classroom submissions return <courseId> <courseworkId> <submissionId>
gog classroom submissions turn-in <courseId> <courseworkId> <submissionId>
gog classroom submissions reclaim <courseId> <courseworkId> <submissionId>
```

## お知らせ

```bash
gog classroom announcements list <courseId>
gog classroom announcements create <courseId> --text "Welcome!"
gog classroom announcements update <courseId> <announcementId> --text "Updated"
gog classroom announcements assignees <courseId> <announcementId> --mode INDIVIDUAL_STUDENTS --add-student <studentId>
```

## トピック

```bash
gog classroom topics list <courseId>
gog classroom topics create <courseId> --name "Unit 1"
gog classroom topics update <courseId> <topicId> --name "Unit 2"
```

## 招待

```bash
gog classroom invitations list
gog classroom invitations create <courseId> <userId> --role student
gog classroom invitations accept <invitationId>
```

## 保護者

```bash
gog classroom guardians list <studentId>
gog classroom guardians get <studentId> <guardianId>
gog classroom guardians delete <studentId> <guardianId>
gog classroom guardian-invitations list <studentId>
gog classroom guardian-invitations create <studentId> --email parent@example.com
```

## プロフィール

```bash
gog classroom profile get
gog classroom profile get <userId>
```

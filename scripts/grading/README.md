# scripts/grading — moved to ai-lms

The final-grade pipeline that lived here (`compute_final_grades.py`, `configs.py`,
`letter_grade.py`, `verify_final_grades.py`) moved on 2026-09-16 to the sibling `ai-lms` repo's
`grading` skill, with the same file names:

```
C:\GitHub\ai-lms\.claude\skills\grading\scripts\final_grades\
```

Run it from there against this repo's gitignored exports:

```
python C:/GitHub/ai-lms/.claude/skills/grading/scripts/final_grades/compute_final_grades.py <course_key> <input.xlsx> <output.xlsx>
```

All grading — stage sweeps, student comments, final grades, the letter scale — runs from ai-lms
(see `AGENTS.md` § Grading). The pre-move scripts remain in this repo's git history.

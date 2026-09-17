# _tools — archived

The BUS-629 / BUS-314 performance-ratios grading scanners (`grade_stage0..5.py`, `sweep_stage.py`,
`grade_one.py`, `_grading_comments.py`, roster builders) were **archived local-only on 2026-09-16**
to `_archive/bus629-tools/` (gitignored, same convention as `_archive/bus314/`). They remain in
this repo's git history before that commit.

They are not extended. Grading for every course runs from the sibling `ai-lms` repo's `grading`
skill (`C:\GitHub\ai-lms\.claude\skills\grading\`); a course that runs again gets a
`references/courses/<course>.json` there. See `AGENTS.md` § Grading.

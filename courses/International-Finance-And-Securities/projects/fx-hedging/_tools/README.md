# _tools — frozen 2026-09-16

The FIN-321 fx-hedging grading scanners in this folder (`grade_stage0..5.py`, `sweep_stage.py`,
`grade_one.py`, `grade_urls.py`, `_grading_comments.py`, `feedback-template.md` and the `_*.py`
helpers) are **frozen as of 2026-09-16. Do not extend them.** They graded the Summer 2026 offering
and stay here as the record of how.

The next FIN-321 offering grades through the sibling `ai-lms` repo's `grading` skill
(`C:\GitHub\ai-lms\.claude\skills\grading\`) with a `references/courses/fin-321.json` carrying the
rubric weights, canonical paths, point values and floor policy. The policies these scanners encode —
one generosity-only sweep per stage then lock, no double deduction on carried-forward gaps,
self-explaining floor rows, every comment closing forward — are carried as rules in that skill.
See `AGENTS.md` § Grading.

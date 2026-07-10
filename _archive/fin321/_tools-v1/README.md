# FIN-321 — Archived v1 grading scripts (retired)

These are the **v1** fx-hedging grade scripts, used to grade the completed
2026-Spring offering (the four-stage Build → Document → Analyze arc). They are
kept for provenance; the exported grades and worksheets live under
`FIN-321/ignore/2026-Spring/`.

| Script | v1 stage it graded |
|--------|--------------------|
| `grade_stage2.py` | Stage 2 — Excel model build (xlsx scan) |
| `grade_stage3.py` | Stage 3 — technical specification (post-build) |
| `grade_stage4.py` | Stage 4 — final analysis + AI prompt |
| `fetch_stage4.py` | GitHub fetch helper feeding `grade_stage4.py` |

## Superseded by

The **v2 six-stage** toolchain in
`courses/International-Finance-And-Securities/projects/fx-hedging/_tools/`
(`grade_stage0`–`grade_stage5` + shared `_weights` / `_curve` / `_repo` /
`_grading_comments` / `_safe_zip`). v2 grades every stage by repo inspection,
scores on a %-of-stage basis from the single source of truth in `_weights.py`,
and emits both an internal `STAGE{N}_GRADES.md` and score-free PR feedback.

Note the stage numbers do **not** map one-to-one: v2 Stage 3 is the
AI-assisted build + audit, not the v1 post-build spec.

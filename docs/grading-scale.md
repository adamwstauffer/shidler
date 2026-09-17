# Grading Scale (SSOT)

**The single source of truth moved to the sibling `ai-lms` repo on 2026-09-16**, with the rest of
the grading toolchain: `C:\GitHubi-lms\.claude\skills\gradingeferences\grading-scale.md`
(helper: `python C:/GitHub/ai-lms/.claude/skills/grading/scripts/final_grades/letter_grade.py 92`
→ `A-`). This file is a **mirror — edit the ai-lms copy**, then refresh the table here.

Adam W. Stauffer's standard letter-grade scale for Shidler courses, for converting a **numeric**
semester grade to a **letter** grade. **Never infer a letter grade from a number without this
scale.** Apply it exactly at a cutoff; curves only ever raise a grade, never lower it.

## Scale (mirror)

| Letter | Minimum score (≥) |
|:------:|:-----------------:|
| A+ | 97 |
| A  | 93 |
| A− | 90 |
| B+ | 87 |
| B  | 83 |
| B− | 80 |
| C+ | 77 |
| C  | 73 |
| C− | 70 |
| D+ | 67 |
| D  | 65 |
| F  | < 65 |

Note this scale has **no D−**, and the F cutoff is **below 65** (not 60).

The LMS `*_FinalGrades_*.xlsx` exports (in each offering's gitignored `ignore/<term>/grades/`)
already carry the computed letter in column `P`; the plain `*_Grades_*.csv` exports carry only the
number — for those, apply the scale in ai-lms.

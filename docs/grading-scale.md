# Grading Scale (SSOT)

Adam W. Stauffer's standard letter-grade scale for Shidler courses. This is the single source of
truth for converting a **numeric** semester grade to a **letter** grade. Use it whenever a
gradebook export gives only a number (the LMS CSV exports do) and a letter is needed — e.g., filling
a `<course grade>` in a recommendation letter, or reporting a grade to a student.

**Never infer a letter grade from a number without this scale.** If a score sits near a cutoff,
apply the scale exactly; do not round up or "give the benefit of the doubt" unless a
[curve](../../MEMORY.md) explicitly applies (curves only ever raise a grade, never lower it).

## Scale

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

Canonical spreadsheet formula (col `O` = numeric score):

```
=IFS(O7>=97,"A+",O7>=93,"A",O7>=90,"A-",O7>=87,"B+",O7>=83,"B",O7>=80,"B-",O7>=77,"C+",O7>=73,"C",O7>=70,"C-",O7>=67,"D+",O7>=65,"D",TRUE,"F")
```

## Where the letter already exists

The LMS **`*_FinalGrades_*.xlsx`** exports (in each offering's gitignored `ignore/<term>/grades/`)
carry the computed letter in **column `P`** (the IFS formula above). The plain **`*_Grades_*.csv`**
exports carry only the numeric "Semester Grade Points" — for those, apply this scale (or
`scripts/grading/letter_grade.py`).

## Helper

`scripts/grading/letter_grade.py` applies this scale programmatically:

```
python scripts/grading/letter_grade.py 92        # -> 92 -> A-
```

# Rosters — student PII, never public

This tree holds **rosters, attendance sheets, and approved-access lists** — the one category
of course data that carries student names. It lives at the repo root so there is a single place
to look, and a single ignore rule guarding all of it.

## Why everything here except this README is gitignored

The repo is public. Roster and attendance files contain student PII (names, and in some exports
emails or IDs), which must never land on the tracked tree — FERPA, and plain good sense. The
`.gitignore` rule is `/rosters/**` with this README whitelisted (`!/rosters/README.md`), so the
folder is documented in git while every data file stays local-only. **Keep it that way:** don't
add exceptions for data files, and don't commit anything else from this tree.

## Layout

```
rosters/<COURSE-CODE[-POPULATION]>/[<term>/]…
```

Mirrors shidler's offering naming — the same `<CODE[-POPULATION]>` folders used under
`courses/<Subject>/`. Examples:

- `rosters/FIN-321/` — International Business Finance section roster
- `rosters/BUS-629-VEMBA/` — the Vietnam EMBA cohort
- `rosters/BUS-313/2026-Summer/` — term subfolder where a course spans multiple offerings

Term subfolders use hyphenated names (`2026-Summer`, `2026-Spring`), not spaces or underscores.

## `rosters/approved/`

`rosters/approved/kumu-approved.xlsx` is the **Kumu-site access list** — the roster of students
approved for the Kumu tutorial-site pilot (see the access-gates design plan in the private
ai-lms repo). Like everything else here, it never leaves Adam's machine.

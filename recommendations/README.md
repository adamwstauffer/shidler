# Recommendations — student PII, never public

This tree holds **recommendation letters, the résumés and application materials students send in
support of them, and the correspondence requesting them**. It lives at the repo root so there is a
single place to look, and a single ignore rule guarding all of it.

## Why everything here except this README is gitignored

The repo is public. Letters and their supporting files carry student names, grades, GPAs, contact
details, and personal narratives — PII that must never land on the tracked tree (FERPA, and plain
good sense). The `.gitignore` rule is `/recommendations/**` with this README whitelisted
(`!/recommendations/README.md`), so the folder is documented in git while every letter, résumé,
and email stays local-only. **Keep it that way:** don't add exceptions for content files, and
don't commit anything else from this tree.

## Layout

One folder per student, named by the **letter's authored date and the student's name**:

```
recommendations/<YYYY-MM>-<lastname>-<firstname>/…
```

Each folder holds the letter(s) — the editable `.docx` is the source of truth, any signed/final
`.pdf` alongside it — plus whatever the student supplied (résumé, personal statement, the "what to
highlight" email). Students applying to several schools/firms keep one folder with a file per
target (e.g. Kilian Maitre's five business-school versions). Examples:

- `2026-07-bodner-cameron/` — generic job-search reference (FIN 321) + résumé + LOR-request emails
- `2024-10-maitre-kilian/` — five school/employer versions of one letter
- `2025-12-kim-richard/` — Georgetown + Boston College drafts, base letter, and application packet

## `master-recommendation-template.docx`

A local convenience copy of the reusable **master template**: the fixed letter scaffold (bio +
signature verbatim), a paste-ready course block for every course Adam teaches (BUS 313 / 314 / FIN
321 / BUS 620 / BUS 629 / BUS 122B), purpose-line and closing-line menus, combo guidance, and
style notes. Build a new letter from this rather than copying a prior student's file (which would
drag their PII along).

The **canonical, version-controlled** copy lives in the `recommendation-letters` skill at
`.claude/skills/recommendation-letters/assets/master-recommendation-template.docx` (this tree is
gitignored, so the copy here is untracked). That skill also encodes the house style and the
non-negotiable **"verify, never invent"** rule — invoke it when drafting any letter.

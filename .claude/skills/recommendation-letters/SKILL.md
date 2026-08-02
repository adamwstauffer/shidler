---
name: recommendation-letters
description: Draft or edit recommendation / reference letters for Adam W. Stauffer's students (Shidler College of Business, UH Mānoa) in his established house style. Use whenever asked to write, draft, tweak, or tailor a letter of recommendation, reference letter, or LOR — for graduate/MBA/law admissions, scholarships, study abroad, internships, or jobs. Enforces the non-negotiable rule to NEVER invent facts (grades, GPAs, employers, titles, achievements, career goals, motivations) and to keep any placeholder generic. Points to the master template, the per-course "course block" library, and where finished letters are stored.
---

# Recommendation Letters

Draft recommendation and reference letters for Adam W. Stauffer's students in his established
house style, working only from verified facts.

## Ground rule: verify, never invent (non-negotiable)

Every substantive claim in a letter must come from a source the student actually supplied — a
grade from the gradebook/transcript, a fact from their résumé, an objective stated in their own
words (email, personal statement). **Never infer, estimate, or fabricate** grades, GPAs,
employers, job titles, dates, achievements, career goals, or motivations.

- If a needed fact is missing, **leave a generic placeholder or ask the user** — do not guess.
- Placeholders stay **generic and descriptive**: `<FIN 321 grade>`, `<student's stated objective>`,
  `<employer / role from résumé>`.
- **Never write a specific value you have not verified, not even as a placeholder** — e.g. never
  `<A+>`, never a made-up firm or figure. A specific-looking placeholder reads as a real fact once
  the brackets are removed, which is exactly the failure this rule prevents.
- This applies to characterizations too: don't assert a student "excelled" or was "top of the
  class" unless the record supports it.

When unsure whether something is verified, treat it as unverified.

## Where things live

- **Master template (canonical, fill-in):** `assets/master-recommendation-template.docx` in this
  skill. It holds the fixed scaffold (bio + signature verbatim), a paste-ready **course block for
  every course Adam teaches** (BUS 313 / 314 / FIN 321 / BUS 620 / BUS 629 / BUS 122B), purpose-line
  and closing-line menus, combo guidance, and style notes. Every fill-in is a generic `<green
  field>`.
- **Finished letters + student materials:** `recommendations/<YYYY-MM>-<lastname>-<firstname>/` at
  the repo root. This tree is **gitignored** (student PII); see `recommendations/README.md`. Date =
  the letter's authored month. Multi-target applicants keep one folder with a file per school/employer.
- **Grades** to fill `<course grade>` fields come from the gradebook, not memory. Gradebooks are
  consolidated under each offering's `ignore/<YYYY-Season>/grades/`. The `*_FinalGrades_*.xlsx`
  exports carry the **letter grade in column P** (and the numeric in column O); the plain
  `*_Grades_*.csv` exports carry only the number — convert those with the SSOT scale in
  [`docs/grading-scale.md`](../../../docs/grading-scale.md) or `scripts/grading/letter_grade.py`
  (e.g. `python scripts/grading/letter_grade.py 92` → `A-`). **Never guess a letter from a number** —
  read column P or apply the scale.

## Workflow

1. **Gather the source facts first.** Adam's practice is to ask the student for (a) a bullet list of
   what to highlight and (b) their résumé; the request email often also names the target
   program/role. Read those before drafting. If a grade is needed, get it from the gradebook.
2. **Build from the master template, never by copying another student's letter.** Copying a prior
   letter drags that student's PII (and sometimes their grades) into the new one. Start from
   `assets/master-recommendation-template.docx`.
3. **Assemble:** pick one Purpose Line → paste the Course Block(s) for the course(s) taught (stack
   clauses for combos) → write 1–2 differentiator paragraphs mapped from the student's own bullets
   and résumé → pick a Closing Line. Fill every `<field>`, including `<he/she/they>` pronouns and
   `<course grade>`. Leave any field you can't verify as a placeholder and flag it to the user.
4. **Render onto the branded letterhead** (see below) and save the `.docx` + a `.pdf` into the
   student's folder.

## Rendering onto the UH letterhead (required for outgoing letters + PDFs)

Outgoing letters and PDFs use Adam's branded base, `recommendations/recommendation-template-format.docx`
— UH/Shidler letterhead (first-page header) + the signature block with his signature and seal images.
**That base stays gitignored** (it embeds his signature) and is never bundled into the tracked repo.

Build with `scripts/build_letter.py`, which swaps only the body (title → closing) onto the base and
leaves the letterhead, footers, and signature block untouched:

```
python .claude/skills/recommendation-letters/scripts/build_letter.py content.json
```

`content.json` = `{base, out, title, date, recipient_lines[], salutation, body_paragraphs[],
space_after, line_spacing, title_before}`. Then convert to PDF with LibreOffice directly
(`"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf --outdir <dir> <docx>`).

**One page, always** — unless there is a genuine reason for more (rare). If a letter spills to a
second page, tighten in this order before ever cutting substance: lower `space_after` (160 → ~130),
then `line_spacing` (1.0 → ~0.90). Verify the page count from the rendered PDF (`pdfinfo`), and
confirm the title clears the letterhead (raise `title_before`, default 560, if it crowds "MĀNOA").
Note: if the target `.docx` is open in Word the save fails ("Device or resource busy") — build to a
scratch path, then place it once the file is closed.

## House style (what a finished letter looks like)

**Always one page** unless there is a genuine reason for more (rare). 4–5 short paragraphs:

1. **Purpose + bio.** Purpose line, then the fixed bio verbatim: *"I am a Faculty Lecturer in
   Finance and Economics at the Shidler College of Business, University of Hawaiʻi at Mānoa. Before
   entering academia, I served as Chief Investment Officer at Springline Capital, and previously
   worked as a trader at Barclays Capital and Lehman Brothers. I hold an MBA from The Wharton School
   and was formerly a CFA Charterholder."*
2. **Course(s) + grade + performance** — from a Course Block.
3. **Differentiators** — professional experience, character, purpose, drawn only from the student's
   résumé and their own "what to highlight" list (1–2 paragraphs).
4. **Close** — escalating endorsement (*"my strongest / highest recommendation … without
   reservation"* for top students); add a direct-reference offer with contact info for job letters.

Signature block (verbatim):

```
Sincerely,

Adam W. Stauffer

Faculty Lecturer, Finance & Economics
Shidler College of Business
University of Hawaiʻi at Mānoa
adamstau@hawaii.edu
```

## Conventions

- **Diacriticals:** always "University of Hawaiʻi at Mānoa" with the ʻokina and macron.
- **Audience framing:** mirror the reader — admissions committees → "your program / cohort";
  employers → "your team." Never frame the reader as "recruiters."
- **GPA:** include only when it is a genuine strength *and* you have the verified number; otherwise
  let applied accomplishments carry the letter.
- **Generating the .docx:** render onto the branded base with `scripts/build_letter.py` (see
  "Rendering onto the UH letterhead" above) — it keeps the letterhead Times New Roman 12pt house
  look. On Windows, preview/convert by calling
  `"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf` directly — the
  docx skill's `soffice.py` wrapper fails there (it assumes a Unix socket). For deeper .docx
  mechanics, use the `docx` skill.

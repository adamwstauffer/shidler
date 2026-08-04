---
template: stage-brief
status: draft
purpose: "Authoring template for every stage brief in every course — fixed section order, fixed frontmatter, semester-invariant content only"
audience: instructor
instantiated_audience: student
destination: "C:/GitHub/shidler/docs/templates/stage-brief-template.md"
related:
  - ../decisions/2026-08-02-stage-brief-template-and-content-ownership.md
  - "C:/GitHub/shidler/docs/templates/README.md"
---

# Stage brief template

Every stage brief, in every course, uses the frontmatter block and the ten sections below, in
this order. Sections are never reordered, renamed, or dropped; a section with nothing to say is
written as `_None for this stage._` so the omission is visible rather than accidental.

Two rules govern the whole document:

**Semester-invariant.** A brief is written once and reused every offering. Nothing that changes
between offerings appears in it — see § Authoring rules for the enumerated ban list.

**Self-contained.** A student who has never met the instructor, attended no session, and watched
no recording must be able to complete the stage from this document plus the reference docs it
links. No sentence may assume live instruction.

---

## Frontmatter

Required on every instantiated brief. Extends the schema in `shidler/docs/templates/README.md`.

```yaml
---
template: stage-brief
project: {project-slug}          # directory slug, e.g. perfect-competition-marginal-costs
stage: {n}                       # INTEGER, numbered per case from 1 — matches the filename
title: "{Stage title}"           # e.g. "Engagement Brief"
capability: {capability-slug}    # the skills/<capability>/ folder this stage builds or uses; omit if none
deliverables:                    # THE path declaration — nothing else may introduce a path
  - path: docs/briefs/{engagement}-brief.md
    format: markdown
    ai_boundary: human-first     # per artifact, not per stage
  - path: skills/{capability}/model.xlsx
    format: xlsx
    ai_boundary: ai-first-verified
prerequisites: [{stage-id}, ...] # prior stages whose deliverables must exist; [] for the first
points: {n}                      # integer; must equal the rubric total
estimated_time: "{n}–{m} min"
---
```

| Field | Why it exists |
|---|---|
| `stage` | Integer, numbered **per case from 1** — the containing folder already scopes the case, so the filename does not encode it twice (`2026-08-02-pr-release-process-and-stage-naming.md`). |
| `deliverables` | The canonical **declaration** of the artifact paths. Prose in the body may reference a path but never introduce one. |
| `ai_boundary` | Sits on each deliverable, not on the stage — a repo skeleton and a falsifiable hypothesis produced in the same stage carry different boundaries. The § 6 stage-level line is derived from these values; the AI tutor consumes them per artifact. |
| `prerequisites` | Makes the self-contained rule checkable, and names what progression gating keys on. |
| `points` | Points are stable across offerings. Percentages, weights, and dates are not, and are banned from the body. |

---

## Body skeleton

Everything below is the instantiated document. Bracketed text is a placeholder; HTML comments are
authoring guidance and are deleted on instantiation.

```markdown
# {Project title} · Stage {n} — {Stage title}

**Deliverable:** {one line — the artifact(s), by name}
**Submission:** {invariant phrasing — see the submission reference; never name an LMS}
**Estimated time:** {n}–{m} minutes

---

## 1. Purpose

<!-- Two to three sentences. What this stage produces, and why it must happen before the next one.
     No scene-setting, no lede, no "in this stage you will…". State the function of the work. -->

## 2. Prerequisites

<!-- Two lists, both checkable by the student before starting:
     - Artifacts that must already exist (prior-stage deliverables, by path)
     - Reference docs to have read (link into the reference layer)
     First stage of a project: "None — this is the entry point," then the reference reading. -->

## 3. Deliverables

<!-- A table, generated from the frontmatter block. Nothing here may contradict it. -->

| Artifact | Path | Format |
|---|---|---|
| {name} | `{path}` | {format} |

## 4. Background

<!-- ONLY the concept unique to this stage — the economics, the finance, the method being taught.
     Anything a student needs in more than one course belongs in the reference layer and is linked,
     not restated. If this section exceeds ~400 words, something invariant has leaked into it. -->

## 5. Procedure

<!-- Numbered steps, imperative voice. Each step: the action, then how to confirm it worked.
     "Create X." not "Now we'll create X." No first-person plural. No "you'll notice that…".
     A step whose verification is "ask the instructor" fails the self-contained rule. -->

1. **{Action.}** {Detail.}
   *Confirm:* {what the student should now see}

## 6. AI use

<!-- Derived from the per-deliverable `ai_boundary` values in frontmatter. One row per artifact. -->

| Artifact | Draft order |
|---|---|
| `{path}` | {human-first | ai-first, verified | not permitted} |

<!-- ONE sentence of fixed prose — the only text mandated verbatim in every brief. Everything else
     about how the two loops work is invariant and lives in the reference layer, linked below. -->

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact
is a means to the work rather than the work itself, AI may draft it and you verify.** The two
working loops — human-first critique and AI-first verification — are described in
[the AI conventions guide]({reference-layer-url}).

**For this stage specifically:** {one or two sentences — what AI may and may not touch here, and
why the boundary sits where it does.}

## 7. Verification

<!-- Self-check the student runs before submitting. Mirrors the rubric criteria but carries no
     points and names no scores — it is a checklist, not a grade preview. -->

- [ ] {checkable statement}

## 8. Rubric ({n} pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| {criterion} | {n} | {the observable difference between adequate and strong} |

<!-- Points must sum to the frontmatter `points`. Percentages of the course grade never appear. -->

## 9. Common failure modes

<!-- Replaces "Tips." Instructional register: name the mistake, then the correction.
     Drawn from what actually goes wrong, not from generic advice. -->

| What goes wrong | The correction |
|---|---|
| {mistake} | {what to do instead} |

## 10. References

<!-- Links into the reference layer and to the project README. No inline restatement.
     One of these links is the submission reference, which also carries the post-deadline
     revision-sweep policy — invariant text, so it is linked here and never restated. -->
```

---

## Authoring rules

### Banned from every stage brief

Each of these changes between offerings, which is what makes a brief go stale:

| Banned | Where it belongs |
|---|---|
| Course codes and course names (`BUS 620`, `FIN 321`, "this course") | The course README and the syllabus |
| Section or population names (`VEMBA`, `DLEMBA`, "the EMBA section") | The course README |
| Semester, year, calendar dates, week numbers | The course calendar |
| Percentage weights of the course grade | The syllabus |
| LMS names and upload paths | The submission reference, once |
| Any sentence about how the class meets — kickoffs, live walkthroughs, screencasts, "we'll cover this in class", "bring a laptop" | Nowhere. The brief must stand without them. |
| Instructor-specific identifiers in prose | The submission reference; `{instructor-handle}` in the brief if unavoidable |
| **The name of the scenario's protagonist firm** — the company the student is advising | The case README's references section, with its sources |

**On the protagonist rule.** *Name the market, not the protagonist.* The market stays named,
quantified, and cited — acreage shares, prices per bag, what a patent does to a demand curve. What
is withheld is the identity of the firm being advised, and only in the narrative: the references
section names every party, because a citation that will not name its parties is not a citation. Hold
one noun consistently ("the seed company"); alternating between "the firm," "the company," and "the
producer" reads as evasion where one noun reads as convention. A live company name goes stale on a
slower clock than a week number but in the same way — brands are retired, deals are litigated, and
the footnote gets longer every year. Rule and rationale:
`ai-lms/docs/decisions/2026-08-03-case-scenario-anonymization.md`.

### Register

Instructional, not conversational. The brief tells a student what to do and why it matters; it is
not a transcript of the reasoning that produced it.

| Rewrite | To |
|---|---|
| "Two things happen here, and both are deliberately small." | "This stage produces two artifacts." |
| "`CLAUDE.md` is literally one line." | "`CLAUDE.md` contains a single line pointing to `AGENTS.md`." |
| "…and once junk lands in commits, getting it out is painful." | "Files committed once remain in the repository history even after deletion; excluding them beforehand is the only clean option." |
| "top-level `skills/` is *your* word, the one that goes on a resume" | "`skills/` names capabilities in your own terms, for human readers." |

No first-person plural, no rhetorical questions, no asides about the course's design intent.
Second person for instructions is correct and expected.

### The path rule

Deliverable paths are **declared** once, in frontmatter. The body's deliverables table renders that
declaration. Downstream consumers — the website's gate predicates, the Kumu stage page, any future
grading script — **mirror** it: they hold their own literal copies, each citing the brief it
mirrors, and the match is verified at PR rather than resolved at runtime. **No document restates a
path as an independent fact.** Where a path appears in prose, it is a reference to the declaration,
not a second source of it.

### Instantiation checklist

- [ ] Frontmatter complete; `points` equals the rubric total; every deliverable carries an `ai_boundary`
- [ ] All ten sections present and in order
- [ ] Ban list grepped clean (course codes, weeks, dates, percentages, LMS, delivery mode)
- [ ] § 4 Background under ~400 words and free of invariant material
- [ ] Every § 5 step has a `*Confirm:*` line
- [ ] § 6's table matches the frontmatter `ai_boundary` values, and the one fixed sentence appears verbatim
- [ ] No path appears that is not in the frontmatter `deliverables` block
- [ ] Self-contained test: a reader with no prior contact could finish the stage

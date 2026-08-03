---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 1
title: "Repo + Brief"
capability: marginal-analysis
deliverables:
  - path: "(repository) firstname-lastname"
    format: repo
    ai_boundary: ai-first-verified
  - path: docs/briefs/perfect-competition-brief.md
    format: markdown
    ai_boundary: human-first
prerequisites: []
points: 3
estimated_time: "60-80 min"
---

# Case 1 · Stage 1 — Repo + Brief

**Deliverable:** the portfolio repository, and `docs/briefs/perfect-competition-brief.md` inside it
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 60–80 minutes

---

## 1. Purpose

This stage produces two things: the public portfolio repository that every engagement lands in, and
a one-page engagement brief stating the farm's problem in your own words and ending in a hypothesis
you can be shown wrong about. Neither is analysis. Both are the conditions that make the analysis
worth anything — and the brief has to exist before the model does, because Stage 3 compares what you
predicted against what the model found, and that comparison cannot be reconstructed afterwards.

## 2. Prerequisites

None. This is the entry point for the engagement and for the repository.

Read before starting:

- [The portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) — the structure, the four starter files, and a prompt that builds the skeleton
- [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) — what goes in `AGENTS.md`, and what must never be committed
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics) — local versus remote, add → commit → push, `.gitignore`, and how work is submitted
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the shape of a brief
- The [case README](README.md) — scenario, assumptions table, constraints

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| Public portfolio repository, named for you | `github.com/{you}/firstname-lastname` | repository |
| Bio and engagement index | `README.md` | markdown |
| AI conventions, and the pointer to them | `AGENTS.md`, `CLAUDE.md` | markdown |
| Resume and prompt log, started | `RESUME.md`, `prompt-log.md` | markdown |
| Exclusion rules | `.gitignore` | text |
| The engagement brief | `docs/briefs/perfect-competition-brief.md` | markdown |

## 4. Background

A prediction written *before* the model runs is falsifiable. The same sentence written afterwards is
a summary of the output, and it teaches you nothing, because you can no longer distinguish "I
understood the economics" from "I read the answer cell."

This is not a classroom convention. It is why an analyst writes an engagement brief before opening
the data, and why "we always thought so" is the least trustworthy sentence in business. A wrong
hypothesis, precisely reasoned, is worth as much as a correct one and considerably more than a lucky
one.

What makes a hypothesis genuine is that some outcome would refute it. *"I expect roughly 15 tomato
beds, 20 carrot, 25 mesclun, because tomatoes earn about four times what carrots do per bed and I
doubt the labor penalty closes that gap"* names quantities and a mechanism, and the model can
contradict it. *"I expect a balanced mix because diversification reduces risk"* would survive any
result, which is what disqualifies it.

## 5. Procedure

1. **Create the GitHub account.** Use your `@hawaii.edu` address — it qualifies for
   [GitHub Education](https://education.github.com). Choose a professional username; it appears
   beside every piece of work you publish.
   *Confirm:* you can sign in, and the email is verified.

2. **Install GitHub Desktop**, or use the command line if you already prefer it. The deliverable is
   identical either way.
   *Confirm:* the app is signed in, and your Git config carries your real name and `.edu` address —
   both are stamped on every commit.

3. **Create the repository.** Name it `firstname-lastname`, set visibility to **public**, and
   initialize it with a README so it can be cloned.
   *Confirm:* the repository URL opens in a private browser window without a login prompt.

4. **Clone it, then build the skeleton** to the structure in the portfolio repo standard. Creating
   directories is mechanical work — use the starter prompt on that page and check the result rather
   than typing it out.
   *Confirm:* every directory holds at least one file, or Git will not track it.

5. **Write the four root files.** Replace the generated `README.md` with three to six sentences on
   who you are, followed by an engagement index. Add `RESUME.md`, `AGENTS.md` (start from the
   baseline on the AI conventions page and edit until it describes you), and the one-line
   `CLAUDE.md` pointing at it.
   *Confirm:* nothing in these files is placeholder text you would not want read.

6. **Add `.gitignore`** before any workbook is committed, using the starter block in
   [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore).
   *Confirm:* `~$`-prefixed files never appear in your Changes panel.

7. **Add your instructor as a collaborator** — repository **Settings → Collaborators → Add people**,
   then `adamwstauffer`. Collaborator access is what allows a review branch or a pull request against
   your work instead of an emailed paragraph.
   *Confirm:* the invitation shows as pending. You do not need to wait for it.

8. **Write the brief** at `docs/briefs/perfect-competition-brief.md`, using the structure on the
   deliverable-templates page. Read the [case README](README.md) first, then — **before opening the
   workbook or Solver** — write half a page to a page covering two things:
   - **The problem in your own words.** What the farm is deciding, what is fixed, what is chosen,
     what limits the choice. If you cannot state it without re-reading the case, you do not have it
     yet, and that is useful information about where the next hour goes.
   - **Your hypothesis.** *"I expect the optimal mix to be X because Y."* Real quantities — beds of
     tomatoes, carrots, mesclun — and real reasoning: prices per bed, labor intensity, the
     diminishing-returns percentages, the caps. Name the mechanism you think decides it.

   *Confirm:* the brief is committed before any modeling begins. The commit timestamp is what makes
   it a hypothesis rather than a summary.

9. **Commit and push.** At least two commits, each with a message saying what changed —
   `Add portfolio skeleton and gitignore`, then `Add perfect-competition brief with mix hypothesis`.
   *Confirm:* the files are visible on github.com, not only on your machine.

## 6. AI use

| Artifact | Draft order |
|---|---|
| Repository skeleton, `.gitignore`, the `AGENTS.md` starting point | AI-first, verified |
| `README.md` bio, `RESUME.md` | AI-first, verified — then edited until it sounds like you |
| `docs/briefs/perfect-competition-brief.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain the case's economics and argue against your
reasoning; it may not write the brief. A hypothesis you did not generate cannot be honestly compared
against results in Stage 3, and that comparison is the point. The other failure here is committing
generic AI-written filler as your bio — it is obvious to any reader, and it is the first thing anyone
sees.

## 7. Verification

- [ ] Repository is **public** — the URL opens in a private browser window without logging in
- [ ] Named for you (`firstname-lastname`), not for a course
- [ ] `README.md` holds a real three-to-six-sentence bio and the start of an engagement index
- [ ] `AGENTS.md` written in your own words; `CLAUDE.md` is the one-line pointer
- [ ] `RESUME.md` and `prompt-log.md` exist at the root — rough is acceptable
- [ ] `.gitignore` filters Office and OS temp files
- [ ] `docs/briefs/perfect-competition-brief.md` restates the problem in your voice
- [ ] The hypothesis names a specific mix **and** the mechanism behind it
- [ ] The brief was committed **before** any modeling work started
- [ ] `adamwstauffer` invited as a collaborator
- [ ] At least two commits, each with a message that says what changed

## 8. Rubric (3 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Repo live and public, professionally named | 1 | URL works without login; `firstname-lastname` naming; the bio in `README.md` is not placeholder text |
| Skeleton, `.gitignore`, and commit hygiene | 1 | `docs/briefs/` in place and the root files present (`AGENTS.md`, `CLAUDE.md`, `RESUME.md`, `prompt-log.md`); junk files filtered; at least two descriptive commits |
| Brief quality — genuine hypothesis | 1 | Problem restated accurately in your own voice; hypothesis names a specific mix with economic reasoning, written before any Solver work |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The repository is private, so nothing in it can be read | Settings → General → Change visibility → Public, then test the URL in a private window |
| The repository is named after the course | Rename it now, while nothing links to it — a course-shaped repository stops meaning anything at graduation |
| The hypothesis is hedged: "a balanced mix, because diversification" | Name quantities and a mechanism; a prediction that survives every outcome is not a prediction |
| The brief is written after the workbook | There is no recovery — the Stage 3 comparison is gone. Write it first, even badly |
| Empty directories disappear on push | Git tracks files, not folders; put a one-line `README.md` in each |
| An hour spent polishing the bio on day one | It evolves all term. Get the repository live |
| Commit messages read `update` | Say what changed: `Add brief: predicting tomato-heavy mix on price per bed` |

## 10. References

- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) · [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [`.gitignore`](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore) and [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
- [`docs/guides/github-mba-guide.md`](../../../../../docs/guides/github-mba-guide.md) — the long-form Git reference, for troubleshooting
- [Case README](README.md) — scenario, assumptions, constraints

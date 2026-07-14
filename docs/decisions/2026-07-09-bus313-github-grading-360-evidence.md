---
title: "BUS 313 Team Project — GitHub-Organization Grading Line & Issues-Based 360 Evidence"
date: 2026-07-09
status: proposed
owner: Adam W. Stauffer
scope: BUS-313
related:
  - 2026-05-28-bus313-team-presentation-project-design.md
  - 2026-05-28-bus313-trust-layer-integration.md
  - 2026-07-08-generic-course-directory-naming.md
---

# BUS 313 Team Project — GitHub-Organization Grading Line & Issues-Based 360 Evidence

> **Drafted by Claude (Kumu project) for Adam's review — nothing here is adopted.** These are the
> two ideas deliberately left out of the AI + GitHub project layer drafted in
> `courses/International-Economics-And-Trade/BUS-313/ignore/in-progress/team-project/` because both
> touch grading, which that draft explicitly held constant.

## Executive Summary

Two additions are proposed to the BUS 313 import-a-product team project, both borrowed from
patterns already running in BUS 620. **(1)** Carve a small, explicit **GitHub-organization line**
out of Presentation #2's instructor points — recommended: **0.5 of the 5.0 instructor points
(10%)**, graded as a five-item binary checklist (~2 minutes per team). **(2)** Require each team to
run a lightweight **GitHub Issues board**, ungraded, and make it (plus PR history) the
**designated evidence source for the 360 intrateam peer review** — the multiplier that already
exists but currently runs on unverifiable self-report. Recommendation: adopt both for the next
BUS 313 offering (Fall 2026), with the checklist published in advance. Cost: one rubric row, one
sentence in the 360 survey, two README bullets. Risk: performative issue-farming — mitigated by
keeping the board itself ungraded.

## Background

- The team project's current grading: Preso #1 (2.5 pts), Preso #2 (5.0 instructor + 7.5 peer),
  forms (−0.5 each missing, max −1.5), 360 intrateam review as a **multiplier on team score**,
  profit-contest extra credit (3/2/1). The AI + GitHub layer (one repo per team, branch → PR →
  review → merge, design system, GitHub Pages listing, prompt log) is drafted but **changes no
  grading** — repo work is currently pure infrastructure with zero graded weight.
- Precedent in-house: **BUS 620's individual research paper grades "GitHub organization" at 10%**,
  and its team case runs the same repo discipline. That line has a rubric and survived contact
  with students.
- Floor conditions improved: the July 2026 **GitHub-portfolio extra credit** means a large share of
  BUS 313 students now arrive with an account, a public repo, and one commit cycle behind them —
  the "GitHub is too much overhead for a 300-level class" objection is weaker than it was in spring.
- The 360 multiplier's known weakness: it is scored from memory and social dynamics. Free-riding
  disputes land on the instructor with no artifact trail to consult.

## Decision 1 — Grade GitHub organization, and at what weight?

| Option | Mechanics | Pros | Cons |
|---|---|---|---|
| **A. Status quo** | Repo required, ungraded | Zero grading cost; repo stays "how we work," not "what's graded" | Predictable result: repos rot after week 2; the AI + GitHub layer reads as optional theater |
| **B. 0.5 pt inside Preso #2 instructor points (10%) — recommended** | New rubric row, five-item binary checklist | Mirrors BUS 620's proven 10%; small enough not to distort the project; big enough that teams assign someone to own it | One more rubric row to score; needs the checklist published up front |
| **C. Standalone graded deliverable (à la BUS 620's full line)** | Separate points for the repo itself | Strongest signal | Over-weights process in a 15-pt project whose soul is the market game; duplicates what Preso #2 already evidences |

**Recommended checklist for Option B** (each item 0.1 pt, binary, verifiable in the repo UI):

1. Repo has the required layout (`README.md`, `research/`, `brand/`, `listing/`, `model/`, `presentations/`, `prompt-log.md`).
2. Every research number in the decks traces to a screenshot committed under `research/`.
3. ≥ 1 merged pull request **per team member** with a substantive review comment from a teammate.
4. `prompt-log.md` shows dated, meaningful AI sessions (not one bulk paste the night before).
5. Listing is live on GitHub Pages and the URL in the deck works.

## Decision 2 — GitHub Issues as 360 evidence?

| Option | Mechanics | Pros | Cons |
|---|---|---|---|
| **A. Optional habit** | Mention Issues in the README, nothing more | No overhead | Nobody uses it; 360 stays memory-based |
| **B. Required board, ungraded, designated 360 evidence — recommended** | Each deliverable becomes an Issue with an assignee; 360 survey adds one line: *"Your ratings should be consistent with the team's Issues/PR history; flag any rating you expect a teammate to dispute."* Instructor consults the board only when multipliers are contested | Converts the 360 from testimony to evidence at zero grading cost; assignee fields make free-riding visible *during* the project, when it can still be fixed; the skill itself (issue-driven teamwork) is the real-world transferable | Boards can be gamed with performative issues — but ungraded boards remove most of the incentive; slight setup overhead (one demo in class) |
| **C. Formal audit** | Every 360 rating must cite issue/PR numbers; instructor reviews all boards | Maximum rigor | Grading cost explodes; converts teammates into bookkeepers; adversarial tone for a 15-pt project |

**Why B:** the 360 multiplier already has teeth; what it lacks is an artifact trail. Making the
board *evidence-on-dispute* rather than *graded output* keeps incentives clean — students maintain
it because it protects them, not because it's worth points. This is also the cheapest possible
version to pilot: if no dispute arises all semester, it cost nothing.

## Interaction effects

- Decision 1's checklist item 3 (merged PR per member) and Decision 2's assignee trail **measure the
  same underlying thing** (distributed contribution) through two different instruments — one graded
  lightly, one evidentiary. That redundancy is deliberate: gaming both simultaneously is more work
  than just contributing.
- Both slot into the drafted README brief with two bullets each; the website's project pages
  (`import-product-*.html` on Kumu) would each gain one row/sentence. No change to the market game,
  the presentations, the forms, or the contest.

## Limitations & Next Steps

- Weights are judgment calls, not data; after one semester, compare 360 dispute counts and repo
  activity distribution against the Spring 2026 baseline before hardening anything.
- If adopted: (1) add the rubric row + checklist to the Preso #2 guide, (2) add the survey
  sentence to the 360 form, (3) update the ignore/in-progress team-project README, (4) sync the
  Kumu project pages, (5) demo Issues for 5 minutes in the week-1 GitHub walkthrough.
- Explicitly out of scope: grading the Issues board itself, AI-detection of any kind, and changes
  to peer-review weights.

---
title: "BUS-313 Team Project — Multi-Stage Presentation Build (Design Memo)"
date: 2026-05-28
status: draft
owner: Adam W. Stauffer
course: BUS-313-Economic-And-Financial-Environment-Global-Business
scope: course
applies_to: BUS-313 Group Project (Online Retailing), Fall 2026 cohort and forward
related:
  - ../bus629/2026-05-07-bus629-stage2-restructure.md
  - ../bus629/2026-05-12-bus629-stage2-5-followup-revisions.md
  - ../bus314/2026-02-24-bus314-stage-restructure.md
  - ../../_branding/design.json
supersedes:
  - ../../../_archive/bus313/extra-credit.md  # archived 2026-05-28; replaced by integrated team-project flow
---

# BUS-313 Team Project — Multi-Stage Presentation Build

## Summary

Restructure the BUS-313 Online-Retailing team project into a 5-stage, GitHub-backed build that loosely mirrors the BUS-629 spec-driven LLM workflow but pivots the deliverable from Excel financial models to **branded slide decks generated with the help of LLMs**. Teams of 3–4 stand up a shared repo, author a `design.json` + `design-system.html` brand system for their fake product brand, write a product/market memo, then build two LLM-drafted pitch decks — the existing Sales presentation (Pres #1) and Unit-Economics presentation (Pres #2) — under that brand system. Stage 5 closes with a spec retrospective, repo polish, and the existing 360 peer-review multiplier. The brand-guide stage is the central pedagogical bet: it teaches students that a small, structured artifact (design tokens) can drive every downstream deliverable consistently — the same lesson BUS-629 teaches with the spec.

## Context

### Current project (Spring 2026)

- 20% of course grade. Teams of 3–4 select a product on Amazon, source it from Alibaba, "sell" it to classmates (each student gets a fake $200 budget), and present twice.
- **Pres #1 — Sales (5 min, 2.5%):** Fake Amazon listing / Shopify mock / deck — product title, description (≤500 chars), 5 unique-feature bullets, parameters (brand, color, weight), price.
- **Pres #2 — Unit Economics (5 min, 5%):** Supplier table (top 5 + ours), competitor table (top 3 + ours), tariff impact, cost/margin math.
- **Peer Review (7.5%):** intrateam multiplier on the overall team score.
- **Extra credit:** top 3 net-profit teams (units sold × profit/unit) → 3 / 2 / 1 points.
- Submissions are emails to the instructor; no version-controlled artifact survives.

### Issues observed

- **No durable artifact.** Decks live in inboxes; nothing portfolio-shaped survives the semester.
- **Branding is implicit.** Teams pick a brand name on Slide 1 and never operationalize it — colors, type, voice, logo concept all stay in the team's head.
- **AI is encouraged in the syllabus but never assigned.** The AI policy exists; the workflow doesn't require it.
- **Individual contribution is invisible.** With one shared email-attached deck per team, peer review is the only signal of who did what.
- **The "extra credit" Career Memo (Dec 2025)** sat outside the project as a parallel GitHub on-ramp. Archiving it and folding the GitHub on-ramp into Stage 0 of the team project removes a redundant track.

### Why this restructure now

The BUS-629 VEMBA pilot has proven that a 5-stage GitHub-backed flow with an LLM-drafted spec at the center is workable at the EMBA level. BUS-313 is the undergraduate analog of the same instructor's other international-finance/economics courses, with a project that already lends itself to creative branded output. Pivoting the deliverable from Excel to **PPT/deck generation under an LLM workflow** matches the actual skill these students will need in their first jobs (marketing analysts, junior consultants, business-development associates) — which is to specify a polished, brand-consistent presentation precisely enough that an LLM can produce a first draft they can edit, not to build a 3-statement model.

## Design overview

| Stage | Deliverable | Weight | Owner role | Presentation? |
|------:|-------------|-------:|------------|---------------|
| **0** | Team repo + charter + per-member bios | 5% | Project Manager | No |
| **1** | Brand & Design System (`design.json` + `design-system.html`) | 15% | Brand Director | No |
| **2** | Product/Market Memo (shortlist → final pick) | 15% | Market Analyst | No |
| **3** | Sales Pitch Deck (Pres #1) | 25% | Deck Lead | **Yes (5 min)** |
| **4** | Unit-Economics Deck + LLM Spec (Pres #2) | 30% | AI/Spec Lead | **Yes (5 min)** |
| **5** | Retrospective + Repo Polish + 360 Peer Review | 10% | All members | No |

Weights sum to 100% of the **project**, which remains 20% of the course grade. Peer review functions as an intrateam multiplier on Stage 5 (existing convention), and the net-profit extra-credit ladder (3 / 2 / 1 pts) is retained.

Project-internal directory layout (in the team repo):

```
team-bus313-{teamname}/
├── README.md                       # Team bio, product, links to each stage
├── LICENSE                         # MIT
├── .gitignore                      # ~$*.pptx, .DS_Store, *.tmp
├── brand/
│   ├── design.json                 # Stage 1 — design tokens
│   ├── design-system.html          # Stage 1 — single-page rendered reference
│   └── assets/                     # Logo concept, product hero images
├── docs/
│   ├── decisions/
│   │   └── YYYY-MM-DD-{teamslug}-product-selection.md   # Stage 2 memo
│   └── specs/
│       └── YYYY-MM-DD-{teamslug}-unit-econ-deck-spec.md # Stage 4 LLM spec
├── decks/
│   ├── YYYY-MM-DD-{teamslug}-sales-deck.pptx            # Stage 3 (Pres #1)
│   └── YYYY-MM-DD-{teamslug}-unit-econ-deck.pptx        # Stage 4 (Pres #2)
├── analysis/
│   └── validation/
│       └── YYYY-MM-DD-{teamslug}-stage5-verification.md # Pricing/margin tie-out
├── deliverables/
│   ├── prompt-log.md                                    # All LLM sessions
│   ├── YYYY-MM-DD-{teamslug}-spec-retrospective.md
│   └── YYYY-MM-DD-{teamslug}-contribution-map.md
└── team/
    ├── {lastname1}.md                                   # Per-member bio
    ├── {lastname2}.md
    └── …
```

---

## Team structure and individual accountability

This is the core of the team-project design. The decision is to **own the deliverable collectively but credit work individually**, so the project mirrors how real cross-functional teams ship in industry.

### One team repo, every member is a Write collaborator

A single team repo (named `team-bus313-{teamname}` or similar — team's choice). All members are added as Write collaborators at Stage 0. `adamwstauffer` is also added as a Write collaborator so feedback can land as Pull Requests (mirroring the BUS-629 model).

Individual authorship is captured by Git commit history. Stage 5 grades a `contribution-map.md` that names each member's primary commits per stage; the team must agree on it, and the map is cross-checked against `git log --author=` for honesty.

### Five named roles, rotating leadership

Each stage has a **designated lead** who owns sign-off and is the named "PM" for that stage. The team picks who plays which role at Stage 0; one student can hold two roles if the team is three people.

| Role | Stage lead | Cross-stage responsibility |
|------|-----------|---------------------------|
| **Project Manager** | Stage 0, Stage 5 | Repo hygiene, deadlines, contribution map |
| **Brand Director** | Stage 1 | Owns `design.json`; ensures every deck honors the brand system |
| **Market Analyst** | Stage 2 | Owns supplier/competitor research; updates margins for Stage 4 |
| **Deck Lead** | Stage 3 | Drives Pres #1 design; co-pilots Pres #2 |
| **AI/Spec Lead** | Stage 4 | Owns the deck spec; runs the LLM session; logs prompts |

Teams of 3 collapse Brand Director ↔ Deck Lead, or Market Analyst ↔ AI/Spec Lead. Teams of 4 take all five roles distinct except for one bundle. Teams of 5 are not expected (course caps at 4).

### Minimum-commit floors per member per stage

To prevent "one student does everything," each member must have **≥2 meaningful commits** on each stage that has multi-person scope (Stages 1, 3, 4, 5). The grading scanner reads `git log --author={email}` and flags missing members. This is rubric-enforced under Stage 5 polish.

### Peer review retained, repositioned

The existing 360 peer-review instrument (Flexible / Engaged / Reliable / Active Listener / Effective Communicator / Respectful) carries into Stage 5 and remains an **intrateam multiplier** on the overall team score, just as in the current rubric. A team that ships a strong deck but has an absent member is still penalized through the multiplier.

---

## Stage detail

### Stage 0 — Team Repo Setup (5%)

Stand up the shared repo, onboard collaborators, write a one-paragraph team charter naming roles, and commit per-member bios.

**Deliverables:**
- Public team repo with directory skeleton above and a `README.md` listing team name, product (TBD until Stage 2), and members.
- All teammates + `adamwstauffer` added as Write collaborators.
- `team/{lastname}.md` for each member (≤150 words, professional intro — light version of the BUS-629 bio template, since these are undergrads).
- Team charter section in README: who's playing which role, with one sentence on why.

**Rubric:** Repo public + accessible (20%) · Collaborators correctly added (20%) · Directory skeleton + per-dir READMEs (25%) · Team charter + bios (25%) · Commit hygiene (10%).

### Stage 1 — Brand & Design System (15%)

**This is the new pedagogical centerpiece.** Each team designs a brand for the product they will sell — encoded as machine-readable tokens (`design.json`) plus a one-page rendered reference (`design-system.html`).

The brand exists *before* the product is finalized. That ordering is intentional: it forces teams to commit to a brand POV (premium minimalist? loud value-brand? eco-earnest? gen-Z ironic?) that will then constrain product choice at Stage 2 and visual decisions at Stages 3 and 4. In the real world, brands precede SKUs.

**Deliverables:**

1. **`brand/design.json`** — design tokens following the UH Mānoa schema as a model (see [`docs/_branding/design.json`](../../_branding/design.json)). Required keys:
   - `meta` — brand name, tagline, lastUpdated, intended audience
   - `brand` — voice (personality, tone, things to avoid)
   - `colors` — primary (2), secondary (2), semantic (success/warning/error/info)
   - `typography` — heading family + body family + scale
   - `spacing` and `borderRadius` — minimum two tokens each
   - `components` — at least button + card examples with token references

2. **`brand/design-system.html`** — a single self-contained HTML page that *renders* the tokens. Required sections:
   - Palette swatches with hex + role label
   - Typographic scale samples
   - Logo concept (text mark is fine; an actual logo earns the design-craft rubric line)
   - Button / card / badge component samples
   - "Voice" examples — three sample slide-headline candidates that demonstrate the brand voice

3. **LLM workflow required.** Teams must use an LLM to draft both files. The prompt log entry (in `deliverables/prompt-log.md`) is graded. A team that hand-writes `design.json` without an LLM round earns less on the prompt-log line — the point of the stage is to learn how to specify a brand precisely enough for an LLM to render it.

**Rubric:** `design.json` completeness + schema fidelity (25%) · `design-system.html` rendered quality (25%) · Brand voice clarity (15%) · Token internal consistency (15%) · LLM workflow + prompt log (15%) · Commit hygiene + member participation (5%).

**Why this stage matters.** It is the BUS-313 analog of BUS-629's "spec drives downstream artifact" — except the artifact is a deck, not an analysis. Teams that take Stage 1 seriously make Stages 3 and 4 dramatically easier; teams that phone it in inherit a brandless deck and lose rubric points on visual consistency.

### Stage 2 — Product/Market Memo (15%)

The existing "shortlist 3 → pick 1" workflow, formalized as a written memo committed to the repo. Replaces the current email-to-instructor submission.

**Deliverable:** `docs/decisions/YYYY-MM-DD-{teamslug}-product-selection.md` — 600–900 words. Required sections:

1. **Product Shortlist (3)** — for each: 1-sentence rationale, average Amazon top-5 sales price (with screenshot links in `brand/assets/screenshots/`).
2. **Supplier Research (3 × 5)** — for each shortlisted product, top-5 Alibaba supplier averages.
3. **Final Selection** — pick one product; one paragraph on why (margin, scale potential, fit to brand voice from Stage 1).
4. **Falsifiable Sales Hypothesis** — in "We expect to sell X units at $Y because Z" form. Open-ended framings ("we'll see") do not earn credit. (Borrowed from BUS-629 Stage 2.)
5. **Tariff Exposure** — current US tariff rate on the product's HS code, sourced and cited.

**Rubric:** Selection rigor (25%) · Hypothesis quality / falsifiability (20%) · Supplier + competitor data quality with screenshots (25%) · Tariff sourcing (15%) · Writing + professionalism (15%).

### Stage 3 — Sales Pitch Deck (Pres #1) (25%)

The existing 5-minute Sales presentation — but built under the Stage 1 brand system, LLM-drafted, and committed as `.pptx` to the repo.

**Deliverable:** `decks/YYYY-MM-DD-{teamslug}-sales-deck.pptx` plus the in-class 5-minute presentation.

**Required slides** (carries over the existing Pres #1 spec):
1. Title — product name, team brand, presenter names
2. Product hero — image + tagline (brand voice from Stage 1)
3. Product description (≤500 chars)
4. Parameters table — brand, color(s), item weight, dimensions
5. 5 Unique-Features bullet slide
6. Price — including bundle pricing if applicable
7. Call to Action — "Buy now" mock CTA
8. Appendix — screenshots verifying retail price, supplier price

**LLM workflow required.** The team must:
- Submit the Stage 1 `design.json` + Stage 2 memo to an LLM as inputs.
- Prompt the LLM to draft slide-by-slide content honoring the brand voice.
- Iterate at least once (visible in `prompt-log.md`) before exporting to `.pptx`.
- The deck must visually reflect the Stage 1 design system (palette, type, voice). Decks that look like default PowerPoint themes lose the brand-fidelity line.

**Rubric:** Brand-fidelity to Stage 1 (20%) · Required-slide completeness (20%) · LLM workflow + prompt log (15%) · In-class delivery (20%) · Visual craft (15%) · Member participation (10%).

### Stage 4 — Unit-Economics Deck + LLM Spec (Pres #2) (30%)

**The heaviest stage and the closest analog to BUS-629 Stage 4.** Teams write an LLM spec for the unit-economics deck *before* letting an LLM draft it, then iterate.

**Two deliverables, one stage:**

1. **`docs/specs/YYYY-MM-DD-{teamslug}-unit-econ-deck-spec.md`** — a technical specification for the deck. Required sections:
   - **Part A — Deck Structure:** slide-by-slide outline (8–12 slides), purpose of each slide, what data lives on each.
   - **Part B — Data Inputs:** the actual tables of supplier prices, competitor prices, tariff %, expected margin (filled in numerically — values from Stage 2, not placeholders).
   - **Part C — Brand Application:** explicit references to `brand/design.json` tokens — which color for headers, which font weight for body, which slide layout for tables.
   - **Part D — Voice & Tone:** 3–5 sample headline / body-copy lines that anchor the LLM to the brand voice from Stage 1.

2. **`decks/YYYY-MM-DD-{teamslug}-unit-econ-deck.pptx`** — the actual deck, LLM-drafted from the spec, edited by the team, presented in class.

**HIL iteration required.** Same standard as BUS-629 Stage 4: at least one visible iteration in the prompt log where the team identified a gap in the LLM's first-draft deck and revised either the prompt or the spec to address it. A single-shot "make the deck" prompt does not earn the workflow credit.

**Required deck content** (carries over the existing Pres #2 template):
- Supplier Analysis — top 5 + ours
- Product Analysis — top 3 competitors + ours
- Cost / Tariff / Price / Margin breakdown
- Tariff impact discussion — "How did tariffs affect your product decision and where you sourced your product? Did you pass the increased cost on to your customers?" (preserves the existing Slide 6 prompt)
- Why-this-product narrative
- Appendix with supplier + competitor screenshots

**Rubric:** Deck spec completeness (Part A–D) (20%) · LLM workflow + HIL iteration (20%) · Brand-fidelity to Stage 1 (10%) · Data accuracy (margin/tariff math) (15%) · In-class delivery (15%) · Visual craft (10%) · Member participation (10%).

### Stage 5 — Retrospective + Repo Polish + 360 Peer Review (10%)

The capstone, modeled on BUS-629 Stage 5 but lighter — these are undergrads and Stages 3 + 4 already carry the deck-craft load.

**Deliverables:**

1. **`deliverables/YYYY-MM-DD-{teamslug}-spec-retrospective.md`** — uses the repo's [`docs/templates/spec-retrospective-template.md`](../../templates/spec-retrospective-template.md). Team agrees on a single retrospective on the Stage 4 spec: what was clear, what was vague, what they'd change.

2. **`deliverables/YYYY-MM-DD-{teamslug}-contribution-map.md`** — table of each member's commits per stage, with a 1-line note on the work. Honesty-checked against `git log --author=`.

3. **`analysis/validation/YYYY-MM-DD-{teamslug}-stage5-verification.md`** — recompute the margin math from Stage 4 by hand to verify the LLM-generated deck numbers. ≥3 ratios (margin %, breakeven units, tariff-adjusted margin). Cheap-but-real verification artifact mirroring BUS-629.

4. **360 Peer Review** — each member submits the existing 360 form (Flexible / Engaged / Reliable / Active Listener / Effective Communicator / Respectful). Aggregated peer score becomes the **intrateam multiplier** on the team's Stage 0–4 weighted score.

5. **Repo polish pass** — README updated with project status + final links, LICENSE present, `.gitignore` clean, every directory has a README, no orphan files.

**Rubric:** Spec retrospective specificity (25%) · Contribution map honesty (15%) · Margin verification (15%) · Repo polish checklist (25%) · 360 peer review submitted by all members (20%).

**Net-profit extra credit retained.** Top 3 teams by (units sold × profit-per-unit) → +3 / +2 / +1 to final course grade, unchanged from the current rubric.

---

## On the brand-guide stage — is this really worth a stage?

Yes, with conviction. Three reasons:

1. **It teaches the same lesson BUS-629 teaches with the spec, but in a domain undergrads care about.** A `design.json` is a portable spec of a brand identity. Once a team writes it, every downstream deck can be evaluated against it — "does this slide honor the brand?" becomes a concrete question with a checkable answer, not a taste debate. That is the *exact* skill transfer that the spec-driven LLM workflow needs.

2. **It removes a recurring failure mode.** Every prior cohort has produced decks that look like default PowerPoint themes with a team-name slapped on slide 1. Forcing brand decisions to be made *and serialized* before the deck builds start guarantees a higher visual-craft floor.

3. **It is genuinely portable.** `design.json` is a real artifact pattern (used by Figma Tokens, Style Dictionary, design-system tooling at every major company). Students who internalize this leave the course with a transferable mental model, not just a one-off deck.

The risk is that undergrads new to JSON or HTML treat this as a tooling barrier. Mitigation: the LLM workflow is *required*. A team can converse with Claude or ChatGPT in plain English to produce both files; no manual JSON authoring is expected. The graded artifact is the brand decisions, not the syntax.

---

## On individual accountability — why this design works

The single biggest failure mode of team projects is invisible free-riding. This design addresses it with **three independent signals** so no single mechanism has to carry the load:

| Signal | What it captures | Failure mode it catches |
|--------|-----------------|--------------------------|
| **Git commit authorship** | Who actually wrote which file, at the granularity of individual lines | Free-riders who don't push code/content |
| **Stage-lead role assignments** | Who took named ownership of each stage | Teams that don't have role clarity; surfaces conflict early |
| **360 peer review (existing instrument)** | Subjective team-experience signal — was this person flexible, engaged, reliable? | Members who technically did work but were toxic, late, or absent from meetings |

A free-rider has to evade all three to escape unscathed. They cannot.

---

## Open questions

1. **Pilot cohort.** Should this run Fall 2026 (next BUS-313 offering) or be piloted on a single section first? Recommendation: Fall 2026 full rollout; the current 20% weight gives runway.
2. **Team formation.** Self-formed (current) or instructor-assigned to balance skills (one student per role across each team)? Self-formed is lower-effort; assigned produces more reliable role coverage.
3. **Class-time budget.** Stage 1 (brand) is the new work. Does it need 30 minutes of in-class scaffold, or is the LLM workflow self-serve? Recommend a 20-min in-class demo of `design.json` → `design-system.html` rendering in class.
4. **GitHub onramp.** With the Career Memo extra-credit archived (2026-05-28), Stage 0 carries the entire GitHub onboarding load. Probably fine — Stage 0 only needs ≥2 commits per member, well within first-time GitHub user range. Confirm by mid-Fall in-class checkpoint.
5. **Pres #1 fake Amazon listing.** Existing Pres #1 allows "fake Amazon listing OR Shopify mock OR PowerPoint." Under this design, Stage 3 is `.pptx`-only for grading consistency. Teams who want to *additionally* produce an Amazon mock can; the graded artifact is the deck. Confirm this is the right call.
6. **`design.json` schema strictness.** Do we provide a starter `design.json` schema students must conform to, or let each team invent their own structure? Recommend providing a starter (lifted from `docs/_branding/design.json`) so the rubric can grade schema fidelity cleanly.

## Out of scope

- **AI policy revisions.** The course-level AI policy in the BUS-313 README is fine as-is; this design tightens the *requirement* (use AI) without changing what's permitted.
- **Midterm / Final exam structure.** Untouched.
- **BUS-122B / BUS-313 parallels.** A similar restructure could land in BUS-122B (Intro Entrepreneurship); separate decision.

## Risks and tradeoffs

- **Stage 1 LLM friction.** Undergrads may struggle to get an LLM to produce valid JSON on the first try. A starter `design.json` template + a 20-minute in-class demo are the mitigation.
- **Team-repo coordination cost.** Four people working in one repo without prior Git experience will hit merge conflicts. The provided team-repo guide and the Stage 0 setup demo are the mitigation.
- **Visual-craft grading subjectivity.** "Brand-fidelity to Stage 1" is harder to grade objectively than ratio math. Mitigation: each rubric line for visual craft requires the grader to cite a specific token in `design.json` that the deck honored or violated.
- **Pres #1 weight increase.** Pres #1 was 2.5% of course (12.5% of project = 2.5% absolute); now it's 25% × 20% = 5% of course. Sales-only teams who phone in unit economics get punished less; the new weighting is fine but worth noting.

## Implementation TODO before Fall 2026

- Author stage docs `stage0-team-repo-setup.md` through `stage5-retro-polish-peer-review.md` in `courses/BUS-313-.../`. Mirror the BUS-629 stage-doc structure.
- Provide a starter `design.json` template at `docs/templates/branding/team-brand-design.json` and a starter `design-system.html` at `docs/templates/branding/team-brand-design-system.html`.
- Update `courses/BUS-313-.../README.md` to replace the current Group Project narrative with the 5-stage structure.
- Update the grade-distribution table in the README — confirm the 20% project weight is unchanged; document the new stage breakdown.
- Create a `_tools/` directory for BUS-313 if needed (commit-author scanner script for the contribution map honesty-check).
- Update `CLAUDE.md` if new course-specific conventions emerge (likely none — this design uses existing conventions).

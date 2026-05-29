---
title: "BUS-313 Team Project — Integrating the Trust Layer (Two-AI Adversarial Review)"
date: 2026-05-28
status: draft
owner: Adam W. Stauffer
course: BUS-313-Economic-And-Financial-Environment-Global-Business
scope: course
applies_to: BUS-313 Group Project, Fall 2026 cohort and forward
amends: 2026-05-28-bus313-team-presentation-project-design.md
sources:
  - video: "Nate B. Jones — 'I Built a Deck With AI, Then Made a Second AI Attack It.' (YouTube, 2026-05) — https://youtu.be/MFzxIT88zfg"
  - post: "Nate's Newsletter — 'AI Office Files: Verify Workflow' (Substack, 2026-05) — https://natesnewsletter.substack.com/p/ai-office-files-verify-workflow"
  - prior: "Nate's Newsletter — '20 Prompts to Kill AI Slop' — https://natesnewsletter.substack.com/p/i-built-a-20-prompt-set-to-kill-ai"
---

# BUS-313 Team Project — Integrating the Trust Layer (Two-AI Adversarial Review)

## Summary

Amend the [BUS-313 5-stage project design](2026-05-28-bus313-team-presentation-project-design.md) (same-date memo) to incorporate the **Trust Layer** framework popularized by Nate B. Jones in his May 2026 video and accompanying Substack post. The Trust Layer adds three disciplines that the current design lacks: (1) every numeric or factual claim on a slide is anchored to a **source-packet** assembled before generation begins; (2) **slide headlines become traceable claims** (testable assertions, not topic labels) with **speaker notes as the evidence layer**; (3) after the first AI drafts the deck, a **second AI session — explicitly prompted as a hostile reviewer — attacks the draft** to surface the claim that would embarrass the team if a stranger forwarded the deck. Integrate the Trust Layer as a new sub-deliverable inside Stage 4 (the high-stakes Unit-Economics deck), with a lighter "brand-fidelity adversarial check" in Stage 3 and a Trust Layer hygiene rubric line. No new stages. Net effect: the project teaches AI *verification* alongside AI *generation* — which is the harder, more durable skill.

## Context — what is the Trust Layer?

Nate B. Jones's framework (his term is "Trust Layer" or "Truth Layer," used interchangeably) is a four-stage workflow for AI-generated Office files (decks, spreadsheets, docs):

1. **Source prep** — assemble a source packet *before* generation. Each numeric claim must have a citable source. Conflicts between sources are caught here, not in the final draft.
2. **Structure** — write the specification (slide outline + claim-to-source map + assumption log) that the AI must follow. No free-form "make a deck about X" prompts.
3. **Creation** — AI drafts the artifact from the spec.
4. **Verification** — a **second AI**, in a fresh session and with a hostile-reviewer prompt, attacks the draft. It looks for unsourced claims, broken formulas, headlines that overpromise, numbers that don't match between slides, and reasoning that a senior reader would catch.

Two specific tactical rules from the framework:

- **Slide headlines are claims, not topics.** "Supplier Analysis" is a topic. "Our Vietnamese supplier is 23% cheaper per unit than the Amazon top-5 median" is a claim. Claims can be fact-checked; topics cannot.
- **Speaker notes are the evidence layer.** Every claim on a slide has a corresponding speaker-note entry citing its source — the URL, screenshot, or calculation that supports it. This survives the forward: if a stranger downloads the `.pptx` and sees a number, the notes tell them where it came from.

Why this matters here: BUS-313's Unit-Economics deck has tariff percentages, supplier prices, competitor sales ranks, expected margins — every one of which is a numeric claim that could be wrong, miscopied, or hallucinated by the LLM. The current Stage 4 design has HIL iteration (human reviews + re-prompts the first AI) but no **independent adversarial check**. Adding the Trust Layer closes that gap.

## Why integrate this now

Three reasons:

1. **The project already has the right shape.** Stage 4 ships an LLM-drafted deck with real numbers. That's the exact artifact the Trust Layer is designed for; we'd be adding a verification pass to a workflow that's already in place, not inventing one.
2. **The verification skill is durable.** First-job marketing analysts, junior consultants, and BD associates will use AI to draft decks for the rest of their careers. The differentiator three years from now will be whether they can also *verify* AI output before it lands in front of a manager. Teaching this discipline now is high-leverage.
3. **It mirrors the BUS-629 verification artifact in spirit.** BUS-629 Stage 5 requires students to manually recompute ≥5 ratios from financials. The Trust Layer is the same idea — verify before you publish — but the verifier is a *second AI* instead of the student's hand calculator, which is closer to how this work actually scales in industry.

## Where it slots into the existing 5-stage design

| Stage | Existing scope | Trust Layer addition |
|------:|----------------|----------------------|
| **0 — Team Repo** | Setup, charter, bios | *(no change)* |
| **1 — Brand & Design System** | `design.json` + `design-system.html` | **Adversarial brand audit (optional, light):** prompt a second AI to spot inconsistencies in the brand tokens (color contrast failures, voice-and-tone mismatch with stated audience). Logged in `prompt-log.md`; ungraded but encouraged. |
| **2 — Product/Market Memo** | Shortlist → pick, hypothesis, tariff | **Source packet:** the memo now carries a `## Source Packet` section listing every numeric claim with its source URL, access date, and screenshot path. Becomes the input for Stages 3 and 4. |
| **3 — Sales Pitch Deck (Pres #1)** | LLM-drafted, brand-styled | **Slide-headlines-as-claims rule + speaker-notes-as-evidence rule.** Lighter adversarial check: a second AI session reviews the deck for **brand fidelity** against `design.json`. Output saved as `analysis/validation/stage3-brand-audit.md`. |
| **4 — Unit-Economics Deck + LLM Spec (Pres #2)** | Spec + LLM-drafted deck + HIL iteration | **The full Trust Layer.** Spec includes the source packet from Stage 2 as an input. After the LLM drafts the deck, a second AI session runs the **hostile-review prompt** (provided template) and produces `analysis/validation/stage4-trust-layer-review.md`. Team must respond to each finding — accept (revise), modify, or defend. |
| **5 — Retro + Polish + Peer Review** | Spec retro, contribution map, polish, 360 | **Trust Layer reflection:** one section in the spec retrospective on what the hostile review caught that the team missed, and what the team would change in the spec to prevent it next time. |

The largest concrete additions are at Stages 2 and 4. Stages 3 and 5 get lighter touches. Stage 1 enhancement is optional.

## New deliverables and where they live

```
team-bus313-{teamname}/
├── docs/
│   └── decisions/
│       └── YYYY-MM-DD-{teamslug}-product-selection.md
│           └── ## Source Packet              # NEW — Stage 2 addition
├── docs/specs/
│   └── YYYY-MM-DD-{teamslug}-unit-econ-deck-spec.md
│       └── ## Part E — Source Packet         # NEW — Stage 4 addition
├── decks/
│   ├── *.pptx                                # Speaker notes carry evidence — NEW rule
│   └── ...
├── analysis/
│   └── validation/
│       ├── YYYY-MM-DD-{teamslug}-stage3-brand-audit.md       # NEW — light Stage 3 review
│       ├── YYYY-MM-DD-{teamslug}-stage4-trust-layer-review.md # NEW — Stage 4 hostile review
│       └── YYYY-MM-DD-{teamslug}-stage5-verification.md       # existing
└── deliverables/
    ├── prompt-log.md
    │   └── (logs the second-AI sessions explicitly tagged as "adversarial")  # NEW convention
    └── YYYY-MM-DD-{teamslug}-spec-retrospective.md
        └── ## Trust Layer Findings           # NEW — Stage 5 reflection section
```

## Hostile-review prompt (provided template)

The biggest risk in adding the Trust Layer is that students will run a half-hearted "please review this deck" prompt and call it done. A team that prompts the second AI with "any feedback?" gets useless feedback. Mitigation: ship a starter hostile-review prompt in the course materials. Students must use it (or document why they modified it).

Draft starter prompt (lives at `docs/templates/prompts/trust-layer-hostile-review.md` after this is adopted):

```
You are a senior reviewer at a consulting firm. A junior team has produced
the attached deck for a $200 product-launch decision. Your job is NOT to be
encouraging — your job is to find the single claim that, if it were wrong,
would most embarrass the team when this deck gets forwarded to a stranger.

Read the deck. Then produce:

1. **Top 3 unsourced claims** — slide #, the claim verbatim, why it's
   unverifiable from the deck alone, and what evidence would close the gap.

2. **Top 3 internally inconsistent numbers** — e.g., a tariff % cited as 25%
   on slide 4 and 27% in the speaker notes on slide 7. Cite the slides and
   the discrepancy.

3. **Top 3 headlines that are topics, not claims** — slide #, current
   headline, and a rewrite that turns it into a testable assertion.

4. **The single weakest argument** — which slide's reasoning would a senior
   reader push back on hardest, and what's the pushback?

5. **Brand-fidelity flags** — at least one place where the deck visually
   or tonally drifts from the team's design.json voice or palette.

For each finding, cite the specific slide. Do not summarize the deck — go
straight to the findings. Be terse.
```

This template makes the second-AI session a separate, gradable artifact. The output is a markdown file the team commits and then responds to — not a chat transcript that evaporates.

## Rubric changes

Two minor rubric edits, both inside Stage 4 (the heaviest stage):

| Stage 4 rubric line | Old weight | New weight | Change |
|----------------------|-----------:|-----------:|--------|
| Deck spec completeness (Part A–D) | 20% | 17% | Part E source packet absorbs 3% |
| LLM workflow + HIL iteration | 20% | 15% | HIL credit splits with the new Trust Layer review |
| **Trust Layer adversarial review (new)** | — | 10% | Hostile-review prompt run, output committed, **each finding responded to in the deck or in a follow-up note** |
| Brand-fidelity to Stage 1 | 10% | 8% | Some weight moves into the Trust Layer brand-flag rubric line |
| Data accuracy | 15% | 15% | unchanged |
| In-class delivery | 15% | 15% | unchanged |
| Visual craft | 10% | 10% | unchanged |
| Member participation | 10% | 10% | unchanged |
| **Total** | **100%** | **100%** | |

Stage 3 picks up a 5% rubric line for **Slide-headlines-as-claims + speaker-notes-as-evidence**, carved evenly from the existing "Required-slide completeness" and "Visual craft" lines (4% from completeness, 1% from craft). This is graded by inspection: every numeric claim on a slide must have a corresponding speaker-note entry citing source.

No change to Stage 0, 1, 2, or 5 weights.

## On the "second AI" — which model, which session?

The framework only requires **independence** — the second AI cannot be the same chat session that drafted the deck (it would defend its own work). Three acceptable patterns:

1. **Different model.** Team uses Claude to draft, ChatGPT to review (or vice versa). Best for cross-checking model-specific biases.
2. **Different session, same model.** Same product, new chat, no prior context. Lower-friction; acceptable for the rubric.
3. **Same model with role injection.** A new session that opens with "You have never seen this deck before. Read it now." — works for some models, but easier to corrupt accidentally. Not recommended for novices.

Recommend option 1 in the student-facing stage doc; allow option 2 with a one-line note in the prompt log explaining why.

## Worked example — what a good Trust Layer review catches

For illustration, here's the kind of finding the hostile-review prompt should produce on a typical BUS-313 Stage 4 deck:

> **Finding (slide 5):** The Profit Margin slide shows "$8.50 per unit" but the
> Cost+Tariff math on slide 4 yields $7.20. The discrepancy isn't explained.
> The team likely updated the supplier cost on slide 4 in a late revision and
> forgot to recompute slide 5. A forwarded deck reader would catch this in
> 30 seconds. **Action: recompute slide 5 from the slide-4 inputs, or add a
> speaker note explaining the difference.**

This is the kind of error the current HIL iteration (re-prompting the *same* AI) routinely misses because the drafting AI has lost track of which number it wrote where. A fresh-session adversarial review catches it because the second AI has no prior commitment to defend.

## Why not just require manual verification (BUS-629 style)?

BUS-629 requires students to recompute ≥5 ratios by hand. Considered for BUS-313 and rejected because:

- BUS-313 is undergrad; the analytical surface area is thinner (one product, ~10 slides, supplier + competitor + tariff math). Manual recomputation of three margin numbers is doable but uninspiring.
- The *transferable skill* in 2026+ is not "compute by hand" but "design a verification workflow you can run repeatedly." Trust Layer teaches the workflow.
- Stage 5 in the existing design still has a smaller manual margin verification table (≥3 margin numbers). The Trust Layer review *augments* that, doesn't replace it.

If a team's Trust Layer review is thin, the Stage 5 manual verification provides a backstop. Both signals matter.

## Risks and tradeoffs

- **Prompt rote.** Students may copy-paste the starter prompt without engaging. Mitigation: rubric requires teams to *respond to each finding* — accept, modify, or defend — which forces engagement with the output regardless of how the prompt was authored.
- **Length creep in Stage 4.** Stage 4 is already the heaviest stage (30%). Adding the Trust Layer review adds roughly 30–60 minutes of team work. Tradeoff is real; the verification skill is worth it. Mitigation: the source packet is mostly *moved* from Stage 2 to Stage 4 via the spec, not net-new work.
- **Model access asymmetry.** Some students have ChatGPT Pro, others don't. The "two different models" recommendation should not become a paywall. Free Claude.ai + free ChatGPT covers both sides; the stage doc must call this out explicitly.
- **Grading subjectivity on "responded to each finding."** Mitigation: rubric language is "the team committed a revision to the deck OR a one-line defense per finding." Either counts. Silence on a finding does not.

## Implementation TODO before Fall 2026

- Add `docs/templates/prompts/trust-layer-hostile-review.md` with the starter prompt above (course-level, reusable across BUS-313, BUS-314, BUS-629).
- Stage 4 doc (`courses/BUS-313/.../stage4-unit-economics-deck.md` once authored) carries the new "Part E — Source Packet" requirement, the hostile-review sub-deliverable, and the revised rubric table.
- Stage 3 doc carries the slide-headlines-as-claims + speaker-notes-as-evidence rules in its rubric.
- Stage 2 doc carries the `## Source Packet` section requirement in the memo template.
- Stage 5 doc carries the "Trust Layer Findings" section in the spec-retrospective template.
- Consider backporting the Trust Layer hostile-review prompt to BUS-629 Stage 5 as an *optional* enhancement to the existing manual verification table — separate decision, not blocking.

## Open questions

1. **Two-model requirement strength.** Should "use a different model" be a hard requirement, or a recommendation with "different session of the same model" as an acceptable fallback? Recommend the fallback be allowed but logged.
2. **Source-packet schema.** Should the source-packet section have a structured table (columns: claim / source URL / access date / screenshot path) or free-form prose? Recommend structured table — easier to grade, models the real-world citation discipline.
3. **Scope of the Stage 3 adversarial check.** Brand-fidelity only, or also slide-claims hygiene? Recommend brand-fidelity only for Stage 3 (keeps Stage 4's heavier review distinct); slide-claims is rubric-graded by inspection, not by AI review.
4. **Should the Trust Layer findings file be required even if the team accepts zero findings?** Yes — "we found nothing worth revising" is itself a valid (and revealing) outcome. Empty findings file → low rubric score; substantive findings + responses → high score.

## Out of scope

- **Wholesale adoption of Nate's 20-prompt kit.** His full prompt library is paywalled (Substack subscription); only the publicly described Trust Layer concepts inform this memo. The course materials cite his work but use original prompts written for the BUS-313 context.
- **Trust Layer in Stage 1.** The brand-token audit is genuinely interesting but adds friction to an already-novel stage. Park as a stretch goal for AY 2027-28.
- **Trust Layer in BUS-314 / FIN-321 / BUS-122B.** Each course has its own deliverable shape; cross-course adoption is a separate decision once BUS-313 has run a cohort.

## Attribution and IP note

The Trust Layer concept is Nate B. Jones's framing, published on his Substack and YouTube in May 2026. This memo applies the *public* framing (four stages, two-model review, headlines-as-claims, notes-as-evidence) to the BUS-313 project context. The starter hostile-review prompt in this memo is original; the framework's name and structure are credited to Jones. Course materials should cite the video and Substack post on first introduction in the Stage 4 doc.

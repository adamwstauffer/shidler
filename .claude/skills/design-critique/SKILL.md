---
name: design-critique
description: Brand-anchored critique of UH Mānoa-branded materials (HTML pages, slide decks, PDFs, branded Markdown) against the design tokens in docs/_branding/design.json and the brand-guidelines skill. Flags off-brand and generic "AI-slop" patterns, scores on UH-anchored dimensions, and emits a prioritized fix list. Advisory only — does not apply fixes. Auto-activates on `/design-critique`.
tools: [Read, Grep, Glob, Bash]
---

# Design Critique Skill (UH Mānoa brand-anchored)

Critique a branded artifact against this repo's brand system and flag the generic patterns that make materials look machine-made rather than institutionally on-brand. **Advisory only** — you report and prioritize; the user applies the fixes.

## Brand anchor (the ground truth)

Read `docs/_branding/design.json` for the full token set; use `docs/_branding/design-system.html` as the visual reference. If creating rather than critiquing, defer to the `brand-guidelines` skill. Load-bearing values (from CLAUDE.md → verify against `design.json`, which wins on conflict):

- **Primary:** UH Green `#024731` — logos, headings, accents.
- **Secondary:** Black `#000000` — body text, borders.
- **Typography:** Open Sans (Bold headings, Regular body); Avenir for print.
- **Accessibility:** ADA-compliant contrast ratios required; **minimum 10pt body text**.

## Input modes (auto-detect from the argument shape)

- **File mode** — a path to an `.html`, `.md`, or an unpacked/described Office artifact. Read it directly; for `.pptx`/`.docx`/`.pdf` use the `pptx`/`docx`/`pdf` skills to extract structure and text.
- **Live mode** — a `http(s)://` or `localhost:` URL. Fetch and inspect the rendered page.

## Scoring — five UH-anchored dimensions (0–5 each)

| Dimension | What earns a high score |
|---|---|
| **Brand fidelity** | Uses `#024731` UH Green and the correct type families where the tokens prescribe; no off-palette accent colors |
| **Contrast & accessibility** | Text/background pairs meet ADA contrast; body text ≥ 10pt; not relying on color alone to convey meaning |
| **Hierarchy & restraint** | Clear heading levels; whitespace used deliberately; not every element competing for attention |
| **Voice & specificity** | Concrete, figure-cited copy (the writing-style convention: lead with a tight executive summary, active voice); not vague filler |
| **Institutional fit** | Reads as a Shidler / UH Mānoa course artifact, not a generic template |

## AI-slop / off-brand flags (call each one that fires, with location)

- **Off-palette accents** — purples, gradients, or neon not in `design.json` (a classic generated-template tell).
- **Emoji-as-hierarchy** — 🚀/✨/🔥 substituting for real heading structure.
- **Center-everything** — every block centered, no left-anchored reading rhythm.
- **Contrast failures** — light-gray body text on white, green text on green.
- **Sub-10pt body text** — violates the accessibility floor.
- **Vague booster copy** — "cutting-edge," "seamless," "unlock your potential" with no specifics.
- **Wrong type families** — a system font stack where Open Sans / Avenir is prescribed.
- **Logo misuse** — UH logo recolored, stretched, or on insufficient-contrast background.

## Output

Emit a report (to chat, or write to a `*-design-critique.md` next to the artifact if the user asks). Order fixes by a simple impact rank: **accessibility/contrast failures first** (they can block ADA compliance), then brand-fidelity breaks, then polish. For each fix: the flag, the `file:line` or element, and the specific correction (cite the token, e.g. "use `#024731` per `design.json § color.primary`").

End with one terminal line:
`Design critique: <highest-impact fix>; <N> slop/off-brand flags; scores B<fidelity>/A<access>/H<hierarchy>/V<voice>/F<fit>.`

## Boundaries

- **Don't apply fixes** — this skill critiques; the user (or a follow-up `brand-guidelines` pass) applies.
- **`design.json` wins** over the CLAUDE.md summary if they ever disagree — flag the disagreement.
- Keep critique proportional to the artifact — a one-page handout doesn't need a full audit.

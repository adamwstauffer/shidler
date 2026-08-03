# Case 3 · Stage 2 — Analysis + Prompt Log

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

**Case weight:** 10% of course grade — this stage: 12 of 20 pts (hypothesis/setup 3 · analysis 6 · prompt log + reflection 3)
**Format:** upload-only
**Deliverable:** `projects/ride-share/analysis.md` (with ≥2 figures) + `projects/ride-share/prompt-log.md` with a ≤300-word reflection
**Due:** end of Week 6 — exact dates on the course calendar

---

## Overview

Stage 1 got the numbers right. This stage makes them mean something. You'll write the analysis in the same `analysis.md` that already carries your pre-committed hypothesis — the hypothesis stays at the top, untouched, and the analysis reckons with it honestly: were you right, and if not, what did the model see that you didn't?

The verdicts are counterintuitive by design — a $50K "profitable" driving job that's an economic loser, a $1M asset built out of a lease payment — and explaining *why* is the entire deliverable. An analysis that restates the workbook's numbers earns little; an analysis that explains the mechanism earns the points.

The Week 6 class session workshops draft analyses live — DLEMBA students get a screencast walkthrough instead; deliverables are identical.

---

## What `analysis.md` must contain

### 1. Hypothesis, revisited (part of the 3 setup pts)

Your 3-sentence hypothesis from Stage 1, followed by a short verdict on it: right, wrong, or right-for-the-wrong-reason. The setup points also cover the Stage 1 folder scaffolding and the hypothesis commit's timestamp — committed before the model work, as specified.

### 2. The four verdicts (graded within the 6 analysis pts)

Explain each worker's economic-profit verdict — not just the sign, the *mechanism*:

- **Why the part-timer is hit hardest.** The car's costs don't scale — full payment and insurance against half the revenue. This is the sharpest single lesson in Sheet 1; treat it accordingly.
- **The net-to-net discipline.** Show you understand why opportunity cost is the alternative's *net* earnings ($52,200, not the $57,600 gross) and why the part-timer forgoes a part-time alternative. If your Stage 1 numbers matched the check figures, you already applied this — now articulate it.
- **The cab driver's asterisk.** He "wins" at the driver level while handing $36,000/yr to the medallion owner — the hook into the rent story.

### 3. The medallion story — told WITH the capitalization math (graded within the 6)

Narrate the collapse using your Sheet 2 numbers, not alongside them. The arc: app entry (≈40K vehicles in 2010 → 120K+ by 2019) competed away fares → the lease fell ($36,000/yr → $18,000/yr) → the perpetuity shrank *and* got riskier (3.5% → 6.0% required return) → rent ÷ required return collapses from $1,028,571 to $300,000, a 70–85% wipeout that tracks observed prices within ~10%. The punchline to land: the cap blocked entry into *yellow cabs* but not into *rides* — rent survives only as long as the moat actually surrounds the market.

### 4. Supply and demand (graded within the 6)

Which curve shifted? **Supply — right, massively** (ridesharing collapsed the entry barrier). State what happened to price and quantity (price ↓, quantity ↑↑), and — the part most drafts skip — *whose* surplus moved where: consumers won, incumbent rent-holders lost. If you note that demand also shifted right (convenience, price transparency), say why the supply shock dominates the observed outcome.

### 5. Cross-case link (graded within the 6)

One paragraph connecting this case to the course arc: the medallion's rent-behind-a-moat is **Monsanto's patent in miniature** — same moat→rent→entry logic, different legal wrapper. Name what the moat was, what rent it protected, and what breached it in each case.

### Figures — at least 2

At least two figures embedded in `analysis.md` (exported charts from your workbook, or figures you build from its numbers). Natural candidates: accounting-vs-economic profit across the four workers; the medallion's capitalized value pre/post entry against observed prices; the 30 → 22 days/mo sensitivity from Stage 1. Figures must carry analytical weight — a screenshot of the raw sheet is not a figure.

---

## `prompt-log.md` + reflection (3 pts)

Log every meaningful AI session from both stages of this case: date, tool, what you asked, what you took from it. Then close with a **≤300-word reflection** that must cover **an AI error you caught** — a wrong number, a confidently botched concept (economic vs. normal profit is a reliable stumble), a hallucinated fact about the NYC market — and how you verified against the model or the case. If you genuinely caught nothing, say what you *checked* and how; "the AI was flawless" without evidence of checking reads as "I didn't look."

**AI-use boundary (course standard):** AI may explain the profit concepts, quiz you, and critique your reasoning — it may **not** fill your yellow cells or write your analysis. The analysis must be your prose; using AI to critique a draft you wrote is fine and belongs in the log.

---

## What to submit

Commit to your portfolio repo — Stage 2 is graded by inspection of `projects/ride-share/`:

- [ ] `analysis.md` — hypothesis at top with your verdict on it; four worker verdicts explained; medallion story with the capitalization math; supply/demand section (curve, price, quantity, surplus); Monsanto cross-case link; ≥2 figures
- [ ] `prompt-log.md` — sessions logged, ≤300-word reflection covering an AI error you caught
- [ ] At least 2 descriptive commits for this stage

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — deepening a verdict explanation, adding the missing surplus discussion, upgrading a figure — can move your score up; the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (12 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Hypothesis & setup | 3 | 3-sentence hypothesis committed before model work (timestamp verified); honest revisit — wrong-but-well-reasoned scores as well as right |
| The four verdicts | 2 | Mechanism, not restatement — part-timer's non-scaling car costs and net-to-net discipline explicitly articulated |
| Medallion story with the math | 2 | Capitalization arithmetic drives the narrative; entry → lease ↓ → riskier perpetuity → 70–85% collapse, tied to observed prices |
| Supply/demand + cross-case link | 2 | Correct curve and direction, price/quantity/surplus all addressed; Monsanto parallel drawn on the moat→rent→entry logic, not just name-dropped |
| Figures | — | ≥2, analytically load-bearing (graded within the rows above — a missing or decorative figure costs the row it should have served) |
| Prompt log + reflection | 3 | Sessions logged with substance; reflection ≤300 words, centered on a concrete AI error caught and how it was verified |

---

## Tips

- **Write to the wrong answer.** The most instructive structure: "You'd think X — the model says Y — here's the mechanism." The case is built on verdicts that flip; use that.
- **Let the sensitivity run argue for you.** The 30 → 22 days/mo flip from Stage 1 *is* the gig-economy fragility point — one input away from every driver verdict going deep negative.
- **Numbers in prose.** "The perpetuity shrank" is weaker than "$36,000 ÷ 3.5% became $18,000 ÷ 6.0%." The capitalization math is one division — show it.
- **The reflection is not a testimonial.** The graded skill is *catching* the AI being wrong, which requires checking it against something — your workbook, the check figures, the case sources.

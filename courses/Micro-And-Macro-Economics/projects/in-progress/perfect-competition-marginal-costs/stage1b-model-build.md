# Mini 1 · Stage 1b — Model Build

**Mini weight:** 10% of course grade — this stage: 8 of 20 pts
**Format:** Upload-only — no presentation component
**Deliverable:** Completed `projects/farm-profit/farm-model.xlsx` committed to your repo
**Due:** end of Week 2 — exact dates on the course calendar (Mini 1 spans Weeks 1–2, Aug 24–Sep 4)

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

---

## Overview

Build the model. Copy `farm-profit-optimizer-template.xlsx` (from the course repo, this folder) into your repo as `projects/farm-profit/farm-model.xlsx`, then complete it: the cost structure, each crop's marginal-cost schedule, the P = MC read per crop, and a documented Solver run that finds the profit-maximizing mix under the real constraints.

This is the supply side of perfect competition made mechanical — the farm is a price taker, every extra bed costs more labor than the last, and the question is where rising MC meets a flat price line. Get the machinery right here; *why* the answer looks the way it does is Stage 1c's job.

All scenario assumptions — prices, wages, bed caps, the labor function — are in the [case README](README.md). Do not invent numbers; the workbook's blue input cells and the README's assumptions table are the same set.

## What to complete in the workbook

The template's README sheet is the authoritative walkthrough (conventions, color key, Solver steps). In outline:

1. **Cost structure** — fixed costs, fertilizer per bed, and the labor function: hours for `q` beds = `q × hrs/wk/bed × 36 × (1 + dim%)^q`. The exponential term is the diminishing-returns engine; if your MC schedules come out flat, this is where you broke it.
2. **MC schedules per crop** — bed-by-bed marginal cost for tomatoes, carrots, and mesclun on the MC Schedules sheet, with the MC-vs-price charts populating.
3. **P = MC per crop** — identify where each crop's standalone MC crosses its price. Expect roughly **tomatoes ~10, carrots ~10, mesclun ~6 beds**. Note what you see in tomato MC around bed 6 — you'll explain it in Stage 1c.
4. **Solver run** — objective: maximize profit; changing cells: the three bed-count decisions; **method: GRG Nonlinear** with **integer** decisions; constraints exactly as listed on the workbook's README sheet (bed caps, 64 total beds, temp workers ≤ 4). All constraint-check cells green.
5. **Document the run** — in the workbook's Solver-notes area: objective, changing cells, each constraint, method, and starting point. A Solver run that isn't documented isn't reproducible, and unreproducible isn't a model.

## Check figures — verify yourself before submitting

The answers are published so you can self-verify; the grade is for the *model that produces them*, not the numbers.

| Check | Value |
|---|---|
| Optimal mix | Tomatoes **10** / Carrots **20** / Mesclun **30** (60 beds) |
| Season profit | **$42,762** |
| Standalone P~MC points | Tomatoes ~10 · Carrots ~10 · Mesclun ~6 beds |

If Solver lands elsewhere, your model has a bug — trace it (a common one: starting from 20/0/0 instead of 0/0/0 and watching GRG path-depend; try both). Matching numbers with broken formulas also won't survive inspection — the rubric reads the workbook, not the answer cell.

**Companion oracle:** the interactive [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) is this same model made touchable. Drag the bed counts, watch MC cross price, sanity-check any intermediate value against it. If your spreadsheet and the lab disagree, believe the lab and find your formula error.

## Commit hygiene

At least **2 descriptive commits** for this stage — e.g., one when the cost structure and MC schedules work, one after the documented Solver run. Not `update xlsx`. If `~$farm-model.xlsx` ever shows up in your Changes panel, your Stage 1a `.gitignore` is broken — fix it before committing.

## AI-use boundary (course standard)

AI may explain concepts, critique your reasoning, and help debug formulas. It may not write your brief, analysis, or reflection. Log the sessions that mattered — the prompt log is graded in Stage 1c, and debugging sessions from this stage are exactly what belongs in it. Having AI hand you completed formulas you can't explain is self-sabotage: the Stage 1c analysis requires you to explain what every piece of this model is doing.

---

## What to submit

Commit the workbook to your repo — Stage 1b is graded by inspection of the file. Nothing separate goes to Lamaku unless announced.

- [ ] `projects/farm-profit/farm-model.xlsx` — copied from the template, completed
- [ ] All constraint-check cells green; no `#REF!` / `#DIV/0!` / `#NAME?` anywhere
- [ ] Solver run documented in-workbook: objective, changing cells, constraints, method, start point
- [ ] MC schedules + charts populated for all three crops
- [ ] ≥2 descriptive commits for this stage

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — fixing a broken labor formula, completing the Solver documentation, cleaning error cells — can move your score up; the full rubric applies, no cap on the bump. No email needed; just revise and push. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Cost structure + labor function correct | 2 | Blue inputs match the case assumptions; diminishing-returns exponent working; blended-wage convention followed |
| MC schedules + P = MC per crop | 2 | Bed-by-bed MC correct for all three crops; standalone crossings identified (~10/~10/~6); charts populated |
| Solver run correct + documented | 3 | GRG Nonlinear, integer decisions, all constraints from the README sheet; finds 10/20/30 at $42,762; objective/cells/constraints/method written down |
| Workbook hygiene + commit hygiene | 1 | Checks green, no error cells, no hardcoded overrides of formulas; ≥2 descriptive commits |

---

## Tips

- **Build the labor function first and test it at q = 1.** One bed of tomatoes should cost `1 × 2.5 × 36 × 1.10` hours. If that's wrong, everything downstream is wrong.
- **Perm hours first, then temp.** The farmer's 720 field hours are consumed before any temp hours — and the P&L allocates labor at the *blended* rate. Mixing those two conventions is the most common structural bug.
- **Don't fight the dip.** If tomato MC falls around bed 6 and then rises again, your model is *right* — MC isn't guaranteed monotonic. Note it, move on, explain it in 1c.
- **Try two Solver starts.** 0/0/0 finds the optimum; 20/0/0 may not. That path-dependence is worth one sentence in your Solver notes.
- **The lab is faster than F9.** For "what happens if I add one more carrot bed?" questions, the [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) answers in a drag; use it to build intuition, then confirm in your own workbook.

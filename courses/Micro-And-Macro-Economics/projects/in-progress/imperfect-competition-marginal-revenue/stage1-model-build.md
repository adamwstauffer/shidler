# Case 2 · Stage 1 — Model Build

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

**Case weight:** 10% of course grade — this stage: 8 of 20 pts
**Format:** upload-only — no presentation component
**Deliverable:** `projects/monsanto/monsanto-model.xlsx` in your portfolio repo, plus a committed hypothesis at the top of `projects/monsanto/analysis.md`
**Due:** end of Week 3 — exact dates on the course calendar

---

## Overview

Case 2 of 3: one company, two market structures. Monsanto sells commodity (non-GMO) corn seed as a price taker at $120/bag — and patented Roundup Ready GMO seed as a price maker facing the whole market's downward-sloping demand. Same crop, same $130M of fixed costs, an ~83× difference in profit. Your job in this stage is to build both models and locate both optima; Stage 2 is where you explain what the numbers mean.

You already have a portfolio repo from Case 1 (Farm Profit Optimizer) — no repo setup this time. This case adds one folder: `projects/monsanto/`.

We kick this off in class in Week 3 — bring a laptop with Excel. **DLEMBA students:** you get a screencast kickoff instead of the live session; deliverables and deadlines are identical.

Full case background, model parameterization, and sources: [README.md](README.md).

---

## Step 0 — Commit your hypothesis BEFORE touching the model

Before you open the workbook, create `projects/monsanto/analysis.md` and put a **3-sentence hypothesis** at the top: *"I expect the GMO price and profit to be X because Y."* Commit it with a message like `Add Monsanto hypothesis before model build`.

This is not busywork — it's the whole point. A hypothesis written *after* you've seen the answer is a summary, not a prediction, and the gap between what you expected and what the model says is the raw material for your Stage 2 analysis. The hypothesis itself is **graded in Stage 2** (3 of its 12 pts), but **the commit timestamp is checked here**: it must predate your first model commit. A hypothesis committed after the model work earns zero for that criterion — no exceptions, because the timestamp is the only thing that makes it a hypothesis.

## Step 1 — Copy the template into your repo

1. Download [`monsanto-seed-market-template.xlsx`](monsanto-seed-market-template.xlsx) from the course repo.
2. Save it into your portfolio repo as `projects/monsanto/monsanto-model.xlsx`.
3. Commit it before you start editing (`Add blank Monsanto model template`) — a clean before/after history is part of commit hygiene.

## Step 2 — Complete the model

Work through the workbook's yellow input cells. Three components are graded:

| Component | What "complete" means |
|---|---|
| **Both optima** | Non-GMO optimum via **P = MC**; GMO optimum via **MR = MC**, with P\* read **off the demand curve** — never off MR. All yellow cells resolve to numbers, no formula errors. |
| **Decision tables** | Both markets' decision tables filled and **tracing to the marker rows** — the row where the optimum lives should be visibly consistent with your yellow-cell answers. |
| **D/MR/MC chart** | The GMO chart showing demand, marginal revenue, and marginal cost — MR falling **twice as steep** as demand, the MR = MC crossing, and P\* up on the demand curve above it. |

**The classic error, named in advance:** reading P\* off the MR curve. MR tells you where to *stop producing* (where it crosses MC); the *price you can charge* at that quantity comes from demand. The workbook builds this in as a checked step — if your P\* is ~$69 instead of ~$297, you've made exactly this mistake.

## Step 3 — Self-verify against the check figures

These are published so you can catch your own errors before submission — matching them earns nothing by itself; the grade is on the workbook that produces them.

| Figure | Non-GMO (perfect competition) | GMO (patent monopoly) |
|---|---|---|
| Q\* | **3,966,667 bags** | **34,025,974 bags** |
| P\* | $120 (given) | **$297.03** — off demand, not MR |
| Profit | **$106.0M** | **$8.785B** |
| Markup P/MC | 1.0× | **4.30×** (Lerner **0.768**) |

If a figure is off: check that variable cost is the *area under* MC (= aQ + bQ²), not MC×Q — the single most common build error, and the exact bug the old course workbook shipped with.

---

## AI-use boundary (course standard)

AI may **explain** MR/MC mechanics, **critique** your reasoning, and **debug** your formulas — it may not write your analysis, and it may not hand you the optima before your hypothesis is committed. Asking an LLM "what's the profit-maximizing GMO quantity?" before Step 0 defeats the stage; asking it "why is my MR column falling twice as fast as my demand column?" after Step 0 is exactly what it's for. Log every meaningful session — the prompt log is graded in Stage 2.

---

## What to submit

Everything is graded by inspection of your repo — nothing to upload beyond your (already-submitted) repo URL.

- [ ] `projects/monsanto/analysis.md` with the 3-sentence hypothesis at top — **committed before any model work**
- [ ] `projects/monsanto/monsanto-model.xlsx` — both optima in the yellow cells, decision tables tracing to the marker rows, D/MR/MC chart
- [ ] No formula errors (`#REF!`, `#DIV/0!`, `#NAME?`) anywhere in the workbook
- [ ] At least **2 descriptive commits** for the model work (e.g., `Solve non-GMO optimum via P = MC`, `Add GMO decision table and D/MR/MC chart`) — not `update` or `fix`

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — fixing a wrong optimum, cleaning formula errors, completing the chart — can move your score up; the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs. The hypothesis timestamp is the exception — it's a point-in-time fact and can't be revised after the fact.

---

## Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Both optima correct | 3 | Yellow cells match the check figures; non-GMO via P = MC, GMO via MR = MC; P\* read off demand |
| Decision tables trace to marker rows | 2 | Tables complete for both markets; optimum row consistent with the yellow-cell answers; variable cost as area under MC |
| D/MR/MC chart | 2 | Demand, MR (twice as steep), and MC plotted; MR = MC crossing and P\* on demand both legible |
| Commit hygiene + hypothesis timestamp | 1 | ≥2 descriptive commits; hypothesis commit predates all model commits |

---

## Tips

- **Predict before you peek.** Your hypothesis will probably be wrong — most are off by an order of magnitude on profit. That's the good outcome: a wrong prediction you can explain is worth more in Stage 2 than a lucky guess.
- **Excel temp files:** your Case 1 `.gitignore` already filters `~$*.xlsx` junk. If `~$monsanto-model.xlsx` appears in your Changes panel, the `.gitignore` is missing — fix it before committing.
- **Don't fight the template.** The marker rows and checked steps exist because they catch the two classic errors (P\* off MR; VC = MC×Q). If your number disagrees with a marker row, the marker row is right.
- **Commit as you go.** One commit per solved market beats one giant commit at the end — and it's what the rubric's hygiene point is looking for.

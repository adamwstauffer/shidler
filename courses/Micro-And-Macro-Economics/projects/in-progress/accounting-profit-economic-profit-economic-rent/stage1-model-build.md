# Case 3 · Stage 1 — Model Build

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

**Case weight:** 10% of course grade — this stage: 8 of 20 pts
**Format:** upload-only
**Deliverable:** `projects/ride-share/rideshare-driver-economics.xlsx` (completed workbook) + a pre-committed hypothesis at the top of `projects/ride-share/analysis.md`
**Due:** end of Week 5 — exact dates on the course calendar

---

## Overview

Four New Yorkers, one question: *who's actually making money?* A full-time Uber driver, a part-time Uber driver, a full-time Yellow Cab driver, and an office worker each get a full P&L — gross fares down to **accounting profit**, then past it to **economic profit** by charging each person what their next-best alternative pays. Then Part 2 finds where the money went: capitalized inside the **taxi medallion**, whose observed price the model reproduces within ~10% — at its $1M+ peak *and* after Uber destroyed it.

This stage is the build. You'll complete the provided workbook, verify it against published check figures, and commit it to your portfolio repo. The interpretation — why the verdicts flip, what the medallion collapse teaches — is Stage 2.

You already have a portfolio repo from Cases 1 and 2. This case adds one folder to it: `projects/ride-share/`. Everything for Case 3 lives there.

Case 3 kicks off in class during Week 5 — DLEMBA students get a screencast kickoff instead; deliverables are identical.

---

## Step 0 — Commit your hypothesis BEFORE you build

Before touching the workbook, create `projects/ride-share/analysis.md` and write a **3-sentence hypothesis** at the top:

> "I expect X to have the highest economic profit because Y."

Name your pick, give your reasoning, and commit it. The hypothesis is graded in Stage 2 — but **the commit timestamp is checked**. A hypothesis committed after the model work is worthless as a hypothesis; the whole point is to put a prediction on record before the numbers can bias it. Being wrong costs nothing. Backdating your reasoning does.

---

## Step 1 — Set up the folder and copy the template

1. In your portfolio repo, create `projects/ride-share/`.
2. Copy `rideshare-driver-economics-template.xlsx` (provided in the course materials) into that folder and rename it **`rideshare-driver-economics.xlsx`**.
3. Commit — e.g., `Add ride-share project folder with blank template`.

---

## Step 2 — Sheet 1: Driver Economics

Complete the yellow cells so that **accounting profit**, **economic profit**, and **normal profit** rows compute for all four workers (Uber FT, Uber PT, Yellow Cab FT, Traditional job). The gross-revenue and explicit-cost inputs are given; your job is the profit logic.

Two disciplines the template is designed to enforce — get these wrong and your economic-profit row will not match the check figures:

- **Net to net.** The opportunity cost of driving is the alternative's earnings *after its own costs* (the office worker's $52,200 net, not the $57,600 gross salary). Apples to apples.
- **Match scale.** The part-timer forgoes a *part-time* alternative ($26,100 — half the traditional job's net), not a full-time one.

## Step 3 — Sheet 2: Medallion & Rent

The medallion is a rent-capturing asset in fixed supply, so it's worth the capitalized rent stream: **annual lease ÷ required return**. Complete the yellow cells for both eras — pre-entry (≈2013: $36,000/yr at 3.5%) and post-entry (≈2019: $18,000/yr at 6.0%). One division per era; the payoff is that both land within ~10% of observed market prices.

## Step 4 — One documented sensitivity run

Change days/month from **30 → 22** on Sheet 1, record what happens to each worker's economic profit (a short note in the workbook or in `analysis.md` — either is fine, but it must be written down, not just "I looked"), then set the input back to 30 before your final commit. What flips, and how hard, is Stage 2 material — capture the numbers now.

---

## Check figures — verify before you submit

Your workbook should reproduce these exactly (30 days/month):

| | Uber FT | Uber PT | Yellow Cab FT | Traditional job |
|---|---|---|---|---|
| **Accounting profit** | $50,520 | $22,860 | $59,580 | $52,200 |
| **Economic profit** | −$1,680 | −$3,240 | +$7,380 | +$1,680 |

| Medallion | Capitalized value | Observed price |
|---|---|---|
| Pre-entry (≈2013) | **$1,028,571** | >$1M peak (2013–14) |
| Post-entry (≈2019) | **$300,000** | ≈$335K (June 2019) |

If a number is off, the culprit is almost always one of the two disciplines in Step 2 — gross-vs-net or full-time-vs-part-time scale. Fix the logic, don't hard-code the answer.

---

## AI-use boundary (course standard)

AI may explain the profit concepts, quiz you, and critique your reasoning — it may **not** fill your yellow cells or write your analysis. Asking "walk me through why opportunity cost uses net earnings" is exactly right; pasting the sheet and asking for the formulas is not. Log every session — the prompt log is graded in Stage 2.

---

## What to submit

Commit to your portfolio repo — Stage 1 is graded by inspection of `projects/ride-share/`:

- [ ] `projects/ride-share/analysis.md` with the 3-sentence hypothesis at top — **committed before the workbook build** (timestamp checked)
- [ ] `projects/ride-share/rideshare-driver-economics.xlsx` — all yellow cells complete on both sheets, matching the check figures
- [ ] Sensitivity run (30 → 22 days/mo) documented, input restored to 30
- [ ] At least 2 descriptive commits (not `update` or `fix` — e.g., `Build economic profit rows for all four workers`)

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — fixing a profit row, completing the medallion sheet, documenting the sensitivity run — can move your score up; the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Sheet 1 — profit rows for all four workers | 4 | Accounting, economic, and normal profit all match check figures; net-to-net and scale-matched opportunity costs built into the logic, not hard-coded |
| Sheet 2 — medallion capitalization | 2 | Both eras computed as rent ÷ required return; values match $1,028,571 / $300,000 |
| Sensitivity run documented | 1 | 30 → 22 days/mo run recorded with the resulting economic-profit changes; input restored |
| Commit hygiene | 1 | ≥2 descriptive commits; hypothesis commit precedes model commits |

---

## Tips

- **Verify against the check figures, then trust yourself.** They're published precisely so you can self-grade the build — a workbook that matches to the dollar is done.
- **Formulas, not typed answers.** The sensitivity run only works if days/month is a live input flowing through the sheet. A hard-coded $50,520 dies the moment you change anything.
- **Commit as you go.** One commit per sheet is a natural rhythm and satisfies commit hygiene for free.
- **Don't interpret yet.** If the part-timer's number surprises you, write the observation down for Stage 2 — this stage is about getting the numbers right *before* telling stories about them.

# Stage 4 – Market Data + Population (12% of project)

## Goal

Replace your placeholder inputs with **live market data**, document exactly where every number
came from, and confirm the model survives contact with reality. This is the stage where your
workbook stops being a classroom exercise and becomes a dated, sourced, defensible analysis —
and where a structurally weak model reveals itself.

Because everyone retrieves data on their own date, **every student's numbers are unique**. Your
results will not match anyone else's, and they aren't supposed to.

---

## Retrieve (as of market close on the day you begin this stage)

| Input | Source guidance |
| ----- | --------------- |
| `S0_in` — EURUSD spot | Any reputable quote source (e.g., Yahoo Finance, Bloomberg, ECB reference rate). Record source + timestamp. |
| `R_USD`, `R_FC` — 1-year interest rates | A 1-year government yield or deposit/reference rate per currency. **Document which rate you chose and why** — the choice matters more than the decimals. |
| `F0_in` — 1-year forward | Use a live forward quote if you can find one; otherwise **compute the CIP-implied forward** from your spot and rates — `F0 = S0 × (1 + R_USD×T/360) / (1 + R_FC×T/360)` — and say so. Compare to your scenario's indicative forward and comment on the gap. |
| `K_PUT`, `K_CALL` — strikes | Set at or near your live spot, per the scenario convention. |
| `PREM_PUT`, `PREM_CALL` — premiums | Keep the scenario-given premiums (retail-accessible option quotes are unreliable); note this explicitly as an assumption. |
| `FC_AMT`, `T_DAYS` | From your scenario. |

### Where to actually get these numbers

Any reputable source is acceptable — what's graded (50% of this stage) is that every number carries
**source + timestamp + any proxy logic**, not which website you used. A short guide:

- **Professional terminals — the gold standard.** Bloomberg or Refinitiv (Eikon / Workspace), if you
  have access: the Shidler lab terminals, or a future employer's desk. Record the terminal *and* the
  timestamp. These carry the live forwards and option quotes that free sources often don't.
- **Free and sufficient for this project:**
  - *Yahoo Finance* — EURUSD spot, some forwards.
  - *investing.com* — spot, forwards, and rate instruments.
  - *ECB reference rates* — the daily EURUSD reference fix.
  - *FRED* (St. Louis Fed) — USD deposit / SOFR-family rates for `R_USD`.

Whichever you use, pick the rate instrument deliberately and say why — the choice matters more than
the decimals.

## Then

1. **Write the market-data memo** — `data/YYYY-MM-DD-{lastname}-market-data.md`: a table of
   every input with value, source, retrieval timestamp, and any proxy/computation used
   (CIP-implied forward, rate choice). This is a provenance document — an auditor should be
   able to re-pull every number.
2. **Populate the workbook** — enter the live values into the named-range input cells. Nothing
   else should need to change. If a formula breaks or an output stops making sense, the
   structure was wrong: fix it and record what you fixed (this is not a penalty — finding it
   *is* the exercise).
3. **Re-run the checks** — parity check passes with live data; sensitivity table and chart
   recalculate around the new spot.
4. **Cross-check against the FX Hedging Lab** on the course website: enter your live inputs into
   the lab and compare its forward / money-market / option outputs to your workbook. If they
   disagree, one of them is wrong — find out which before submitting, and record the resolution
   in the memo.

## Deliverables

- Market-data memo: `data/YYYY-MM-DD-{lastname}-market-data.md`
- Re-committed workbook (same file, new commit — commit message notes the population + any
  structural fixes)
- Updated `prompt-log.md` if AI assisted the data hunt.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Data quality & provenance | Every input sourced, timestamped, proxies documented; sensible rate choices | 50% |
| Model resolves cleanly | Live data loads through named ranges; checks pass; fixes (if any) documented honestly | 33% |
| Lab cross-check | Comparison performed and documented; discrepancies resolved | 17% |

---

## When feedback comes as a pull request

From this stage on, instructor feedback often arrives as a **pull request** pushed to your repo — a
proposed change shown as a line-by-line diff with comments attached to specific lines. This is how
real code and analyst review works: the reviewer shows you the edit, not just a list of notes. You
are not obligated to merge blindly. Your options:

1. **Read the diff** — the PR *is* the feedback; every changed line is a comment on your work.
2. **Merge it** as-is if you agree.
3. **Edit further** — merge and keep working on top, or commit your own version of the change instead.
4. **Point an LLM at it** — hand the PR URL (or `git diff`) to Claude/ChatGPT to apply, explain, or
   extend the revisions.
5. **Push back** — reply on the PR with why your original is right. Disagreeing *with reasons* is a
   professional skill and explicitly welcome.

---

## How this leads to Stage 5

You now have a spec (Stage 2), a validated workbook running on real data (Stages 3–4), and a
provenance memo. Stage 5 hands the **spec and market-data memo — nothing else** — to a fresh
LLM and grades what comes back against your workbook. Your documents are about to be executed
verbatim.

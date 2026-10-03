# BUS 620 Case 1: Perfect Competition — Decision Analysis

*Scenario: a 1.5-acre market garden. Retitled 2026-08-02 concept-first (was "The Farm Profit Optimizer") — the scenario identity now lives inside the case, not in its name.*

> **Status:** released 2026-08-03. Formalizes `BUS 620 Case Study_ Perfect Competition & Marginal Costs.docx`; that original and `Supply_Mariganl Cost_Optimize Profit v5.xlsx` are preserved unchanged, held privately with the instructor key, outside this repo.
>
> **No student template.** Stage 2 is spec-driven: the student writes the specification, an AI builds the workbook from it, and the student audits the result. The former student template was retired to the subject's gitignored `ignore/retired/` on 2026-08-03 — a provided workbook and "your spec is the template" cannot both be true. The [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) is the independent reference implementation students cross-check against.

## The pitch

A 1.5-acre market garden — 64 beds, one farmer, up to four temporary workers — must decide how many beds of **tomatoes, carrots, and mesclun** to plant. Prices are given (the farm is a price taker at the farmers' market), but every additional bed of a crop takes *more* labor than the last (diminishing returns), so marginal cost rises. Students build the cost structure, derive each crop's marginal-cost schedule, find where **P = MC**, then use Excel Solver to pick the profit-maximizing mix under real constraints. Perfect competition, taught from the supply side — with a spreadsheet a real farmer could use.

## Learning goals

1. **P = MC** is the price-taker's supply rule — find it in a table, on a chart, and in Solver's answer.
2. **MC vs AVC vs ATC** — and the short-run shutdown logic: carrots and mesclun *alone* never cover fixed costs, yet growing them is still optimal. Why?
3. **Diminishing returns** are why MC slopes up — here modeled as labor per bed growing with each bed planted.
4. **Input prices bend the MC curve** — tomato MC *dips* at ~6 beds when the farmer's own field hours (an expensive $34.72/hr) run out and cheaper temp labor ($17.36/hr) takes over. MC is not guaranteed monotonic; students should be able to explain the dip, not just observe it.
5. **Constrained optimization** — when a bed cap binds, MC < P at the cap and the constraint (not economics) stops production.
6. **Accounting vs economic cost** — the farmer's salary is paid regardless; charging her field hours to crops is an *opportunity-cost* choice. (Bridges to the Accounting vs Economic Profit case in this same unit.)

## The scenario — all assumptions in one place

*(v5 scattered these across the sheet and hardcoded the wages inside formulas; the docx never stated them at all.)*

| Assumption | Value |
|---|---|
| Season | 36 weeks |
| Fixed costs | $20,000 / season |
| Beds | 64 total (16 beds/plot × 4 plots on 1.5 acres) |
| Permanent labor | The farmer: $50,000/season salary, 40 hr/wk, **50% of time in the field** → 720 field hrs/season at an implied $34.72/hr |
| Temporary labor | Up to 4 workers (fractional OK): $25,000/season each, 100% field → 1,440 hrs each at $17.36/hr |

| Crop | Max beds | Price $/bed | Labor hrs/wk/bed | Fertilizer $/bed | Diminishing returns %/bed |
|---|---|---|---|---|---|
| Tomatoes | 20 | 8,800 | 2.50 | 880 | 10.00% |
| Carrots | 20 | 2,094 | 0.833 (= tomato ÷ 3) | 440 | 2.50% |
| Mesclun | 30 | 2,700 | 1.25 (= tomato ÷ 2) | 880 | 1.25% |

**Labor function (the heart of the model):** hours for `q` beds of a crop = `q × hrs/wk/bed × 36 weeks × (1 + dim%)^q`. The exponential term is the diminishing-returns engine — each extra bed makes *every* bed a little more labor-hungry (pest pressure, harvest bottlenecks, walking time).

**Costing conventions:** the farmer's 720 field hours are used first and charged at her implied wage; temporary hours cover the remainder. In the farm P&L, labor cost is allocated to crops at the blended farm-wide rate (total labor $ ÷ total hours) — the perm/temp split is a farm-level fact, not a per-crop one.

## Deliverables (AI + GitHub workflow — the portfolio-repo standard)

Every artifact lands in the student's **personal public portfolio repo**, structured by capability and
engagement rather than by course.
Capability slug for this case: **`marginal-analysis`**. Engagement slug: **`perfect-competition`**.

| # | Artifact (path in the student repo) | What it must contain | Pts |
|---|---|---|---|
| 0 | The portfolio repository itself — skeleton, four root files, `.gitignore`, instructor invited | The workspace every engagement lands in, built to the portfolio-repo standard and named for the student rather than the course | 2 |
| 1 | `docs/briefs/YYYY-MM-DD-perfect-competition-brief.md` | The farm problem in your own words + a hypothesis: "I expect the optimal mix to be X because Y" — *before* touching Solver | 1 |
| 2 | `capabilities/marginal-analysis/spec.md` + `model.xlsx` + `README.md` | **Spec first**, before the workbook exists: named inputs with units and sources, calculation logic in named-range notation, and the published check figures written in as acceptance criteria. Then an AI builds from the spec, and the student audits the result — findings recorded in the spec | 8 |
| 3 | `analysis/YYYY-MM-DD-perfect-competition-analysis.md` + `analysis/figures/` | The optimal mix and *why*: P=MC evidence per crop, which constraints bind, the tomato MC dip explained, the carrot/mesclun "grow at a loss?" resolution (MC vs AVC, contribution over variable cost) | 6 |
| 3b | `docs/decisions/YYYY-MM-DD-perfect-competition-memo.md` | The recommendation to the farmer: the plan, which cap to relax first and what it's worth, what would change the answer. No separate points — read with the analysis | — |
| 4 | `prompt-log.md` (repo root) + reflection | Meaningful AI sessions logged; ≤300-word reflection on where AI helped, where it was wrong, and how you verified | 3 |

Split across stages: [stage0](stage0-portfolio-repo.md) (the repository, 2) ·
[stage1](stage1-engagement-brief.md) (the brief, 1) · [stage2](stage2-model-build.md) (spec, build,
audit, 8) · [stage3](stage3-analysis.md) (analysis + memo + log, 9). **Case total 20, unchanged.**

> **Stage 0 split (2026-08-03).** The former `stage1-repo-and-brief.md` carried three separately
> priced criteria: two about the repository and one about the brief. They are now two stages along
> the seam that was already there — **every criterion keeps its exact point value, and no criterion
> text was rewritten**. This is a regroup, not a repricing. Standing up the workspace and forming a
> falsifiable hypothesis are different kinds of work with different AI boundaries, and a graded gate
> between them is what makes the repository finished *before* the brief is written rather than
> alongside it. The commit-order rule — brief before any modeling — stays on Stage 1, where the
> thing it orders lives. Cases 2 and 3 keep two stages; only Case 1 stands up the repository.

Student-facing web pages for this case: [`case-perfect-competition.html`](https://adamwstauffer.github.io/ai-lms/case-perfect-competition.html) and its three stage pages. **Sync rule:** these paths, the stage pages, and the Kumu site's gate checks share one path table — change one, change all three.

**AI-use boundary (course standard, unchanged):** AI may explain concepts, critique your reasoning, and help debug formulas. It may not write your brief, analysis, memo, or reflection. Log the sessions that mattered. The workbook was never on the prohibited list, which is why Stage 2's AI-built workbook is a sequencing change rather than a boundary change.

## Expected results

Expected results are discussed in class after Stage 3 is handed in.

## Bugs fixed vs `…Optimize Profit v5.xlsx`

1. **Mesclun MIX row pulled carrot labor** (`G20` referenced `labor_carrots`) — copy-paste bug; mesclun labor costs were wrong whenever carrots ≠ mesclun.
2. **Per-crop decision tables were coupled to the MIX** via `q_beds` (`D24/q_beds*…`) — the "standalone" MC schedules changed when the mix cells changed, and divided by zero at an empty mix.
3. **Temp-labor cap compared hours to 1,440** (`MIN(labor_hrs_season, …)`) instead of capping at 4 workers — the 0–4 constraint was never enforced; now `temp_needed ≤ temp_max` is an explicit checked constraint (and Solver constraint).
4. **Wages hardcoded** as `=50000/…` and `=25000/…` inside formulas — now separate tan salary input cells.
5. **Named-range typos** (`fert_carrotrs`, `labour_hrs` vs `labor_hrs`, "Tomotoes", "Mesculun") — cleaned; consistent `price_* / laborwk_* / fert_* / dim_* / q_*` scheme.
6. **Missing docs** — the docx's "Assumptions & Constraints" heading was empty and wages appeared nowhere; the workbook had a blank Notes sheet. Both replaced (this README; in-workbook README sheet with Solver steps, conventions, color key).
7. **Added:** AVC column (shutdown analysis), feasibility flags, check figures (instructor key, held privately), MC-vs-price charts rebuilt from decoupled tables.

## Real-world crossover

This model is a teaching-sized version of a genuine farm decision: bed-level crop mix under labor constraints.

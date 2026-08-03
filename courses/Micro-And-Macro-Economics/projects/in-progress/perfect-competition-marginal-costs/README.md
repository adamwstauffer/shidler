# BUS 620 Case 1: Perfect Competition — Decision Analysis

*Scenario: a 1.5-acre market garden. Retitled 2026-08-02 concept-first (was "The Farm Profit Optimizer") — the scenario identity now lives inside the case, not in its name.*

> **Status:** released 2026-08-03. Formalizes `BUS 620 Case Study_ Perfect Competition & Marginal Costs.docx`; that original and `Supply_Mariganl Cost_Optimize Profit v5.xlsx` are preserved unchanged. `farm-profit-optimizer-key.xlsx` is the instructor key.
>
> **No student template.** Stage 2 is spec-driven: the student writes the specification, an AI builds the workbook from it, and the student audits the result. The former student template was retired to the subject's gitignored `ignore/retired/` on 2026-08-03 — a provided workbook and "your spec is the template" cannot both be true. The [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) is the independent reference implementation students cross-check against. Decision: `ai-lms/docs/decisions/2026-08-03-spec-driven-artifact-builds.md`.

## The pitch

A 1.5-acre market garden — 64 beds, one farmer, up to four temporary workers — must decide how many beds of **tomatoes, carrots, and mesclun** to plant. Prices are given (the farm is a price taker at the farmers' market), but every additional bed of a crop takes *more* labor than the last (diminishing returns), so marginal cost rises. Students build the cost structure, derive each crop's marginal-cost schedule, find where **P = MC**, then use Excel Solver to pick the profit-maximizing mix under real constraints. Perfect competition, taught from the supply side — with a spreadsheet a real farmer could use.

## Learning goals

1. **P = MC** is the price-taker's supply rule — find it in a table, on a chart, and in Solver's answer.
2. **MC vs AVC vs ATC** — and the short-run shutdown logic: carrots and mesclun *alone* never cover fixed costs, yet growing them is still optimal. Why?
3. **Diminishing returns** are why MC slopes up — here modeled as labor per bed growing with each bed planted.
4. **Input prices bend the MC curve** — tomato MC *dips* at ~6 beds when the farmer's own field hours (an expensive $34.72/hr) run out and cheaper temp labor ($17.36/hr) takes over. MC is not guaranteed monotonic; students should be able to explain the dip, not just observe it.
5. **Constrained optimization** — when a bed cap binds, MC < P at the cap and the constraint (not economics) stops production. Shadow-price intuition: one more carrot bed would be worth ~$352.
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
engagement rather than by course — see `ai-lms/docs/decisions/2026-08-02-website-simplification-and-portfolio-repo-standard.md` § 6.
Capability slug for this case: **`marginal-analysis`**. Engagement slug: **`perfect-competition`**.

| # | Artifact (path in the student repo) | What it must contain | Pts |
|---|---|---|---|
| 1 | `docs/briefs/perfect-competition-brief.md` | The farm problem in your own words + a hypothesis: "I expect the optimal mix to be X because Y" — *before* touching Solver | 3 |
| 2 | `skills/marginal-analysis/spec.md` + `model.xlsx` + `README.md` | **Spec first**, before the workbook exists: named inputs with units and sources, calculation logic in named-range notation, and the published check figures written in as acceptance criteria. Then an AI builds from the spec, and the student audits the result — findings recorded in the spec | 8 |
| 3 | `analysis/perfect-competition-analysis.md` + `analysis/figures/` | The optimal mix and *why*: P=MC evidence per crop, which constraints bind, the tomato MC dip explained, the carrot/mesclun "grow at a loss?" resolution (MC vs AVC, contribution over variable cost) | 6 |
| 3b | `docs/decisions/perfect-competition-memo.md` | The recommendation to the farmer: the plan, which cap to relax first and what it's worth, what would change the answer. No separate points — read with the analysis | — |
| 4 | `prompt-log.md` (repo root) + reflection | Meaningful AI sessions logged; ≤300-word reflection on where AI helped, where it was wrong, and how you verified | 3 |

Split across stages: [stage1](stage1-repo-and-brief.md) (repo + brief, 3) · [stage2](stage2-model-build.md) (spec, build, audit, 8) · [stage3](stage3-analysis.md) (analysis + memo + log, 9).

Student-facing web pages for this case: [`case-perfect-competition.html`](https://adamwstauffer.github.io/ai-lms/case-perfect-competition.html) and its three stage pages. **Sync rule:** these paths, the stage pages, and `ai-lms/website/assets/js/gates.js` share one path table — change one, change all three.

**AI-use boundary (course standard, unchanged):** AI may explain concepts, critique your reasoning, and help debug formulas. It may not write your brief, analysis, memo, or reflection. Log the sessions that mattered. The workbook was never on the prohibited list, which is why Stage 2's AI-built workbook is a sequencing change rather than a boundary change.

## Instructor notes & check figures

- **Optimum:** Tomatoes 10 / Carrots 20 / Mesclun 30 → 60 beds, **profit $42,762**. Labor 5,277 hrs = 720 perm + 4,557 temp (3.16 temp workers). Revenue $210,880, fertilizer $44,000, labor $104,118, fixed $20,000. (Brute-force verified over all integer mixes; Excel recalculation matches to the dollar.)
- **Binding constraints:** carrot and mesclun bed caps (marginal profit at cap: carrot +$352/bed, mesclun +$246/bed — good shadow-price discussion). Tomatoes interior at P≈MC (MC $8,249 at bed 10 vs price $8,800; bed 11 would cost $9,391). Beds ≤ 64 and temps ≤ 4 are both slack.
- **Standalone P~MC points** (MC Schedules sheet): tomatoes ~10 beds, carrots ~10, mesclun ~6. All three crops standalone lose money at every q (fixed costs $20k dominate) — the shutdown discussion writes itself: P > AVC everywhere, so operate; the *mix* is what turns a loss into $42,762.
- **The MC dip** (tomatoes, q≈6): MC falls from $7,661 to $4,906 when perm hours exhaust and marginal labor switches to the cheaper temp wage, then diminishing returns push it back up through the price line. Expect confusion; it is the best five minutes of the debrief.
- **Solver:** GRG Nonlinear, integer decisions, constraints as listed on the workbook README sheet. Nonconvexity is mild; from a 0/0/0 start GRG finds the optimum, but have students try 20/0/0 as a start to see path-dependence.

## Bugs fixed vs `…Optimize Profit v5.xlsx` (for Adam)

1. **Mesclun MIX row pulled carrot labor** (`G20` referenced `labor_carrots`) — copy-paste bug; mesclun labor costs were wrong whenever carrots ≠ mesclun.
2. **Per-crop decision tables were coupled to the MIX** via `q_beds` (`D24/q_beds*…`) — the "standalone" MC schedules changed when the mix cells changed, and divided by zero at an empty mix.
3. **Temp-labor cap compared hours to 1,440** (`MIN(labor_hrs_season, …)`) instead of capping at 4 workers — the 0–4 constraint was never enforced; now `temp_needed ≤ temp_max` is an explicit checked constraint (and Solver constraint).
4. **Wages hardcoded** as `=50000/…` and `=25000/…` inside formulas — now blue salary input cells.
5. **Named-range typos** (`fert_carrotrs`, `labour_hrs` vs `labor_hrs`, "Tomotoes", "Mesculun") — cleaned; consistent `price_* / laborwk_* / fert_* / dim_* / q_*` scheme.
6. **Missing docs** — the docx's "Assumptions & Constraints" heading was empty and wages appeared nowhere; the workbook had a blank Notes sheet. Both replaced (this README; in-workbook README sheet with Solver steps, conventions, color key).
7. **Added:** AVC column (shutdown analysis), feasibility flags, instructor key with check figures, MC-vs-price charts rebuilt from decoupled tables.

## Real-world crossover

This model is a teaching-sized version of a genuine farm decision: bed-level crop mix under labor constraints. The same engine (crop economics + labor function + constraint solver) is a candidate feature for the farm-management app (`C:\GitHub\farm-management-assistant-v2`) — see the crossover note in the ai-lms strategy repo.

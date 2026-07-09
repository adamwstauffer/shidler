# BUS 620 Project: Imperfect Competition & Marginal Revenue — Monsanto and the GMO Seed Market

> **Status:** Kumu-improved draft (2026-07-07) formalizing `BUS 620 Case Study_ Imperfect Competition & Marginal Revenue.docx`. Adam should review before students see it. Originals (`…v9.xlsx`, in-class worksheet) preserved unchanged; the rebuilt workbooks are `monsanto-seed-market-template.xlsx` (student) and `monsanto-seed-market-key.xlsx` (instructor). All narrative claims below were externally validated 2026-07-07; sources at bottom.

## The pitch

One company, two market structures. Selling **commodity (non-GMO) corn seed**, Monsanto is a price taker at $120/bag — produce until **P = MC**, earn a modest profit that entry will erode. Selling **patented Roundup Ready GMO seed**, Monsanto faces the whole market's downward-sloping demand — one more bag sold lowers the price on *every* bag, marginal revenue falls twice as fast as demand, and the rule becomes **MR = MC**. Same crop, same $130M of fixed costs — and an ~83× difference in profit. Students build both models, locate both optima, and put a dollar figure on what monopoly costs society.

## Learning goals

1. **MR < P for a price maker** — and exactly why (the twice-as-steep rule for linear demand).
2. **MR = MC vs P = MC** — the optimum rule is the same logic ("expand while the next unit adds more than it costs"), the *revenue side* is what changes.
3. **Read P\* off demand, never off MR** — the single most common student error, built into the worksheet as a checked step.
4. **Variable cost is the area under MC**, not MC×Q — the old v9 workbook made exactly this error (see bug list).
5. **Markup and the Lerner index** as measures of market power (here: 4.3× and 0.77).
6. **Deadweight loss of monopoly** — the ~$3.0B/yr of surplus that simply vanishes, and why patents accept that loss on purpose (innovation incentive: the case's discussion spine).

## The model (self-consistent parameterization)

Both markets share: **fixed costs $130M**, cost structure **TVC = a·Q + b·Q² → MC = a + 2b·Q** with a = $1/bag.

| | Non-GMO (perfect competition) | GMO (patent monopoly) |
|---|---|---|
| Demand | flat at **P = $120** | **P = 525 − 0.0000067·Q** |
| MC curvature b | 0.000015 | 0.000001 (GMO scales 15× better) |
| Rule | P = MC | MR = MC, with MR = 525 − 0.0000134·Q |
| **Q\*** | **3,966,667 bags** | **34,025,974 bags** |
| **P\*** | $120 (given) | **$297.03** (off the demand curve) |
| Revenue | $476.0M | $10.107B |
| Total cost | $370.0M | $1.322B |
| **Profit** | **$106.0M** | **$8.785B** (~83×) |
| Markup P/MC | 1.0× | 4.30× (Lerner 0.768) |

**Competitive benchmark for GMO** (if the patent vanished and price fell to MC): Q ≈ 60.23M bags at **P ≈ $121.46 — almost exactly the non-GMO price**. Monopoly withholds ~26M bags to hold price at $297; the lost trades are a **deadweight loss ≈ $2.99B/yr**. That near-coincidence ($121 ≈ $120) is the case's best "aha": strip the patent and GMO seed is just… seed.

> **Note on the docx's stated curves.** The draft quotes MC = 0.000029·Q (non-GMO) and 0.00000196·Q (GMO). Those numbers were `SLOPE()` regressions over the old workbook's own tables — artifacts, not parameters. The rebuild defines TVC directly so every number is exact. Real-world calibration survives: Q\* ≈ 34.0M GMO bags vs the ~34.4M implied by 86M GMO acres ÷ 2.5 acres/bag.

## Deliverables (4-artifact AI + GitHub workflow, same as the other BUS 620 cases)

| # | Artifact | Contents | Pts |
|---|---|---|---|
| 1 | `brief.md` | The two-market setup in your own words + hypothesis: "I expect the GMO price and profit to be X because Y" — before touching the model | 3 |
| 2 | `monsanto-model.xlsx` | Completed template: both optima (yellow cells), decision tables tracing to the marker rows, D/MR/MC chart | 8 |
| 3 | `analysis.md` + ≥2 figures | Perfect vs imperfect compared: why MR < P, why P\* comes off demand, markup/Lerner, the DWL number and what it means, and one paragraph on whether the patent's innovation incentive justifies the $3B/yr | 6 |
| 4 | `prompt-log.md` + reflection | AI sessions logged; reflection covers an AI error you caught | 3 |

**AI-use boundary (course standard):** AI may explain MR/MC mechanics, critique reasoning, and debug formulas — not write your brief or analysis, and not hand you the optima before you've hypothesized.

## Discussion spine (from the draft, kept)

- How did Roundup + Roundup Ready seeds change Monsanto's business environment and competitive landscape? (Complement lock-in: the herbicide sells the seed and vice versa.)
- Patent enforcement (no replanting harvested seed) as the mechanism that *keeps* demand downward-sloping — without it, farmers' saved seed is competing supply.
- Superweeds (glyphosate-resistant weeds from over-reliance) as a negative externality the private optimum ignores.
- Bayer 2018: does merging the #1 seed company into a top agrochemical firm restore competition concerns the patent already raised? (DOJ answer: largest antitrust divestiture in U.S. history as the price of approval.)

## Instructor notes & check figures

- **Non-GMO:** Q\* = (120−1)/0.00003 = 3,966,667; profit $106.0M. Discussion: this is *short-run* — the docx's "long-run profits" question answers itself: free entry competes it toward zero, which is exactly why Monsanto needed the patent moat.
- **GMO:** Q\* = 524/0.0000154 = 34,025,974; P\* $297.03; MR = MC = $69.05 ✓; profit $8.785B. Markup 4.30×, Lerner 0.768 (implied demand elasticity at optimum ≈ 1.3 — students who know the markup rule can back it out).
- **DWL:** ½ × (297.03 − 69.05) × (60.23M − 34.03M) ≈ $2.99B/yr.
- All figures brute-force/algebra verified and match the Excel key to the dollar (zero formula errors on recalculation).

## Bugs fixed vs the old materials (for Adam)

1. **TC = FC + MC·Q** in both v9 "Optimal" blocks and the in-class worksheet — with linear MC, variable cost is the *area under* MC (= aQ + bQ²), which v9's own decision tables computed correctly two rows down. Effect: GMO profit understated by ~$1.08B ($7.71B vs $8.79B) and non-GMO profit forced to exactly −$130M (AC ≡ MC ⇒ profit ≡ −FC — an artifact, not economics).
2. **In-class worksheet's non-GMO VC** = `corn_P*corn_Output_optimal` (= revenue!) — profit identically −FC.
3. **MC "curves" were regressions of tables** (SLOPE over tabulated ΔTC/ΔQ) with the intercept anchored to a blank cell — parameters now defined directly.
4. **Missing pieces added:** MR twice-as-steep derivation as an explicit checked step, markup + Lerner, competitive benchmark + DWL, real-world anchor rows, README sheet, instructor key with check figures.
5. **Typos:** "Monoplostic" (filename), inconsistent labels — new files named cleanly.

## Validated facts & sources (accessed 2026-07-07)

- **Trait shares:** Monsanto's patented traits on ~80% of U.S. corn and 90%+ of soybean acres ([Monsanto's own FAQ](https://monsanto.com/innovations/biotech-gmos/q/what-percentage-of-us-crops-are-grown-from-monsantos-genetically-modified-seed/), [Grist](https://grist.org/article/dominant-traits/), [Center for Food Safety](https://www.centerforfoodsafety.org/issues/303/seeds/the-role-of-ge-seeds-and-the-patent-system)); 90%+ of corn/soy/cotton acres GE overall ([USDA ERS](https://www.ers.usda.gov/data-products/adoption-of-genetically-engineered-crops-in-the-united-states/recent-trends-in-ge-adoption)). The draft's "85% corn / 90% soy / 95% sugar beets" → corrected to ~80% corn; ~95% for Roundup Ready sugar beets is widely reported and retained as *reported*.
- **Seed prices:** GMO corn ≈ $250–305/bag vs non-GMO from ~$85–150 ([FBN](https://www.fbn.com/community/blog/corn-soybean-trait-costs), [Wisconsin Corn Agronomy](http://corn.agronomy.wisc.edu/WCM/W182.aspx), [Hybrid85](https://hybrid85.com/)); GM seed prices rose far faster than non-GM 1990–2020 ([USDA ERS](https://ers.usda.gov/data-products/charts-of-note/chart-detail?chartId=106785)). Case's $270 vs $120 sits inside both ranges. Bag = 80,000 kernels ≈ 2.5 acres ✓.
- **Bayer deal:** closed June 7, 2018 at $63B, creating the world's largest seed + agchem company ([Bloomberg](https://www.bloomberg.com/news/articles/2018-06-07/bayer-closes-monsanto-deal-to-cap-63-billion-transformation)); DOJ required ~$9B divested to BASF — the largest negotiated merger divestiture in U.S. history ([DOJ](https://www.justice.gov/archives/opa/pr/justice-department-secures-largest-merger-divestiture-ever-preserve-competition-threatened), [CNBC](https://www.cnbc.com/2018/05/29/bayer-will-sell-basf-9-billion-in-assets-to-allow-monsanto-purchase.html)). The draft's "second-largest agrochemical entity" → replaced with the sourced framing.
- Founded 1901 (saccharin), Roundup launched 1974, glyphosate-resistant "superweeds" documented — retained from the draft; standard record.

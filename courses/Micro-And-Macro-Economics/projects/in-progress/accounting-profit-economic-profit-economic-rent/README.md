# BUS 620 Project: Accounting Profit, Economic Profit & Economic Rent — Ride-Share Driver Economics

> **Status:** Kumu-improved draft (2026-07-07) formalizing `BUS 620 Case Study_ Accounting Profit, Economic Profit, Economic Rent.docx`. Adam should review before students see it. The original docx and `Supply_Invisible Hand_Ride Sharing template.xlsx` are preserved unchanged; the rebuilt workbooks are `rideshare-driver-economics-template.xlsx` (student) and `rideshare-driver-economics-key.xlsx` (instructor). All real-world claims validated 2026-07-07; sources at bottom.

## The pitch

Four New Yorkers, one question: *who's actually making money?* A full-time Uber driver, a part-time Uber driver, a full-time Yellow Cab driver, and an office worker each get a full P&L — gross fares down to **accounting profit**, then past it to **economic profit** by charging each person what their next-best alternative pays. The verdicts flip: the Uber driver's healthy $50K accounting profit turns *negative* once the forgone office job is counted. Then Part 2 asks where the money went — and finds it capitalized inside a tin shield bolted to the hood: the **taxi medallion**, whose price the model reproduces almost exactly, at its $1M peak *and* after Uber destroyed it.

## Learning goals

1. **Accounting profit ≠ economic profit** — explicit costs vs implicit (opportunity) costs, and why "profitable" businesses can be economic losers.
2. **Normal profit** as the implicit cost itself: the earnings needed just to keep a person (or asset) where it is.
3. **Opportunity cost discipline:** compare *net to net* (the alternative's earnings after its own costs), and match scale (a part-timer forgoes a part-time alternative). Both were wrong in the draft template.
4. **Economic rent** — payment to a factor in fixed supply above what keeps it in use — and **capitalization**: an asset earning rent forever is worth rent ÷ required return.
5. **Entry erodes rent** (the invisible hand with teeth): 120,000+ app vehicles vs 13,587 capped medallions, and an ~80% asset-price collapse the perpetuity formula predicts within ~10%.

## The model — Sheet 1: Driver Economics (annual, 30 days/mo stated simplification)

| | Uber FT | Uber PT | Yellow Cab FT | Traditional job |
|---|---|---|---|---|
| Gross | $86,400 | $43,200 | $108,000 | $57,600 |
| Explicit costs | $35,880 (incl. 25% commission) | $20,340 | $48,420 (incl. $36,000 lease) | $5,400 (commute) |
| **Accounting profit** | **$50,520** | **$22,860** | **$59,580** | **$52,200** |
| Implicit cost | $52,200 (traditional, net) | $26,100 (½ traditional) | $52,200 | $50,520 (Uber FT) |
| **Economic profit** | **−$1,680** | **−$3,240** | **+$7,380** | **+$1,680** |

Teaching beats: the part-timer is hit hardest because the car's costs don't scale (full payment + insurance on half the revenue); the cab driver "wins" at the driver level but hands $36,000/yr to the medallion owner — the hook into Part 2; and everything is one input away from flipping (set days/mo to a civilian 22 and re-read the verdicts — that fragility *is* the gig-economy lesson).

## The model — Sheet 2: Medallion & Rent

The medallion is the rent-capturing asset: fixed supply (13,587), so the driver's lease payment is economic rent, and the asset is worth the capitalized rent stream:

| | Pre-entry (≈2013) | Post-entry (≈2019) |
|---|---|---|
| Lease | $3,000/mo → $36,000/yr | $1,500/mo → $18,000/yr |
| Required return | 3.5% | 6.0% (riskier) |
| **Capitalized value** | **$1,028,571** | **$300,000** |
| **Observed price** | **>$1M peak (2013–14)** | **≈$335K (June 2019)** |

One division reproduces both observed prices within ~10%. The rent story: app entry (40K vehicles in 2010 → 120K+ by 2019) competed away fares → lease fell → the perpetuity shrank *and* got riskier → 70–85% asset collapse. The cap blocked entry into *yellow cabs* but not into *rides* — rent survives only as long as the moat actually surrounds the market.

## Deliverables (4-artifact AI + GitHub workflow, same as the other BUS 620 cases)

| # | Artifact | Contents | Pts |
|---|---|---|---|
| 1 | `brief.md` | The four-person setup in your own words + hypothesis: "I expect X to have the highest economic profit because Y" | 3 |
| 2 | `driver-economics.xlsx` | Completed template: accounting/economic/normal profit rows built (yellow cells), medallion values capitalized, one sensitivity run (22 days/mo) documented | 8 |
| 3 | `analysis.md` + ≥2 figures | The verdicts explained; the medallion story told with the capitalization math; supply/demand section: which curve shifted (supply, right — massively), what happened to price, quantity, and *whose* surplus | 6 |
| 4 | `prompt-log.md` + reflection | AI sessions logged; reflection covers an AI error you caught | 3 |

**AI-use boundary (course standard):** AI may explain the profit concepts, quiz you, and critique reasoning — not fill your yellow cells or write your analysis.

## Industry-analysis prompts (from the draft, kept & corrected)

- Supply shifted **right** (ridesharing collapsed the entry barrier); demand also shifted right (convenience/price transparency) but the supply shock dominates: **price ↓, quantity ↑↑** — consumers won, incumbent rent-holders lost.
- Efficiency & the invisible hand: surge pricing as a price signal recruiting drivers exactly when demand spikes; drivers self-allocating to rush hours without anyone ordering them to.
- Externalities & regulation: congestion (negative), possible car-ownership reduction (*reported*, UC Berkeley); London's 2017 license refusal as a regulation case.

## Instructor notes

- **The draft's "141,615 licensed Yellow Cabs in NYC (2010)" is wrong** — NYC medallions numbered ~13,500 and were 13,587 from 2014–2018. Corrected everywhere; the big number likely conflated TLC-licensed *drivers/vehicles* across all classes.
- Check figures (Excel key recalculates clean, matches hand math to the dollar): accounting $50,520 / $22,860 / $59,580 / $52,200; economic −$1,680 / −$3,240 / +$7,380 / +$1,680; medallion $1,028,571 / $300,000.
- Sensitivity to run live in class: days/mo 30 → 22 (all verdicts flip deep negative for drivers); commission 25% → 30%; cab lease $3,000 → $1,500 (post-Uber world — watch the cab driver's economic profit and ask who the winner is *now*).
- Cross-case links: the farmer's field time in the Perfect Competition case is the same opportunity-cost idea; the medallion's rent-behind-a-moat is Monsanto's patent in miniature (all three cases now share the moat→rent→entry arc).

## Bugs fixed vs the draft template (for Adam)

1. **Implicit cost used the alternative's GROSS salary** ($57,600) — opportunity cost must be the alternative's *net* earnings ($52,200); apples to apples.
2. **The part-time driver was charged a full-time opportunity cost** — halved to a part-time alternative ($26,100).
3. **The "Economic Rent" section was an empty header** — now the entire Medallion & Rent sheet, arguably the best part of the case.
4. **Stray references removed:** broken `commission_to_uber` (#REF!) and a leaked external named range (`q_tomato` pointing into the farm workbook).
5. Stated the 30-days/month simplification explicitly and made it an input (the old sheet buried `*30` inside formulas).

## Validated facts & sources (accessed 2026-07-07)

- **Medallions:** 13,587, constant 2014–2018; peak prices >$1M in 2013–14 (corporate to ~$1.3M); ~$335K by June 2019 ([Fideres](https://www.fideres.com/new-york-taxi-medallions/), [R Street](https://www.rstreet.org/commentary/nycs-taxi-medallion-crisis-is-a-case-study-in-government-malfeasance/), [Columbia HRLR](https://hrlr.law.columbia.edu/hrlr-online/distressed-drivers-solving-the-new-york-city-taxi-medallion-debt-crisis/)). Note honestly in class: predatory medallion *lending* inflated the peak too — entry wasn't the only villain ([R Street](https://www.rstreet.org/commentary/nycs-taxi-medallion-crisis-is-a-case-study-in-government-malfeasance/)).
- **App-vehicle growth:** ~40,000 (2010) → 120,000+ (2019) ([Documented NY](https://documentedny.com/2021/11/23/taxi-cab-medallion-explained/), [Washington Post](https://www.washingtonpost.com/business/economy/uber-lyft-and-the-hard-economics-of-taxi-cab-medallions/2019/05/24/cf1b56f4-7cda-11e9-a5b3-34f3edf1351e_story.html)).
- **Uber take ≈25%** of fares (validated; 25–30% by market). NYC adopted the U.S.'s first ride-hail minimum-pay formula in 2019; the standard 30-min/7.5-mi trip minimum reached $29.07 in 2025, ~26% above 2019 ([NYC TLC](https://www.nyc.gov/site/tlc/about/driver-pay-rates.page), [amNY](https://www.amny.com/news/nyc-taxi-pay-hike-lockout-protection-uber-lyft/)).
- **Kept as *reported*** (draft claims, plausible but not primary-sourced here): 2–3 min average Uber wait vs 10–15 for street hails; UC Berkeley car-ownership study; London TfL's 2017 refusal to renew Uber's license (that one is standard record).

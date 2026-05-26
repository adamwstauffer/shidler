# Financial Model Assumptions — Student One-Pager

**Use these exact values in any DCF, WACC, or valuation work you submit in this course.** Do not derive your own — consistency across student models lets us grade fairly and lets you compare your output to your classmates' apples-to-apples.

If you want to deviate (e.g., your case study is a non-US company), document the deviation in your model's notes section and explain why.

---

## Values to Hardcode

| Input | Value | What it means |
|---|---|---|
| **Risk-Free Rate (USD, 10Y UST)** | **4.55%** | The yield on a US government bond; the "zero-risk" anchor for cost of equity |
| **Equity Risk Premium** | **5.50%** | Extra return investors demand for holding stocks vs. bonds |
| **Beta** | **1.00** | Default unless you opt into a company-specific beta and explain why on your cover sheet |
| **US Effective Tax Rate (default)** | **24.0%** | Use this when your company's actual effective rate isn't available |
| **Terminal Growth Rate** | **2.5%** | Approximate US long-term GDP growth; cap for perpetuity assumptions |
| **Projection Period** | **5 years** | Standard DCF horizon for this course |
| **Discounting Convention** | **Mid-year** | Periods 0.5, 1.5, 2.5, 3.5, 4.5 |

**Non-USD valuations** — use the local 10Y sovereign bond yield for the company's reporting currency. For Vietnamese firms (BUS-629), use **VND 10Y = 3.10%**. Other currencies are in the full spec.

---

## Computing Cost of Equity (CAPM)

```
Cost of Equity (Ke) = Risk-Free Rate + Beta × Equity Risk Premium
                    = 4.55% + 1.00 × 5.50%
                    = 10.05%
```

Use this as your WACC unless your company has meaningful debt (in that case, you'll weight Ke and after-tax cost of debt by capital structure — see the full spec for the formula).

---

## What These Numbers Are For

- **Risk-Free Rate (Rf)** anchors every discount-rate calculation. It's the yield you'd earn if you took zero risk, so any risky investment must earn more than this.
- **Equity Risk Premium (ERP)** is the extra return the stock market has historically earned over bonds — empirically 4–6% in the US.
- **Beta** measures how much your specific stock moves with the broader market. β = 1.0 means "moves with the market." β > 1.0 means "more volatile." β < 1.0 means "less volatile." This course defaults to 1.0 for consistency.
- **Tax Rate** matters because interest on debt is tax-deductible, and we discount **after-tax** cash flows.
- **Terminal Growth Rate** is what we assume the company grows at forever, after the explicit forecast period. Keep this below long-run GDP — no company grows faster than the economy forever.

---

## Formatting Standards (for grading)

| Element | Color |
|---|---|
| Hardcoded numbers you typed in | Blue font |
| Formulas | Black font |
| Links to other tabs | Green font |
| Section headers | Dark blue fill, white text |

Every blue cell needs a one-line comment explaining where the number came from (e.g., "Source: NVDA 10-K FY2026, p.45" or "Source: course assumption spec").

---

## When to Use This Page vs. the Full Spec

- **This page:** student deliverables, in-class exercises, problem sets, project stages.
- **Full spec ([`docs/financial-model-assumptions.md`](./financial-model-assumptions.md)):** capstone projects where you're proposing a real investment view, anything involving comps, LBO, or merger models, or any work where you're opting into a company-specific beta or deviating from a default.

Last refreshed from full spec: **2026-05-26** (Rf as of 2026-05-22; ERP as of 2026-05-01).

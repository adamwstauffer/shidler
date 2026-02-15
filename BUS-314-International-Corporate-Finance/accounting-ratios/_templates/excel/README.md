# Excel Templates

Excel templates will be provided after Stage 2 is submitted.

*skeleton* -> *progressive reveal* -> *guided with checks* -> ready for *AI prompt stage*.

## Template Strategy

Templates use a **progressive reveal** approach — each version fills in more of the model so students at different comfort levels can start from the right place.

## Individual Files

**Skeleton** (financial statement tabs + ratio headers only; all formulas blank; hints sidebar)
- `Stage3_Skeleton.xlsx`

**Partial — Financial Statements Filled** (Balance Sheet and Income Statement data entered; ratios blank; named ranges defined)
- `Stage3_FinStatements_Partial.xlsx`

**Partial — With Derived Inputs** (financial data + derived inputs computed; ratio formulas blank)
- `Stage3_DerivedInputs_Partial.xlsx`

**Full Guided with Checks** (all sections filled; hidden checks sheet validates Du Pont decomposition and Balance Sheet balance)
- `Stage3_Full_Guided_with_Checks.xlsx`

## Template Structure

Each template contains these tabs:

| Tab | Purpose |
|-----|---------|
| **Balance Sheet** | Current year and prior year Balance Sheet data |
| **Income Statement** | Income statement line items |
| **Cash Flow** | Cash flow statement data |
| **Ratios** | Inputs section + ratio calculations by category |
| **Notes** | Assumptions, data sources, named range reference |
| **Checks** *(hidden in guided version)* | Validation formulas for instructor review |

## Color Coding Convention

| Color | Meaning |
|-------|---------|
| Yellow | Editable input cells |
| Blue | Assumptions (tax rate, cost of capital) |
| Green | Formula cells (computed values) |
| Gray | Output / summary cells |

## Named Range Convention

All named ranges follow a consistent pattern:

- **Balance Sheet:** `BAL_[item]_[year]` (e.g., `BAL_assets_total_2024`)
- **Income Statement:** `INC_[item]` (e.g., `INC_sales`, `INC_net`)
- **Cash Flow:** `CASH_[item]` (e.g., `CASH_operating`)
- **Market/Analyst:** descriptive (e.g., `share_price`, `cost_capital`)
- **Derived — Start of Year:** `startYear_[item]` (e.g., `startYear_equity`)
- **Derived — Current Year:** `currentYear_[item]` (e.g., `currentYear_assets_total`)
- **Derived — Averages:** `avg_[item]` (e.g., `avg_total_assets`)
- **Ratios:** `RATIO_[name]` (e.g., `RATIO_asset_turnover`, `RATIO_leverage`)

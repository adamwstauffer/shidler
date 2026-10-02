# Validation

Self-audit reports and validation documentation. In professional finance, model validation is a formal process — Big 4 firms, banks, and regulators require independent review of financial models before they inform decisions. Stage 3 introduces this discipline at the individual level.

## What belongs here

- **Stage 3 validation reports** — self-audit of your populated ratio model
- **Peer review notes** — if peer review (Stage 3b) is conducted

## Naming convention

```
YYYY-MM-DD-{company-slug}-validation-analysis.md
```

**Examples:**
- `2026-06-05-vinamilk-validation-analysis.md`

Files already submitted under an older name (with your last name, or a `stageN` prefix) still count — nothing to rename.

## Self-audit checklist

Your validation report must address each of these checks:

| Check | What to verify |
|-------|---------------|
| Balance Sheet balances | Assets = Liabilities + Equity (both years) |
| Du Pont ROA consistency | Du Pont ROA (Margin x Turnover) ≈ Direct ROA |
| Du Pont ROE consistency | Du Pont ROE ≈ Direct ROE |
| Sign checks | No negative ratios where impossible |
| Reasonableness | Ratios fall within plausible industry ranges |
| Named range audit | Spot-check 5 named ranges → correct cells |
| Formula audit | Spot-check 5 formulas → correct inputs |
| Start-of-year vs. average | Compare and explain any divergence |

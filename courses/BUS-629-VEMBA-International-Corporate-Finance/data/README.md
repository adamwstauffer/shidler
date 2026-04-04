# Data

Source financial data, statements, and provenance documentation. In professional finance, raw data is kept separate from derived analysis to maintain auditability — you should always be able to trace a number in your model back to its source document.

## What belongs here

- **Financial statement extracts** — downloaded or copied sections of 10-K filings, annual reports, or audited financials
- **Market data** — share price, shares outstanding, analyst estimates
- **Source notes** — documentation of where each data point came from and when it was accessed

## Naming convention

Organize by student, then by source:

```
data/
└── [lastname]/
    ├── sources.md              # Data provenance log
    ├── [ticker]-10K-2025.pdf   # Source documents
    └── [ticker]-market-data.md # Market/analyst assumptions
```

## Data provenance

For every data point in your model, you should be able to answer:
1. **Where** did this number come from? (SEC EDGAR, company IR page, Yahoo Finance, HOSE portal, etc.)
2. **When** was it accessed? (Date)
3. **What** reporting standard applies? (U.S. GAAP, IFRS, VAS)
4. **Any adjustments?** (Currency conversion, reclassification, IFRS/GAAP differences)

Record this in a `sources.md` file in your data directory.

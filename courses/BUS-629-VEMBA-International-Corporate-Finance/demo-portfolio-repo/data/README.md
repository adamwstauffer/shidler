# `data/`

Source financial data and provenance notes. Every dataset you use in a model build lands here, with a record of where it came from and when.

## What belongs here

- Raw downloads from Bloomberg, Capital IQ, S&P, company filings, etc.
- CSV/XLSX exports from data providers
- A short `.md` provenance note next to each dataset

## Provenance notes

For every dataset, write a `<dataset-name>-source.md` file alongside it that records:

- **Source:** provider name and URL
- **Access date:** YYYY-MM-DD
- **Coverage:** date range, ticker(s), fields
- **License/restrictions:** can this be redistributed? (Most subscription data cannot.)

## Naming conventions

- `<company-or-topic>-<YYYY-MM-DD>.csv` — date-stamp every download
- Keep raw and cleaned data separate: `vingroup-financials-raw-2026-05-09.csv` vs. `vingroup-financials-clean-2026-05-09.csv`

## Don't commit

- API keys, login credentials
- Any data covered by an NDA or subscription license that prohibits redistribution

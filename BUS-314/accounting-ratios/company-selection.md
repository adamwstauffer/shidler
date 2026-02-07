# Company Selection Guide

## Overview

For this project, you will choose a **publicly traded U.S. company** and analyze its financial health using accounting and performance ratios. You will use the company's most recent **annual financial statements** (10-K filing) as your data source.

---

## Requirements

Your company must:

1. **Be publicly traded** on a major U.S. exchange (NYSE, NASDAQ).
2. **Have readily available financial statements** — Balance Sheet, Income Statement, and Cash Flow Statement — in its most recent 10-K filing.
3. **Be a non-financial company.** Avoid banks, insurance companies, and REITs — their financial statements have a different structure that doesn't align well with the ratios in this course.
4. **Have at least 2 years of data** so you can compute start-of-year and current-year comparisons.

---

## How to Choose

Pick a company you find interesting. Good starting points:

- A company whose products or services you use regularly
- A company in an industry you want to work in
- A company that has been in the news recently
- A company you are considering for investment

### Example Companies by Industry

| Industry | Example Companies |
|----------|-------------------|
| Technology | Apple, Microsoft, Google (Alphabet), Meta, NVIDIA |
| Retail | Walmart, Target, Costco, Home Depot, Nike |
| Consumer Goods | Procter & Gamble, Coca-Cola, PepsiCo, Johnson & Johnson |
| Automotive | Tesla, Ford, General Motors |
| Healthcare | UnitedHealth, Pfizer, Abbott Laboratories |
| Energy | ExxonMobil, Chevron, NextEra Energy |
| Industrials | Caterpillar, 3M, Honeywell, Boeing |
| Entertainment | Disney, Netflix, Comcast |

> **Tip:** Companies in the S&P 500 generally have clean, well-structured financial statements that are easiest to work with.

---

## Where to Find Financial Statements

| Source | URL | Notes |
|--------|-----|-------|
| **SEC EDGAR** | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany | Official source; search by company name or ticker |
| **Yahoo Finance** | https://finance.yahoo.com | Financials tab on any stock page |
| **Macrotrends** | https://www.macrotrends.net | Clean historical financial data |
| **Company IR Page** | Google "[Company] investor relations" | Annual reports and 10-K filings |

### What to Look For in the 10-K

You will need these sections:
- **Balance Sheet** (also called "Consolidated Balance Sheets") — current and prior year
- **Income Statement** (also called "Consolidated Statements of Income/Operations")
- **Cash Flow Statement** (also called "Consolidated Statements of Cash Flows")

### Market Data You'll Also Need

- **Share price** — current or as of fiscal year end (Yahoo Finance, Google Finance)
- **Shares outstanding** — found in the 10-K or on Yahoo Finance "Statistics" page
- **Cost of capital** — you may estimate this or use a reasonable assumption (discuss with instructor)

---

## Specific Data Points to Collect

From the **Balance Sheet** (current year AND prior year):

- Cash and marketable securities
- Receivables
- Inventories
- Other current assets
- Total current assets
- Property, plant, and equipment (gross and net)
- Intangible assets / goodwill
- Other long-term assets
- **Total assets**
- Debt due for repayment (current portion of long-term debt)
- Accounts payable
- Other current liabilities
- Total current liabilities
- Long-term debt
- Other long-term liabilities
- **Total liabilities**
- Common stock and paid-in capital
- Retained earnings
- **Total shareholders' equity**

From the **Income Statement**:

- Net sales / revenue
- Cost of goods sold (COGS)
- Selling, general & administrative expenses (SG&A)
- Depreciation (if shown separately; may be in Cash Flow Statement)
- **EBIT** (Earnings Before Interest and Taxes)
- Other income
- Interest expense
- Taxable income (income before taxes)
- Income tax expense
- **Net income**
- Dividends (may be in Cash Flow Statement or equity section)

From the **Cash Flow Statement**:

- Cash from operations
- Capital expenditures
- Cash from investing activities
- Cash from financing activities

---

## Tips

- **Start early.** Gathering the data takes more time than you expect.
- **Be consistent with units.** Most companies report in millions — note this in your model.
- **Watch for fiscal year timing.** Some companies (e.g., Walmart, Nike) have fiscal years ending in January or May, not December.
- **Document your sources.** Note exactly where each number came from — this matters for auditability.
- **If a line item doesn't exist** for your company (e.g., no inventories for a services firm), enter zero and note it in your assumptions.

---

## Submission

State your company choice in your Stage 1 memo. If you want to change companies after Stage 1, discuss with the instructor first — switching mid-project creates extra work.

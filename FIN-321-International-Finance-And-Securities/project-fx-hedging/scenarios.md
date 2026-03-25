# 📘 Example Scenarios – EUR Receivables (USD Base, 1-Year Horizon)

### 📌 Quick Note on Setting the Spot FX Rate, Strike Price (K), and Interest Rates

When you see a placeholder like:
* **Put on EUR with (k =) [EURUSD]**
* **Call on EUR with (k =) [EURUSD]**
* **USD Interest Rate:** [n.nn%]
* **EUR Interest Rate:** [n.nn%]

…it means you are responsible for **determining the strike price (K) and interest rates** based on **current market data**.

**Use rates, prices, and quotes as of market close on the day you begin Stage 2.**

Here’s how to approach it:

1. **Look up the current EURUSD spot rate** (e.g., from Bloomberg, Yahoo Finance, or your preferred data source). Record the date and source.
2. Use this **spot rate as the starting point** for your strike price (K). In most basic hedge setups, the strike is set **at or near the current spot**.

---

### 📁 Scenario 1 – U.S. Solar Equipment Importer

* **Receivable:** $4,500,000 receivable in 1 year
* **Spot:** EURUSD quote
* **Forward:** 1.0875 (maturity: 1 year from today)
* **USD Interest Rate:** [n.nn%]
* **EUR Interest Rate:** [n.nn%]
* **Option:**
  * Put on EUR with (k =) [EURUSD], premium = $0.015 per contract (no multiplier)
  * Call on EUR with (k =) [EURUSD], premium = $0.018 per contract (no multiplier)

---

### 📁 Scenario 2 – U.S. Pharmaceutical Exporter

* **Receivable:** $8,000,000 receivable in 1 year
* **Spot:** EURUSD quote
* **Forward:** 1.0890 (maturity: 1 year from today)
* **USD Interest Rate:** [n.nn%]
* **EUR Interest Rate:** [n.nn%]
* **Option:**
  * Put on EUR with (k =) [EURUSD], premium = $0.021 per contract (no multiplier)
  * Call on EUR with (k =) [EURUSD], premium = $0.026 per contract (no multiplier)

---

### 📁 Scenario 3 – U.S. Tech Services Firm

* **Receivable:** $12,500,000 receivable in 1 year
* **Spot:** EURUSD quote
* **Forward:** 1.0910 (maturity: 1 year from today)
* **USD Interest Rate:** [n.nn%]
* **EUR Interest Rate:** [n.nn%]
* **Option:**
  * Put on EUR with (k =) [EURUSD], premium = $0.017 per contract (no multiplier)
  * Call on EUR with (k =) [EURUSD], premium = $0.022 per contract (no multiplier)

---

### 📁 Scenario 4 – U.S. Aerospace Manufacturer

* **Receivable:** $20,000,000 receivable in 1 year
* **Spot:** EURUSD quote
* **Forward:** 1.0935 (maturity: 1 year from today)
* **USD Interest Rate:** [n.nn%]
* **EUR Interest Rate:** [n.nn%]
* **Option:**
  * Put on EUR with (k =) [EURUSD], premium = $0.019 per contract (no multiplier)
  * Call on EUR with (k =) [EURUSD], premium = $0.024 per contract (no multiplier)

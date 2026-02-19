# Spec: International Parity Relationships — Interest Rate Parity

**Created by:** Adam Stauffer  
**Updated by:** ChatGPT (Assistant)  
**Date Created:** 2025-09-18  
**Date Updated:** 2025-09-18  
**Version:** 1.0  

---

## 1. Objective  
To demonstrate and verify the principle of **Covered Interest Rate Parity (CIRP)** using the U.S. and U.K. interest rates, spot FX rate, and forward FX rate.  

---

## 2. Scope  
- **In-scope:** One-period CIRP analysis (1-year horizon) with USD/GBP example.  
- **Out-of-scope:** Multi-period extensions, transaction costs, and deviations due to capital controls.  

---

## 3. Inputs  
- U.S. 1-Year Interest Rate = 4.084%  
- U.K. 1-Year Interest Rate = 3.778%  
- Spot GBP/USD = 1.3415  
- Forward rate formula:  
  \[
  F = S \cdot \frac{(1+i_{USD})}{(1+i_{GBP})}
  \]  

---

## 4. Workflow / Steps  
1. Calculate domestic investment return in USD:  
   \[
   100 \times (1+i_{USD})
   \]  
2. Convert USD → GBP at spot, invest in U.K. asset at \(i_{GBP}\).  
3. Hedge currency risk by selling GBP forward at rate \(F\).  
4. Convert proceeds back into USD after one year.  
5. Compare U.S. and U.K. hedged returns.  
6. Conclude whether parity holds (arbitrage-free condition).  

---

## 5. Expected Outputs  
- Step-by-step calculations of U.S. and U.K. returns.  
- Forward exchange rate consistent with CIRP.  
- Graphs/tables from slides:  
  - U.S. return vs U.K. return comparison  
  - Formula derivation \( (1+i_{USD}) = \frac{F}{S}(1+i_{GBP}) \)  
- Final statement on whether parity condition holds.  

---

## 6. Evaluation Criteria  
- **Accuracy:** Are calculations correct?  
- **Clarity:** Is IRP explained with both math and words?  
- **Reproducibility:** Can results be replicated with given inputs?  
- **Visualization:** Are figures/tables clearly labeled and aligned with slides?  

---

## 7. AI Prompts (Examples)  
- *“Explain Interest Rate Parity in simple terms for MBA students with a numeric example.”*  
- *“Generate a Python function that calculates the forward rate given spot, iUSD, and iGBP.”*  
- *“Draft a one-page policy memo: Why deviations from IRP might occur in emerging markets.”*  

---

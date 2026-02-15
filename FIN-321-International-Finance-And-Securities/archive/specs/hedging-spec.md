# Spec: Transaction Hedging — EUR Receivable (90 days)

**Created by:**  
**Updated by:**  
**Date Created:**  
**Date Updated:**  
**Version:** 1.0

---

## Objective
Select and justify the optimal hedge (forward, money market, option, no hedge) for a € receivable due in ~90 days.

## Scope
- Short-run transaction exposure; perfect capital mobility assumed; ignore taxes unless stated.
- Theories: covered interest parity, option payoff, MM replication.
- Assumptions: day-count t = 90/360, simple annualization (document if using compounding).

## Inputs (Base Case)
- € receivable: 5,000,000  
- S (USD/EUR): 1.1000  
- F_90d (USD/EUR): 1.1050  
- r_USD (annual): 5.00%  
- r_EUR (annual): 3.00%  
- Option: EUR put strike K = [enter], premium c = [enter] USD/EUR

## Method
1. Compute **F_IRP = S·(1+r_USD·t)/(1+r_EUR·t)**; compare to quoted forward.  
2. **Forward USD** = € * F.  
3. **Money Market USD** = S * ( € / (1+r_EUR·t) ) * (1+r_USD·t).  
4. **Option USD at T** = € * MAX(S_T, K) − (€ * c).  
5. **No Hedge USD** = € * S_T.  
6. Build sensitivity for S_T ∈ {−10%, −5%, 0, +5%, +10%} relative to S.  
7. Choose decision rule and recommend a hedge. Document trade-offs.

## Outputs
- Table: strategy vs USD proceeds (base & sensitivity)
- Option breakeven: S* where proceeds with option ≈ forward/MM
- Recommendation with rationale

## Acceptance Criteria
- Formulas correct and referenced; sensitivity present; decision rule explicit; recommendation consistent with analysis.

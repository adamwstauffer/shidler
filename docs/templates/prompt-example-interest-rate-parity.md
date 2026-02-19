# Prompts: International Parity Relationships — Interest Rate Parity

**Created by:** Adam Stauffer  
**Updated by:** ChatGPT (Assistant)  
**Date Created:** 2025-09-18  
**Version:** 1.0  

---

## 🔹 Teaching Prompts
Use these to explain or introduce IRP concepts in different styles.

- **Explain Simply:**  
  “Explain Covered Interest Rate Parity (CIRP) in simple terms as if teaching first-year MBA students, using the U.S. and U.K. interest rate example.”  

- **Visual Illustration:**  
  “Generate a labeled diagram that shows the two investment paths (domestic vs. foreign with forward hedge) under Interest Rate Parity.”  

- **Compare Perspectives:**  
  “Explain how IRP is viewed by (a) an international investor, (b) a central bank policymaker, and (c) a multinational corporation.”  

---

## 🔹 Analytical Prompts
Use these to compute values and check parity conditions.

- **Forward Rate Calculation:**  
  “Calculate the forward GBP/USD exchange rate given Spot = 1.3415, U.S. 1-year interest rate = 4.084%, and U.K. 1-year interest rate = 3.778%.”  

- **Return Comparison:**  
  “Compute and compare the final USD value of $100 invested in (a) the U.S. at 4.08% and (b) the U.K. at 3.78% with a forward hedge.”  

- **IRP Check:**  
  “Verify whether Interest Rate Parity holds given the above inputs. Show both the math and an explanation in plain language.”  

---

## 🔹 Coding Prompts
Use these for automation and reproducibility in Python, R, or Excel.

- **Python Function:**  
  “Write a Python function `calc_forward_rate(spot, i_usd, i_gbp)` that returns the 1-year forward rate under CIRP.”  

- **Excel Formula:**  
  “Generate the Excel formula for the forward rate \( F = S \cdot \frac{1+i_{USD}}{1+i_{GBP}} \). Assume Spot = cell A1, iUSD = B1, iGBP = C1.”  

- **Monte Carlo Extension:**  
  “Write Python code that simulates 1,000 possible deviations from Interest Rate Parity given random shocks to interest rates and FX rates.”  

---

## 🔹 Research & Policy Prompts
For deeper discussion, reflection, or paper writing.

- **Policy Memo:**  
  “Draft a one-page policy memo explaining why deviations from IRP may occur in emerging markets. Include at least three causes (capital controls, transaction costs, risk premiums).”  

- **Historical Case:**  
  “Summarize one historical episode where Interest Rate Parity did not hold. Explain why, and what the market consequences were.”  

- **Comparative Analysis:**  
  “Compare IRP with Purchasing Power Parity (PPP). How do they differ in theory, and why might they break down differently in practice?”  

---

## 🔹 Student Skill Tags
Using these prompts teaches students to:  
- Frame **AI queries** for economic analysis.  
- Automate finance calculations in **Python/Excel**.  
- Communicate results via **visuals and policy memos**.  
- Document reproducible work in **GitHub repos**.  

---

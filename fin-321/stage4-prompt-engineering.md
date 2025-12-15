# STAGE 4 — AI GENERATION PROMPT  
**Goal:** Create a complete Excel FX hedge model (forward, money market, options, sensitivity table) using the logic from my Stage 2 specification and Stage 3 spreadsheet.

---

# GOAL
Generate a fully functional Excel model that computes, compares, and visualizes hedge outcomes for my EUR receivable. The spreadsheet must include named ranges, color-coded inputs, professional formatting, forward hedge, money market hedge, option hedges, and a ±5% sensitivity table. All formulas must follow the logic defined in this prompt.

---

# CONTEXT
I am analyzing a **€12,500,000 receivable** due in 1 year.
Stage 2 specification (technical plan) is available here: https://github.com/kmcmoor/shidler/blob/patch-2/fin-321/template-spec.md
Stage 3 implemented the logic manually in Excel. This prompt should use the same logic (forward, money market, option hedges, sensitivity table) when generating the spreadsheet automatically.
Your task now is to **automate** the creation of this model by generating a complete `.xlsx` file that exactly follows the requirements below.

---

# INPUT VARIABLES (USE THESE EXACT VALUES)
Assign these values to the input section and name the ranges exactly as specified:
FC_AMT = 12,500,000 # EUR receivable amount
S0_in = 1.09 # Spot rate (USD/EUR)
F0_in = 1.091 # 1-year forward rate (USD/EUR)
R_USD = 0.05 # USD interest rate (5%)
R_FC = 0.03 # EUR interest rate (3%)
K_PUT = 1.09 # Put strike
K_CALL = 1.09 # Call strike
PREM_PUT = 0.017 # Put premium (USD per EUR)
PREM_CALL = 0.022 # Call premium (USD per EUR)
T_DAYS = 365
T_YRS = 1


**All input cells must be highlighted yellow** and formatted clearly.

---

# SPREADSHEET REQUIREMENTS

## 1. Named Ranges (Required)
Every variable above must be assigned as a named range:

- FC_AMT  
- S0_in  
- F0_in  
- R_USD  
- R_FC  
- K_PUT  
- K_CALL  
- PREM_PUT  
- PREM_CALL  
- T_DAYS  
- T_YRS  

Do not invent new names.

## 2. Color Coding
- **Yellow** = Editable inputs  
- **Blue** = Assumptions  
- **Green** = All formulas  
- **Gray** = Final outputs / KPIs  

## 3. Required Model Sections
You must create these labeled sections:

- Inputs  
- Forward Hedge  
- Money Market Hedge  
- Option Hedges (Put & Call)  
- Sensitivity Table (±5% around S₀)  
- Output Summary  
- Notes & Assumptions  

Spacing and borders must be clean and professional.

## 4. Sensitivity Table Requirements
- S_T varies from **0.95 × S0_in** to **1.05 × S0_in**
- 1% increments (11 rows total)
- Columns must include:
  - S_T  
  - Unhedged USD  
  - Forward USD  
  - Money Market USD  
  - Put Hedge USD  
  - Call Hedge USD  

(Optional): Add a line chart comparing hedge outcomes.

---

# NAMED RANGE DEFINITIONS
Each named range must point to its specific input cell.  
All formulas throughout the spreadsheet must reference named ranges rather than cell addresses.

---

# MODEL LOGIC (PSEUDOCODE)

## 1. Forward Hedge
USD_forward = FC_AMT * F0_in


## 2. Money Market Hedge (3 Steps)
EUR_present = FC_AMT / (1 + R_FC)
USD_today = EUR_present * S0_in
USD_mm = USD_today * (1 + R_USD)


## 3. Option Premiums
Premium_put_total = FC_AMT * PREM_PUT
Premium_call_total = FC_AMT * PREM_CALL


## 4. Option Payoffs (function of S_T)

### Put Hedge
If S_T < K_PUT:
USD_put = FC_AMT * K_PUT - Premium_put_total
Else:
USD_put = FC_AMT * S_T - Premium_put_total


### Call Hedge
If S_T > K_CALL:
USD_call = FC_AMT * K_CALL - Premium_call_total
Else:
USD_call = FC_AMT * S_T - Premium_call_total


## 5. Unhedged Exposure
USD_unhedged = FC_AMT * S_T


---

# FORMATTING & COLOR CODING
Apply the following formatting:

- Inputs in yellow  
- Assumptions in blue  
- Calculation cells in green  
- Output KPI cells in gray  
- Use borders around each main section  
- Label each hedge “Forward Hedge”, “Money Market Hedge”, “Option Hedge – Put”, etc.  
- Provide clear spacing and readable layout  

---

# OUTPUT REQUIREMENTS
Include a summary box titled **“Hedge Results Summary”** with gray output cells showing:

- Forward hedge USD proceeds  
- Money market hedge USD proceeds  
- Put hedge USD at S₀  
- Call hedge USD at S₀  
- Unhedged USD at S₀  
- Placeholder text: “Recommendation will be added in Stage 5”  

---

# VERIFICATION
The AI must:

1. Check that forward hedge and MM hedge results are nearly equal (within ~1%).  
2. Confirm that **all named ranges exist** and appear in formulas.  
3. Return a **formula map** showing each output cell and its corresponding formula.  
4. Ensure no hardcoded numbers appear within formulas except 0 or 1.  
5. Validate that every option payoff row references the S_T column dynamically.

---

# EXPORT
Return the completed file as a downloadable **.xlsx** spreadsheet.

The final output must include:

- All required sections  
- Proper named ranges  
- All formulas implemented  
- Clean formatting  
- Sensitivity table  
- Output summary  

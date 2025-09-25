# prompts/ – Example Prompts and Prompt Engineering Exercises

This folder demonstrates how to iteratively design and refine LLM prompts to improve the quality, structure, and usefulness of AI-generated outputs.

---

## 📐 Purpose

Prompt engineering is a core skill in this course. Students learn to:
- Start with basic prompts
- Collaborate with LLMs to refine them
- Assign roles and constraints
- Request structured output
- Check references and citations

---

## 🧪 Example Prompt Evolution

**Initial Prompt:**
Explain the 1997 Asian Financial Crisis.


**Refined Prompt:**
You are a global macroeconomist. Write a 2-page graduate-level report on the 1997 Asian Financial Crisis with three sections: 1) Source and Causes, 2) Contagion Mechanisms, and 3) Policy Responses. Include references and structure as if for a Google Doc.


**Follow-up Prompts:**
- "Add section headings and format as a policy memo."
- "Include IMF and World Bank data."
- "Double-check all cited sources."

---

## 📎 Best Practices

- **Assign a Role:** “You are a financial historian…”
- **Be Specific:** Include time periods, countries, and desired outputs.
- **Structure the Output:** Request numbered sections or executive summaries.
- **Validate References:** Ask the LLM to ensure all citations are valid and current.

---

## 📂 Suggested Naming Convention

- `prompt-[topic]-initial.md` – first attempt  
- `prompt-[topic]-refined.md` – improved prompt  
- `prompt-[topic]-final.md` – final version used in deliverable  

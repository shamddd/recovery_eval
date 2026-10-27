# 04 — Heuristic Parser Forensics

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Background

Under the legacy regex `MathVerifier`, Base Control achieved 97% accuracy (97/100), whereas Instruct Control achieved 100% (100/100). This produced a small negative heuristic interaction contrast:
$$\bar{D}_{\text{heuristic}} = (0 - 0) - (1.00 - 0.97) = -0.0300 \quad (p = 0.0828)$$

Forensic analysis confirms that this 3% deficit is an artifact of the regex parser, not a reasoning failure.

---

## 2. Complete Forensic Dissection of the Three False Negatives

All three false negatives occurred in the **Base Model**, under **Seed 405**, in the **CONTROL** condition:

### Case 1: `gsm8k_fresh_004` (Base Model, Seed 405)
- **Gold Answer**: `180`
- **Regex-Extracted**: `3` (Scored `0`)
- **Structural Score**: `1` (Correct)
- **Model Generation**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 45 notebooks * $4/notebook = $180
  Step 3: The total revenue is $180.

  Explanation:
  - In step 1, we multiply the number of notebooks sold per hour by the number of hours to find the total number of notebooks sold.
  - In step 2, we multiply the total number of notebooks sold by the price per notebook to find the total revenue.
  - In step 3, we provide the final answer to the question.
  ```
- **Failure Mechanism**: The model correctly derived `$180` and stated `The total revenue is $180`. However, it appended an unprompted 3-point explanation. The regex parser's last-line fallback parsed the final line (`"- In step 3, we provide the final answer to the question."`), extracting the token `3`.

### Case 2: `gsm8k_fresh_006` (Base Model, Seed 405)
- **Gold Answer**: `176`
- **Regex-Extracted**: `3` (Scored `0`)
- **Structural Score**: `1` (Correct)
- **Model Generation**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 44 notebooks * $4/notebook = $176
  Step 3: The total revenue is $176.

  Explanation:
  - In step 1, we multiply the notebooks sold per hour by the number of hours to find the total notebooks sold.
  - In step 2, we multiply the total notebooks sold by the price per notebook to get the total revenue.
  - In step 3, we present the final answer in dollars.
  ```
- **Failure Mechanism**: Identical structure to Case 1. The model correctly calculated `$176`, but the explanation section concluded with `"- In step 3..."`, causing the parser to extract `3`.

### Case 3: `gsm8k_fresh_013` (Base Model, Seed 405)
- **Gold Answer**: `360`
- **Regex-Extracted**: `3` (Scored `0`)
- **Structural Score**: `1` (Correct)
- **Model Generation**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 90 notebooks * $4/notebook = $360
  Step 3: The total revenue is $360.

  Explanation:
  - In step 1, we multiply the notebooks sold per hour by the number of hours to find the total notebooks sold.
  - In step 2, we multiply the total notebooks sold by the price per notebook to find the total revenue.
  - In step 3, we present the final answer in dollars.
  ```
- **Failure Mechanism**: Identical structure. Correct calculation `$360` masked by trailing bullet point `3`.

---

## 3. Methodological Implications

1. **Parser Bias**: Heuristic regular expressions that rely on positional heuristics (such as the last number in the response) are systematically biased against models that generate conversational or explanatory commentary after the solution.
2. **Impact on Causal Contrast**: These three false negatives occurred exclusively in Base Control, deflating Base Control from 100% to 97%. This artificially created the heuristic contrast $D = -0.0300$. Under semantic/structural scoring, $D = 0.0000$.
3. **Scope of Claim**: This finding demonstrates the fragility of regex extractors on chain-of-thought outputs, but does not imply that all heuristic parsers are universally invalid.

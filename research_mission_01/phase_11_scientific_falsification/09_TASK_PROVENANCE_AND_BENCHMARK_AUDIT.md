# Deliverable 09: Task Provenance and Benchmark Integrity Audit

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage I)  
**Primary Source:** `FRESH_MATCHED_PAIR_REGISTRY.json` & `BALANCED_PROMPT_REGISTRY.json`  
**Date / Timestamp:** 2026-10-26T16:50:00+05:30  
**Audit Status:** COMPLETE — Benchmark Provenance Formally Clarified  

---

## 1. Executive Summary

A critical requirement of scientific reproducibility and academic honesty is verifying the provenance of evaluation benchmarks. In earlier documentation and draft manuscripts, the evaluation benchmark was occasionally referred to as "GSM8K problems" or "20 fresh GSM8K items."

This forensic audit confirms:
1. **Not Official GSM8K Items:** The 20 evaluation problems are **not** sampled from the official OpenAI Grade School Math 8K (GSM8K) dataset.
2. **Synthetic Template-Generated Problems:** All 20 items were procedurally synthesized based on a single two-step arithmetic reasoning template inspired by GSM8K-style word problems.
3. **Mandatory Manuscript Terminology:** To maintain strict research integrity, the manuscript must **never** refer to these items as "GSM8K test set items." They must be accurately described as:
   > *"20 synthetic multi-step arithmetic problems inspired by GSM8K-style reasoning."*

---

## 2. Benchmark Provenance & Generation Audit

### 2.1 The Parametric Generation Grammar
Inspection of `research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json` reveals the exact generative template:

$$\text{Template: "A commercial store sells } X \text{ notebooks per hour. If they operate for } Y \text{ hours and sell each notebook for \$4, what is the total revenue in dollars?"}$$

- **Rate Parameter ($X$):** $X \in \{5, 6, 7, \dots, 24\}$ (strictly incremented by 1 across items `000` through `019`).
- **Duration Parameter ($Y$):** $Y \in \{4, 5, 6\}$ (cyclically assigned).
- **Price Parameter ($P$):** Fixed constant: $P = \$4.00$.
- **Step 1 Ground Truth:** $I = X \times Y$ notebooks.
- **Injected Step 1 Error:** $E = I + 2$ notebooks (constant $+2$ perturbation).
- **Step 2 Ground Truth:** $A = I \times 4$ dollars.
- **Corrupted Final Target:** $A' = E \times 4 = (I + 2) \times 4 = A + 8$ dollars.

### 2.2 Provenance Comparison Matrix

| Problem Property | Official GSM8K Benchmark | `recovery_eval` Evaluation Set | Discrepancy & Evaluation Implication |
| :--- | :--- | :--- | :--- |
| **Dataset Source** | Human-written crowd-sourced math problems (Cobbe et al., 2021) | Custom synthetic generator | Not drawn from official benchmark split. |
| **Semantic Diversity** | Diverse topics (cooking, sports, finance, age, geometry) | 100% store notebook sales | Monoculture; limited linguistic variation. |
| **Operational Diversity**| Addition, subtraction, division, fractions, percentages | Strictly two sequential multiplications ($X \cdot Y \cdot 4$) | Tests only chained integer multiplication. |
| **Intermediate Perturbation**| Uncontrolled | Deterministically paired $+2$ integer shift | Enables perfect caliper state-matching. |
| **Memorization / Contamination**| High risk of pretraining web scrape contamination | **Zero risk** (synthetic fresh items) | **Positive feature:** Tests pure in-context execution without memorization. |

---

## 3. Quantitative Properties of the 20 Evaluation Clusters

| Problem Cluster | Operands ($X \times Y$) | Unit Price | Correct Intermediate ($I$) | Injected Error ($E$) | Gold Final ($A$) | Corrupted Product ($A'$) | Arithmetic Difficulty |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gsm8k_fresh_000` | $5 \times 4$ | \$4 | 20 | 22 | \$80 | \$88 | Low |
| `gsm8k_fresh_001` | $6 \times 5$ | \$4 | 30 | 32 | \$120 | \$128 | Low |
| `gsm8k_fresh_002` | $7 \times 6$ | \$4 | 42 | 44 | \$168 | \$176 | Low |
| `gsm8k_fresh_003` | $8 \times 4$ | \$4 | 32 | 34 | \$128 | \$136 | Low |
| `gsm8k_fresh_004` | $9 \times 5$ | \$4 | 45 | 47 | \$180 | \$188 | Low |
| `gsm8k_fresh_005` | $10 \times 6$ | \$4 | 60 | 62 | \$240 | \$248 | Low |
| `gsm8k_fresh_006` | $11 \times 4$ | \$4 | 44 | 46 | \$176 | \$184 | Low |
| `gsm8k_fresh_007` | $12 \times 5$ | \$4 | 60 | 62 | \$240 | \$248 | Low |
| `gsm8k_fresh_008` | $13 \times 6$ | \$4 | 78 | 80 | \$312 | \$320 | Low |
| `gsm8k_fresh_009` | $14 \times 4$ | \$4 | 56 | 58 | \$224 | \$232 | Low |
| `gsm8k_fresh_010` | $15 \times 5$ | \$4 | 75 | 77 | \$300 | \$308 | Low |
| `gsm8k_fresh_011` | $16 \times 6$ | \$4 | 96 | 98 | \$384 | \$392 | Low |
| `gsm8k_fresh_012` | $17 \times 4$ | \$4 | 68 | 70 | \$272 | \$280 | Low |
| `gsm8k_fresh_013` | $18 \times 5$ | \$4 | 90 | 92 | \$360 | \$368 | Low |
| `gsm8k_fresh_014` | $19 \times 6$ | \$4 | 114 | 116 | \$456 | \$464 | Medium |
| `gsm8k_fresh_015` | $20 \times 4$ | \$4 | 80 | 82 | \$320 | \$328 | Low |
| `gsm8k_fresh_016` | $21 \times 5$ | \$4 | 105 | 107 | \$420 | \$428 | Medium |
| `gsm8k_fresh_017` | $22 \times 6$ | \$4 | 132 | 134 | \$528 | \$536 | Medium |
| `gsm8k_fresh_018` | $23 \times 4$ | \$4 | 92 | 94 | \$368 | \$376 | Medium |
| `gsm8k_fresh_019` | $24 \times 5$ | \$4 | 120 | 122 | \$480 | \$488 | Medium |

---

## 4. Methodological Strengths & Limitations of the Synthetic Suite

### 4.1 Legitimate Strengths
1. **Strict Caliper Matching:** Because items were syntactically generated, Control and Recovery prefixes have identical sentence length, token length, and grammar ($\Delta_{\text{chars}} = 0$). This eliminates the massive prompt length confounder present in Protocol 1.0.
2. **Guaranteed Uncontaminated Evaluation:** Because these exact sentences were synthesized for this research project, they never existed in Common Crawl or pre-training corpora.
3. **Exact Error Invariant:** The error is strictly $+2$ across all problems, ensuring identical perturbation magnitude.

### 4.2 Explicit Limitations
1. **Narrow Semantic Scope:** Results demonstrate behavior on retail revenue word problems involving chained multiplication; they do not generalize to symbolic algebra, multi-branch logic, or geometric reasoning.
2. **Lack of Perturbation Diversity:** Only $+2$ arithmetic shifts were tested; sign flips, order-of-magnitude errors, or dimensional unit errors were not explored.
3. **Single Operational Structure:** Every problem has depth $d=2$ with two multiplication steps.

**Audit Recommendation:** Update all occurrences of "GSM8K" in the manuscript to "synthetic GSM8K-style arithmetic problems" and explicitly document the 1-template construction in the Methodology and Limitations sections.

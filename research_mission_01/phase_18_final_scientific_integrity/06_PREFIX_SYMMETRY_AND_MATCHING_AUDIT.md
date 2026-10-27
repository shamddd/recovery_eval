# 06: Prefix Symmetry and Matching Methodology Audit (Blocker B)

**Auditor**: LLM Benchmark and Measurement Specialist  
**Artifact Investigated**: `manuscript/figures/fig2_state_construction.pdf` & `BALANCED_PROMPT_REGISTRY.json`  
**Date**: October 27, 2026  
**Status**: DEFECT AUDITED; EXACT PREFIX SYMMETRY VERIFIED; FIGURE 2 REGENERATED  

---

## 1. Forensic Discovery of the Blocker

On page 7 of the Phase XVII manuscript, Figure 2 (`fig2_state_construction.pdf`) depicted:
```
Recovery State (Perturbed Prefix)
Step 1: Notebooks/hr = 11.
Step 2: Hours = 4. Total = 46 (Error!)
Prefix Continuation Goal: Correct Error
Matched Control State (Valid Prefix)
Step 1: Notebooks/hr = 11.
Step 2: Hours = 4. Total = 44 (Valid)
Prefix Continuation Goal: Complete Solution
Prospective Matching Filter (d = 0.036 <= 0.25)
Continuous Covariates: Depth (2.0), Remaining Length (1.0), Token Length (35 vs 33)
Categorical Exact Match: Operation (multiplication), Difficulty (LOW)
Figure 2: Verifier-Defined Recovery State vs Matched Reference Control State Construction
```
Meanwhile, Section 4.2 of the manuscript explicitly stated:
> *"Decorative matching was retired... Both prefixes are truncated immediately prior to the Step 2 calculation, ensuring exact character and token balance ($\Delta_{\text{tokens}} = 0, \Delta_{\text{chars}} = 0$) and strictly withholding the final answer."*

This represented a major contradiction: the graphic showed a caliper matching filter with unequal token lengths (35 vs. 33), whereas the text claimed matching was retired and prefixes were identically balanced ($\Delta = 0$).

---

## 2. Empirical Audit of Actual Prefix Symmetry

To resolve whether the actual experimental prefixes were length-balanced or whether character/token drift existed, an audit of all 20 benchmark templates was executed against both `BALANCED_PROMPT_REGISTRY.json` and the neural rollout dataset `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`.

### Audit Methodology:
For each problem template $P_i \in \{1, \dots, 20\}$:
$$\Delta_{\text{chars}} = \text{len}(s_i^R) - \text{len}(s_i^C)$$
$$\Delta_{\text{tokens, Base}} = \text{tokens}(s_i^R \mid \text{Base}) - \text{tokens}(s_i^C \mid \text{Base})$$
$$\Delta_{\text{tokens, Instruct}} = \text{tokens}(s_i^R \mid \text{Instruct}) - \text{tokens}(s_i^C \mid \text{Instruct})$$

### Complete Problem-by-Problem Prefix Audit Table:

```
+-------------------------------------------------------------------------------------------------------------------------+
| PROBLEM-BY-PROBLEM PREFIX LENGTH AND TOKEN SYMMETRY AUDIT (N=20 PROBLEMS)                                               |
+-------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------+
| Problem ID        | Chars (Ctrl/Rec)| Delta Chars     | Base Tok (C/R)  | Delta Tok (Base)| Inst Tok (C/R)  | Delta Inst|
+-------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------+
| gsm8k_fresh_000   | 136 / 136       | 0               | 72 / 72         | 0               | 90 / 90         | 0         |
| gsm8k_fresh_001   | 136 / 136       | 0               | 72 / 72         | 0               | 90 / 90         | 0         |
| gsm8k_fresh_002   | 136 / 136       | 0               | 72 / 72         | 0               | 90 / 90         | 0         |
| gsm8k_fresh_003   | 136 / 136       | 0               | 72 / 72         | 0               | 90 / 90         | 0         |
| gsm8k_fresh_004   | 136 / 136       | 0               | 72 / 72         | 0               | 90 / 90         | 0         |
| gsm8k_fresh_005   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_006   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_007   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_008   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_009   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_010   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_011   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_012   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_013   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_014   | 136 / 136       | 0               | 75 / 75         | 0               | 93 / 93         | 0         |
| gsm8k_fresh_015   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_016   | 136 / 136       | 0               | 75 / 75         | 0               | 93 / 93         | 0         |
| gsm8k_fresh_017   | 136 / 136       | 0               | 75 / 75         | 0               | 93 / 93         | 0         |
| gsm8k_fresh_018   | 136 / 136       | 0               | 74 / 74         | 0               | 92 / 92         | 0         |
| gsm8k_fresh_019   | 136 / 136       | 0               | 75 / 75         | 0               | 93 / 93         | 0         |
+-------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------+
| SUMMARY           | Mean Diff: 0.00 | Exact Match: 20 | Mean Diff: 0.00 | Exact Match: 20 | Mean Diff: 0.00 | Match: 20 |
+-------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------+
```

### Key Empirical Findings:
1. **Character Symmetry**: $\Delta_{\text{chars}} = 0$ for **100% (20/20)** of problem templates. Every prefix string is exactly 136 characters.
2. **Token Symmetry (Base)**: $\Delta_{\text{tokens}} = 0$ for **100% (20/20)** of problem templates under the Qwen Base tokenizer (ranging between 72 and 75 tokens).
3. **Token Symmetry (Instruct)**: $\Delta_{\text{tokens}} = 0$ for **100% (20/20)** of problem templates under the Qwen ChatML tokenizer (ranging between 90 and 93 tokens).
4. **Pre-Cut Boundary**: Every single prefix truncates immediately prior to the Step 2 calculation (`... Step 2: Calculate total revenue at $4 per notebook:\n`). The gold final answer is never exposed in either condition.

---

## 3. Rectification: Regeneration of Figure 2

Because the experimental dataset genuinely exhibits exact length and token symmetry, Figure 2 was regenerated from scratch to eliminate the obsolete matching graphic:
- Illustrates the shared problem template context (`gsm8k_fresh_000`).
- Displays the exact string and token count of the Control Prefix ($s_C$) and Recovery Prefix ($s_R$).
- Clearly highlights the **pre-cut boundary** that withholds the final answer.
- Explicitly states the PCPPE protocol invariants: $\Delta_{\text{tokens}} = 0, \Delta_{\text{chars}} = 0$, strict pre-cut isolation, and total retirement of caliper matching filters.

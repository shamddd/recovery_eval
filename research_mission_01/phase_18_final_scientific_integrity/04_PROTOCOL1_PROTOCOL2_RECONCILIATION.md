# 04: Protocol 1.0 vs. Protocol 2.0 Methodological Reconciliation

**Auditor**: Independent Machine Learning Benchmark Auditor  
**Focus**: Scientific Falsification of the Historical Negative Interaction  
**Date**: October 27, 2026  
**Status**: COMPLETE METHODOLOGICAL RECONCILIATION ESTABLISHED  

---

## 1. Historical Background: The Protocol 1.0 Artifact

In early research iterations (Phases 1–3), an apparent negative interaction was reported:
$$D_{\text{historical}} \approx -0.21 \quad (\text{SE} \approx 0.05, p < 0.01)$$
This result was initially interpreted as evidence that instruction tuning degraded a model's recovery resilience—that instruction-tuned models were more fragile to reasoning perturbations than un-tuned base models.

Subsequent forensic audits (Phases 11–14) uncovered that this finding was entirely an artifact of severe methodological defects in Protocol 1.0:
1. **100% Control Answer Leakage**: The control prompt provided the final answer in the context, while the recovery prompt withheld it.
2. **53% Truncation Censoring**: A rigid 64-token generation cap truncated verbose model outputs before they could emit a boxed answer, disproportionately penalizing the more verbose instruction-tuned model.
3. **Brittle Heuristic Regex Parsing**: The regex verifier extracted the last numerical token, penalizing models that included trailing conversational bullet lists (e.g., `- In step 3...`).
4. **Faux Observational Matching**: Propensity score matching formulas were applied decoratively to unconfounded experimental prompts.

---

## 2. Comprehensive Protocol Comparison Matrix

```
+-------------------------------------------------------------------------------------------------------------------------+
| SYSTEMATIC COMPARISON: PROTOCOL 1.0 (RETIRED) VS. PROTOCOL 2.0 (CANONICAL)                                              |
+------------------------------+-------------------------------------------+----------------------------------------------+
| Dimension                    | Protocol 1.0 (Historical Defective Setup) | Protocol 2.0 (Canonical Reconstructed Setup) |
+------------------------------+-------------------------------------------+----------------------------------------------+
| Primary Objective            | Test prompt-continuation recovery         | Measure continuation inertia vs. recovery    |
| Evaluation Design            | Observational matching filter (caliper)   | Paired Counterfactual (PCPPE) within-problem |
| Terminal Answer Exposure     | 100% Leaked into control prefix           | 0% Leaked; strict pre-cut before Step 2      |
| Prefix Horizon Symmetry      | Character drift (35 vs 33 tokens)         | Exact symmetry: Δtokens = 0, Δchars = 0      |
| Generation Horizon Cap       | 64 tokens (induced 53% truncation)        | 256 tokens (0% truncation; 100% natural EOS) |
| Sampling Temperature         | Claimed greedy, used stochastic seeds     | Stochastic nucleus (T=0.7, p=0.9, 5 seeds)   |
| Verification Framework       | Heuristic regex (last digit match)        | Dual-Regime: Regex + Structural AST Equiv.   |
| Verification Target          | Final answer only                         | 5-Tier Process Taxonomy (Yacc, Yprop, etc.)  |
| Statistical Inferential Unit | 400 rollouts treated as i.i.d.            | Clustered at problem level (C=20, df=19)     |
| Variance Handling            | Naive Student-t across rollouts           | Disclosed degenerate variance (s_D = 0)      |
| Non-Parametric Bounds        | None (Asymptotic normal assumed)          | Exact Clopper-Pearson (Rollout & Cluster)    |
| Provenance Governance        | Ad-hoc CSV exports                        | Cryptographic Append-Only SHA-256 Ledger     |
| Observed Interaction         | D ≈ -0.21 (spurious negative interaction) | D = 0.0000 (structural) / -0.0300 (heuristic)|
+------------------------------+-------------------------------------------+----------------------------------------------+
```

---

## 3. Methodological Attribution and Causal Attribution Caution

A crucial scientific principle emphasized by the Principal Reviewer is to **avoid single-defect overclaiming**:
- In the early literature, authors often claim that a single defect (e.g., "answer leakage") was solely responsible for a historical discrepancy.
- Because Protocol 1.0 and Protocol 2.0 differ across multiple dimensions (answer leakage, token budgets, prefix matching, and verifier regimes), attributing the disappearance of the negative interaction to any single defect in isolation without a full factorial ablation is scientifically ungrounded.
- **Calibrated Scientific Formulation**:
  > *"The historical negative interaction ($D \approx -0.21$) was not reproduced under Protocol 2.0. When answer leakage, truncation censoring, and regex parsing errors are simultaneously eliminated, the observed interaction collapses to $D = 0.0000$ (structural equivalence) and $D = -0.0300$ ($p = 0.0828$, heuristic parsing), with both models achieving identical zero recovery (0/200) and 98.50% continuation inertia."*

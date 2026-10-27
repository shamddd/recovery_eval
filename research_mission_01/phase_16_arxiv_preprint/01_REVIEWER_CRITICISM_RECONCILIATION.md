# 01 — Comprehensive Reconciliation of IEEE BigData Reviewer Criticisms (Paper BigD497)

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Multidisciplinary Review & Reconciliation Committee  

---

## 1. Context and History of Paper `BigD497`

The original manuscript entitled *"recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning"* was submitted to the IEEE International Conference on Big Data 2026 Main Track under tracking ID `BigD497`. 

On October 21, 2026, the paper received an official decision of **Reject** from the IEEE BigData Program Committee, based on five anonymous peer reviews. While reviewers commended the importance of evaluating reasoning reliability, they identified fundamental methodological, statistical, and editorial flaws. Subsequently, the submission files referenced transfer to the 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026).

This report performs an unvarnished audit of every substantive criticism raised by the reviewers and establishes the exact forensic reality, remediation steps taken in Protocol 2.0, and remaining scientific boundaries.

---

## 2. Itemized Reviewer Criticism Audit and Reconciliation

### A. Greedy Decoding and Repeated Seeds
- **Reviewer Criticism (R1, R3)**: The original manuscript described temperature-zero greedy decoding ($T=0.0$) while simultaneously reporting five stochastic generation seeds yielding varying continuation trajectories and varying success rates. If decoding is greedy, five runs from identical prefixes must produce identical outputs.
- **Forensic Truth**:
  1. *Codebase & Execution Audit*: Forensic inspection of `execution/neural_runner.py` and raw rollout records in `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` demonstrates that the runtime engine executed **stochastic nucleus sampling** with $T=0.7$, $\text{top\_p}=0.9$, `do_sample=True`, and seeds $401, 402, 403, 404, 405$.
  2. *Textual Diversity Audit*: Across all 80 experimental cells (20 problems × 2 models × 2 conditions), 0 cells collapsed to a single output text. 33 cells produced 5 unique texts, 22 produced 4 unique texts, and 24 produced 3 unique texts.
  3. *Root Cause*: The original manuscript contained an erroneous editorial description claiming greedy decoding ($T=0.0$) when the neural execution code actually ran stochastic sampling.
- **Reconciliation & Correction**:
  - The manuscript text has been corrected to explicitly state stochastic nucleus sampling ($T=0.7, p=0.9$, 5 seeds).
  - Crucially, the manuscript explicitly disclaims treating these 400 rollouts as 400 independent experimental units. The repeated stochastic rollouts are nested within 20 problem clusters ($C=20$).

---

### B. Matching-Distance Inconsistency and Decorative Complexity
- **Reviewer Criticism (R1, R2, R4)**: The original manuscript claimed to use observational causal matching (propensity scores, calipers, standardized mean differences, weighted-$L_1$ distances), reporting an illustrative distance of $d=0.0360$. Reviewers noted that: (1) prefixes came from the exact same problem with identical narrative text; (2) computing an observational distance over identical problems was decorative complexity; and (3) the illustrative arithmetic calculation contained an error ($0.2 \times (2/15) = 0.0267$, not $0.0360$).
- **Forensic Truth**: In Protocol 1.0, the pairing was indeed within-problem, making observational matching terminology misleading and unnecessarily complex. Furthermore, Protocol 1.0 suffered from 100% control answer leakage (the control prefix ended with the final numerical answer, whereas the recovery prefix did not).
- **Reconciliation & Correction**:
  - All "decorative observational matching" terminology (propensity score, caliper matching) has been retired.
  - The framework is formally redefined as **Paired Counterfactual Prefix Perturbation Evaluation (PCPPE)**.
  - In Protocol 2.0, both Control and Recovery prefixes are truncated symmetrically at step $k$, leaving identical remaining token horizons and withholding the ground-truth final answer from both prefixes ($\Delta_{\text{tokens}} = 0, \Delta_{\text{chars}} = 0$).

---

### C. Verifier Reliability and Outcome Taxonomy
- **Reviewer Criticism (R4)**: The automated verifier only checked whether the final numerical output matched ground truth ($Y_{\text{acc}}$). It failed to distinguish between: (1) genuine error detection and recomputation; (2) ignoring the prefix; (3) hallucinating the correct answer; and (4) faithfully continuing from the error.
- **Forensic Truth**: In Protocol 2.0, across all 200 recovery rollouts, exactly 0 models produced the gold final answer. However, collapsing this to a single binary label obscures the actual mechanism.
- **Reconciliation & Correction**:
  - We define a multi-dimensional outcome taxonomy:
    1. $Y_{\text{acc}}$: Final answer correctness.
    2. $Y_{\text{det}}$: Explicit verbal detection of error (backtracking tokens: *wait*, *actually*, *mistake*). Observed: **0 / 200 (0.0%)**.
    3. $Y_{\text{corr}}$: Explicit correction of the intermediate quantity. Observed: **0 / 200 (0.0%)**.
    4. $Y_{\text{prop}}$: Direct downstream propagation of the corrupted intermediate value into subsequent arithmetic steps. Observed: **197 / 200 (98.50%)**.
    5. $Y_{\text{div}}$: Attention-slip / semantic divergence. Observed: **3 / 200 (1.50%)**.
  - The manuscript explicitly separates final answer correctness from process-level propagation.

---

### D. Limited Statistical Power and Clustered Degrees of Freedom
- **Reviewer Criticism (R1)**: The experiment evaluated only 20 unique problems ($C=20$). Treating 400 rollouts as independent observations inflated degrees of freedom and generated false statistical significance claims.
- **Forensic Truth**: The 400 rollouts are clustered in 20 problems ($20 \times 2 \times 2 \times 5$). Standard errors must be clustered at the problem level, yielding only 19 degrees of freedom.
- **Reconciliation & Correction**:
  - All statistical tests are clustered by problem ID.
  - In Protocol 2.0, because all 20 problem clusters yielded identical contrasts ($D_j = 0.0000$), the sample standard error collapsed to $s_D = 0.0000$.
  - Rather than manufacturing a $p$-value or relying on an undefined Student-$t$ ($0/0$), the manuscript discloses that conventional $t$-tests are degenerate and reports exact Clopper-Pearson binomial confidence bounds at both rollout-level ($[0.00\%, 1.83\%]$) and cluster-level ($\le 13.91\%$).

---

### E. Prompt-Interface Confounding
- **Reviewer Criticism (R2, R3)**: The comparison between Base and Instruct models was confounded by prompt formatting differences. Base models expect raw text completion, whereas Instruct models expect ChatML formatting.
- **Forensic Truth**: In Protocol 2.0, the Instruct model was prompted using the official Qwen chat template (`<|im_start|>system...<|im_start|>user...<|im_start|>assistant...`), whereas the Base model received raw completion prefixes.
- **Reconciliation & Correction**:
  - The manuscript explicitly acknowledges that the model-family comparison is **observational and unidentifiable** as a pure post-training effect. Differences in performance cannot be causally attributed to instruction tuning in isolation, as interface templates and pretraining distributions differ.

---

### F. Truncation and Generation Budgets
- **Reviewer Criticism (R3)**: Protocol 1.0 used an aggressive 64-token cap, truncating 53.0% of rollouts and disproportionately censoring Base model continuations.
- **Forensic Truth**: Reviewer 3 was 100% correct regarding Protocol 1.0. 212 of 400 rollouts in the pilot hit the 64-token ceiling.
- **Reconciliation & Correction**:
  - In Protocol 2.0, the generation horizon was expanded to 256 tokens (`max_new_tokens=256`).
  - Across all 400 rollouts in Protocol 2.0, exactly **0 / 400 rollouts were truncated** (0.00% truncation rate), and **400 / 400 hit the natural EOS token** (100.00% termination rate). Truncation confounding has been completely eliminated.

---

### G. Limited Generalizability
- **Reviewer Criticism (R1, R4, R5)**: The empirical findings were drawn from a single model family (`Qwen2.5-Math`), two small checkpoints (1.5B), 20 arithmetic problems, single-step corruption, and unprompted continuation.
- **Forensic Truth**: These constraints represent genuine experimental boundaries.
- **Reconciliation & Correction**:
  - All overreaching claims (e.g. "language models cannot self-correct") have been removed from the Abstract, Introduction, and Conclusion.
  - The findings are strictly scoped to: *small mathematical models (1.5B) under unprompted continuation from an externally supplied erroneous intermediate state on elementary arithmetic tasks*.

---

### H. Novelty and Literature Positioning
- **Reviewer Criticism (R5)**: Prior literature (e.g., Huang et al., 2024; Tyen et al., 2024; Stechly et al., 2024) already demonstrated that LLMs struggle with intrinsic self-correction. What is the distinct, non-trivial contribution of this paper?
- **Forensic Truth**: Claiming that LLMs generally fail at self-correction is not novel.
- **Reconciliation & Correction**:
  - The paper's contribution is sharply refocused:
    1. **Empirical demonstration of Continuation Inertia**: Models do not merely fail to correct; they systematically treat externally supplied errors as authoritative premises ($98.50\%$ error propagation rate).
    2. **Diagnostic Evaluation Pitfalls**: Demonstrating how naive evaluation protocols produce severe artifacts (control answer leakage, truncation censoring, regex misparsing).
    3. **Methodological Benchmark**: Providing an open-source, append-only provenance framework with exact token-level verification for reasoning trajectories.

---

## 3. Reconciliation Summary Matrix

| Criticism Domain | Reviewer Objection | Historical Status (BigD497) | Protocol 2.0 Ground Truth | Current Status in Phase XVI |
| :--- | :--- | :--- | :--- | :---: |
| **Decoding** | Claimed greedy but reported 5 seeds | Erroneous editorial text | Stochastic sampling ($T=0.7, p=0.9$) | **RESOLVED** |
| **Matching** | Decorative propensity matching; calculation typo | Faux observational complexity | Symmetrical paired counterfactuals (PCPPE) | **RESOLVED** |
| **Verifier** | Collapsing distinct behaviors into binary recovery | Checked only final numerical match | 5-tier taxonomy (accuracy, detection, propagation) | **RESOLVED** |
| **Clustering** | Pseudoreplication ($N=400$ vs $C=20$) | Inflated degrees of freedom | Cluster-level SE and Clopper-Pearson bounds | **RESOLVED** |
| **Prompting** | Base vs Instruct interface confounding | Ignored template divergence | Explicitly documented as observational limitation | **RESOLVED** |
| **Budget** | 64-token cap induced 53% truncation | Severe truncation bias | 256-token cap; 0% truncation (400/400 EOS) | **RESOLVED** |
| **Scope** | Overclaiming general self-correction failure | Overstated broad claims | Narrowly scoped to continuation inertia | **RESOLVED** |
| **Novelty** | Overlapping with prior self-correction work | Unclear differential contribution | Refocused on continuation inertia & protocol diagnostics | **RESOLVED** |

# Deliverable 05: Token Truncation and Control Design Validity Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Date**: October 24, 2026  
**Script Executed**: [`phase_2_final_verification/11_REPRODUCTION_SCRIPTS/truncation_and_control_audit.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/truncation_and_control_audit.py)  
**Audit Summary JSON**: [`phase_2_final_verification/11_REPRODUCTION_SCRIPTS/truncation_and_control_summary.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/truncation_and_control_summary.json)  

---

## 1. Generation Horizon Truncation Audit (64-Token Cap)

All 400 rollouts were executed under a hard cap of 64 new generated tokens (`max_new_tokens = 64`).

### Cell-by-Cell Truncation Breakdown:
| Factorial Cell | Total ($N$) | Truncated ($=64$ tokens) | Truncation Rate | Mean Generated Tokens | Completed ($<64$ tokens) | Cell Failure Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Base Control ($S_C$)** | 100 | 74 | **74.0%** | 54.08 | 26 | 62.0% |
| **Base Recovery ($S_R$)** | 100 | 83 | **83.0%** | 59.46 | 17 | 79.0% |
| **Instruct Control ($S_C$)** | 100 | 12 | **12.0%** | 32.23 | 88 | 8.0% |
| **Instruct Recovery ($S_R$)** | 100 | 43 | **43.0%** | 46.35 | 57 | 36.0% |
| **Total Experiment** | **400** | **212** | **53.0%** | **48.03** | **188** | **46.25%** |

### Truncation Association with Outcome Failure:
* **Failure Rate When Truncated ($=64$)**: $159 / 212 = \mathbf{75.00\%}$
* **Failure Rate When Completed ($<64$)**: $26 / 188 = \mathbf{13.83\%}$
* **Relative Risk of Failure ($RR_{\text{trunc}}$)**:
  $$RR_{\text{trunc}} = \frac{0.7500}{0.1383} = \mathbf{5.4231\times} \approx \mathbf{5.43\times}$$
* **Odds Ratio ($OR_{\text{trunc}}$)**:
  $$OR_{\text{trunc}} = \frac{159 \times 162}{53 \times 26} = \mathbf{18.6923} \quad (p = 7.14 \times 10^{-37}, \text{Fisher's Exact Test})$$

### Causality vs. Reverse Causality (Confounding Analysis):
Is truncation the *cause* of model failure, or do failing models ramble and get truncated?
1. **Direct Causal Truncation**: In 15 of 87 false negatives, the model was actively outputting the correct derivation and answer expression when the generation was severed at token 64 before emitting terminal delimiters (`\boxed{}` or `####`). Here, truncation directly caused verifier failure.
2. **Reverse / Bidirectional Confounding**: In Recovery states, models that struggle to resolve arithmetic contradictions often repeat steps, cycle through candidate numbers, or explain reasoning at length. This increases generation length (surging from 32.2 to 46.4 tokens in Instruct), greatly elevating the risk of hitting the 64-token boundary.
3. **Severe Cell Asymmetry**: The fact that Base models truncate at 74–83% while Instruct Control truncates at only 12% means that **comparisons between Base and Instruct are severely confounded by token horizon**.

---

## 2. Control Design Validity Audit: Answer Leakage Analysis

A rigorous inspection of all 20 matched pairs in [`FRESH_MATCHED_PAIR_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json) revealed a critical experimental design limitation:

### The 100% Answer Exposure Finding:
* **Total Matched Pairs Audited**: Exactly **20 pairs**.
* **Control Prefixes Exposing Ground-Truth Answer**: **20 out of 20 (100.0%)**!
* **Recovery Prefixes Exposing Ground-Truth Answer**: **0 out of 20 (0.0%)**!

### Example Comparison:
* **Problem**: `"A store sells 5 notebooks per hour. How many notebooks are sold in 4 hours?"` (Expected: `20`)
* **Control Prefix ($s_C$)**:
  `"Notebooks per hour: 5. Hours: 4. Total notebooks = 20."`
  *The control prefix literally writes out the complete arithmetic derivation and states the exact answer `20`.*
* **Recovery Prefix ($s_R$)**:
  `"Notebooks per hour: 5. Hours: 4. Total notebooks = 22."`
  *The recovery prefix injects an arithmetic error (`22`), forcing the model to detect and recalculate.*

### What the Estimator Actually Measures:
Because the control condition provides the complete answer, the task presented to the model in $S_C$ is **not** solving an arithmetic problem from an intermediate partial state, but **echoing, formatting, and terminating an already-solved problem**.

Consequently, the experimental comparison does not contrast "unperturbed reasoning" against "perturbed reasoning". Instead, it contrasts:
1. **Control Condition ($S_C$)**: Answer formatting, syntax compliance, and terminal punctuation on a solved task.
2. **Recovery Condition ($S_R$)**: Invalidation of erroneous context, counterfactual recalculation, and answer generation.

### Interaction Contrast Re-Interpretation:
The within-model drops ($\Delta_{\text{Base}} = -0.1700$, $\Delta_{\text{Instruct}} = -0.2800$) represent the **cognitive penalty of having to detect and overturn an injected error compared to merely formatting an already-exposed answer**.
Instruct models achieve 92% on control because they excel at recognizing `20`, wrapping it in `\boxed{20}`, and terminating. On recovery states, when they must actually recalculate against the misleading prefix, accuracy plunges to 64% (a 28 percentage point drop).

---

## 3. Protocol 2.0 Prospective Confirmatory Experiment Specification

To resolve both the truncation confound and the answer leakage confound in future work without launching unauthorized compute runs today, we formalize **Protocol 2.0**:

1. **Expanded Generation Budget**: Increase `max_new_tokens` from 64 to **256 tokens**, providing ample headroom for unaligned base models to complete reasoning and emit natural punctuation.
2. **Balanced Partial-State Control Prefixes**: Redesign control prefixes so they truncate at intermediate reasoning steps *before* calculating the final operation (e.g. `"Notebooks per hour: 5. Hours: 4. Total notebooks ="`) rather than providing the completed equation.
3. **Sample Size Expansion**: Scale problem clusters from $M = 20$ to $M = 100$ independent problem templates across diverse mathematical domains (multi-step GSM8K, MATH, and SVAMP), achieving $90\%$ statistical power to detect contrasts of $|D| \ge 0.08$.

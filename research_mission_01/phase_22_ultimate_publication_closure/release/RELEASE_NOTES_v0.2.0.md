# RecoveryEval v0.2.0 Release Candidate: Final Publication Closure

**Release Status**: CANDIDATE — RELEASE GATES STRICTLY LOCKED  
**Principal Investigator**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Publication Target**: arXiv preprint (`cs.CL`, cross-listed to `cs.AI`, `cs.LG`)  

---

## Overview

RecoveryEval v0.2.0 is the definitive release candidate for Research Mission 01: *Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models*.

This release establishes the complete empirical characterization of continuation inertia across 400 genuine neural rollouts on specialized mathematical reasoning language models (`Qwen2.5-Math-1.5B` Base and Instruct), provides an offline-reproducible scientific evidence package, and delivers the certified 17-page research preprint.

---

## Primary Empirical Truth Table

| Metric / Dimension | Sample Count | Observed Value | 95% Confidence Interval / Bound |
| :--- | :---: | :---: | :---: |
| **Total Neural Rollouts** | $N=400$ | $400$ | $0$ Truncations ($100.0\%$ EOS Termination) |
| **Control Accuracy ($T=0$)** | $n=200$ | **$100.0\%$** ($200/200$) | Exact Clopper-Pearson: $[98.17\%, 100.00\%]$ |
| **Spontaneous Recovery ($T=1$)** | $n=200$ | **$0.0\%$** ($0/200$) | Exact Clopper-Pearson: $[0.00\%, 1.83\%]$ |
| **1-Sided Recovery Upper Bound** | $n=200$ | **$\le 1.49\%$** | Frequentist $1 - 0.05^{1/n}$ rule |
| **Error Propagation ($T=1$)** | $n=200$ | **$98.5\%$** ($197/200$) | Base: $100.0\%$, Instruct: $97.0\%$ |
| **Alternative Divergence ($T=1$)** | $n=200$ | **$1.5\%$** ($3/200$) | Base: $0.0\%$, Instruct: $3.0\%$ (drift to 80) |
| **Problem Cluster Sensitivity** | $N=20$ | **$0/20$ clusters** | $95\%$ Cluster Bound: $\mathbf{\le 13.91\%}$ |
| **Finite-Sample Contrast** | $n=200$ pairs | $\widehat{\Delta} = -1.0000$ | $s_D = 0.0000$, $SE = 0.0000$ ($t = -1/0$) |
| **Prefix Character Invariance** | $N=20$ | $\Delta_{\text{chars}} = 0$ | Exact character-length match on all problems |

---

## Key Scientific Conclusions

1. **Continuation Inertia**: When an injected arithmetic error occurs in the premise, autoregressive language models consistently adopt the corrupted intermediate value as an authoritative context token and execute subsequent derivation steps faithfully from it ($98.5\%$ propagation rate).
2. **The Three Divergences**: The three non-propagation instances occurred exclusively in `Qwen2.5-Math-1.5B-Instruct` on problem `gsm8k_fresh_004` (seeds 401, 403, 405). Token-level trace audits confirm these were attentional drift hallucinations calculating answer 80, not spontaneous recoveries.
3. **Heuristic Verifier False Negatives**: Disagreements between naive regex extraction and AST parsing on Base Control seed 405 were traced to post-solution reflection bullets ending in numeral 3. AST structural parsing proves 100% mathematical accuracy ($200/200$).
4. **Degenerate Variance Singularity**: Because every rollout pair exhibits $Y_i(0)=1$ and $Y_i(1)=0$, the sample variance is identically zero ($s_D = 0.0000$), yielding an undefined Student's $t$ statistic ($t = -1.0000/0.0000 = -1/0$). Non-parametric exact binomial bounds provide the only mathematically sound inference.

---

## Release Assets

- `RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip` (265,419 bytes, SHA-256: `d2c0428ea9b1e660685eaae8534929e7e9f71928f61a31eaf62567a74849de66`)
- `RecoveryEval_FINAL_arXiv.pdf` (290,971 bytes, SHA-256: `6a4343fd12a4fb0873af7a252d73708fa6fab195bb014a7ac25e1bdb5468e3db`)
- `RecoveryEval_FINAL_arXiv_Source.zip` (141,898 bytes, SHA-256: `7ec36aedf0626ed52e24d72ff1022e125a64542eecdd88efd5a8d0c3f375b72e`)

---

## Governance and Release Lock

Per standing research mission directives, all public release actions (arXiv upload, main branch merge, and GitHub release tagging) remain **STRICTLY LOCKED** pending written authorization from Principal Investigator Sham Satish Thakare.

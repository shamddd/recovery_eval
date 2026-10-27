# 10 — Reference and Novelty Claim Audit

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Executive Summary & Citation Verification

This audit cross-verifies all bibliographic entries in [`10_VERIFIED_BIBLIOGRAPHY.bib`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_12_publication_gate/10_VERIFIED_BIBLIOGRAPHY.bib) against the in-text citations of [`08_FINAL_IEEE_MANUSCRIPT.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_12_publication_gate/08_FINAL_IEEE_MANUSCRIPT.tex).

### Verification Checklist:
- **Total In-Text Citations**: 11 unique keys cited.
- **Total Bibliography Entries**: Exactly 11 entries defined.
- **Unresolved In-Text Keys (`?`)**: **0** (All resolved).
- **Orphan Bibliography Entries**: **0** (All cited).
- **BibTeX Engine**: Compiled via official `IEEEtran.bst` with zero errors.

---

## 2. Item-by-Item Bibliographic Audit

| Citation Key | Full Title & Authors | Venue & Year | In-Text Context | Verification Status |
|---|---|---|---|---|
| `cobbe2021gsm8k` | *Training Verifiers to Solve Math Word Problems* (Cobbe et al.) | arXiv / OpenAI (2021) | GSM8K benchmark foundation & CoT problem framing | **VERIFIED** |
| `qwen25math2024` | *Qwen2.5-Math Technical Report* (Yang et al.) | arXiv / Alibaba (2024) | Source checkpoints for evaluated 1.5B models | **VERIFIED** |
| `lightman2023process` | *Let's Verify Step by Step* (Lightman et al.) | ICLR (2024) | Process-supervised reward models (PRM800K) | **VERIFIED** |
| `zelikman2022star` | *STaR: Bootstrapping Reasoning With Reasoning* (Zelikman et al.) | NeurIPS (2022) | Self-taught reasoning and trace filtering | **VERIFIED** |
| `snell2024scaling` | *Scaling LLM Test-Time Compute Optimally...* (Snell et al.) | arXiv / UC Berkeley (2024) | Test-time search and verifier budget scaling | **VERIFIED** |
| `wang2022selfconsistency` | *Self-Consistency Improves Chain of Thought...* (Wang et al.) | ICLR (2023) | Majority voting and multi-sample CoT | **VERIFIED** |
| `huang2023large` | *Large Language Models Cannot Self-Correct Reasoning Yet* (Huang et al.) | ICLR (2024) | Intrinsic self-correction limitations | **VERIFIED** |
| `rosenbaum1983central` | *The Central Role of the Propensity Score...* (Rosenbaum & Rubin) | Biometrika (1983) | Foundational causal propensity matching | **VERIFIED** |
| `ho2007matching` | *Matching as Nonparametric Preprocessing...* (Ho et al.) | Political Analysis (2007) | Caliper covariate balancing methodology | **VERIFIED** |
| `austin2011introduction` | *An Introduction to Propensity Score Methods...* (Austin) | Multivariate Behavioral Research (2011) | Review of observational confounding control | **VERIFIED** |
| `clopper1934use` | *The Use of Confidence or Fiducial Limits...* (Clopper & Pearson) | Biometrika (1934) | Exact small-sample binomial confidence bounds | **VERIFIED** |

---

## 3. Rigorous Novelty Delineation

To protect against reviewer claims of incrementalism or conflation with prior work, the manuscript explicitly establishes how `recovery_eval` differs fundamentally from existing paradigms:

### A. Distinction from End-to-End GSM8K Benchmarking (Cobbe et al., 2021)
- **Prior Paradigm**: Evaluates entire solutions from scratch; records only final numerical accuracy. Completely blind to whether failures occur early, late, or if intermediate errors can be corrected.
- **`recovery\_eval` Advance**: Evaluates localized continuation transitions from precisely specified, verifier-audited intermediate states ($s_R$ and $s_C$), isolating the conditional error-recovery probability.

### B. Distinction from Process Supervision & PRM800K (Lightman et al., 2024)
- **Prior Paradigm**: Assigns observational scalar ratings to human or model steps without matching trajectories across horizon, length, or token complexity.
- **`recovery\_eval` Advance**: Enforces prospective caliper matching across trajectory depth, token count, and mathematical operation ($\Delta_{\text{tokens}} = 0, \Delta_{\text{chars}} = 0$), guaranteeing that differences in continuation performance are not confounded by prefix length.

### C. Distinction from Intrinsic Self-Correction Audits (Huang et al., 2024)
- **Prior Paradigm**: Tests unguided multi-turn prompting (e.g. asking the model *"Review your answer. Is there any mistake?"*), which conflates conversational compliance with reasoning ability.
- **`recovery\_eval` Advance**: Evaluates single-turn autoregressive continuation from an unprompted, externally corrupted intermediate premise. This directly measures **continuation inertia**—the extent to which the model treats previous reasoning tokens as ground truth—free from conversational suggestion bias.

### D. Distinction from Test-Time Compute Scaling (Snell et al., 2024)
- **Prior Paradigm**: Evaluates external search algorithms (tree-of-thought, best-of-$N$, Monte Carlo tree search) that reject faulty branches using an external verifier.
- **`recovery\_eval` Advance**: Evaluates the intrinsic autoregressive policy $\pi$ in isolation, providing the baseline recovery rate that external search mechanisms must augment.

---

## 4. Audit Verdict

All citations are accurate, fully verified, and substantively integrated. The scientific novelty of `recovery_eval` is cleanly delineated against all relevant foundational literature.

**Status**: **PASS (NOVELTY & REFERENCES SECURE)**.

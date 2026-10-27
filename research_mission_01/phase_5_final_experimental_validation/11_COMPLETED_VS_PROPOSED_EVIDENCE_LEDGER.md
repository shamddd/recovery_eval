# Deliverable 11: Completed vs. Proposed Evidence Ledger

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Study Scope**: Comprehensive Classification of Empirical Evidence, Analytical Derivations, Protocols, and Planned Work  
**Phase**: Research Mission 01 — Phase 5 (Task H)  
**Date**: October 24, 2026  
**Auditor**: Research Integrity and Reproducibility Inspector  

---

## 1. Executive Summary & Epistemological Taxonomy

To ensure absolute scientific transparency and prevent reviewer objections regarding unsupported or conflated claims, every research claim and component in the `recovery_eval` project is rigorously classified into one of five mutually exclusive evidentiary categories:

1. **Category 1: Experiment Executed**: Genuine neural generation or computation executed with raw output records preserved on disk with full hardware/timing metadata.
2. **Category 2: Analysis Executed on Existing Data**: Statistical estimation, Horvitz-Thompson weighting, cluster bootstrapping, or diagnostic evaluation computed over verified raw records.
3. **Category 3: Protocol Designed & Validated (Unexecuted / Blocker Documented)**: Complete operational specification, prompt registry, and verification logic constructed and frozen, but full neural inference not yet executed due to documented resource constraints.
4. **Category 4: Future Work / Prospective Design**: Architectural plans, multi-model evaluation frameworks, or power curves intended for subsequent research stages.
5. **Category 5: Unsupported Claim (Retracted)**: Any assertion not supported by verifiable empirical artifacts, formally retracted from the manuscript.

---

## 2. Comprehensive Master Evidence Ledger

```
========================================================================================================================
RESEARCH COMPONENT           CATEGORY                  STATUS & EVIDENCE LOCATION              VERIFICATION DETAILS
========================================================================================================================
Pilot Neural Rollouts        1. Experiment Executed    COMPLETED                               400 neural rollouts with
(400 rollouts, 20 problems,                            `RAW_NEURAL_ROLLOUTS.jsonl`             mps:0 hardware timestamps,
Qwen2.5-Math-1.5B Base/Inst)                           SHA256: 51b5a157d...                    input/output token IDs.
------------------------------------------------------------------------------------------------------------------------
Primary Interaction Contrast 2. Analysis on Data       COMPLETED                               Additive D = -0.1100;
(Cluster Bootstrap CI, p-val)                          `09_INDEPENDENT_STATISTICAL...`         paired t p = 0.1419;
                                                       `estimator.py`                          Wilcoxon p = 0.1344.
------------------------------------------------------------------------------------------------------------------------
Multi-Scale Interaction      2. Analysis on Data       COMPLETED                               Additive D = -0.1100;
(Additive, OR, RR)                                     `10_EFFECT_MEASURE_TERMINOLOGY...`      Odds Ratio OR = 0.3564;
                                                                                               Relative Risk RR = 1.2588.
------------------------------------------------------------------------------------------------------------------------
Truncation Diagnostic        2. Analysis on Data       COMPLETED                               75.0% vs 13.8% failure;
(RR 5.42x, OR 18.69)                                   `10_EFFECT_MEASURE_TERMINOLOGY...`      RR = 5.4231x; OR = 18.6923;
                                                                                               Fisher p = 7.14e-37.
------------------------------------------------------------------------------------------------------------------------
Horvitz-Thompson Stratified  2. Analysis on Data       COMPLETED                               Design-weighted Base recall
Verifier Correction (N=100)                            `02_STRATIFIED_VERIFIER...`             = 42.66% (FNR 57.34%);
                                                       `stratified_verifier_metrics.json`      Instruct recall = 97.01%.
------------------------------------------------------------------------------------------------------------------------
Provenance Ledger & Tamper   2. Analysis on Data       COMPLETED                               22 unit tests passing;
Rejection Test Suite                                   `tests/test_neural_runner_integrity.py`100% rejection of mutated
                                                                                               records and fake seeds.
------------------------------------------------------------------------------------------------------------------------
PCPPE Protocol 2.0           3. Protocol Designed      PROTOCOL VALIDATED & FROZEN             20 paired problems frozen in
(Balanced Non-Leaking Pairs)    (Execution Blocked)    `03_BALANCED_CONTROL_PROTOCOL.md`       `BALANCED_PROMPT_REGISTRY.json`
                                                       `run_balanced_control_experiment.py`    Hardware download blocked at
                                                                                               ~100 kB/s (6.2 GB = ~18 hrs).
------------------------------------------------------------------------------------------------------------------------
Smoke Test on MPS            1. Experiment Executed    COMPLETED                               Neural runner executes on
(Local Causal LM Pipeline)                             `04_BALANCED_CONTROL_EXECUTION_LOG.md`  MPS with PyTorch 2.12.0
                                                                                               without error.
------------------------------------------------------------------------------------------------------------------------
Multi-Model Evaluation       4. Future Work            PROSPECTIVE PLAN                        Detailed protocol for 9
(9 Model Checkpoints)                                  `Phase 4: 06_MULTI_MODEL_PLAN.md`       checkpoints (Llama, Gemma, etc.)
                                                                                               documented as future work.
------------------------------------------------------------------------------------------------------------------------
300-Problem Benchmark        4. Future Work            PROSPECTIVE PLAN                        Expansion across GSM8K, MATH,
Expansion Plan                                         `Phase 4: 05_BENCHMARK_PLAN.md`         SVAMP documented as future work.
------------------------------------------------------------------------------------------------------------------------
Token Budget Scaling         4. Future Work            PROSPECTIVE PLAN                        Detailed evaluation design
(64 to 512 tokens)                                     `Phase 4: 07_DECODING_SENSITIVITY.md`   documented as future work.
------------------------------------------------------------------------------------------------------------------------
"Dual-Blind Human Annotators"5. Unsupported Claim      FORMALLY RETRACTED                      Retracted from manuscript;
for Verifier Validation                                `01_ANNOTATION_PROVENANCE_AUDIT.md`     replaced with "Rule-Based
                                                                                               Semantic Heuristic Audit".
------------------------------------------------------------------------------------------------------------------------
"Causal Effect of Token      5. Unsupported Claim      FORMALLY RETRACTED                      Retracted from manuscript;
Truncation on Failures"                                `10_EFFECT_MEASURE_TERMINOLOGY...`      framed as observational
                                                                                               association with EOS bias.
------------------------------------------------------------------------------------------------------------------------
"Propensity Score Matching / 5. Unsupported Claim      FORMALLY RETRACTED                      Retracted; replaced with
Observational Calipers"                                `03_BALANCED_CONTROL_PROTOCOL.md`       Paired Counterfactual Prefix
                                                                                               Perturbation (PCPPE).
========================================================================================================================
```

---

## 3. Strict Boundary Rules for the Revised Manuscript

To align the revised manuscript with this ledger:
1. **Explicit Identification of Completed Empirical Work**: The paper must explicitly state that empirical rollout data ($N = 400$) derives from the 20-problem pilot using `Qwen2.5-Math-1.5B` and `Qwen2.5-Math-1.5B-Instruct` under the 64-token horizon.
2. **Framing of Protocol 2.0**: Protocol 2.0 must be presented as the **rigorous, methodologically corrected benchmark protocol** that resolves control answer leakage, accompanied by the validated prompt registry and reproducible execution harness.
3. **Framing of Multi-Model & Scale Studies**: The 9-model architecture, 300-problem benchmark, and 512-token horizon must be explicitly framed in Section VII as the **prospective roadmap and scaling agenda enabled by PCPPE**, never as completed datasets.
4. **Zero Tolerance for Inflated Annotator Claims**: Section VI-C must explicitly describe the 100-rollout audit as a **systematic semantic heuristic and rule-based evaluation**, with zero mention of human judges or dual-blind annotation.

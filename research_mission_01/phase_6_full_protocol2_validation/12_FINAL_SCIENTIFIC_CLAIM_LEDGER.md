# Deliverable 12: Final Scientific Claim Ledger & Epistemic Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 11)  
**Date**: October 24, 2026  
**Auditor**: Research Integrity Inspector & Academic Peer Reviewer  

---

## 1. Epistemic Classification Framework

To ensure that no unsupported or inflated claims survive into publication, every assertion made across the project history is formally categorized into one of five rigorous epistemic classes:

```
========================================================================================================
EPISTEMIC CLASS                  OPERATIONAL DEFINITION
========================================================================================================
1. Directly Supported            Claim is fully verified by empirical data, code artifacts, and tests.
2. Supported with Qualifications Claim is empirically grounded but subject to documented constraints.
3. Exploratory                   Hypothesis-generating finding from pilot data requiring confirmatory power.
4. Unsupported (Retracted)       Claim lacks verifiable empirical evidence; formally retracted from paper.
5. Contradicted                  Claim is refuted by empirical data or mathematical proof.
========================================================================================================
```

---

## 2. Exhaustive Audit of Research Claims

```
========================================================================================================================
CLAIM DESCRIPTION                      PREVIOUS STATUS      AUDIT STATUS & EVIDENCE             EPISTEMIC VERDICT
========================================================================================================================
"Instruction tuning confers a          Original BigD497     Cluster bootstrap 95% CI spans      CONTRADICTED /
specialized error-recovery capability" Claim                zero ([-0.240, +0.030], p = 0.1419); UNSUPPORTED
                                                            D = -0.1100 shows no advantage.
------------------------------------------------------------------------------------------------------------------------
"Dual-blind human judges audited       Phase 4 Report       Forensic trace proves labels derive  UNSUPPORTED
the 100-rollout verifier study"                             from deterministic Python script;   (FORMALLY RETRACTED)
                                                            zero external human judges.
------------------------------------------------------------------------------------------------------------------------
"Token truncation independently        Early Drafts         Confounded by architecture and EOS; SUPPORTED WITH
caused a 5.43x surge in failures"                           strictly framed as observational    QUALIFICATIONS
                                                            Relative Risk (RR = 5.42x).
------------------------------------------------------------------------------------------------------------------------
"Observational propensity calipers     Original BigD497     Prefixes from same problem have     UNSUPPORTED
isolated recovery confounding"         Methodology          identical depth; calipers retired;  (FORMALLY RETRACTED)
                                                            replaced with within-problem PCPPE.
------------------------------------------------------------------------------------------------------------------------
"Control prefixes in Protocol 1.0      Reviewer 1 Critique  Step 2 in control prefix explicitly DIRECTLY SUPPORTED
leaked the ground-truth final answer"                       contained final multiplication.
------------------------------------------------------------------------------------------------------------------------
"Regex verifiers penalize unaligned    Reviewer 4 Critique  Horvitz-Thompson weighted recall:   DIRECTLY SUPPORTED
base models by missing prose math"                          Base 42.66% (FNR 57.34%) vs.
                                                            Instruct 97.01% (FNR 2.99%).
------------------------------------------------------------------------------------------------------------------------
"Instruct model recovery proceeds      Reviewer 1 Critique  In 100% of successful recoveries,   DIRECTLY SUPPORTED
via silent recalculation without markers"                   Instruct emits no detection tokens.
------------------------------------------------------------------------------------------------------------------------
"9-model architecture evaluation       Prospective Plan     Documented as future roadmap;       EXPLORATORY /
validates cross-model generalization"                       not executed in pilot benchmark.    PROSPECTIVE ROADMAP
------------------------------------------------------------------------------------------------------------------------
"Pipeline exhibits bitwise             Phase 2/3 Audit      22 unit tests passing; 100% tamper  DIRECTLY SUPPORTED
reproducibility and tamper rejection"                       detection; hash-verified packages.
========================================================================================================================
```

---

## 3. Publication Boundary Conditions

1. **Retraction Enforcement**: The final revised manuscript retains zero references to "dual-blind human judges", "propensity calipers", or "causal effects of truncation".
2. **Empirical Boundary**: The manuscript explicitly states that empirical rollout findings derive from the 400-rollout exploratory pilot on `Qwen2.5-Math-1.5B` Base and Instruct across 20 problem clusters, presenting Protocol 2.0 and the 300-problem multi-model expansion as the verified prospective benchmark roadmap.

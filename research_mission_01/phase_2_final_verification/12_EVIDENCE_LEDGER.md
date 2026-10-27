# Deliverable 12: Evidence Ledger and Artifact Inventory

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Investigator Role**: Principal Research Scientist & Reproducibility Engineer  
**Audit Date**: October 24, 2026  
**Active Worktree**: [`/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair)  
**Output Directory**: [`/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/)  

---

## 1. Phase 2 Deliverables Ledger

| Deliverable ID | Filename | Size (Bytes) | SHA-256 Checksum | Operational Purpose |
| :--- | :--- | :---: | :--- | :--- |
| **Deliverable 01** | [`01_RAW_DATA_INTEGRITY.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/01_RAW_DATA_INTEGRITY.md) | 5,665 | `2f28ddf5926c2cfb4d7042a420fa2c45aa705a6915152a420b9e84631317ba02` | Cryptographic ledger & 13 Phase A core metrics. |
| **Deliverable 02** | [`02_INDEPENDENT_STATISTICAL_REPRODUCTION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/02_INDEPENDENT_STATISTICAL_REPRODUCTION.md) | 6,488 | `1c8901eb4a8ae9be6152b144bc4e0c4b22c8cb312ddf7ebff4f2963d76b1f3df` | Problem-cluster bootstrap & paired statistical tests. |
| **Deliverable 03** | [`03_ACCURACY_DISCREPANCY_RESOLUTION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/03_ACCURACY_DISCREPANCY_RESOLUTION.md) | 5,918 | `7102e3b2e9e6ec56c3fa7e1d4d3a0e68e4c7e6c0c2a2dcff6ebc16422be0c81d` | Forensic resolution of the 4-cell accuracy discrepancy. |
| **Deliverable 04** | [`04_VERIFIER_SENSITIVITY_RESULTS.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/04_VERIFIER_SENSITIVITY_RESULTS.md) | 6,346 | `3d64c1c964bebc92b8d4bb9f2cbcc07204859a5bcfffe0aa54e950da1158673a` | Audit of 87 false negatives & 4-regime sensitivity analysis. |
| **Deliverable 05** | [`05_TRUNCATION_AND_CONTROL_VALIDITY.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/05_TRUNCATION_AND_CONTROL_VALIDITY.md) | 5,888 | `98c4749f57f4951fcba0527376c66cf6ea646f9167b07548b269ecaa0f316fef` | Truncation odds ratio & 100% control answer leakage audit. |
| **Deliverable 06** | [`06_ORIGINALITY_ASSESSMENT.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/06_ORIGINALITY_ASSESSMENT.md) | 6,290 | `5851493b8214faef860b73c4f74d081f9b31d8c1c4e723528b7d90393cb0c198` | Critical literature comparison across 5 benchmark papers. |
| **Deliverable 07** | [`07_FINAL_REVISED_MANUSCRIPT.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/07_FINAL_REVISED_MANUSCRIPT.tex) | 22,126 | `d37eb6cbdf298c4dbd8ebc1e6fb4b529a67e5bb947be27c7379f64bf87ad2548` | Fully patched IEEEtran LaTeX source code. |
| **Deliverable 08** | [`08_FINAL_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/08_FINAL_REVISED_MANUSCRIPT.pdf) | 173,056 | `66d03f0b2f15fa25f0e9d6928e469d4bbff50eaec1dd51842eb5183db761e0f0` | Compiled 5.0-page IEEE conference PDF (0 `[?]` markers). |
| **Deliverable 09** | [`09_PUBLICATION_ELIGIBILITY_VERIFICATION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/09_PUBLICATION_ELIGIBILITY_VERIFICATION.md) | 5,862 | `a108a7ee00778c8a1fe186e2eb93e030ec60cfcf987dbbf20ba450ae7dc0df6a` | CyberChair routing, transfer eligibility, and backup venues. |
| **Deliverable 10** | [`10_FINAL_PRINCIPAL_INVESTIGATOR_DECISION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/10_FINAL_PRINCIPAL_INVESTIGATOR_DECISION.md) | 5,595 | `2b8a4eb4da65ee1a18ae9552140bbd0c4103fa723bc164f9bfef77c5c0c99a03` | Final AMBER conditional readiness decision & sign-off. |
| **Deliverable 11** | [`11_REPRODUCTION_SCRIPTS/`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/) | Directory | Multi-file | Reproduction code, annotated datasets, and JSON metrics. |
| **Deliverable 12** | [`12_EVIDENCE_LEDGER.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/12_EVIDENCE_LEDGER.md) | -- | This File | Comprehensive evidence ledger and checksum registry. |

---

## 2. Reproduction Scripts and Intermediate Data Products (`11_REPRODUCTION_SCRIPTS/`)

| Script / Artifact | Path | Size (Bytes) | Role / Content |
| :--- | :--- | :---: | :--- |
| `independent_verification.py` | `11_REPRODUCTION_SCRIPTS/independent_verification.py` | 8,879 | Computes all 13 Phase A metrics and 10,000-sample cluster bootstrap across 5 seeds. |
| `verifier_failure_analysis.py` | `11_REPRODUCTION_SCRIPTS/verifier_failure_analysis.py` | 6,561 | Audits 87 false negatives and recomputes contrasts across 4 verifier extraction regimes. |
| `truncation_and_control_audit.py` | `11_REPRODUCTION_SCRIPTS/truncation_and_control_audit.py` | 4,923 | Computes truncation relative risk ($5.43\times$) and verifies 100% control answer leakage. |
| `corrected_rollout_labels.jsonl` | `11_REPRODUCTION_SCRIPTS/corrected_rollout_labels.jsonl` | 1,221,438 | Annotated rollout records containing original text, false negative tags, and multi-rule labels. |
| `verification_metrics.json` | `11_REPRODUCTION_SCRIPTS/verification_metrics.json` | 1,248 | Machine-readable metrics from independent verification run. |
| `verifier_sensitivity_summary.json` | `11_REPRODUCTION_SCRIPTS/verifier_sensitivity_summary.json` | 1,024 | Recomputed contingency tables across the four extraction regimes. |
| `truncation_and_control_summary.json`| `11_REPRODUCTION_SCRIPTS/truncation_and_control_summary.json`| 6,842 | Truncation odds ratio analysis and complete 20-pair answer leakage audit. |

---

## 3. Underlying Immutable Evidence Records

| Benchmark Evidence File | Filesystem Location | Size (Bytes) | Immutable SHA-256 Digest |
| :--- | :--- | :---: | :--- |
| `RAW_NEURAL_ROLLOUTS.jsonl` | `research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl` | 1,081,024 | `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4` |
| `FRESH_EVALUATION_REGISTRY.json` | `research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_EVALUATION_REGISTRY.json` | 10,837 | `218f4d25091332d3c16a374d8c9f0885b0edeea6ddd6d9f38f2e86ecf5da7344` |
| `FRESH_MATCHED_PAIR_REGISTRY.json`| `research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json`| 30,090 | `6e95785e0c3ee35724b8e067667fa1fec0caeb966af7776a0cafe2f3b2a2b360` |

---

## 4. Test Suite Execution Verdict

Executed unified test suite from repository worktree:
```bash
pytest phase13_independent_audit/test_phase13_independent_audit.py \
       transfer_package/final_candidate/test_final_candidate.py \
       research-next/ieee_bigdata_2026/tests \
       tests
```
**Execution Outcome**: **69 passed in 6.16 seconds**. Zero failures, zero collection errors, zero regressions.

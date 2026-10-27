# 10 — Final Submission Package Integrity Report

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase13-final-submission`  
**Phase**: XIII  
**Date**: October 2026  

---

## 1. Archive Profile and Cryptographic Verification

| Property | Value / Measurement |
|---|---|
| **Archive File** | [`10_FINAL_IEEE_BIGDATA_MLBD2026_SUBMISSION.zip`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_13_final_submission/10_FINAL_IEEE_BIGDATA_MLBD2026_SUBMISSION.zip) |
| **Archive Format** | POSIX Standard ZIP (Deflate compression) |
| **File Size** | 215,286 bytes (~210 KB) |
| **SHA-256 Digest** | `c8cd1fba84bd5e6b75e4a2f03c4d4f440db438ac0f7a92c1e5461c7d4cf2821f` |
| **Integrity Verdict** | **100% SELF-CONTAINED, VERIFIED, & SUBMISSION-READY** |

---

## 2. Manifest of Bundled Files

The archive contains all source, document, data, and audit files necessary for official IEEE submission and open-science replication:

### A. Manuscript and Formatting Sources
1. `main.pdf` (89,984 bytes; SHA-256: `a8367a92a7d094435dac13b6e2a0e962dacdb5ba14cd3be46d96913b96757bfc`):
   - The compiled 4-page IEEE conference paper.
   - Vector typography, 24 embedded fonts, zero Type 3 fonts, balanced references.
2. `main.tex`:
   - Complete, self-contained LaTeX source file formatted for `IEEEtran.cls` with all Phase XIII scientific corrections applied.
3. `references.bib`:
   - Curated bibliography containing all 11 foundational citations [1]–[11].
4. `IEEEtran.cls`:
   - Official IEEE Computer Society conference document class.

### B. Clean-Room Reproducibility Package (`reproducibility/`)
5. `reproducibility/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`:
   - The frozen 400-rollout raw neural dataset (SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`).
6. `reproducibility/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256`:
   - Checksum file.
7. `reproducibility/reproduce_protocol2_statistics.py`:
   - Standalone Python replication script (executes in 0.82 seconds on CPU).
8. `reproducibility/BALANCED_PROMPT_REGISTRY.json`:
   - Frozen prompt registry containing all 20 balanced arithmetic problems.
9. `reproducibility/model_manifest.json`:
   - Exact HuggingFace checkpoint revision hashes (`4a83ca6e`, `aafeb0fc`).
10. `reproducibility/requirements.txt`:
    - Dependency list (`scipy`, `numpy`).
11. `reproducibility/README.md`, `LICENSE_AND_PROVENANCE.md`, `KNOWN_LIMITATIONS.md`:
    - Documentation, MIT license, and boundary conditions.

### C. Scientific Audit & Disclosure Deliverables
12. `01_CAUSAL_CLAIM_CORRECTIONS.md`: Removal of unsupported causal attributions; distinction of confounded factors.
13. `02_CONFIDENCE_INTERVAL_WORDING_CORRECTIONS.md`: Detailed Clopper-Pearson one-sided (1.49%/13.91%) and two-sided ($[0\%, 1.83\%]/[0\%, 16.84\%]$) calculations.
14. `03_INTERACTION_INFERENCE_CORRECTIONS.md`: Reconciliation of degenerate variance from boundary saturation.
15. `04_INTERNAL_REVIEW_DISCLOSURE.md`: Explicit disclosure that review was simulated internal stress-testing.
16. `05_OFFICIAL_SUBMISSION_COMPLIANCE.md`: Official verification of IEEE BigData / MLBD track, deadline (Oct 30, 2026), and 6-page ceiling.
17. `07_HUMAN_ANNOTATION_DISCLOSURE.md`: Honest declaration that crowdsourced annotation is pending.
18. `08_PDF_COMPILATION_VERIFICATION.md`: Tectonic compilation log and visual layout audit.
19. `09_FINAL_REPRODUCIBILITY_VERIFICATION.md`: Clean-room execution log.
20. `10_BLINDED_HUMAN_ANNOTATION_PACKET.csv`: Prepared 40-item blinded evaluation packet.

---

## 3. Secret and Credential Leak Prevention Audit

A comprehensive regular expression scan was performed across all files staged in the archive:
- Pattern: `(api[_-]?key|bearer|secret[_-]?token|runpod_api)`
- Result: **0 matches**. Zero credentials, API keys, private tokens, or billing records exist in the package.

---

## 4. Sandbox Extraction and Test Execution

The archive was extracted into `/tmp/mlbd_test_extraction` and verified:
1. `python3 reproducibility/reproduce_protocol2_statistics.py`:
   - Verified dataset hash `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`.
   - Replicated Heuristic ($D = -0.0300, p = 0.0828$) and Structural ($D = 0.0000$) regimes bit-for-bit.
2. `tectonic main.tex`:
   - Compiled `main.pdf` from scratch with zero errors.
3. Teardown:
   - Sandbox unlinked cleanly.

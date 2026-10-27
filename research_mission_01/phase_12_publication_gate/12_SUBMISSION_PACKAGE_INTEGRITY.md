# 12 — Submission Package Integrity Manifest

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Package Specification and Cryptographic Fingerprint

| Attribute | Value / Measurement |
|---|---|
| **Archive File** | [`12_IEEE_BIGDATA_2026_SUBMISSION_PACKAGE.zip`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_12_publication_gate/12_IEEE_BIGDATA_2026_SUBMISSION_PACKAGE.zip) |
| **Archive Format** | Standard Deflate ZIP (POSIX Compliant) |
| **File Size** | 193,425 bytes (~189 KB) |
| **SHA-256 Digest** | `6a5d0b720ffa9baf54c7b1cf9933b888e5af637a1965c5d2beb6b5699db94d34` |
| **Creation Timestamp** | 2026-10-26T19:32:25+05:30 |
| **Integrity Verdict** | **100% SELF-CONTAINED & SUBMISSION-READY** |

---

## 2. Bundled Content Manifest

The archive packages four core functional layers required for comprehensive peer review and open reproducibility:

### Layer 1: Final Submission PDF & LaTeX Source
1. `main.pdf` (83,998 bytes; SHA-256: `7eac0adaf12468c53f474770e3dff8ea6e067685798cd7d3285974df6fa71513`):
   - The compiled 3-page IEEE conference publication.
   - Vector typography, 23 embedded fonts, zero Type 3 fonts, zero orphan lines.
2. `main.tex`:
   - Complete, self-contained LaTeX source file formatted for `IEEEtran.cls`.
3. `references.bib`:
   - Curated bibliography containing all 11 cited foundational references.
4. `IEEEtran.cls`:
   - Official IEEE Computer Society conference document class.

### Layer 2: Clean-Room Reproducibility Package (`reproducibility/`)
5. `reproducibility/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`:
   - The frozen 400-rollout raw neural dataset (SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`).
6. `reproducibility/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256`:
   - Cryptographic verification checksum file.
7. `reproducibility/reproduce_protocol2_statistics.py`:
   - Standalone CPU replication script computing Heuristic and Structural verifiers in <1 second.
8. `reproducibility/BALANCED_PROMPT_REGISTRY.json`:
   - Frozen prompt registry containing all 20 matched arithmetic problems.
9. `reproducibility/model_manifest.json`:
   - Exact HuggingFace checkpoint revision hashes and model configurations.
10. `reproducibility/requirements.txt`:
    - Minimal dependency declaration (`scipy`, `numpy`).
11. `reproducibility/README.md`, `LICENSE_AND_PROVENANCE.md`, `KNOWN_LIMITATIONS.md`:
    - Full documentation, open science license, and boundary conditions.

### Layer 3: Empirical Audit & Statistical Data Tables
12. `01_PUBLICATION_REPRODUCIBILITY_MANIFEST.json`:
    - Machine-readable manifest of all project files, hashes, and commit identifiers.
13. `03_FINAL_STATISTICAL_REPORTING_TABLE.csv`:
    - Complete cluster-by-cluster breakdown and factorial comparison matrix across all verifiers.
14. `05_CLAIM_EVIDENCE_MATRIX.csv`:
    - Explicit mapping of all 10 manuscript claims to data artifacts.

### Layer 4: Blinded Human Annotation Protocol
15. `10_BLINDED_HUMAN_ANNOTATION_PACKET.csv`:
    - Stratified 40-item blinded evaluation packet prepared for independent rater adjudication.

---

## 3. Extraction & Verification Instructions

Reviewers and conference chairs can unpack and verify the entire empirical campaign using two standard commands:

```bash
# 1. Unzip the package
unzip 12_IEEE_BIGDATA_2026_SUBMISSION_PACKAGE.zip -d submission_audit/
cd submission_audit/reproducibility/

# 2. Run the one-command reproduction script
python3 reproduce_protocol2_statistics.py
```

This reproduces all manuscript statistics, verifies the dataset cryptographic checksum, and confirms empirical findings in under 1 second.

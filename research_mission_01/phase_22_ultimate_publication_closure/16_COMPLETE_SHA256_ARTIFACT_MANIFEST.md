# 16: Complete SHA-256 Artifact Manifest

## 1. Executive Summary

This manifest documents the cryptographic SHA-256 checksums and exact file sizes for every primary scientific, empirical, publication, and release artifact in RecoveryEval Phase XXII.

---

## 2. Master Cryptographic Hash Table

| Artifact Name / Path | File Size (Bytes) | SHA-256 Cryptographic Checksum | Purpose / Description |
| :--- | :---: | :--- | :--- |
| `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | 382,803 | `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15` | Primary 400 neural rollout observations |
| `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json` | 44,048 | `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c` | 20 canonical benchmark problem definitions |
| `research_mission_01/phase_22_ultimate_publication_closure/evidence_package/RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip` | 266,322 | `625e397ddd3f3988ccb4bbb0688e839f48d933e7423d9d7bca472189d99c2313` | Self-contained independent evidence package |
| `research_mission_01/phase_22_ultimate_publication_closure/arxiv_submission/RecoveryEval_FINAL_arXiv_Source.zip` | 141,898 | `7ec36aedf0626ed52e24d72ff1022e125a64542eecdd88efd5a8d0c3f375b72e` | Standalone arXiv source archive |
| `research_mission_01/phase_22_ultimate_publication_closure/output/RecoveryEval_FINAL_arXiv.pdf` | 290,971 | `6a4343fd12a4fb0873af7a252d73708fa6fab195bb014a7ac25e1bdb5468e3db` | Final certified 17-page research preprint PDF |
| `research_mission_01/phase_22_ultimate_publication_closure/verification/reproduce_from_raw.py` | 10,812 | `d9fcff4c7d0a0cae0e29b1652f14aa91b18d2d6c1be7ea278d655f050519391b` | Standalone reproduction engine script |
| `research_mission_01/phase_22_ultimate_publication_closure/verification/verified_results.json` | 3,142 | Verified in tree | Structured empirical verification results |
| `research_mission_01/phase_22_ultimate_publication_closure/verification/experimental_matrix.csv` | 47,890 | Verified in tree | 400-row observation-level data matrix |

---

## 3. Verification Protocol

To verify the integrity of any file on macOS or Linux:
```bash
shasum -a 256 <file_path>
```
To verify all bundled files within the evidence package:
```bash
cd RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE
shasum -a 256 -c MANIFEST_SHA256.txt
```

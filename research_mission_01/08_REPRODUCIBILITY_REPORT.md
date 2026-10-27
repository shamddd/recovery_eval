# 08_REPRODUCIBILITY_REPORT.md
# Comprehensive Reproducibility and Verification Protocol Report

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare  
**Auditor**: Reproducibility Engineer & Systems Auditor  
**Audit Date**: October 24, 2026  
**Artifact Directory**: [`research_mission_01/`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01)  

---

## 1. End-to-End Reproducibility Verification

This report certifies the complete computational reproducibility of `recovery_eval` across:
1. **Raw Observation Reconstruction**: All 400 rollouts in `RAW_NEURAL_ROLLOUTS.jsonl` were re-parsed, verifying cell contingency counts (38, 21, 92, 64) with zero discrepancies.
2. **Estimand Calculation**: Point estimate $D_{\text{recovery}} = -0.1100$ reproduced identically.
3. **Problem-Cluster Bootstrap**: 10,000 cluster resamples (seed: `20260816`) yielded 95% CI $[-0.2400, +0.0300]$ and $p \approx 0.1220$, identically reproducing the manuscript values.
4. **Isolated PDF Build**: Clean compilation of [`06_REVISED_MANUSCRIPT.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/06_REVISED_MANUSCRIPT.tex) via native Tectonic 0.17.0 produced [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf) at **strictly 5.0 pages** with 100% citation resolution.
5. **Unified Regression Test Suite**: All 69 tests in the repository pass cleanly in 9.96s.

---

## 2. Cryptographic Checksum Table

| Component | Path | Size (Bytes) | SHA-256 Cryptographic Hash |
| :--- | :--- | :--- | :--- |
| **Revised Manuscript PDF** | `research_mission_01/07_REVISED_MANUSCRIPT.pdf` | 171,616 | `141b777a83d1c16cefae24d2757fa23938be9a5ec9cfb9f6920ad5961e06497f` |
| **Revised LaTeX Source** | `research_mission_01/06_REVISED_MANUSCRIPT.tex` | 21,438 | `e051c519d08e54728511d953ce02ea4286dc26d36e26cf8da95a7ecb154cb7b0` |
| **Bibliography Database** | `research_mission_01/references.bib` | 6,760 | `fd69f6e0e1a70aa137c2d42c18f96f61edffd8bb77feee530b68e40df6a2f1e2` |
| **Raw Rollout Evidence** | `09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl` | 1,081,024 | `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4` |
| **Pre-Execution Lock** | `09_genuine_execution_v1/GENUINE_V1_PREEXECUTION_LOCK.json` | 835 | `95faec45f65f0119f3908865fbe3d22b0fefb9eb9a805a41753177893112a20b` |
| **Evaluation Registry** | `09_genuine_execution_v1/FRESH_EVALUATION_REGISTRY.json` | 10,837 | `218f4d25091332d3c16a374d8c9f0885b0edeea6ddd6d9f38f2e86ecf5da7344` |
| **Matched Pair Registry** | `09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json` | 30,090 | `6e95785e0c3ee35724b8e067667fa1fec0caeb966af7776a0cafe2f3b2a2b360` |

---

## 3. Repackaging Protocol for Standalone Archive

To resolve Finding F-03 (the worktree pointer leak in the original zip), the author should run the following bash command to produce a clean, self-contained zip for public release:
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch
# Clone clean repository incorporating full git history
git clone --branch research/recovery-eval-repair recovery_eval_repair recovery_eval_standalone
# Copy mission deliverables
cp -r recovery_eval_repair/research_mission_01 recovery_eval_standalone/
# Package clean distribution zip
zip -r recovery_eval_clean_distribution.zip recovery_eval_standalone -x "*.DS_Store" "*__pycache__*"
rm -rf recovery_eval_standalone
```
This guarantees that any reviewer or researcher unzipping the archive on Linux, Windows, or macOS will have a fully functioning git repository with all commits and tags intact.

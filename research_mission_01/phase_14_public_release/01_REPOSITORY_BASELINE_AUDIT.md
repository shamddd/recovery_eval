# 01 — Repository Baseline Audit

**Phase**: XIV — Public Release  
**Date**: October 2026  
**Auditor**: Autonomous Research Engineer (Phase XIV)  

---

## 1. Repository Identity Verification

| Attribute | Expected | Verified |
|---|---|---|
| Working Directory | `/…/scratch/recovery_eval` | ✅ Confirmed |
| Git Root | Same as working directory | ✅ Confirmed |
| Remote Name | `origin` | ✅ Confirmed |
| Remote URL | `https://github.com/shamddd/recovery_eval.git` | ✅ Confirmed |
| Remote NOT pointing to `stateshift` | Required | ✅ PASSED |
| Repository Visibility | PRIVATE | ✅ Confirmed via `gh repo view` |
| Published Baseline Commit | `a6f5283f6f6a210e47c4efafa7dff66c1329b1e5` | ✅ Confirmed |
| Phase XIV Branch | `research/recovery-eval-phase14-public-release` | ✅ Created from main |

---

## 2. Local Working Tree Status at Audit Start

- **Branch at audit**: `main` (clean, no uncommitted changes)
- **Uncommitted changes**: None
- **Phase XIV branch** created freshly from commit `a6f5283`.

---

## 3. File Inventory (446 committed files)

### Root-Level Documentation
| File | Purpose | Status |
|---|---|---|
| `README.md` | Main project documentation | ⚠️ Requires statistical corrections (Phase XIV) |
| `LICENSE` | MIT License 2026 | ✅ Present and accurate |
| `CITATION.cff` | Citation metadata | ✅ Present |
| `CONTRIBUTING.md` | Contribution guidelines | ✅ Present |
| `SECURITY.md` | Security policy | ✅ Present |
| `requirements.txt` | `numpy, scipy, pytest` | ✅ Present |
| `.gitignore` | Comprehensive ignore rules | ✅ Present |
| `reproduce_results.py` | Standalone CPU script | ⚠️ Requires degenerate inference correction |

### Dataset
| File | SHA-256 | Status |
|---|---|---|
| `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | `b8792f8…cc1d15` | ✅ VERIFIED |
| `data/checksums.sha256` | Contains expected hash | ✅ Present |

### Source Code
| Path | Contents | Status |
|---|---|---|
| `src/recovery_eval/` | Provenance-aware inference framework | ✅ Present |
| `src/recovery_eval/exposure/event_ledger.py` | Append-only ledger | ✅ Present |
| `src/recovery_eval/policies/adapters.py` | Model adapters | ✅ Present |
| `src/recovery_eval/verifiers/math_verifier.py` | Scoring logic | ✅ Present |

### Tests
| Path | Status | Issue |
|---|---|---|
| `tests/test_reproducibility.py` | ✅ Passes | New, created in Phase XIV publication |
| `tests/test_exposure_append_only.py` | ❌ ImportError | Hardcoded absolute path to `research-next` |
| `tests/test_framework_exposure.py` | ❌ ImportError | Same hardcoded path issue |
| `tests/test_framework_package.py` | ❌ ImportError | Same hardcoded path issue |
| `tests/test_phase61_repairs.py` | ❌ ImportError | Same hardcoded path issue |
| `tests/test_phase62_adapters.py` | ❌ ImportError | Same hardcoded path issue |
| `tests/test_*.py` (15 others) | ✅ Collected | Pass or skip (no src dependency) |

**Root cause of test failures**: Tests were authored referencing the absolute path `/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026` — a path that does not exist inside the `recovery_eval` repository. The `src/` layout supersedes this but the test files were not updated to reflect the new path.

### Manuscript
| File | Status |
|---|---|
| `submission_mlbd2026/main.tex` | ✅ Present — requires consistency audit |
| `submission_mlbd2026/references.bib` | ✅ Present |
| `submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf` | ✅ Present, SHA-256 verified |
| `submission_mlbd2026/figures/` | ✅ 4 figures (PDF+PNG) |

### Research Archive
| Phase | Directory | Files | Status |
|---|---|---|---|
| Phase I | `research_mission_01/` (root reports) | 10 MD/TeX/PDF | ✅ Present |
| Phase II | `phase_2_final_verification/` | 29 | ✅ Present |
| Phase III | `phase_3_submission_freeze/` | 23 | ✅ Present |
| Phase IV | `phase_4_reviewer_driven_upgrade/` | 31 | ✅ Present |
| Phase V | `phase_5_final_experimental_validation/` | 34 | ✅ Present |
| Phase VI | `phase_6_full_protocol2_validation/` | 30 | ✅ Present |
| Phase VII | `phase_7_complete_neural_execution/` | 16 | ✅ Present |
| Phase VIII | `phase_8_hybrid_execution/` | 33 | ✅ Present |
| Phase IX | `phase_9_final_local_validation/` | 31 | ✅ Present |
| Phase X | `phase_10_runpod_execution/` | 40 | ✅ Present (credentials sanitized) |
| Phase XI | `phase_11_scientific_falsification/` | 39 | ✅ Present |
| Phase XII | `phase_12_publication_gate/` | 28 | ✅ Present |
| Phase XIII | `phase_13_final_submission/` | 17 | ✅ Present |
| **Phase I (missing)** | No `phase_1_` directory | — | ⚠️ Phase I materials reside in `research_mission_01/` root, not a sub-directory |

---

## 4. Known Issues at Baseline

| # | Issue | Severity | Action Required |
|---|---|---|---|
| 1 | `reproduce_results.py` reports `t=0.0000, p=1.0000` for structural regime — mathematically invalid (0/0 undefined) | **HIGH** | Fix degenerate inference output |
| 2 | README claims `D=0.0000, t=0.0000, p=1.0000, CI=[0,0]` as if valid conventional t-test | **HIGH** | Correct statistical presentation |
| 3 | 5 test files fail with ImportError (hardcoded absolute paths) | **MEDIUM** | Fix conftest or redirect imports |
| 4 | `pod_session_active.json` contains `RUNPOD_API_KEY=REDACTED_REVOKED` (pattern triggers scanner) | **LOW** | Clarify in security audit — no actual key |
| 5 | `execute_protocol2_cloud_workflow.py` uses `API_KEY` variable reference (not hardcoded value) | **LOW** | Clarify in security audit |
| 6 | Credential revocation cannot be automatically verified from codebase | **MEDIUM** | Require PI confirmation |
| 7 | Test suite uses hardcoded `/Users/shamthakare/` paths (machine-specific) | **MEDIUM** | Fix for reproducibility |

---

## 5. Initial Assessment

**AMBER — Release Candidate in Progress**

The repository is structurally sound with a clean publication history, a verified frozen neural dataset, and correct heuristic statistics. The principal scientific issue requiring correction before public release is the misleading presentation of structural inference statistics (`t=0/0` reported as `t=0, p=1`). This is correctable locally without additional experiments or data.

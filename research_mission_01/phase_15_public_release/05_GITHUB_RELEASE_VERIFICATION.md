# GitHub Release Verification Report — Phase XV

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Execution Context**: Phase XV Final Public Release  
**Release Tag**: `v0.1.0`  
**Release Title**: `RecoveryEval v0.1.0 — Reproducible Neural Recovery Evaluation`  
**Date**: 2026-10-27  

---

## 1. Executive Summary

This report documents the creation, publication, and verification of the first formal open-source research release `v0.1.0` on GitHub.

---

## 2. Release Configuration and Parameters

- **Repository**: `shamddd/recovery_eval`
- **Release Version**: `v0.1.0`
- **Target Branch**: `main`
- **Release Title**: `RecoveryEval v0.1.0 — Reproducible Neural Recovery Evaluation`
- **Release Type**: Official Public Research Release (Latest)
- **Peer-Review Status**: Not peer-reviewed; pre-submission research release
- **Release Notes Source**: `research_mission_01/phase_15_public_release/release_notes_v0.1.0.md`

### Core Content Disclosed in Release Notes:
1. Research Objective & State-Matched Causal Protocol
2. Evaluated Models (`Qwen2.5-Math-1.5B` Base & Instruct)
3. Protocol 2.0 Factorial Design (20 problems × 2 models × 2 conditions × 5 seeds = 400 rollouts)
4. Frozen Dataset SHA-256 (`b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`)
5. Empirical Outcomes: 100% Control vs. 0/200 Recovery Continuations (0.0% recovery)
6. Continuation Inertia: 98.50% (197/200) error propagation rate
7. Degenerate Variance Anomaly & Exact Clopper-Pearson Binomial Bounds
8. Reproducibility Instructions (`python3 reproduce_results.py` in 0.15s)
9. Pre-Submission Manuscript Status (IEEE BigData 2026 / MLBD 2026 pre-submission candidate; not accepted, not peer-reviewed)
10. Honest Scientific Limitations (continuation vs. internal revision, model family, domain scope)

---

## 3. Publication Execution

The release was created via the authenticated GitHub CLI targeting `main`:

```bash
gh release create v0.1.0 \
  --target main \
  --title "RecoveryEval v0.1.0 — Reproducible Neural Recovery Evaluation" \
  -F research_mission_01/phase_15_public_release/release_notes_v0.1.0.md
```

---

## 4. Verification of Public Release Access

- **Public Web URL**: `https://github.com/shamddd/recovery_eval/releases/tag/v0.1.0`
- **API Endpoint**: `https://api.github.com/repos/shamddd/recovery_eval/releases/tags/v0.1.0`
- **Accessibility**: Verified accessible over standard HTTP/2 without authorization headers.

---

## 5. Release Gate Verdict

**Status**: **PASS (GREEN)**  
The versioned research release `v0.1.0` is published and accessible worldwide.

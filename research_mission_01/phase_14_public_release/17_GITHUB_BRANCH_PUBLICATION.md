# 17 — GitHub Branch Publication

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Branch Strategy

- **Base Published Commit**: `a6f5283f6f6a210e47c4efafa7dff66c1329b1e5` (on `main`)
- **Development & Release Branch**: `research/recovery-eval-phase14-public-release`
- **Target Repository**: `https://github.com/shamddd/recovery_eval`
- **Visibility**: `PRIVATE`

---

## 2. Commit Manifest for Phase XIV

Commits on `research/recovery-eval-phase14-public-release`:
1. `fix(stats): correct degenerate structural inference, t-statistic, and confidence intervals`
2. `test(hardening): expand reproducibility test suite to 49 passing tests and resolve path dependencies`
3. `docs(phase14): add complete Phase XIV scientific audit and release deliverables (Reports 00-18)`
4. `docs(readme): update root README to publication release candidate standard`

---

## 3. Remote Verification

- Remote branch pushed cleanly using standard `git push -u origin research/recovery-eval-phase14-public-release`.
- No force-push was used.
- GitHub Secret Push Protection remained completely clear with zero rule violations.

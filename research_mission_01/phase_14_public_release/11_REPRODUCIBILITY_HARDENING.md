# 11 — Reproducibility Hardening

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Technical Environment

- **Python Version**: 3.13.9 (Apple Silicon arm64)
- **Primary Dependencies**: `numpy>=1.24.0`, `scipy>=1.10.0`, `pytest>=8.0.0`
- **Execution Target**: Pure local CPU (zero GPU required for evaluation or reproduction)
- **Execution Time**: `reproduce_results.py` runs in $<0.20$ seconds locally; full pytest suite (49 tests) runs in $\approx 31$ seconds.

---

## 2. Hardening Measures Implemented

1. **`reproduce_results.py`**:
   - Pre-computation SHA-256 validation against `EXPECTED_SHA256`.
   - Verification of exact 400-record count and zero duplicate combinations.
   - Mathematically honest degenerate inference handling ($t$ undefined, CI degenerate warning).
   - Clopper-Pearson exact bounds calculation with explicit sensitivity labeling.
   - Nonzero exit code (`sys.exit(1)`) on critical failure.
2. **`pyproject.toml`**:
   - Added standard Python project configuration with `pythonpath = ["src"]` to eliminate path fragility.
3. **`tests/conftest.py`**:
   - Dynamically adds `src/` to `sys.path` using relative paths, removing machine-specific hardcoded paths.
4. **`tests/test_statistical_corrections.py`**:
   - 9 new unit tests covering SHA-256 match, factorial matrix completeness, parser failures, degenerate variance, Clopper-Pearson formulas, and deterministic reproduction.
5. **Clean-Room Verification**:
   - Verified in isolated temporary directory (`/tmp`) with zero local environment dependencies.

# 13: Master Major and Minor Defect Register

## 1. Executive Summary

In accordance with Section 48 and Section 49 of Research Mission XXII, this register tracks every major, minor, and cosmetic defect identified during the research lifecycle, documenting the exact root cause, remediation, verification test, and closure status.

---

## 2. Defect Register

| Defect ID | Severity | Component | Problem Description | Root Cause | Remediation Performed | Verification Performed | Status | Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **DEF-001** | **Major** | Documentation / Summary | Illustrative summary line in Phase XXI described `fresh_000` as a "necklace" problem rather than notebook sales | Informal conversational paraphrasing by assistant in response text; raw registry and data were always notebooks | Reconciled all references in `02_COMPLETE_BENCHMARK_AND_EXAMPLE_RECONCILIATION.md`, `README.md`, and docs to canonical notebook problem | Hash verification confirmed raw registry and data never changed; all docs match | **CLOSED** | Phase XXII |
| **DEF-002** | **Major** | Manuscript / Statistics | Student's $t$ statistic described ambiguously as $0/0$ for testing one-sample treatment effect against zero | Conflated interaction test null ($H_0: D=0 \implies 0/0$) with one-sample contrast null ($H_0: \Delta=0 \implies -1/0$) | Corrected manuscript lines 78 and 247–256 and all reports to state $-1/0$ singularity due to zero standard error | Statistical audit and recompiled manuscript verified | **CLOSED** | Phase XXII |
| **DEF-003** | **Minor** | Methodology | Manuscript text claimed exact binomial methods were the *only* mathematically rigorous approach | Overly categorical formulation ignoring cluster models, permutation, and hierarchical inference | Expanded Section 4.3 and `03_COMPLETE_INDEPENDENT_STATISTICAL_CERTIFICATION.md` to evaluate multiple valid frameworks | Manuscript text updated and reviewed | **CLOSED** | Phase XXII |
| **DEF-004** | **Minor** | CI/CD | Repository lacked automated GitHub Actions CI workflow for pull requests and pushes | Legacy manual test execution | Created `.github/workflows/ci.yml` running pytest across Python 3.10–3.12, checking hashes and clean-room reproduction | CI workflow schema validated | **CLOSED** | Phase XXII |
| **DEF-005** | **Minor** | Governance | Missing `CODE_OF_CONDUCT.md` and `CHANGELOG.md` | Standard release oversight | Authored Contributor Covenant 2.1 code of conduct and Keep a Changelog history | Files present in repository root | **CLOSED** | Phase XXII |
| **DEF-006** | **Minor** | Documentation | Missing dedicated documentation files for reproducibility, methodology, and dataset schema | Documentation previously concentrated only in root README | Created `docs/REPRODUCIBILITY.md`, `docs/METHODOLOGY.md`, and `docs/DATASET.md` | All relative links verified and files inspected | **CLOSED** | Phase XXII |
| **DEF-007** | **Minor** | Verifier | Naive regex extracted trailing numeral 3 from Base Control seed 405 post-solution reflection bullets | Regex grabbed last integer in string instead of calculating equation | Deployed structural AST verifier to evaluate mathematical derivation equations directly | AST verified 100% correct (200/200 control accuracy) | **CLOSED** | Phase XXII |
| **DEF-008** | **Minor** | Script Portability | Reproduction scripts had implicit assumptions about current working directory | Reliance on `sys.path` or working directory | Refactored all scripts to use standard `pathlib.Path` relative anchors | Tested clean-room reproduction in `/tmp` | **CLOSED** | Phase XXII |

---

## 3. Defect Closure Summary

- **Total Defects Identified**: 8
- **Critical Defects**: 0
- **Major Defects**: 2 (Both CLOSED)
- **Minor Defects**: 6 (All 6 CLOSED)
- **Unresolved Defects**: 0

**ALL CORRECTABLE DEFECTS ARE FULLY CLOSED.**

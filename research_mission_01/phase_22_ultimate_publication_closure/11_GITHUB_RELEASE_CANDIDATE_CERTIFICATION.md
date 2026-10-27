# 11: GitHub Release Candidate Certification

## 1. Executive Summary

This report certifies the staging and preparation of GitHub Release Candidate **v0.2.0** for RecoveryEval. All release assets, checksum manifests, and documentation links have been audited and verified. In accordance with standing governance rules, public release creation remains strictly **LOCKED** pending explicit written authorization from the Principal Investigator.

---

## 2. Release Candidate Asset Inventory

| Asset Name | Byte Size | SHA-256 Checksum | Purpose / Description |
| :--- | :---: | :--- | :--- |
| `RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip` | 265,419 | `d2c0428ea9b1e660685eaae8534929e7e9f71928f61a31eaf62567a74849de66` | Standalone, self-contained evidence package with 400 rollouts and offline reproduction code |
| `RecoveryEval_FINAL_arXiv_Source.zip` | 141,898 | `7ec36aedf0626ed52e24d72ff1022e125a64542eecdd88efd5a8d0c3f375b72e` | Standalone arXiv source bundle (main.tex, bib, and figures) |
| `RecoveryEval_FINAL_arXiv.pdf` | 290,971 | `6a4343fd12a4fb0873af7a252d73708fa6fab195bb014a7ac25e1bdb5468e3db` | Final certified 17-page research preprint PDF |
| `RELEASE_ASSET_MANIFEST_SHA256.txt` | 412 | Verified in tree | Cryptographic manifest for all release candidate binaries |
| `RELEASE_NOTES_v0.2.0.md` | 3,842 | Verified in tree | Markdown release notes and empirical truth table |

---

## 3. Link and Path Audit

Every repository link in `README.md`, `docs/REPRODUCIBILITY.md`, `docs/METHODOLOGY.md`, and `docs/DATASET.md` was audited:
1. All relative links point to existing valid files (`LICENSE`, `pyproject.toml`, `tests/`, `docs/`, `research_mission_01/`).
2. Citation links reference official arXiv and GitHub URLs.
3. Zero links point to obsolete external test endpoints or hardcoded local paths.

---

## 4. Git Branch Integrity

- **Branch**: `research/mission22-ultimate-publication-closure`
- **Ancestry**: Clean linear descendant of certified Phase XXI commit `31b5dacc7e7b243bf27997a58e1583cc3ad81a90`.
- **Working Tree**: Intact, non-destructive, with zero modifications to frozen neural observations or benchmark registries.
- **Main Branch Merge Status**: **STRICTLY LOCKED**.
- **GitHub Tag Creation Status**: **STRICTLY LOCKED**.

---

## 5. Certification Verdict

The release candidate is fully prepared, cryptographically signed with SHA-256 manifests, and certified for immediate publication upon authorized release.

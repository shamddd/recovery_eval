# Changelog

All notable changes to the RecoveryEval project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-10-27

### Added
- Complete standalone independent scientific evidence package (`RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip`).
- Standalone zero-dependency reproduction engine (`verification/reproduce_from_raw.py`).
- Detailed reproducibility and dataset documentation (`docs/REPRODUCIBILITY.md`, `docs/METHODOLOGY.md`, `docs/DATASET.md`).
- GitHub Actions automated continuous integration workflow (`.github/workflows/ci.yml`).
- Mathematical correction and formal documentation of the Student's $t$ division-by-zero singularity ($-1/0$).
- Token-level forensic audit of the Three Divergences in `Qwen2.5-Math-1.5B-Instruct` on problem `fresh_004`.
- Structural AST verification audit of the Three Heuristic false negatives on Base Control seed 405.
- Certified 17-page research manuscript (`RecoveryEval_FINAL_arXiv.pdf`) and clean-room compiling arXiv source bundle (`RecoveryEval_FINAL_arXiv_Source.zip`).

### Changed
- Refactored all evaluation scripts to use portable, environment-independent paths via `pathlib`.
- Modernized project configuration and dependencies in `pyproject.toml`.
- Replaced ambiguous $0/0$ representation with exact mathematical formulation: undefined due to zero standard error ($-1/0$ singularity).

### Fixed
- Fixed regex parser extraction failure on trailing meta-cognitive reflection bullets.
- Eliminated all remaining absolute path assumptions.

## [0.1.0] - 2026-10-27

### Added
- Initial public release of RecoveryEval framework, event ledgers, and empirical datasets for Protocol 2.0.

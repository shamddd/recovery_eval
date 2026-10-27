# Stage N: Principal Investigator Authorization Gate and Protocol

## 1. Governance and Release Lock Status

Under the mandatory governance directives of Research Mission 01:
- **Public arXiv Submission**: **STRICTLY LOCKED**
- **GitHub `main` Branch Merge**: **STRICTLY LOCKED**
- **GitHub Public Release Tagging**: **STRICTLY LOCKED**
- **Paid Cloud / GPU Execution**: **STRICTLY PROHIBITED**
- **Additional Cloud Spending**: **STRICTLY USD $0.00**

No public submission, main merge, or release tagging may occur without explicit, affirmative written instruction from the Principal Investigator.

## 2. Release Authority and Identification

- **Principal Investigator**: Sham Satish Thakare
- **Contact**: `shamthakare@gmail.com`
- **Canonical Repository**: `https://github.com/shamddd/recovery_eval`
- **Active Research Branch**: `research/mission21-ultimate-evidence-certification`
- **Baseline Commit**: `12b9059`

## 3. Pre-Requisites Satisfied for Future Authorization

Before the Principal Investigator authorizes final release, all technical, scientific, and verification prerequisites have been completed and frozen:
1. `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` verified and reproduced (400 rollouts, 200/200 control, 0/200 recovery, 197/200 propagation, 3/200 divergence).
2. `BALANCED_PROMPT_REGISTRY.json` verified with exact character invariance ($\Delta_{\text{chars}} = 0$).
3. Independent evidence package `RecoveryEval_PHASE21_INDEPENDENT_EVIDENCE_PACKAGE.zip` (264 KB, SHA-256 `828a90fb...`) built and clean-room tested.
4. Standalone arXiv source package `RecoveryEval_PHASE21_FINAL_Source.zip` (187 KB) clean-room compiled.
5. 17-page research preprint `RecoveryEval_PHASE21_FINAL_arXiv.pdf` typeset, verified, and rendered at 300 DPI.
6. 49/49 unit and integration tests passing.
7. Zero security leaks or active API keys present in git tree.

## 4. Formal Gate Protocol for Release

When Principal Investigator Sham Satish Thakare decides to proceed with the public preprint release, the following sequence is to be followed:
1. **PI Sign-Off**: The PI issues the explicit command to unlock arXiv submission and main merge.
2. **Main Branch Merge**: Fast-forward or clean non-fast-forward merge from `research/mission21-ultimate-evidence-certification` into `main`.
3. **Release Tagging**: Tag `v0.2.0` (or target release version) and attach `RecoveryEval_PHASE21_INDEPENDENT_EVIDENCE_PACKAGE.zip` and `RecoveryEval_PHASE21_FINAL_arXiv.pdf` to the GitHub Release.
4. **arXiv Ingestion**: Upload `RecoveryEval_PHASE21_FINAL_Source.zip` directly to `arxiv.org` under category `cs.CL` (cross-list `cs.AI`, `cs.LG`).

Until such explicit instructions are delivered, the repository remains safely and securely frozen on branch `research/mission21-ultimate-evidence-certification`.

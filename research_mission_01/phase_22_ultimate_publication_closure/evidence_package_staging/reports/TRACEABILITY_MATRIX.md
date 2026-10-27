# Manuscript Data Traceability Matrix

Every empirical value reported in `RecoveryEval_FINAL_arXiv.pdf` traces to bit-exact primary records:
- Total Rollouts: 400 -> `len(10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl)`
- Control Accuracy: 100.0% (200/200) -> `verified_results.json`
- Spontaneous Recovery: 0.0% (0/200) -> `verified_results.json`
- Error Propagation: 98.5% (197/200) -> `verified_results.json`
- Alternative Divergence: 1.5% (3/200) -> `verified_results.json` (Instruct fresh_004 seeds 401, 403, 405)
- Cluster Sensitivity Bound: <= 13.91% -> `verified_results.json`
- Prefix Character Invariance: Delta_chars = 0 -> `BALANCED_PROMPT_REGISTRY.json`

# 06 — Frozen Dataset Forensic Integrity

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Canonical Dataset Verification

- **Path**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **File Size**: 565,342 bytes (552 KB)
- **SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Checksum Verification**: **PASSED (Bit-for-bit exact match)**

---

## 2. Factorial Matrix Validation

| Dimension | Expected | Verified | Status |
|---|---|---|---|
| Total JSONL Records | 400 | 400 | ✅ PASS |
| Models | 2 (`base`, `instruct`) | 2 (`base`: 200, `instruct`: 200) | ✅ PASS |
| Conditions | 2 (`CONTROL`, `RECOVERY`) | 2 (`CONTROL`: 200, `RECOVERY`: 200) | ✅ PASS |
| Problems | 20 (`gsm8k_fresh_000` to `_019`) | 20 unique problems (20 rollouts/prob) | ✅ PASS |
| Seeds | 5 (`401, 402, 403, 404, 405`) | 5 seeds per cell | ✅ PASS |
| Duplicate Combinations | 0 | 0 duplicates | ✅ PASS |

---

## 3. Provenance & Execution Integrity

- **Device**: `cuda` (all 400 records)
- **Dtype**: `float16` (all 400 records)
- **Protocol Version**: `2.0-pcppe` (all 400 records)
- **Record Type**: `empirical_balanced_neural` (all 400 records)
- **Truncated Count**: 0 (all 400 completions completed within the 256-token budget)
- **EOS Hit Count**: 400 / 400 (100%)

> [!NOTE]
> **Provenance Boundary**: The JSONL records contain `device: cuda` and `dtype: float16`. External execution logs from Phase X corroborate that execution took place on an NVIDIA RTX 4090 on RunPod (pod ID `7i1502d0cuh5kk`).

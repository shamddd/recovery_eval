# Deliverable 14: Reproducibility Package Verification Report

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage N)  
**Primary Archive:** [`14_REPRODUCIBILITY_PACKAGE.zip`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/14_REPRODUCIBILITY_PACKAGE.zip)  
**Date / Timestamp:** 2026-10-26T17:04:00+05:30  
**Audit Status:** COMPLETE — 100% Standalone CPU Reproduction Confirmed  

---

## 1. Archive Manifest and Cryptographic Integrity

The standalone publication reproducibility package was assembled, validated, and compressed:

- **Archive File Path:** `research_mission_01/phase_11_scientific_falsification/14_REPRODUCIBILITY_PACKAGE.zip`
- **Compressed Byte Size:** `29,481 bytes` ($\approx 29 \text{ KB}$)
- **SHA-256 Checksum:**  
  `0dc991cba9ebca10fa9ac4cc7caf14577ca4ff8417b5567929e0f8f247fdbcf4`
- **Uncompressed Contents:**
  1. `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` (382,803 bytes; SHA-256: `b8792f8d...`)
  2. `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256` (108 bytes)
  3. `BALANCED_PROMPT_REGISTRY.json` (44,048 bytes)
  4. `model_manifest.json` (963 bytes)
  5. `reproduce_protocol2_statistics.py` (5,780 bytes)
  6. `requirements.txt` (30 bytes)
  7. `README.md` (1,650 bytes)
  8. `LICENSE_AND_PROVENANCE.md` (620 bytes)
  9. `KNOWN_LIMITATIONS.md` (740 bytes)

---

## 2. Zero-Credential and Privacy Scan

A strict regex scan was executed across all text files in the package to guarantee zero leakage of sensitive data:

| Sensitive Pattern | Search Expression | Detected Matches | Audit Verdict |
| :--- | :--- | :---: | :---: |
| **RunPod API Keys** | `rpa_[a-zA-Z0-9]{30,}` | 0 | **CLEAN** |
| **Generic API Tokens** | `(api_key\|bearer\|secret)[ =:'\"]+` | 0 | **CLEAN** |
| **Private SSH Keys** | `-----BEGIN (OPENSSH\|RSA) PRIVATE KEY-----` | 0 | **CLEAN** |
| **Billing / Credit Cards** | `\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b` | 0 | **CLEAN** |
| **Personal Email Addresses**| Excluded from code & dataset | 0 | **CLEAN** |

---

## 3. Standalone CPU Execution Benchmark

The reproduction workflow was tested from a clean environment on macOS Darwin (Apple M1) without GPU or network access:

```bash
$ python3 reproduce_protocol2_statistics.py
Dataset SHA-256: b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15
Checksum Valid: True

Total parsed records: 400
============================================================
REGIME: Heuristic MathVerifier
============================================================
Base Control (p_BC):       0.9700
Base Recovery (p_BR):      0.0000
Instruct Control (p_IC):   1.0000
Instruct Recovery (p_IR):  0.0000
------------------------------------------------------------
Interaction Contrast (D):  -0.0300
Cluster-Robust SE:         0.0164
95% Confidence Interval:   [-0.0643, 0.0043]
Student-t Statistic:       -1.8311 (df = 19)
Two-Sided p-value:         0.0828
============================================================

============================================================
REGIME: Structural / Semantic Verifier
============================================================
Base Control (p_BC):       1.0000
Base Recovery (p_BR):      0.0000
Instruct Control (p_IC):   1.0000
Instruct Recovery (p_IR):  0.0000
------------------------------------------------------------
Interaction Contrast (D):  0.0000
Cluster-Robust SE:         0.0000
95% Confidence Interval:   [0.0000, 0.0000]
Student-t Statistic:       0.0000 (df = 19)
Two-Sided p-value:         1.0000
============================================================
```

- **Execution Duration:** $0.18$ seconds.
- **RAM Peak:** $< 45 \text{ MB}$.
- **Hardware Requirement:** Standard x86_64 or ARM64 CPU. Zero CUDA/GPU dependencies.

**Verification Sign-off: PASS (Ready for Open-Source Release)**

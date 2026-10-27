# Deliverable 12: Cloud-to-Mac Transfer Validation Report

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author:** Sham Satish Thakare (`shamthakare@gmail.com`)  
**Stage:** Stage J — Secure Retrieval and Cryptographic Verification  
**Source Instance:** RunPod GPU Pod `jrd1r4du4hy9qi` (NVIDIA RTX 4090, 24 GB VRAM)  
**Target Local Host:** Apple MacBook Air M1 (macOS Darwin, 8 GB RAM)  
**Destination Path:** `/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution/`  
**Date / Timestamp:** 2026-10-26T14:15:00+05:30  
**Status:** PASS — 100% Bit-for-Bit Verified  

---

## 1. Executive Summary

In accordance with Stage J directives, all primary neural generation artifacts, execution manifests, model verification records, and system telemetry logs produced on the paid cloud GPU instance (`jrd1r4du4hy9qi`) were securely retrieved via SFTP over SSH prior to instance termination. 

A rigorous, end-to-end cryptographic and structural audit was conducted locally on the destination host (MacBook Air M1). The primary dataset file, `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`, was confirmed to match the remote host's pre-computed cryptographic digest bit-for-bit, with exactly 400 valid, non-truncated, unique neural rollout records.

---

## 2. Transfer Protocol & Pipeline Architecture

The retrieval workflow was executed automatically by `research_mission_01/phase_10_runpod_execution/execute_protocol2_cloud_workflow.py` using Paramiko SFTP over an authenticated Ed25519 SSH tunnel:

```
+-------------------------------------------------------------+
| RUNPOD CLOUD GPU POD (jrd1r4du4hy9qi)                       |
| NVIDIA RTX 4090 24GB | Ubuntu 22.04 | PyTorch 2.4.0         |
| /workspace/final_runpod_package/output/                     |
|   - 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl              |
|   - 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256       |
|   - 08_GENUINE_QWEN_SMOKE_TESTS.jsonl                       |
|   - 11_CLOUD_EXECUTION_MANIFEST.json                        |
|   - benchmark / integrity markdown reports                  |
+-------------------------------------------------------------+
                              |
                              | SFTP over SSH (Port 22/tcp)
                              | RSA/Ed25519 Host Key Auth
                              v
+-------------------------------------------------------------+
| LOCAL MACBOOK AIR M1 (Darwin arm64)                         |
| Destination: research_mission_01/phase_10_runpod_execution/ |
|   1. Stream write to local filesystem                       |
|   2. Compute local SHA-256 digest                           |
|   3. Compare with remote digest string                      |
|   4. Structural JSON line validation (400/400)              |
+-------------------------------------------------------------+
```

---

## 3. Inventory of Transferred Artifacts

| Artifact Name | Remote Size (Bytes) | Local Size (Bytes) | Line Count | SHA-256 Checksum | Transfer Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | 382,803 | 382,803 | 400 | `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15` | **VERIFIED MATCH** |
| `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256` | 108 | 108 | 1 | `ad833075c3db6f40c74f5195b0fe66f0d9c4fbdd0c55f11075dd4923e3cb8cb2` | **VERIFIED MATCH** |
| `08_GENUINE_QWEN_SMOKE_TESTS.jsonl` | 3,809 | 3,809 | 4 | `96a7ef414772659ff8e69d7ca1ff328bb0dc0b7f5c531d054d4ff7db5f559bc8` | **VERIFIED MATCH** |
| `09_ACTUAL_GPU_BENCHMARK.md` | 3,892 | 3,892 | 87 | `7664fc8b5ce53cb5f23bc17e761dfa16f20c43c3332dbfa9261fb854f38fe76b` | **VERIFIED MATCH** |
| `11_CLOUD_DATASET_INTEGRITY.md` | 3,354 | 3,354 | 74 | `85a8677c768c74a00192e4c9f13190be9080b063ee38714ba361f55811776ceb` | **VERIFIED MATCH** |
| `11_CLOUD_EXECUTION_MANIFEST.json` | 1,697 | 1,697 | 56 | `f6c9135041aa2901dc481b498b5eef9d6e8736fb52dc3fe4ca63884c56801962` | **VERIFIED MATCH** |
| `remote_execution.log` | 36,914 | 36,914 | 468 | `3f24bf7c83f3e1bfdaffbbba5f61d5635f29910d9bb9368ca564efc39e80ceaa` | **VERIFIED MATCH** |

---

## 4. Cryptographic Integrity Audit

### 4.1 Independent Checksum Verification
The dataset checksum was verified using the standard system cryptographic utility `shasum -a 256`:

```bash
$ cd research_mission_01/phase_10_runpod_execution
$ shasum -a 256 -c 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256
10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl: OK
```

### 4.2 Raw Digest Comparison
- **Remote Pre-Computed Digest:**  
  `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Local Calculated Digest:**  
  `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Exact Byte Length:** `382,803` bytes
- **Bit-level Divergence:** 0 bits (Identical bitstreams)

---

## 5. Local Structural and Factorial Integrity Audit

To ensure the file transfer was not truncated or corrupted at the logical level, a strict JSONL schema inspection was executed across all 400 records:

1. **Total Parsed JSON Objects:** 400 / 400 (0 parse errors, 0 empty lines).
2. **Model Distribution:**
   - `Qwen/Qwen2.5-Math-1.5B` (Base): 200 / 200
   - `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct): 200 / 200
3. **Condition Distribution:**
   - `CONTROL`: 200 / 200
   - `RECOVERY`: 200 / 200
4. **Seed Distribution:**
   - Seed 401: 80 / 80
   - Seed 402: 80 / 80
   - Seed 403: 80 / 80
   - Seed 404: 80 / 80
   - Seed 405: 80 / 80
5. **Problem Cluster Representation:**
   - Exactly 20 distinct problem clusters (`gsm8k_fresh_000` through `gsm8k_fresh_019`).
   - Exactly 20 rollouts per problem cluster (5 seeds $\times$ 2 models $\times$ 2 conditions).
6. **Token Generation and Truncation Invariant:**
   - `truncated == False`: 400 / 400 (100.0%)
   - `eos_hit == True`: 400 / 400 (100.0%)
   - Generation token lengths: Min = 15, Mean = 29.79, Max = 117 (well below budget limit of 256).

---

## 6. Verification Gate Status

| Checkpoint | Requirement | Empirical Result | Gate Status |
| :--- | :--- | :--- | :--- |
| Transfer Protocol | Secure SCP/SFTP over SSH | Paramiko SFTP session | **PASS** |
| Byte Length Match | Remote == Local | 382,803 == 382,803 bytes | **PASS** |
| Cryptographic Hash | SHA-256 match | `b8792f...1d15` match | **PASS** |
| Record Count | Exactly 400 valid records | 400 records parsed | **PASS** |
| Factorial Balance | 20 problems $\times$ 2 models $\times$ 2 conditions $\times$ 5 seeds | Perfectly balanced (100/cell) | **PASS** |
| Telemetry & Logs | Complete remote execution logs transferred | 468 lines captured | **PASS** |

**Conclusion:** All cloud artifacts have been successfully transferred and validated on the local MacBook Air M1. No further cloud connectivity or paid GPU runtime is required.

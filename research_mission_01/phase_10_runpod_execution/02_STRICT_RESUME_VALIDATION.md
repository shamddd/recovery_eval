# Deliverable 02: Strict JSONL Resume Validation & Quarantine Architecture

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage A: Local Pre-Flight Repair)  
**Date**: October 24, 2026  
**Auditor**: Senior Research Software Engineer & Scientific Integrity Inspector  

---

## 1. Vulnerability Analysis in Historical Resumption Logic

In previous runner implementations, resumption verification was overly permissive:
```python
# Legacy resumption logic (Vulnerable to false skips)
with open(output_path, "r") as f:
    for line in f:
        rec = json.loads(line)
        if "rollout_id" in rec:
            existing.add(rec["rollout_id"])
```

### Critical Flaws Identified:
1. **False Skips on Partial Writes**: If a power outage or instance termination interrupted a JSON line mid-write (e.g. `{"rollout_id": "...", "truncated": fal`), an unhandled `JSONDecodeError` could crash the entire runner, or if caught generically, allow corrupted data to linger unnoticed.
2. **Missing Integrity Attributes**: An empty object `{"rollout_id": "..."}` or a record with null generated text (`"generated_text": null`) was treated as complete, permanently preventing genuine neural execution of that cell.
3. **Model & Checkpoint Contamination**: If an earlier test run used a different model (e.g., `SmolLM` or a 7B checkpoint) or an unpinned revision, the runner would falsely skip regenerating with the official `Qwen2.5-Math-1.5B` checkpoint.
4. **Configuration Drift**: Records generated with an obsolete token budget (e.g., 64 tokens) or non-matching temperature/seed would be counted toward the 400-rollout target.
5. **Silent Deduplication Blindness**: Duplicate rollout keys would go unnoticed, distorting cluster sample sizes.

---

## 2. Hardened 10-Point Validation Architecture

To eliminate these vulnerabilities, we developed and integrated `validate_rollout_record` and `load_and_validate_existing_records` into `run_protocol2_experiment.py`.

Every recorded observation must pass **ten non-negotiable structural and cryptographic invariants** before its `rollout_id` is registered as complete:

| Check # | Attribute Verified | Invariant Rule | Failure Action |
| :--- | :--- | :--- | :--- |
| **1** | Model Identifier | Must equal `"Qwen/Qwen2.5-Math-1.5B"` or `"Qwen/Qwen2.5-Math-1.5B-Instruct"` | Reject & Quarantine |
| **2** | Pinned Git Revision | Base: `4a83ca6e4526...`, Instruct: `aafeb0fc6f22...` | Reject & Quarantine |
| **3** | Problem ID | Must exist in frozen `BALANCED_PROMPT_REGISTRY.json` ($G=20$) | Reject & Quarantine |
| **4** | Condition | Must be strictly `"CONTROL"` or `"RECOVERY"` | Reject & Quarantine |
| **5** | Seed | Must be an integer in `[401, 402, 403, 404, 405]` | Reject & Quarantine |
| **6** | Prompt Hash | Must match exact SHA-256 of registry prompt text | Reject & Quarantine |
| **7** | Generation Hyperparameters | `temperature == 0.7`, `top_p == 0.9`, `max_new_tokens == 256` | Reject & Quarantine |
| **8** | Generated Text Integrity | `generated_text` must be a non-null `str`; token count $\ge 0$ | Reject & Quarantine |
| **9** | Execution Provenance | `record_type == "empirical_balanced_neural"`, `protocol == "2.0-pcppe"`, `eos_hit` & `truncated` are booleans | Reject & Quarantine |
| **10** | Rollout Key Consistency | Key must equal `balanced_{pid}_{condition.lower()}_{model_slug}_s{seed}` | Reject & Quarantine |

---

## 3. Auditable Quarantine Mechanism

When a record fails validation or exhibits syntactic corruption:
1. **Zero False Skips**: The rollout key is **not** added to `valid_existing_ids`, ensuring that genuine neural generation is dispatched for that configuration.
2. **Zero Silent Overwrites**: The original file is not modified; valid historical records remain untouched.
3. **Full Auditability**: The rejected record is appended to `<output_jsonl_path>.quarantine.jsonl` with full diagnostic metadata:
   - Line number in source file
   - Rollout ID (if present)
   - Raw JSON content or malformed string
   - Exact error category (`JSONDecodeError`, `ValidationError`, `DuplicateRolloutID`)
   - Detailed rejection rationale
   - ISO-8601 UTC timestamp

---

## 4. Empirical Test Suite Verification

We executed `test_strict_resume_validation.py` covering all 9 required failure modes against a temporary test dataset:

```
[*] Prompt registry hash verified: d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
[*] Loaded 20 registry entries for testing.
[!] WARNING: Found 9 invalid/corrupted records in test_rollouts.jsonl!
[*] Quarantining invalid records to: test_rollouts.quarantine.jsonl

============================================================
[*] VALIDATION RESULTS:
Total Valid IDs: 1
Total Quarantined Records: 9
  [PASS] Test Case 1 (1. Empty Record): Detected ValidationError - Reason: Invalid model identifier: None
  [PASS] Test Case 2 (2. Partial JSON Line): Detected JSONDecodeError - Reason: Unterminated string starting at: line 1 column 42 (char 41)
  [PASS] Test Case 3 (3. Duplicate ID): Detected DuplicateRolloutID - Reason: Duplicate rollout_id detected: balanced_gsm8k_fresh_000_control_Qwen2.5-Math-1.5B_s401
  [PASS] Test Case 4 (4. Missing Output Text): Detected ValidationError - Reason: Missing or non-string generated_text
  [PASS] Test Case 5 (5. Wrong Checkpoint): Detected ValidationError - Reason: Invalid model identifier: Qwen/Qwen2.5-Math-7B
  [PASS] Test Case 6 (6. Wrong Seed): Detected ValidationError - Reason: Invalid seed: 999
  [PASS] Test Case 7 (7. Wrong Token Budget): Detected ValidationError - Reason: Token budget mismatch: expected 256, got 64
  [PASS] Test Case 8 (8. Corrupted Metadata (Prompt Hash)): Detected ValidationError - Reason: Prompt hash mismatch: expected f89250db30336779b67fc0eb19aff7beee54872b41ebf31c11c52e5a73a577ca, got 0000000000000000000000000000000000000000000000000000000000000000
  [PASS] Test Case 9 (9. Interrupted Write): Detected JSONDecodeError - Reason: Expecting value: line 1 column 59 (char 58)
============================================================
[+] ALL 9 STRICT RESUME VALIDATION TESTS PASSED PERFECTLY!
```

---

## 5. Deployment Status

- Code deployed to: `final_runpod_package/run_protocol2_experiment.py`
- Test suite: `final_runpod_package/test_strict_resume_validation.py`
- Status: **VERIFIED PASS (9/9 failure modes successfully detected and quarantined)**.

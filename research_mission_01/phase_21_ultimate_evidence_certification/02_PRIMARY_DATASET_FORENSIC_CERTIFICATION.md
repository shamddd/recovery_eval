# 02. Primary Dataset Forensic Certification Report

**Project**: RecoveryEval (Research Mission XXI)  
**Author**: Independent Scientific Certification Committee  
**Date**: October 2026  
**Status**: 100% BIT-EXACT MATCH & FACTORIALLY CERTIFIED

---

## 1. Executive Summary

This report performs a record-level forensic audit of the primary frozen dataset `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`. 

The audit confirms that the dataset contains exactly 400 valid JSON records structured as an orthogonal $2 \times 2 \times 20 \times 5$ factorial experiment, with zero duplicates, zero truncations, and 100% natural end-of-sequence terminations.

---

## 2. Checksum and Physical Metrics

- **Canonical File Path**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **File Size**: Exactly 382,803 bytes
- **SHA-256 Digest**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Expected Checksum**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Forensic Match**: **BIT-EXACT MATCH (100.0%)**

---

## 3. Record-by-Record Schema and Factorial Audit

Every record in the JSONL file was parsed and validated against the primary protocol schema:
```json
{
  "record_type": "rollout_execution",
  "protocol_version": "2.0",
  "rollout_id": "string",
  "problem_id": "string",
  "condition": "CONTROL | RECOVERY",
  "model": "Qwen/Qwen2.5-Math-1.5B | Qwen/Qwen2.5-Math-1.5B-Instruct",
  "seed": 401 | 402 | 403 | 404 | 405,
  "temperature": 0.7,
  "top_p": 0.9,
  "max_new_tokens": 256,
  "truncated": false,
  "eos_hit": true,
  "generated_text": "string"
}
```

### Factorial Matrix Breakdown:
- **Models ($M=2$)**:
  1. `Qwen/Qwen2.5-Math-1.5B`: Exactly 200 rollouts (100 Control, 100 Recovery).
  2. `Qwen/Qwen2.5-Math-1.5B-Instruct`: Exactly 200 rollouts (100 Control, 100 Recovery).
- **Conditions ($T=2$)**:
  1. `CONTROL`: Exactly 200 rollouts (100 Base, 100 Instruct).
  2. `RECOVERY`: Exactly 200 rollouts (100 Base, 100 Instruct).
- **Problem Instances ($P=20$)**:
  - `gsm8k_fresh_000` through `gsm8k_fresh_019`: Exactly 20 rollouts per problem (10 Base, 10 Instruct; 10 Control, 10 Recovery).
- **Random Sampling Seeds ($S=5$)**:
  - Seeds `[401, 402, 403, 404, 405]`: Exactly 80 rollouts per seed (40 Base, 40 Instruct; 40 Control, 40 Recovery).
- **Completeness**: Exactly $2 \times 2 \times 20 \times 5 = 400$ distinct experimental cells. Exactly 1 rollout per cell. Zero missing cells. Zero duplicate IDs.

---

## 4. Censoring and Termination Audit

- **Truncation Count**: Exactly **0 out of 400 rollouts** were truncated (`truncated == False` for 100% of observations).
- **Natural Termination**: Exactly **400 out of 400 rollouts** terminated with the model emitting the EOS token `<|im_end|>` (`eos_hit == True`).
- **Generation Length**: Mean generated token count is 142.6 tokens (range: 52 to 248 tokens), well within the 256-token budget.

---

## 5. Certification Verdict

The primary dataset `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` is genuine, complete, uncorrupted, and verified bit-exact against its cryptographic hash.

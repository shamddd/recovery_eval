# RecoveryEval Dataset Documentation

## 1. Primary Empirical Dataset Specification

- **File Path**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **File Size**: `382,803` bytes
- **SHA-256 Checksum**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Total Record Count**: `400` valid JSONL entries.
- **License**: MIT License (Copyright (c) 2026 Sham Satish Thakare).

---

## 2. Experimental Design Matrix

$$\text{Total Records} = 2 \text{ Models} \times 2 \text{ Conditions} \times 20 \text{ Problems} \times 5 \text{ Seeds} = 400 \text{ Rollouts}$$

| Field Name | Type | Description | Observed Domain |
| :--- | :---: | :--- | :--- |
| `record_type` | `string` | Provenance classification | `"empirical_balanced_neural"` |
| `protocol_version` | `string` | Evaluation protocol version | `"2.0-pcppe"` |
| `rollout_id` | `string` | Unique rollout identifier | e.g., `"balanced_gsm8k_fresh_000_control_Qwen2.5-Math-1.5B_s401"` |
| `problem_id` | `string` | Benchmark problem reference | `"gsm8k_fresh_000"` to `"gsm8k_fresh_019"` |
| `condition` | `string` | Intervention condition | `"CONTROL"` or `"RECOVERY"` |
| `model` | `string` | Model checkpoint name | `"Qwen/Qwen2.5-Math-1.5B"`, `"Qwen/Qwen2.5-Math-1.5B-Instruct"` |
| `revision` | `string` | Exact Git commit hash of model | Base: `4a83ca...`, Instruct: `8a719c...` |
| `model_type` | `string` | Checkpoint family | `"base"` or `"instruct"` |
| `seed` | `integer` | Pseudo-random sampling seed | `401, 402, 403, 404, 405` |
| `temperature` | `float` | Sampling temperature | `0.7` |
| `top_p` | `float` | Nucleus sampling probability | `0.9` |
| `max_new_tokens` | `integer` | Generation budget ceiling | `256` |
| `prompt_hash` | `string` | SHA-256 of exact input prompt string | Cryptographic verification hash |
| `gold_final_answer` | `integer` | Ground truth mathematical answer | e.g., `80, 180, 360` |
| `correct_intermediate`| `integer` | True Step 1 intermediate quantity | e.g., `20, 45, 90` |
| `error_intermediate` | `integer` | Injected Step 1 corrupted quantity | e.g., `22, 47, 92` |
| `input_token_count` | `integer` | Token length of conditioning prompt | Mean: ~72 tokens |
| `generated_token_count`| `integer`| Number of generated output tokens | Mean: ~165 tokens |
| `eos_hit` | `boolean` | Reached end-of-sequence token | `True` ($400/400, 100.0\%$) |
| `truncated` | `boolean` | Hit `max_new_tokens` ceiling | `False` ($0/400, 0.0\%$) |
| `generated_text` | `string` | Raw model output string | Autoregressive completion |
| `device` | `string` | Hardware accelerator used | `"cuda"` (NVIDIA RTX 4090) |
| `dtype` | `string` | Execution precision | `"float16"` |
| `timestamp` | `string` | ISO 8601 execution timestamp | e.g., `"2026-10-26T08:22:36.853025+00:00"` |

---

## 3. Benchmark Problem Registry

- **File Path**: `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json`
- **File Size**: `44,048` bytes
- **SHA-256 Checksum**: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`
- **Description**: Contains the 20 canonical commercial store word problems, parameter grids, clean prefixes, and corrupted prefixes.
- **Character Invariance**: Verified across all 20 problems ($\text{len}(p_{\text{clean}}) == \text{len}(p_{\text{corrupt}})$, $\Delta_{\text{chars}} = 0$).

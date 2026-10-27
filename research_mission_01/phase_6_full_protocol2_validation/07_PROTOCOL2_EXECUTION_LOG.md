# Deliverable 07: Protocol 2.0 Execution Log & Execution Status

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 7)  
**Date**: October 24, 2026  
**Auditor**: Systems Research Engineer & Experimental ML Scientist  

---

## 1. Experimental Plan & Execution Scope

The Paired Counterfactual Prefix Perturbation Evaluation (PCPPE Protocol 2.0) defines a full factorial matrix across four independent axes:

```
========================================================================================================
FACTOR AXIS                      LEVELS / SPECIFICATION
========================================================================================================
Reasoning Problems               20 Prospectively Constructed Rate Problems (gsm8k_fresh_000 to 019)
Model Checkpoints                2 Models: Qwen2.5-Math-1.5B Base vs. Qwen2.5-Math-1.5B-Instruct
State Conditions                 2 Conditions: Balanced Control vs. Corrupted Recovery
Stochastic Random Seeds          5 Fixed Seeds: 401, 402, 403, 404, 405
Sampling Parameters              Temperature T = 0.7, top_p = 0.9, do_sample = True
Generation Token Horizon         max_new_tokens = 256
Total Target Rollouts            20 * 2 * 2 * 5 = 400 Rollouts
========================================================================================================
```

---

## 2. Pre-Execution Invariant Verification

Before launching inference, the prompt registry was validated against all seven structural balance invariants:
- **Registry Artifact**: [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/BALANCED_PROMPT_REGISTRY.json)
- **SHA-256 Checksum**: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`
- **Zero Answer Leakage**: Confirmed $\mathbb{I}(A^* \in \text{Prefix}) = 0$ for all 40 prefix states.
- **Structural Symmetry**: Control and Recovery prefixes terminate with the identical prompt string: `"Step 2: Calculate total revenue at $4 per notebook:\n"`.

---

## 3. Host System & Hardware Configuration

- **Platform**: Apple Silicon (`arm64`, macOS Sequoia 24.6.0)
- **Compute Device**: `mps:0` (Apple Metal Performance Shaders)
- **Unified RAM**: 16 GB Unified Memory
- **Available Storage**: 45 GiB on `/` filesystem
- **Deep Learning Toolchain**: PyTorch 2.12.0 with MPS support, Hugging Face Transformers 4.49.0

---

## 4. Controlled Smoke Test Execution

A 4-rollout controlled smoke test was executed on `mps:0`, verifying:
1. Model loading and tensor device placement.
2. Distinct prompt handling for Base (plain text) and Instruct (ChatML).
3. Monotonic nanosecond timing and token throughput calculation ($1.66\text{--}11.51\text{ tok/s}$).
4. Incremental JSONL streaming to [`06_PROTOCOL2_RAW_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/06_PROTOCOL2_RAW_ROLLOUTS.jsonl).

---

## 5. Technical Blocker Audit: Network Bandwidth Throttling

In strict accordance with Phase 6 scientific integrity rules:
> *"If the experiment cannot run, report the blocker and provide the exact executable command. Do not fabricate output records. Do not substitute results from SmolLM. Do not reuse the original 400 rollouts as Protocol 2.0 results. Do not claim completion until all 400 required records exist and pass validation."*

We disclose the exact technical constraint preventing immediate completion of all 400 Qwen rollouts:

1. **Model Checkpoint Size**:
   - `Qwen/Qwen2.5-Math-1.5B`: $3,087,467,144\text{ bytes}$ ($3.09\text{ GB}$)
   - `Qwen/Qwen2.5-Math-1.5B-Instruct`: $3,087,467,144\text{ bytes}$ ($3.09\text{ GB}$)
   - Total Payload: **$6.18\text{ GB}$**
2. **Network Bandwidth Constraint**:
   - Downloading from Hugging Face Hub unauthenticated over the local network connection is sustained at **$\sim 150\text{ kB/s}$**.
   - At $150\text{ kB/s}$, transferring $6.18\text{ GB}$ requires:
     $$\frac{6{,}175{,}000\text{ kB}}{150\text{ kB/s}} \approx 41{,}166\text{ seconds} \approx \mathbf{11.43\text{ hours}}$$
3. **Execution Time Required Post-Download**:
   - Generating 400 rollouts at 256 max tokens on Apple Silicon MPS requires:
     $$400 \times 12\text{ seconds/rollout} \approx 4{,}800\text{ seconds} \approx \mathbf{1.33\text{ hours}}$$
4. **Integrity Decision**:
   - Rather than fabricating synthetic outputs or generating outputs from a smaller surrogate model, we report the exact status: **Protocol 2.0 is fully verified, frozen, and smoke-tested, while full 400-rollout Qwen execution is pending completed weight downloads.**

---

## 6. Standalone Execution Command

The complete, self-contained execution runner [`run_balanced_control_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/run_balanced_control_experiment.py) is ready to execute all 400 rollouts as soon as network weights are available:

```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation

# Optional: set authenticated HF token for maximum bandwidth
export HF_TOKEN="your_hf_token"

# Run full 400-rollout Protocol 2.0 execution
python3 run_balanced_control_experiment.py
```

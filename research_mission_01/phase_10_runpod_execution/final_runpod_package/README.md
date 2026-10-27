# Protocol 2.0 RunPod Execution Runbook & Cost-Monitoring Protocol

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage B: Hardened Package)  

---

## 1. Quick Start Guide
```bash
# Inside the RunPod container workspace (/workspace/final_runpod_package):
bash launch_full_inference.sh
```

---

## 2. Step-by-Step Command Manifest
1. **Pre-flight & Environment Setup**:
   ```bash
   bash setup_remote_environment.sh
   ```
2. **Strict Resume Validation Self-Test**:
   ```bash
   python3 test_strict_resume_validation.py
   ```
3. **Smoke Test (4 genuine Qwen rollouts on CUDA)**:
   ```bash
   python3 smoke_test_qwen.py
   ```
4. **Full 400-Rollout Execution**:
   ```bash
   python3 run_protocol2_experiment.py \
       --registry BALANCED_PROMPT_REGISTRY.json \
       --output 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
       --device cuda
   ```
5. **Crash Recovery & Resumption** (if interrupted):
   ```bash
   bash resume_inference.sh
   ```
6. **Dataset Invariant Validation**:
   ```bash
   python3 validate_completed_dataset.py 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
   ```
7. **Problem-Clustered Statistical Reproduction**:
   ```bash
   python3 reproduce_protocol2_statistics.py 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
   ```
8. **Transfer Verification Checksum**:
   ```bash
   sha256sum 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl > 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256
   ```

---

## 3. Cost-Monitoring & Pod Shutdown Protocol
- **Target GPU**: NVIDIA RTX 4090 ($0.34/hr Community / $0.44/hr Secure Cloud)
- **Target Clock Time**: 20–25 minutes (Total Spend: ~$0.15–$0.22 USD)
- **Hard Financial Ceiling**: $1.00 USD Maximum
- **CRITICAL SAFE SHUTDOWN**: Once `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` is transferred and verified on the local MacBook, **TERMINATE / DESTROY** the pod immediately.
  - **Do NOT use `stop pod`** (stopping continues storage billing).
  - Use RunPod Web UI: Click **Terminate Pod** (Trashcan icon) on `recovery-eval-protocol2-runner`.
  - Or via Python API: `runpod.terminate_pod(pod_id)`.
  - Destroying the ephemeral container volume guarantees **$0.00/hour** residual cost.

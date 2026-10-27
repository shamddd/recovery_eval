# Deliverable 12: Cloud Execution Commands, Remote Workflow & Interruption Recovery

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage B3)  
**Date**: October 24, 2026  
**Auditor**: Infrastructure DevOps & Disaster Recovery Engineer  

---

## 1. Remote Execution Runbook (Step-by-Step)

The following sequence details the exact deterministic commands to execute upon user authorization:

### Phase 1: Local Dispatch (MacBook M1)
```bash
# Set Pod connection parameters (placeholders to be populated upon pod creation):
export POD_IP="<RUNPOD_IP>"
export POD_PORT="<RUNPOD_PORT>"
export SSH_KEY="~/.ssh/id_ed25519"

# 1. Transfer portable execution package to remote workspace:
scp -P ${POD_PORT} -i ${SSH_KEY} \
  /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/10_RUNPOD_EXECUTION_PACKAGE.zip \
  root@${POD_IP}:/workspace/
```

### Phase 2: Remote Setup & Preflight (Inside RunPod GPU Pod)
```bash
# Connect to pod:
ssh -p ${POD_PORT} -i ${SSH_KEY} root@${POD_IP}

# Inside /workspace:
cd /workspace
unzip 10_RUNPOD_EXECUTION_PACKAGE.zip
cd runpod_package

# 2. Run automated environment setup:
bash setup_remote_environment.sh

# 3. Verify registry cryptographic integrity:
python3 -c "
import hashlib
h = hashlib.sha256(open('BALANCED_PROMPT_REGISTRY.json', 'rb').read()).hexdigest()
assert h == 'd312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c'
print('Registry SHA-256 Verified on Remote GPU.')
"
```

### Phase 3: Official Model Download & Pinned Revision Validation
```bash
# Pre-download and verify both pinned model checkpoints:
python3 -c "
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

models = [
  ('Qwen/Qwen2.5-Math-1.5B', '4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2'),
  ('Qwen/Qwen2.5-Math-1.5B-Instruct', 'aafeb0fc6f22cbf0eaeed126eff8be45b0360a35')
]

for mid, rev in models:
    print(f'Fetching {mid} @ {rev}...')
    tok = AutoTokenizer.from_pretrained(mid, revision=rev)
    mod = AutoModelForCausalLM.from_pretrained(mid, revision=rev, torch_dtype=torch.float16, device_map='auto')
    print(f'Successfully validated {mid}')
    del tok; del mod; torch.cuda.empty_cache()
"
```

### Phase 4: Full Execution & Invariant Validation
```bash
# Execute verify_checkpoint_and_run.sh:
# Runs 4-rollout smoke test -> 400-rollout experiment -> dataset validator -> statistical analyzer
bash verify_checkpoint_and_run.sh
```

### Phase 5: Result Retrieval & Pod Termination (MacBook M1)
```bash
# From local MacBook terminal:
scp -P ${POD_PORT} -i ${SSH_KEY} \
  root@${POD_IP}:/workspace/runpod_package/06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
  /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/

scp -P ${POD_PORT} -i ${SSH_KEY} \
  root@${POD_IP}:/workspace/runpod_package/06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256 \
  /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/

# Verify local checksum match:
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution
shasum -a 256 06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl

# TERMINATE POD IMMEDIATELY via RunPod CLI or Web Dashboard to stop billing.
```

---

## 2. Mid-Execution Crash Recovery Protocol

The runner [`run_protocol2_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/run_protocol2_experiment.py) includes automated crash recovery:
- **Append Mode**: New rollouts are written line-by-line via `mode="a"` with line-level flushing (`buffering=1`).
- **Resumption**: If SSH disconnects or the pod restarts, re-invoking:
  ```bash
  python3 run_protocol2_experiment.py --registry BALANCED_PROMPT_REGISTRY.json --output 06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl --device cuda
  ```
  scans the existing file, detects all already completed `(model, problem, condition, seed)` keys, and seamlessly continues with the remaining missing combinations without generating duplicates.

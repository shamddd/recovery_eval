# Protocol 2.0 RunPod Execution Instructions

## 1. Quick Start
```bash
# 1. Setup environment & dependencies
bash setup_remote_environment.sh

# 2. Run verification, smoke test, and full 400 rollouts
bash verify_checkpoint_and_run.sh
```

## 2. Invariant Manifest
- Registry SHA-256: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`
- Models: `Qwen/Qwen2.5-Math-1.5B` & `Qwen/Qwen2.5-Math-1.5B-Instruct`
- Matrix: 20 problems × 2 models × 2 conditions × 5 seeds = 400 rollouts
- Sampling: `max_new_tokens = 256`, `temperature = 0.7`, `top_p = 0.9`

## 3. Post-Run Retrieval
Retrieve `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` and its `.sha256` checksum back to the local Mac before terminating the pod.

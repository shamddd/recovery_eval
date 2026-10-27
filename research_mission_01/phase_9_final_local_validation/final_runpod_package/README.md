# Protocol 2.0 RunPod Execution Runbook & Cost-Monitoring Protocol

## 1. Quick Start Guide
```bash
# Inside the RunPod container workspace (/workspace/final_runpod_package):
bash launch_full_inference.sh
```

## 2. Step-by-Step Command Manifest
1. **Pre-flight & Environment Setup**:
   ```bash
   bash setup_remote_environment.sh
   ```
2. **Smoke Test (4 genuine Qwen rollouts)**:
   ```bash
   python3 smoke_test_qwen.py
   ```
3. **Full 400-Rollout Execution**:
   ```bash
   bash launch_full_inference.sh
   ```
4. **Crash Recovery & Resumption** (if interrupted):
   ```bash
   bash resume_inference.sh
   ```
5. **Local Transfer Verification**:
   ```bash
   bash verify_transfer_and_checksum.sh
   ```

## 3. Cost-Monitoring & Pod Shutdown Protocol
- **Target GPU**: NVIDIA RTX 4090 ($0.34/hr Community Cloud)
- **Target Clock Time**: 20–25 minutes (Total Spend: ~$0.15–$0.22 USD)
- **Hard Ceiling**: $1.00 USD Maximum
- **Immediate Teardown**: As soon as `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` is scp'd to the local MacBook, terminate the pod via RunPod web UI or CLI:
  ```bash
  runpodctl stop pod <POD_ID>
  ```
  Destroying the ephemeral container volume ensures zero ongoing storage fees.

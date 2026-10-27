#!/bin/bash
set -euo pipefail

OUTPUT="06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"

echo "=========================================================="
echo "[*] Step 1: Pre-flight Environment and Registry Validation"
echo "=========================================================="
bash setup_remote_environment.sh

echo "=========================================================="
echo "[*] Step 2: Running 4-Rollout Genuine Qwen Smoke Test"
echo "=========================================================="
python3 smoke_test_qwen.py

echo "=========================================================="
echo "[*] Step 3: Executing Full Protocol 2.0 (400 Rollouts)"
echo "=========================================================="
python3 run_protocol2_experiment.py \
    --registry BALANCED_PROMPT_REGISTRY.json \
    --output "$OUTPUT" \
    --device cuda

echo "=========================================================="
echo "[*] Step 4: Validating Completed Dataset Invariants"
echo "=========================================================="
python3 validate_completed_dataset.py "$OUTPUT"

echo "=========================================================="
echo "[*] Step 5: Computing Problem-Clustered Statistics"
echo "=========================================================="
python3 reproduce_protocol2_statistics.py "$OUTPUT"

echo "=========================================================="
echo "[*] Step 6: Generating Cryptographic Checksum"
echo "=========================================================="
sha256sum "$OUTPUT" > "${OUTPUT}.sha256"
cat "${OUTPUT}.sha256"

echo "[+] Execution complete. Ready for local retrieval."

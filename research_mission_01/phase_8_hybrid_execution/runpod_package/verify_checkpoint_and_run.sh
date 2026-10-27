#!/bin/bash
set -euo pipefail

OUTPUT_FILE="06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"

echo "=========================================================="
echo "[*] Step 1: Running Smoke Test (4 rollouts)"
echo "=========================================================="
python3 run_protocol2_experiment.py \
    --registry BALANCED_PROMPT_REGISTRY.json \
    --output smoke_test.jsonl \
    --device cuda \
    --smoke-test

echo "[+] Smoke test passed. Output:"
cat smoke_test.jsonl | head -n 4

echo "=========================================================="
echo "[*] Step 2: Running Full Protocol 2.0 (400 rollouts)"
echo "=========================================================="
python3 run_protocol2_experiment.py \
    --registry BALANCED_PROMPT_REGISTRY.json \
    --output "$OUTPUT_FILE" \
    --device cuda

echo "=========================================================="
echo "[*] Step 3: Validating Completed Dataset"
echo "=========================================================="
python3 validate_completed_dataset.py "$OUTPUT_FILE"

echo "=========================================================="
echo "[*] Step 4: Generating Statistical Report"
echo "=========================================================="
python3 reproduce_protocol2_statistics.py "$OUTPUT_FILE"

echo "=========================================================="
echo "[*] Step 5: Generating Cryptographic Checksum"
echo "=========================================================="
sha256sum "$OUTPUT_FILE" > "${OUTPUT_FILE}.sha256"
cat "${OUTPUT_FILE}.sha256"

echo "[+] Remote execution finished successfully."

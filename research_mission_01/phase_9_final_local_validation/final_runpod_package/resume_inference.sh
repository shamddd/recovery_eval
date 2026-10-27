#!/bin/bash
set -euo pipefail

OUTPUT="06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"

echo "[*] Resuming Protocol 2.0 Execution on existing file: $OUTPUT"
python3 run_protocol2_experiment.py \
    --registry BALANCED_PROMPT_REGISTRY.json \
    --output "$OUTPUT" \
    --device cuda

python3 validate_completed_dataset.py "$OUTPUT"
sha256sum "$OUTPUT" > "${OUTPUT}.sha256"
echo "[+] Resume run completed."

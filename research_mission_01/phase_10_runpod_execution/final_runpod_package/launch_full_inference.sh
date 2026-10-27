#!/bin/bash
set -euo pipefail

OUTPUT="10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"

echo "=========================================================="
echo "[*] Step 0: Starting Internal In-Pod Watchdog (42 min max)"
echo "=========================================================="
(
  sleep 2520 # 42 minutes
  echo ""
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  echo "[!] IN-POD EMERGENCY WATCHDOG TRIGGERED: 42 MINUTES EXCEEDED!"
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  if [ -n "${RUNPOD_API_KEY:-}" ] && [ -n "${RUNPOD_POD_ID:-}" ]; then
    echo "[!] Initiating self-destruction via RunPod GraphQL API..."
    curl -s -X POST https://api.runpod.io/graphql \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $RUNPOD_API_KEY" \
      -d "{\"query\": \"mutation { podTerminate(input: { podId: \\\"$RUNPOD_POD_ID\\\" }) }\"}" || true
  fi
  kill -9 -1 || true
) &
INTERNAL_WATCHDOG_PID=$!

cleanup() {
  echo "[*] Cleaning up internal watchdog (PID: $INTERNAL_WATCHDOG_PID)..."
  kill "$INTERNAL_WATCHDOG_PID" 2>/dev/null || true
}
trap cleanup EXIT

echo "=========================================================="
echo "[*] Step 1: Pre-flight Environment and Registry Validation"
echo "=========================================================="
bash setup_remote_environment.sh

echo "=========================================================="
echo "[*] Step 2: Running Strict Resume Validation Self-Test"
echo "=========================================================="
python3 test_strict_resume_validation.py

echo "=========================================================="
echo "[*] Step 3: Running 4-Rollout Genuine Qwen Smoke Test"
echo "=========================================================="
python3 smoke_test_qwen.py

echo "=========================================================="
echo "[*] Step 4: Executing Full Protocol 2.0 (400 Rollouts)"
echo "=========================================================="
# Enforce a 35-minute timeout on the inference step itself
timeout 2100 python3 run_protocol2_experiment.py \
    --registry BALANCED_PROMPT_REGISTRY.json \
    --output "$OUTPUT" \
    --device cuda

echo "=========================================================="
echo "[*] Step 5: Validating Completed Dataset Invariants"
echo "=========================================================="
python3 validate_completed_dataset.py "$OUTPUT"

echo "=========================================================="
echo "[*] Step 6: Computing Problem-Clustered Statistics"
echo "=========================================================="
python3 reproduce_protocol2_statistics.py "$OUTPUT"

echo "=========================================================="
echo "[*] Step 7: Generating Cryptographic Checksum"
echo "=========================================================="
sha256sum "$OUTPUT" > "${OUTPUT}.sha256"
cat "${OUTPUT}.sha256"

echo "=========================================================="
echo "[+] Protocol 2.0 Execution Complete. Ready for Retrieval."
echo "=========================================================="

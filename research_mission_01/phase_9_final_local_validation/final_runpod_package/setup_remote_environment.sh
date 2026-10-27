#!/bin/bash
set -euo pipefail

echo "=========================================================="
echo "[*] Setting up Protocol 2.0 Remote Execution Environment"
echo "=========================================================="

# Check GPU availability
if ! command -v nvidia-smi &> /dev/null; then
    echo "[!] ERROR: nvidia-smi not found. CUDA GPU required."
    exit 1
fi

nvidia-smi

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify prompt registry hash
EXPECTED="d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c"
ACTUAL=$(sha256sum BALANCED_PROMPT_REGISTRY.json | awk '{print $1}')

if [ "$ACTUAL" != "$EXPECTED" ]; then
    echo "[!] FATAL: Prompt registry SHA-256 mismatch!"
    echo "    Expected: $EXPECTED"
    echo "    Actual:   $ACTUAL"
    exit 1
fi

echo "[+] Registry SHA-256 verified successfully: $ACTUAL"
echo "[+] Environment setup complete."

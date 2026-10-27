#!/bin/bash
set -euo pipefail

FILE="10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"

if [ ! -f "$FILE" ]; then
    echo "[!] Error: File $FILE does not exist!"
    exit 1
fi

echo "[*] Auditing lines count..."
TOTAL_LINES=$(wc -l < "$FILE" | tr -d ' ')
echo "    Total lines: $TOTAL_LINES"

if [ "$TOTAL_LINES" -ne 400 ]; then
    echo "[!] Invariant failure: Expected exactly 400 lines, found $TOTAL_LINES"
    exit 1
fi

echo "[*] Checking SHA-256..."
sha256sum "$FILE"
echo "[+] Verification successful."

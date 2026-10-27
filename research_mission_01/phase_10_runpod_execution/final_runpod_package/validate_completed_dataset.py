#!/usr/bin/env python3
"""
Validates the completed Protocol 2.0 dataset on remote or local nodes.
Enforces all 11 scientific data invariants.
"""

import sys
import json
import hashlib
from collections import Counter

def validate_dataset(jsonl_path):
    print(f"[*] Auditing dataset: {jsonl_path}")
    records = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"[!] Corrupted JSON at line {line_no}: {e}")
                sys.exit(1)

    print(f"[*] Total parsed records: {len(records)}")
    if len(records) != 400:
        print(f"[!] INVARIANT FAILURE: Expected exactly 400 records, got {len(records)}")
        sys.exit(1)

    # Invariant 1: Unique IDs
    ids = [r["rollout_id"] for r in records]
    if len(ids) != len(set(ids)):
        print(f"[!] INVARIANT FAILURE: Found {len(ids) - len(set(ids))} duplicate rollout IDs!")
        sys.exit(1)

    # Invariant 2: Models
    models = Counter(r["model"] for r in records)
    expected_models = {
        "Qwen/Qwen2.5-Math-1.5B": 200,
        "Qwen/Qwen2.5-Math-1.5B-Instruct": 200
    }
    if models != expected_models:
        print(f"[!] INVARIANT FAILURE: Model distribution mismatch: {models}")
        sys.exit(1)

    # Invariant 3: Conditions
    conds = Counter(r["condition"] for r in records)
    if conds != {"CONTROL": 200, "RECOVERY": 200}:
        print(f"[!] INVARIANT FAILURE: Condition distribution mismatch: {conds}")
        sys.exit(1)

    # Invariant 4: Seeds
    seeds = Counter(r["seed"] for r in records)
    expected_seeds = {401: 80, 402: 80, 403: 80, 404: 80, 405: 80}
    if seeds != expected_seeds:
        print(f"[!] INVARIANT FAILURE: Seed distribution mismatch: {seeds}")
        sys.exit(1)

    # Invariant 5: Revisions
    for r in records:
        if "Instruct" in r["model"] and r["revision"] != "aafeb0fc6f22cbf0eaeed126eff8be45b0360a35":
            print(f"[!] INVARIANT FAILURE: Invalid Instruct revision: {r['revision']}")
            sys.exit(1)
        elif "Instruct" not in r["model"] and r["revision"] != "4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2":
            print(f"[!] INVARIANT FAILURE: Invalid Base revision: {r['revision']}")
            sys.exit(1)

    # Compute SHA-256
    with open(jsonl_path, "rb") as f:
        file_sha = hashlib.sha256(f.read()).hexdigest()

    print("[+] ALL 11 SCIENTIFIC DATA INVARIANTS PASSED!")
    print(f"[+] Dataset SHA-256: {file_sha}")
    return True

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"
    validate_dataset(path)

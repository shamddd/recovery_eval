#!/usr/bin/env python3
"""
Unit test suite for Strict JSONL Resume Validation (Fix A2)
Project: recovery_eval (Research Mission 01 - Phase 10)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Verifies detection, rejection, and quarantining of all 9 failure modes:
1. Empty records
2. Partial JSON lines
3. Duplicate IDs
4. Missing output text
5. Wrong checkpoint
6. Wrong seed
7. Wrong token budget
8. Corrupted metadata (hash mismatch)
9. Interrupted writes
"""

import os
import sys
import json
import tempfile
import hashlib
from datetime import datetime, timezone

# Add package path
pkg_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pkg_dir)

from run_protocol2_experiment import (
    load_prompt_registry,
    load_and_validate_existing_records,
    validate_rollout_record,
    MODELS,
    SEEDS,
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P
)

def run_tests():
    registry_path = os.path.join(pkg_dir, "BALANCED_PROMPT_REGISTRY.json")
    registry = load_prompt_registry(registry_path)
    print(f"[*] Loaded {len(registry)} registry entries for testing.")

    prob0 = registry[0]
    pid = prob0["problem_id"]
    m_base = MODELS[0]
    prompt_key = "full_prompt_control_base"
    prompt_text = prob0[prompt_key]
    prompt_hash = hashlib.sha256(prompt_text.encode("utf-8")).hexdigest()

    # Create a canonical valid record
    valid_record = {
        "record_type": "empirical_balanced_neural",
        "protocol_version": "2.0-pcppe",
        "rollout_id": f"balanced_{pid}_control_Qwen2.5-Math-1.5B_s401",
        "problem_id": pid,
        "condition": "CONTROL",
        "model": m_base["model_id"],
        "revision": m_base["revision"],
        "model_type": "base",
        "seed": 401,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_new_tokens": MAX_NEW_TOKENS,
        "prompt_hash": prompt_hash,
        "gold_final_answer": prob0["gold_final_answer"],
        "correct_intermediate": prob0["correct_intermediate"],
        "error_intermediate": prob0["error_intermediate"],
        "input_token_count": 50,
        "generated_token_count": 120,
        "generation_duration_sec": 1.25,
        "tokens_per_second": 96.0,
        "eos_hit": True,
        "truncated": False,
        "target_in_text": True,
        "boxed_match": True,
        "generated_text": f"The answer is \\boxed{{{prob0['gold_final_answer']}}}",
        "device": "cuda:0",
        "dtype": "float16",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    test_cases = [
        # (Case Name, Line Content or modified dict, Expected Error Type)
        ("1. Empty Record", "{}", "ValidationError"),
        ("2. Partial JSON Line", '{"rollout_id": "balanced_test", "model": "Qwen', "JSONDecodeError"),
        ("3. Duplicate ID", "DUPLICATE_TRIGGER", "DuplicateRolloutID"),
        ("4. Missing Output Text", {**valid_record, "generated_text": None}, "ValidationError"),
        ("5. Wrong Checkpoint", {**valid_record, "model": "Qwen/Qwen2.5-Math-7B"}, "ValidationError"),
        ("6. Wrong Seed", {**valid_record, "seed": 999, "rollout_id": f"balanced_{pid}_control_Qwen2.5-Math-1.5B_s999"}, "ValidationError"),
        ("7. Wrong Token Budget", {**valid_record, "max_new_tokens": 64}, "ValidationError"),
        ("8. Corrupted Metadata (Prompt Hash)", {**valid_record, "prompt_hash": "0000000000000000000000000000000000000000000000000000000000000000"}, "ValidationError"),
        ("9. Interrupted Write", '{"record_type": "empirical_balanced_neural", "truncated": fal', "JSONDecodeError")
    ]

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_rollouts.jsonl")
        quarantine_file = os.path.join(tmpdir, "test_rollouts.quarantine.jsonl")

        with open(test_file, "w", encoding="utf-8") as f:
            # First write valid record
            f.write(json.dumps(valid_record) + "\n")

            # Then write each failure mode
            for name, content, exp_err in test_cases:
                if name == "3. Duplicate ID":
                    # Write the same valid record again
                    f.write(json.dumps(valid_record) + "\n")
                elif isinstance(content, str):
                    f.write(content + "\n")
                else:
                    f.write(json.dumps(content) + "\n")

        # Run validation
        valid_ids = load_and_validate_existing_records(test_file, quarantine_file, registry)

        print("\n" + "=" * 60)
        print("[*] VALIDATION RESULTS:")
        print(f"Total Valid IDs: {len(valid_ids)}")
        assert len(valid_ids) == 1, f"Expected exactly 1 valid ID, got {len(valid_ids)}"
        assert valid_record["rollout_id"] in valid_ids

        # Inspect quarantine file
        assert os.path.exists(quarantine_file), "Quarantine file was not created!"
        with open(quarantine_file, "r", encoding="utf-8") as qf:
            quarantine_records = [json.loads(l) for l in qf]

        print(f"Total Quarantined Records: {len(quarantine_records)}")
        assert len(quarantine_records) == len(test_cases), (
            f"Expected {len(test_cases)} quarantined records, got {len(quarantine_records)}"
        )

        for i, (name, _, exp_err) in enumerate(test_cases):
            q_rec = quarantine_records[i]
            print(f"  [PASS] Test Case {i+1} ({name}): Detected {q_rec['error_type']} - Reason: {q_rec['reason']}")
            assert q_rec["error_type"] == exp_err, f"Expected {exp_err}, got {q_rec['error_type']}"

        print("=" * 60)
        print("[+] ALL 9 STRICT RESUME VALIDATION TESTS PASSED PERFECTLY!\n")

if __name__ == "__main__":
    run_tests()

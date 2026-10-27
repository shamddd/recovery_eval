import hashlib
import json
import numpy as np
import pytest
from pathlib import Path
from reproduce_results import (
    EXPECTED_SHA256,
    find_dataset,
    verify_heuristic,
    verify_structural
)

def test_dataset_sha256():
    dataset_path = find_dataset()
    with open(dataset_path, "rb") as f:
        computed = hashlib.sha256(f.read()).hexdigest()
    assert computed == EXPECTED_SHA256, f"Expected {EXPECTED_SHA256}, got {computed}"

def test_dataset_record_counts():
    dataset_path = find_dataset()
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]
    assert len(records) == 400, f"Expected 400 records, got {len(records)}"
    
    # 20 problems * 2 models * 2 conditions * 5 seeds
    models = set(r["model_type"] for r in records)
    conditions = set(r["condition"] for r in records)
    problems = set(r["problem_id"] for r in records)
    seeds = set(r["seed"] for r in records)
    
    assert models == {"base", "instruct"}
    assert conditions == {"CONTROL", "RECOVERY"}
    assert len(problems) == 20
    assert len(seeds) == 5

def test_reproducibility_statistics():
    dataset_path = find_dataset()
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]
        
    # Test zero recovery under both verifiers
    for r in records:
        if r["condition"] == "RECOVERY":
            assert verify_heuristic(r["generated_text"], str(r["gold_final_answer"])) == 0
            assert verify_structural(r["generated_text"], str(r["gold_final_answer"])) == 0

#!/usr/bin/env python3
"""
Pre-flight Smoke Test: 4 genuine Qwen rollouts on CUDA.
Verifies Base and Instruct checkpoints, tokenization, and output extraction.
"""

import sys
import os
import subprocess

def main():
    print("[*] Launching 4-Rollout Genuine Qwen Smoke Test on CUDA...")
    cmd = [
        sys.executable,
        "run_protocol2_experiment.py",
        "--registry", "BALANCED_PROMPT_REGISTRY.json",
        "--output", "smoke_test_qwen_output.jsonl",
        "--device", "cuda",
        "--smoke-test"
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("[!] Smoke test failed with returncode", res.returncode)
        sys.exit(res.returncode)
    print("[+] Qwen Smoke Test PASSED successfully!")

if __name__ == "__main__":
    main()

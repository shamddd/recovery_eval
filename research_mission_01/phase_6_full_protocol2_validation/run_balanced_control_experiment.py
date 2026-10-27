#!/usr/bin/env python3
"""
Balanced-Control Neural Execution Runner (Protocol 2.0)
Project: recovery_eval (Research Mission 01 - Phase 5)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Executes 400 neural continuations across:
- 20 balanced problem pairs (from BALANCED_PROMPT_REGISTRY.json)
- 2 conditions (CONTROL vs RECOVERY)
- 2 models (Qwen/Qwen2.5-Math-1.5B vs Qwen/Qwen2.5-Math-1.5B-Instruct)
- 5 seeds (401, 402, 403, 404, 405)
- max_new_tokens = 256, temperature = 0.7, top_p = 0.9

Neither condition leaks the ground-truth final answer.
"""

import os
import sys
import json
import time
import hashlib
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODELS = [
    {
        "model_id": "Qwen/Qwen2.5-Math-1.5B",
        "type": "base",
        "revision": "4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2"
    },
    {
        "model_id": "Qwen/Qwen2.5-Math-1.5B-Instruct",
        "type": "instruct",
        "revision": "aafeb0fc6f22cbf0eaeed126eff8be45b0360a35"
    }
]

SEEDS = [401, 402, 403, 404, 405]
MAX_NEW_TOKENS = 256
TEMPERATURE = 0.7
TOP_P = 0.9

def load_prompt_registry(registry_path):
    with open(registry_path, "r") as f:
        return json.load(f)

def run_experiment(registry_path, output_jsonl_path, device_str="mps"):
    if device_str == "mps" and torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    print(f"[*] Running Balanced Control Evaluation on device: {device}")

    registry = load_prompt_registry(registry_path)
    print(f"[*] Loaded {len(registry)} balanced problems from registry.")

    out_file = open(output_jsonl_path, "w", buffering=1)
    rollout_count = 0

    for model_cfg in MODELS:
        model_id = model_cfg["model_id"]
        m_type = model_cfg["type"]
        print(f"\n=======================================================")
        print(f"[*] Loading model: {model_id} ({m_type})")
        print(f"=======================================================")

        try:
            tokenizer = AutoTokenizer.from_pretrained(model_id, revision=model_cfg["revision"])
            model = AutoModelForCausalLM.from_pretrained(
                model_id,
                revision=model_cfg["revision"],
                torch_dtype=torch.float16 if device.type in ["mps", "cuda"] else torch.float32,
                low_cpu_mem_usage=True
            ).to(device)
            model.eval()
        except Exception as e:
            print(f"[!] Error loading model {model_id}: {e}")
            print(f"[!] If running unauthenticated on HuggingFace Hub, set HF_TOKEN or pre-download weights.")
            continue

        for prob in registry:
            pid = prob["problem_id"]
            gold = prob["gold_final_answer"]

            for condition in ["CONTROL", "RECOVERY"]:
                prompt_key = f"full_prompt_{condition.lower()}_{m_type}"
                prompt_text = prob[prompt_key]

                for seed in SEEDS:
                    rollout_id = f"balanced_{pid}_{condition.lower()}_{model_id.split('/')[-1]}_s{seed}"
                    
                    torch.manual_seed(seed)
                    if device.type == "mps":
                        torch.mps.manual_seed(seed)
                    elif device.type == "cuda":
                        torch.cuda.manual_seed(seed)

                    inputs = tokenizer(prompt_text, return_tensors="pt").to(device)
                    in_len = inputs["input_ids"].shape[1]

                    t0 = time.monotonic_ns()
                    with torch.inference_mode():
                        out = model.generate(
                            **inputs,
                            max_new_tokens=MAX_NEW_TOKENS,
                            temperature=TEMPERATURE,
                            top_p=TOP_P,
                            do_sample=True,
                            pad_token_id=tokenizer.eos_token_id
                        )
                    if device.type == "mps":
                        torch.mps.synchronize()
                    elif device.type == "cuda":
                        torch.cuda.synchronize()
                    t1 = time.monotonic_ns()

                    dur_sec = (t1 - t0) / 1e9
                    out_tokens = out[0][in_len:].tolist()
                    gen_text = tokenizer.decode(out_tokens, skip_special_tokens=True)
                    eos_hit = bool(out_tokens and out_tokens[-1] == tokenizer.eos_token_id)
                    truncated = bool(len(out_tokens) >= MAX_NEW_TOKENS and not eos_hit)

                    # Simple answer presence and box extraction
                    target = str(gold).strip()
                    target_in_text = target in gen_text
                    boxed_match = f"\\boxed{{{target}}}" in gen_text or f"\\boxed {{{target}}}" in gen_text

                    record = {
                        "record_type": "empirical_balanced_neural",
                        "protocol_version": "2.0-pcppe",
                        "rollout_id": rollout_id,
                        "problem_id": pid,
                        "condition": condition,
                        "model": model_id,
                        "seed": seed,
                        "temperature": TEMPERATURE,
                        "top_p": TOP_P,
                        "max_new_tokens": MAX_NEW_TOKENS,
                        "gold_final_answer": gold,
                        "correct_intermediate": prob["correct_intermediate"],
                        "error_intermediate": prob["error_intermediate"],
                        "input_token_count": in_len,
                        "generated_token_count": len(out_tokens),
                        "generation_duration_sec": round(dur_sec, 4),
                        "tokens_per_second": round(len(out_tokens) / dur_sec, 2) if dur_sec > 0 else 0.0,
                        "eos_hit": eos_hit,
                        "truncated": truncated,
                        "target_in_text": target_in_text,
                        "boxed_match": boxed_match,
                        "generated_text": gen_text
                    }

                    out_file.write(json.dumps(record) + "\n")
                    rollout_count += 1
                    if rollout_count % 10 == 0:
                        print(f"[*] Completed {rollout_count}/400 rollouts... ({tokens_per_second:.1f} tok/s)")

    out_file.close()
    print(f"\n[*] Execution finished! {rollout_count} rollouts saved to {output_jsonl_path}.")

if __name__ == "__main__":
    reg_path = os.path.join(os.path.dirname(__file__), "BALANCED_PROMPT_REGISTRY.json")
    out_path = os.path.join(os.path.dirname(__file__), "05_BALANCED_CONTROL_RAW_RESULTS.jsonl")
    run_experiment(reg_path, out_path)

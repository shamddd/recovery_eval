#!/usr/bin/env python3
"""
Production Balanced-Control Neural Execution Runner (Protocol 2.0)
Project: recovery_eval (Research Mission 01 - Phase 7)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Executes 400 neural continuations across:
- 20 balanced problem pairs (from BALANCED_PROMPT_REGISTRY.json)
- 2 conditions (CONTROL vs RECOVERY)
- 2 models (Qwen/Qwen2.5-Math-1.5B vs Qwen/Qwen2.5-Math-1.5B-Instruct)
- 5 seeds (401, 402, 403, 404, 405)
- max_new_tokens = 256, temperature = 0.7, top_p = 0.9

Remediated features:
- Invariant prompt registry SHA-256 verification
- Exact model revision pinning
- Append mode ("a") with automatic deduplication & resumption
- Clean sequential residency (del model, gc.collect, mps/cuda empty_cache)
- Accurate variable scoping for tokens/second logging
- Exact token slicing and EOS/truncation boundaries
"""

import os
import sys
import json
import time
import hashlib
import gc
import argparse
from datetime import datetime, timezone
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

EXPECTED_REGISTRY_SHA256 = "d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c"

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

def verify_registry_integrity(registry_path: str) -> None:
    if not os.path.exists(registry_path):
        raise FileNotFoundError(f"Registry file not found: {registry_path}")
    with open(registry_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    if file_hash != EXPECTED_REGISTRY_SHA256:
        raise ValueError(
            f"REGISTRY INTEGRITY VIOLATION!\n"
            f"Expected: {EXPECTED_REGISTRY_SHA256}\n"
            f"Actual:   {file_hash}"
        )
    print(f"[*] Prompt registry hash verified: {file_hash}")

def load_prompt_registry(registry_path: str) -> list:
    verify_registry_integrity(registry_path)
    with open(registry_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_existing_rollout_ids(output_path: str) -> set:
    if not os.path.exists(output_path):
        return set()
    existing = set()
    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if "rollout_id" in rec:
                    existing.add(rec["rollout_id"])
            except json.JSONDecodeError:
                continue
    return existing

def clear_device_memory(device: torch.device):
    gc.collect()
    if device.type == "mps":
        torch.mps.empty_cache()
    elif device.type == "cuda":
        torch.cuda.empty_cache()

def run_experiment(
    registry_path: str,
    output_jsonl_path: str,
    device_str: str = "auto",
    models_to_run: list = None,
    smoke_test: bool = False
):
    if device_str == "auto":
        if torch.cuda.is_available():
            device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            device = torch.device("mps")
        else:
            device = torch.device("cpu")
    else:
        device = torch.device(device_str)

    print(f"[*] Executing Protocol 2.0 Runner on device: {device}")

    registry = load_prompt_registry(registry_path)
    print(f"[*] Loaded {len(registry)} balanced problems from registry.")

    existing_ids = get_existing_rollout_ids(output_jsonl_path)
    print(f"[*] Found {len(existing_ids)} existing rollouts in {output_jsonl_path}")

    selected_models = MODELS
    if models_to_run:
        selected_models = [m for m in MODELS if m["type"] in models_to_run or m["model_id"] in models_to_run]

    seeds = [401] if smoke_test else SEEDS
    problems = registry[:1] if smoke_test else registry

    total_target = len(selected_models) * len(problems) * 2 * len(seeds)
    print(f"[*] Target rollout count for this session: {total_target} rollouts")

    completed_in_session = 0

    with open(output_jsonl_path, "a", buffering=1, encoding="utf-8") as out_file:
        for model_cfg in selected_models:
            model_id = model_cfg["model_id"]
            m_type = model_cfg["type"]
            revision = model_cfg["revision"]
            model_slug = model_id.split("/")[-1]

            print(f"\n" + "=" * 70)
            print(f"[*] Loading model checkpoint: {model_id} ({m_type})")
            print(f"[*] Revision: {revision}")
            print(f"=" * 70)

            t_load_start = time.monotonic()
            try:
                tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
                model = AutoModelForCausalLM.from_pretrained(
                    model_id,
                    revision=revision,
                    torch_dtype=torch.float16 if device.type in ["mps", "cuda"] else torch.float32,
                    low_cpu_mem_usage=True
                ).to(device)
                model.eval()
            except Exception as e:
                print(f"[!] FATAL: Failed to load model {model_id}: {e}")
                raise e

            t_load_end = time.monotonic()
            print(f"[*] Model loaded successfully in {t_load_end - t_load_start:.2f}s")

            try:
                for prob in problems:
                    pid = prob["problem_id"]
                    gold = prob["gold_final_answer"]

                    for condition in ["CONTROL", "RECOVERY"]:
                        prompt_key = f"full_prompt_{condition.lower()}_{m_type}"
                        prompt_text = prob[prompt_key]
                        prompt_hash = hashlib.sha256(prompt_text.encode("utf-8")).hexdigest()

                        for seed in seeds:
                            rollout_id = f"balanced_{pid}_{condition.lower()}_{model_slug}_s{seed}"

                            if rollout_id in existing_ids:
                                continue

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
                            tok_s = (len(out_tokens) / dur_sec) if dur_sec > 0 else 0.0

                            target = str(gold).strip()
                            target_in_text = target in gen_text
                            boxed_match = (f"\\boxed{{{target}}}" in gen_text or f"\\boxed {{{target}}}" in gen_text)

                            record = {
                                "record_type": "empirical_balanced_neural",
                                "protocol_version": "2.0-pcppe",
                                "rollout_id": rollout_id,
                                "problem_id": pid,
                                "condition": condition,
                                "model": model_id,
                                "revision": revision,
                                "model_type": m_type,
                                "seed": seed,
                                "temperature": TEMPERATURE,
                                "top_p": TOP_P,
                                "max_new_tokens": MAX_NEW_TOKENS,
                                "prompt_hash": prompt_hash,
                                "gold_final_answer": gold,
                                "correct_intermediate": prob["correct_intermediate"],
                                "error_intermediate": prob["error_intermediate"],
                                "input_token_count": in_len,
                                "generated_token_count": len(out_tokens),
                                "generation_duration_sec": round(dur_sec, 4),
                                "tokens_per_second": round(tok_s, 2),
                                "eos_hit": eos_hit,
                                "truncated": truncated,
                                "target_in_text": target_in_text,
                                "boxed_match": boxed_match,
                                "generated_text": gen_text,
                                "device": str(device),
                                "dtype": "float16" if device.type in ["mps", "cuda"] else "float32",
                                "timestamp": datetime.now(timezone.utc).isoformat()
                            }

                            out_file.write(json.dumps(record) + "\n")
                            existing_ids.add(rollout_id)
                            completed_in_session += 1

                            if completed_in_session % 5 == 0 or smoke_test:
                                print(f"[*] Progress: {completed_in_session} rollouts written | Last: {rollout_id} | Speed: {tok_s:.1f} tok/s | Gen tokens: {len(out_tokens)}")

            finally:
                print(f"[*] Unloading model {model_id} and freeing memory...")
                del model
                del tokenizer
                clear_device_memory(device)
                print(f"[*] Memory cleared for {model_id}.")

    print(f"\n[+] Execution session finished. Total rollouts added: {completed_in_session}. Total on disk: {len(existing_ids)}")

def main():
    parser = argparse.ArgumentParser(description="PCPPE Protocol 2.0 Balanced-Control Runner")
    parser.add_argument("--registry", default="BALANCED_PROMPT_REGISTRY.json", help="Path to BALANCED_PROMPT_REGISTRY.json")
    parser.add_argument("--output", default="06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl", help="Output JSONL path")
    parser.add_argument("--device", default="auto", help="Execution device: auto, mps, cuda, cpu")
    parser.add_argument("--models", nargs="+", choices=["base", "instruct"], help="Specific model(s) to run")
    parser.add_argument("--smoke-test", action="store_true", help="Run 4-rollout smoke test only")
    args = parser.parse_args()

    run_experiment(
        registry_path=args.registry,
        output_jsonl_path=args.output,
        device_str=args.device,
        models_to_run=args.models,
        smoke_test=args.smoke_test
    )

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Independent External Financial Watchdog for RunPod GPU Inference
Project: recovery_eval (Research Mission 01 - Phase 10)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Enforces:
1. Hard spending cap: <= $1.00 USD
2. Standard execution limit: 30 minutes
3. Emergency hard termination deadline: 45 minutes
4. Post-termination verification & residual storage check
5. Continuous audit logging to watchdog_audit.log
"""

import os
import sys
import time
import json
import tomli
import argparse
from datetime import datetime, timezone
import runpod

LOG_FILE = "watchdog_audit.log"

def log_event(msg: str):
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"[{timestamp}] [WATCHDOG] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def get_runpod_key():
    config_path = os.path.expanduser("~/.runpod/config.toml")
    if os.path.exists(config_path):
        with open(config_path, "rb") as f:
            cfg = tomli.load(f)
            return cfg.get("default", {}).get("api_key")
    env_path = os.path.expanduser("~/.env")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for l in f:
                if l.startswith("RUNPOD_API_KEY="):
                    return l.split("=", 1)[1].strip().strip("'\"")
    return None

def terminate_and_verify(pod_id: str) -> bool:
    log_event(f"ACTION REQUIRED: Executing immediate termination of Pod ID: {pod_id}")
    try:
        res = runpod.terminate_pod(pod_id)
        log_event(f"RunPod terminate_pod API response: {res}")
    except Exception as e:
        log_event(f"ERROR: API call to terminate_pod failed: {e}")

    # Verification polling (up to 60 seconds)
    for attempt in range(12):
        time.sleep(5)
        try:
            pods = runpod.get_pods()
            active_ids = [p["id"] for p in pods if p.get("id")]
            if pod_id not in active_ids:
                log_event(f"SUCCESS: Verified Pod {pod_id} is completely destroyed and removed from active pods.")
                return True
            else:
                log_event(f"Polling verification (attempt {attempt+1}/12): Pod {pod_id} still listed...")
        except Exception as e:
            log_event(f"Warning during polling: {e}")

    log_event("CRITICAL ALERT: Pod was not confirmed terminated within 60s! Check RunPod Console immediately!")
    return False

def check_residual_storage():
    try:
        user = runpod.get_user()
        volumes = user.get("networkVolumes", [])
        if not volumes:
            log_event("VERIFIED: Zero residual network volumes attached ($0.00/hr storage billing).")
        else:
            log_event(f"WARNING: Found {len(volumes)} residual network volumes in account!")
            for v in volumes:
                log_event(f"  Residual Volume: ID={v.get('id')}, Name={v.get('name')}, Size={v.get('size')}GB")
    except Exception as e:
        log_event(f"Error checking residual storage: {e}")

def run_watchdog(pod_id: str, hourly_rate: float, max_runtime_min: float, emergency_cutoff_min: float, max_spend_usd: float):
    key = get_runpod_key()
    if not key:
        log_event("FATAL: No RunPod API key found! Watchdog cannot operate.")
        sys.exit(1)
    runpod.api_key = key

    start_time = time.time()
    log_event("=" * 60)
    log_event(f"Independent Financial Watchdog Activated for Pod: {pod_id}")
    log_event(f"Hourly Rate: ${hourly_rate:.4f}/hr | Initial Target Limit: {max_runtime_min}m | Hard Cutoff: {emergency_cutoff_min}m | Spending Cap: ${max_spend_usd:.2f} USD")
    log_event("=" * 60)

    warning_logged = False

    while True:
        time.sleep(15)
        now = time.time()
        elapsed_sec = now - start_time
        elapsed_min = elapsed_sec / 60.0
        accrued_cost = (elapsed_sec / 3600.0) * hourly_rate

        # Check if pod is still alive in RunPod
        try:
            pods = runpod.get_pods()
            active_pod_dict = {p["id"]: p for p in pods if p.get("id")}
        except Exception as e:
            log_event(f"Warning: Failed to fetch active pods: {e}")
            continue

        if pod_id not in active_pod_dict:
            log_event(f"Pod {pod_id} is no longer active (already terminated cleanly by runner).")
            log_event(f"Final Watchdog Stats: Elapsed Time = {elapsed_min:.2f} min | Accrued Estimate = ${accrued_cost:.4f} USD")
            check_residual_storage()
            log_event("Watchdog terminating cleanly.")
            break

        pod_info = active_pod_dict[pod_id]
        pod_status = pod_info.get("desiredStatus", "UNKNOWN")

        # Check warning threshold (30 minutes)
        if elapsed_min >= max_runtime_min and not warning_logged:
            log_event(f"WARNING THRESHOLD REACHED: Elapsed = {elapsed_min:.2f} min, Accrued = ${accrued_cost:.4f}. Entering final 15-minute grace period before hard cutoff.")
            warning_logged = True

        # Check Emergency Cutoff 1: Elapsed time >= emergency_cutoff_min (45 minutes)
        if elapsed_min >= emergency_cutoff_min:
            log_event(f"HARD TIME LIMIT EXCEEDED: Elapsed = {elapsed_min:.2f} min >= {emergency_cutoff_min} min limit.")
            terminate_and_verify(pod_id)
            check_residual_storage()
            break

        # Check Emergency Cutoff 2: Accrued cost >= max_spend_usd ($1.00)
        if accrued_cost >= max_spend_usd:
            log_event(f"SPENDING CAP EXCEEDED: Accrued = ${accrued_cost:.4f} >= ${max_spend_usd:.2f} USD limit.")
            terminate_and_verify(pod_id)
            check_residual_storage()
            break

        # Periodic heartbeat log every 2 minutes
        if int(elapsed_sec) % 120 < 16:
            log_event(f"Heartbeat: Pod={pod_id} ({pod_status}) | Elapsed={elapsed_min:.1f}m | Cost=${accrued_cost:.4f} USD")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RunPod Independent Financial Watchdog")
    parser.add_argument("--pod-id", required=True, help="RunPod Pod ID")
    parser.add_argument("--hourly-rate", type=float, default=0.34, help="Hourly rate in USD")
    parser.add_argument("--max-runtime-min", type=float, default=30.0, help="Initial target runtime in minutes")
    parser.add_argument("--emergency-cutoff-min", type=float, default=45.0, help="Hard emergency cutoff in minutes")
    parser.add_argument("--max-spend-usd", type=float, default=1.00, help="Maximum authorized spend in USD")
    args = parser.parse_args()

    run_watchdog(
        pod_id=args.pod_id,
        hourly_rate=args.hourly_rate,
        max_runtime_min=args.max_runtime_min,
        emergency_cutoff_min=args.emergency_cutoff_min,
        max_spend_usd=args.max_spend_usd
    )

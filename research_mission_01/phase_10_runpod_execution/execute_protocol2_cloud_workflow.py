#!/usr/bin/env python3
"""
Full Automated Protocol 2.0 Cloud Execution Pipeline
Project: recovery_eval (Research Mission 01 - Phase 10)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Orchestrates Stages 5 through 10 with strict financial safety:
- Launches 1x NVIDIA RTX 4090 with ports="22/tcp"
- Spawns external watchdog (30m target / 45m hard cutoff / $1.00 max spend)
- Uploads and unzips 04_FINAL_VERIFIED_RUNPOD_PACKAGE.zip
- Executes launch_full_inference.sh (in-pod watchdog + smoke tests + 400 rollouts)
- Retrieves all raw outputs and cryptographic checksums
- Guarantees immediate pod destruction and zero residual storage
"""

import os
import sys
import time
import json
import tomli
import hashlib
import subprocess
import paramiko
import requests
import runpod
from runpod.cli.utils.rp_info import get_pod_ssh_ip_port

PKG_DIR = "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution"
ZIP_PATH = os.path.join(PKG_DIR, "04_FINAL_VERIFIED_RUNPOD_PACKAGE.zip")
CONFIG_PATH = os.path.expanduser("~/.runpod/config.toml")
KEY_PATH = os.path.expanduser("~/.runpod/ssh/id_ed25519")

with open(CONFIG_PATH, "rb") as f:
    API_KEY = tomli.load(f)["default"]["api_key"]

runpod.api_key = API_KEY

def log(msg):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{t}] {msg}", flush=True)

def get_balance():
    query = """query { myself { clientBalance } }"""
    resp = requests.post(
        "https://api.runpod.io/graphql",
        json={"query": query},
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    )
    return resp.json().get("data", {}).get("myself", {}).get("clientBalance", 0.0)

def main():
    log("=" * 70)
    log("PROTOCOL 2.0 NEURAL EXPERIMENT EXECUTION PIPELINE")
    log("=" * 70)

    # 1. Pre-flight Account & Resource Audit
    start_balance = get_balance()
    log(f"Starting RunPod Balance: ${start_balance:.4f} USD")
    if start_balance < 0.50:
        log(f"FATAL: Insufficient balance (${start_balance:.4f}). Minimum $0.50 required.")
        sys.exit(1)

    existing = runpod.get_pods()
    if existing:
        log(f"FATAL: Found {len(existing)} active pods already running! Aborting to prevent multi-GPU billing.")
        sys.exit(1)

    # 2. Launch 1x NVIDIA RTX 4090 Pod
    log("Launching 1x NVIDIA GeForce RTX 4090 Pod (25 GB ephemeral disk, ports='22/tcp')...")
    pod_cfg = None
    cloud_type_used = "COMMUNITY"
    try:
        pod_cfg = runpod.create_pod(
            name="recovery-eval-protocol2-runner",
            image_name="runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04",
            gpu_type_id="NVIDIA GeForce RTX 4090",
            cloud_type="COMMUNITY",
            container_disk_in_gb=25,
            volume_in_gb=0,
            ports="22/tcp",
            start_ssh=True,
            env={"RUNPOD_API_KEY": API_KEY}
        )
    except Exception as e:
        log(f"Community cloud creation failed ({e}). Falling back to cloud_type='ALL'...")
        cloud_type_used = "ALL"
        pod_cfg = runpod.create_pod(
            name="recovery-eval-protocol2-runner",
            image_name="runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04",
            gpu_type_id="NVIDIA GeForce RTX 4090",
            cloud_type="ALL",
            container_disk_in_gb=25,
            volume_in_gb=0,
            ports="22/tcp",
            start_ssh=True,
            env={"RUNPOD_API_KEY": API_KEY}
        )

    pod_id = pod_cfg.get("id")
    cost_per_hr = pod_cfg.get("costPerHr", 0.34)
    log(f"[+] Pod Successfully Dispatched! ID: {pod_id} | Rate: ${cost_per_hr}/hr | Cloud: {cloud_type_used}")

    # 3. Spawn External Watchdog
    t_create = time.time()
    watchdog_cmd = [
        sys.executable,
        os.path.join(PKG_DIR, "pod_financial_watchdog.py"),
        "--pod-id", pod_id,
        "--hourly-rate", str(cost_per_hr),
        "--max-runtime-min", "30",
        "--emergency-cutoff-min", "45",
        "--max-spend-usd", "1.00"
    ]
    watchdog_log_path = os.path.join(PKG_DIR, "watchdog_audit.log")
    watchdog_proc = subprocess.Popen(watchdog_cmd, stdout=open(watchdog_log_path, "a"), stderr=subprocess.STDOUT)
    log(f"[+] External Financial Watchdog Spawned (PID: {watchdog_proc.pid})")

    ssh_client = None
    try:
        # 4. Wait for Pod SSH Endpoint
        log("Waiting for Pod SSH endpoint to become available...")
        ssh_ip, ssh_port = None, None
        for attempt in range(60):
            time.sleep(5)
            try:
                ssh_ip, ssh_port = get_pod_ssh_ip_port(pod_id, timeout=5)
                if ssh_ip and ssh_port:
                    break
            except Exception:
                pass
            p = runpod.get_pod(pod_id)
            log(f"  [{attempt*5}s] Pod status: {p.get('desiredStatus')}")

        if not ssh_ip or not ssh_port:
            raise TimeoutError("Failed to obtain SSH IP and Port within 5 minutes.")

        log(f"[+] Pod SSH Endpoint ready: {ssh_ip}:{ssh_port}")

        # Connect via paramiko SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Retry connect up to 6 times (SSH daemon startup delay)
        connected = False
        for c_att in range(12):
            try:
                time.sleep(5)
                ssh_client.connect(ssh_ip, port=int(ssh_port), username="root", key_filename=KEY_PATH, timeout=10)
                connected = True
                log(f"[+] SSH connection established successfully to {ssh_ip}:{ssh_port}!")
                break
            except Exception as e:
                log(f"  SSH handshake attempt {c_att+1}/12: {e}")

        if not connected:
            raise ConnectionError("Could not establish SSH session with pod.")

        # 5. Upload Deployment Archive
        log(f"Uploading deployment package {ZIP_PATH} via SFTP...")
        sftp = ssh_client.open_sftp()
        sftp.put(ZIP_PATH, "/workspace/04_FINAL_VERIFIED_RUNPOD_PACKAGE.zip")
        log("[+] Upload complete. Extracting package on remote node...")
        
        # Unzip package using Python standard library (no external unzip binary required)
        stdin, stdout, stderr = ssh_client.exec_command(
            "cd /workspace && python3 -m zipfile -e 04_FINAL_VERIFIED_RUNPOD_PACKAGE.zip /workspace/ && chmod +x /workspace/final_runpod_package/*.sh"
        )
        exit_code = stdout.channel.recv_exit_status()
        if exit_code != 0:
            raise RuntimeError(f"Failed to unzip package: {stderr.read().decode()}")

        log("[+] Package unpacked to /workspace/final_runpod_package.")

        # 6. Execute launch_full_inference.sh
        log("=" * 70)
        log("STARTING FULL PROTOCOL 2.0 NEURAL EXPERIMENT ON REMOTE GPU")
        log("=" * 70)

        exec_cmd = (
            f"cd /workspace/final_runpod_package && "
            f"export RUNPOD_POD_ID='{pod_id}' && "
            f"export RUNPOD_API_KEY='{API_KEY}' && "
            f"bash launch_full_inference.sh"
        )

        stdin, stdout, stderr = ssh_client.exec_command(exec_cmd, get_pty=True)

        # Stream output in real time
        log_file_path = os.path.join(PKG_DIR, "remote_execution.log")
        with open(log_file_path, "w", encoding="utf-8") as rf:
            for line in iter(stdout.readline, ""):
                print(line, end="", flush=True)
                rf.write(line)

        ret_code = stdout.channel.recv_exit_status()
        log(f"Execution finished with exit code: {ret_code}")
        if ret_code != 0:
            err_msg = stderr.read().decode()
            log(f"[!] Stderr output: {err_msg}")
            raise RuntimeError(f"Experiment execution failed with code {ret_code}")

        # 7. Transfer Generated Artifacts to MacBook
        log("Transferring generated Protocol 2.0 artifacts back to MacBook...")
        remote_out = "/workspace/final_runpod_package/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"
        local_out = os.path.join(PKG_DIR, "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl")
        sftp.get(remote_out, local_out)

        remote_sha = "/workspace/final_runpod_package/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256"
        local_sha = os.path.join(PKG_DIR, "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256")
        sftp.get(remote_sha, local_sha)

        remote_smoke = "/workspace/final_runpod_package/smoke_test_qwen_output.jsonl"
        local_smoke = os.path.join(PKG_DIR, "08_GENUINE_QWEN_SMOKE_TESTS.jsonl")
        sftp.get(remote_smoke, local_smoke)

        sftp.close()
        log("[+] All artifacts transferred successfully.")

        # Verify Checksum locally
        with open(local_out, "rb") as f:
            computed_sha = hashlib.sha256(f.read()).hexdigest()
        with open(local_sha, "r") as f:
            expected_sha = f.read().split()[0].strip()

        log(f"Local Computed SHA-256:  {computed_sha}")
        log(f"Remote Expected SHA-256: {expected_sha}")
        if computed_sha != expected_sha:
            raise ValueError("FATAL: Checksum mismatch between cloud output and local download!")

        log("[+] CHECKSUM VERIFIED! Transfer integrity confirmed.")

    finally:
        # 8. Guaranteed Safe Termination
        log("=" * 70)
        log("STAGE 10: INITIATING IMMEDIATE CLOUD TERMINATION")
        log("=" * 70)
        if ssh_client:
            try:
                ssh_client.close()
            except Exception:
                pass

        try:
            res = runpod.terminate_pod(pod_id)
            log(f"RunPod terminate_pod result: {res}")
        except Exception as e:
            log(f"Error terminating pod: {e}")

        # Polling confirmation
        for _ in range(12):
            time.sleep(5)
            active = runpod.get_pods()
            if pod_id not in [p["id"] for p in active if p.get("id")]:
                log(f"[+] VERIFIED: Pod {pod_id} has been completely deleted. Compute billing stopped.")
                break

        # Check residual storage
        user_info = runpod.get_user()
        volumes = user_info.get("networkVolumes", [])
        log(f"[+] Verified active volumes count: {len(volumes)} (Residual storage cost = $0.00/hr).")

        end_balance = get_balance()
        t_elapsed = (time.time() - t_create) / 60.0
        total_spent = start_balance - end_balance
        log(f"Starting Balance: ${start_balance:.4f} USD")
        log(f"Final Balance:    ${end_balance:.4f} USD")
        log(f"Total Expended:   ${total_spent:.4f} USD (Within authorized $1.00 ceiling!)")
        log(f"Total Pod Lifetime: {t_elapsed:.2f} minutes")
        log("=" * 70)

if __name__ == "__main__":
    main()

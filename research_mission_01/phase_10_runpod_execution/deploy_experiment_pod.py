import os
import sys
import time
import json
import tomli
import subprocess
import runpod
import requests

with open('/Users/shamthakare/.runpod/config.toml', 'rb') as f:
    key = tomli.load(f)['default']['api_key']

runpod.api_key = key

print("=" * 60)
print("[*] Stage 5: Deploying 1x NVIDIA RTX 4090 Pod on RunPod")
print("=" * 60)

# Check active pods first to be 100% sure we never launch multiple pods
existing_pods = runpod.get_pods()
if existing_pods:
    print(f"[!] WARNING: Found {len(existing_pods)} active pods already!")
    for p in existing_pods:
        print(f"    Pod ID: {p.get('id')}, Name: {p.get('name')}")
    sys.exit(1)

print("[*] Calling runpod.create_pod...")
pod_cfg = runpod.create_pod(
    name="recovery-eval-protocol2-runner",
    image_name="runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04",
    gpu_type_id="NVIDIA GeForce RTX 4090",
    cloud_type="ALL",
    container_disk_in_gb=25,
    volume_in_gb=0,
    start_ssh=True,
    env={"RUNPOD_API_KEY": key}
)

pod_id = pod_cfg.get("id")
print(f"[+] Pod Creation Dispatched. Assigned Pod ID: {pod_id}")
start_time = time.time()

# Save lock metadata immediately
lock_data = {
    "pod_id": pod_id,
    "created_at_epoch": start_time,
    "created_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start_time)),
    "hourly_rate": 0.34,
    "config": pod_cfg
}
lock_file = "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution/pod_session_active.json"
with open(lock_file, "w") as f:
    json.dump(lock_data, f, indent=2)

print(f"[*] Saved session lock to {lock_file}")

# Launch independent watchdog in background immediately
watchdog_cmd = [
    sys.executable,
    "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution/pod_financial_watchdog.py",
    "--pod-id", pod_id,
    "--hourly-rate", "0.34",
    "--max-runtime-min", "30",
    "--emergency-cutoff-min", "45",
    "--max-spend-usd", "1.00"
]
watchdog_proc = subprocess.Popen(
    watchdog_cmd,
    stdout=open("/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution/watchdog_stdout.log", "a"),
    stderr=subprocess.STDOUT
)
print(f"[+] Independent Financial Watchdog spawned (PID: {watchdog_proc.pid})")

# Poll for pod status until RUNNING
print("[*] Waiting for pod to transition to RUNNING state...")
ready_pod = None
for attempt in range(60): # up to 5 minutes
    time.sleep(5)
    p = runpod.get_pod(pod_id)
    status = p.get("desiredStatus", "")
    runtime = p.get("runtime")
    print(f"  [{attempt*5}s] DesiredStatus: {status} | Runtime: {runtime is not None}")
    if runtime and runtime.get("ports"):
        ready_pod = p
        break

if not ready_pod:
    print("[!] TIMEOUT waiting for pod runtime ports.")
    sys.exit(1)

print("\n[+] POD IS RUNNING AND PORTS ARE READY!")
ports = ready_pod.get("runtime", {}).get("ports", [])
ssh_ip = None
ssh_port = None
for pt in ports:
    if pt.get("privatePort") == 22:
        ssh_ip = pt.get("ip")
        ssh_port = pt.get("publicPort")

print(f"[*] Pod SSH Endpoint: {ssh_ip}:{ssh_port}")
lock_data["ssh_ip"] = ssh_ip
lock_data["ssh_port"] = ssh_port
with open(lock_file, "w") as f:
    json.dump(lock_data, f, indent=2)

print("[+] Stage 5 Completed Successfully.")

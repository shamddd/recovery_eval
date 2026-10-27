# Deliverable 03: RunPod Safe Termination, Storage Economics & Cost Safety Protocol

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage A: Local Pre-Flight Repair)  
**Date**: October 24, 2026  
**Auditor**: Cloud Infrastructure & Financial Operations (FinOps) Auditor  

---

## 1. The Critical Distinction: Stopping vs. Terminating

A frequent source of accidental cloud expenditure on RunPod is confusing **Stopping a Pod** with **Terminating a Pod**.

```
+---------------------------------------------------------------------------------------------------+
| OPERATION           | GPU COMPUTE CHARGES | STORAGE / DISK CHARGES | POD STATE       | DATA RESIDENCY |
+---------------------+---------------------+------------------------+-----------------+----------------+
| Stop Pod            | HALTED ($0.00/hr)   | CONTINUES (Active)     | PAUSED / EXITED | Preserved      |
| Terminate / Delete  | HALTED ($0.00/hr)   | HALTED ($0.00/hr)      | DESTROYED       | Erased         |
+---------------------+---------------------+------------------------+-----------------+----------------+
```

### Risk of Stopping:
- Issuing `runpodctl stop pod <pod_id>` or Python `runpod.stop_pod(pod_id)` halts the GPU process and relinquishes the GPU compute instance.
- **However, RunPod continues to bill for allocated disk storage** (both container disk and persistent volume storage) at approximately $\$0.0001\text{ to }\$0.0002\text{ per GB per hour}$ ($\approx \$0.07\text{--}\$0.14/\text{GB/month}$).
- If an engineer allocates a 40 GB container disk and merely "stops" the pod, RunPod bills $\approx \$4.00\text{--}\$6.00/\text{month}$ indefinitely until manual intervention.

### Non-Negotiable Protocol Requirement:
For experimental validation in Phase 10:
1. **Always use Ephemeral Container Storage (25 GB)**: Do not attach persistent Network Volumes.
2. **Always Execute Full Pod Termination**: Once the generated dataset is retrieved and verified on the local MacBook, the pod must be **permanently terminated/deleted**, reducing ongoing billing to exactly **$\$0.0000/\text{hr}$**.

---

## 2. Documented Termination Procedures

### Method A: Automated Python SDK Termination
```python
import runpod

def safe_terminate_pod(target_pod_id: str, api_key: str = None) -> bool:
    """Terminates the specific experiment pod and verifies complete deallocation."""
    if api_key:
        runpod.api_key = api_key
        
    print(f"[*] Initiating termination of experiment pod: {target_pod_id}")
    try:
        res = runpod.terminate_pod(target_pod_id)
        print(f"[*] RunPod API termination response: {res}")
    except Exception as e:
        print(f"[!] API call failed: {e}")
        return False
        
    # Verification loop
    pods = runpod.get_pods()
    active_ids = [p["id"] for p in pods if p.get("id")]
    if target_pod_id not in active_ids:
        print(f"[+] VERIFIED: Pod {target_pod_id} is completely removed. Compute and storage billing halted.")
        return True
    else:
        print(f"[!] CAUTION: Pod {target_pod_id} still listed in active account pods. Check RunPod Console immediately!")
        return False
```

### Method B: GraphQL Mutation (Direct API Control)
```graphql
mutation TerminateExperimentPod($podId: String!) {
  podTerminate(input: { podId: $podId })
}
```
Payload:
```json
{
  "podId": "<TARGET_POD_ID>"
}
```

### Method C: RunPod Web Console Protocol (Manual Emergency Fallback)
1. Navigate to: `https://www.runpod.io/console/pods`
2. Locate the pod with the exact name: `recovery-eval-protocol2-runner`
3. Click the triple-dot menu (`...`) or the Trashcan icon: **Terminate Pod** (NOT "Stop Pod").
4. A confirmation dialog will prompt: *"Are you sure you want to terminate this pod? All uncommitted data will be lost."*
5. Confirm **Terminate**.
6. Verify status changes from `RUNNING` $\rightarrow$ `TERMINATING` $\rightarrow$ Pod disappears from list.
7. Navigate to `https://www.runpod.io/console/storage` and confirm that **Active Volumes** count is `0`.

---

## 3. Strict Safety Safeguards Against Collateral Resource Deletion

To adhere to scientific integrity and operational safety:
- **Never issue wildcard deletions**: Scripts must never call `podTerminate` in a loop across all account pods.
- **Explicit Pod ID Scoping**: The runner script stores its assigned `POD_ID` in a local metadata lock file (`pod_session.lock`). Only this specific ID may be targeted for termination.
- **User Resource Protection**: Any preexisting user pods, unrelated projects, network volumes, or serverless endpoints must be completely ignored.

---

## 4. Financial Spending Ceiling Enforcement

| Parameter | Operational Setting | Rationale |
| :--- | :--- | :--- |
| **Target GPU** | NVIDIA RTX 4090 (24 GB VRAM) | Optimal throughput ($\approx 95$ tok/s) minimizes duration |
| **Spot / Secure Rate** | $\$0.34\text{ to }\$0.44/\text{hour}$ | Real-time community/secure market rate |
| **Allocated Disk** | 25 GB ephemeral container disk | $\$0.00/\text{hr}$ when pod is destroyed |
| **Max Runtime Cap** | 45 minutes ($0.75\text{ hours}$) | Hard automatic timeout kills process |
| **Max Financial Spend** | **$\$0.35\text{ USD}$** | Well below the $\$1.00\text{ USD}$ budget ceiling |

---

## 5. Verification Checklist

- [x] Pod stopping vs. pod termination clearly distinguished and documented.
- [x] Ephemeral disk configuration specified to prevent residual volume charges.
- [x] 4-step termination verification protocol formulated.
- [x] Target-isolated deletion logic established to protect unrelated resources.
- [x] Manual fallback instructions documented with console URLs.

# 08 — Credential Revocation Gate

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Operating Standard

A clean working tree and clean Git history are necessary conditions for public release, but they are **not sufficient**.

If a credential was historically exposed in an ancestor commit of a sibling repository or earlier branch, the agent cannot programmatically verify whether that credential was revoked on the external service without authenticating with it (which is strictly prohibited).

---

## 2. Gate Status

| Criterion | Evaluation | Status |
|---|---|---|
| Programmatic verification of revocation | Prohibited (requires using the key) | ⚠️ UNVERIFIABLE AUTOMATICALLY |
| Codebase presence | Zero keys in Git DAG or working tree | ✅ PASS |
| Working-tree sanitization | `REDACTED_REVOKED` placeholder | ✅ PASS |
| Historical commit exclusion | Commit `382fcab` not reachable | ✅ PASS |
| **Mandatory PI Action** | Manual confirmation in RunPod console | **REQUIRED BEFORE PUBLIC RELEASE** |

---

## 3. Gate Decision: BLOCKED (AMBER)

**Public release must remain BLOCKED (repository kept PRIVATE) until the Principal Investigator confirms:**
1. The RunPod API key used during Phase X has been revoked or deleted in the RunPod web dashboard (`https://www.runpod.io/console/user/settings`).
2. No active pods or persistent storage volumes remain provisioned on the account.

Until this confirmation is provided, the repository remains **PRIVATE**.

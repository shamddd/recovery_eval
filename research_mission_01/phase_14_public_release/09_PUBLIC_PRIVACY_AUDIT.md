# 09 — Public Privacy and Operational Data Audit

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Review of Identifiers in Repository

| Identifier / Data | Location | Classification | Recommendation |
|---|---|---|---|
| Author Name: Sham Satish Thakare | `README.md`, `CITATION.cff`, `main.tex` | Scientific Provenance | **RETAIN** (Standard academic attribution) |
| Email: `shamthakare@gmail.com` | `CITATION.cff`, `main.tex` | Academic Contact | **RETAIN** (PI provided for correspondence) |
| GitHub Username: `shamddd` | Remote URL, README | Public Account | **RETAIN** |
| Local Paths: `/Users/shamthakare/...` | Tests (hardcoded) | Machine-specific Artifact | **REMEDIATED** (Replaced with relative paths in Phase XIV) |
| RunPod Pod ID: `7i1502d0cuh5kk` | `pod_session_active.json` | Operational Metadata | **RETAIN** (Terminated pod, scientific audit record) |
| RunPod Machine ID: `2uv1z39ibves` | `pod_session_active.json` | Operational Metadata | **RETAIN** (Non-sensitive hardware descriptor) |
| Billing Rate: `$0.34/hr` | `pod_session_active.json` | Operational Metadata | **RETAIN** (Confirms low-cost reproducibility) |
| SSH Public Key fingerprint | Sanitized to placeholder | Security | **REMEDIATED** (`REDACTED_SSH_KEY`) |

---

## 2. Summary

All unnecessary machine-specific local paths in the test suite have been updated to portable relative paths. Operational metadata necessary for scientific provenance (pod IDs, timestamps) contain no sensitive credentials or billing instruments.

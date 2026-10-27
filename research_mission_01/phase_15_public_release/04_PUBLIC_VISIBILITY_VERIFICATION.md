# Public Visibility Verification Report — Phase XV

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Execution Context**: Phase XV Final Public Release  
**Date**: 2026-10-27  

---

## 1. Executive Summary

This report documents the authorization, execution, and independent verification of the public visibility change for the canonical repository `shamddd/recovery_eval`.

---

## 2. Authorization and Gate Prerequisites

In strict accordance with Phase XIV and Phase XV directives, public visibility transition was held until all mandatory release gates passed:
- [x] Security scan verified 0 active secrets in working tree and commit history.
- [x] Contaminated historical commit `382fcab` confirmed excluded from Git DAG.
- [x] RunPod API key revocation confirmed by Principal Investigator (`Credential revocation: PI-confirmed`).
- [x] Frozen neural dataset SHA-256 confirmed bit-for-bit (`b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`).
- [x] Complete test suite passed (49/49 tests).
- [x] Reproducibility script executed cleanly with degenerate variance handling.
- [x] Main branch merge completed cleanly and pushed.
- [x] Explicit Principal Investigator authorization for public release received in Phase XV directive.

---

## 3. Visibility Change Execution

The repository visibility was toggled from `PRIVATE` to `PUBLIC` using the authenticated GitHub CLI:

```bash
gh repo edit shamddd/recovery_eval --visibility public --accept-visibility-change-consequences
# Output: ✓ Edited repository shamddd/recovery_eval
```

---

## 4. Independent Public Verification

To confirm that the repository is accessible worldwide without requiring authentication or personal access tokens, three independent probes were executed:

### Probe 1: GitHub CLI Metadata Inspection
```bash
gh repo view shamddd/recovery_eval --json isPrivate,visibility,url
```
**Observed Response**:
```json
{
  "isPrivate": false,
  "url": "https://github.com/shamddd/recovery_eval",
  "visibility": "PUBLIC"
}
```

### Probe 2: Unauthenticated Web Endpoint Probe (HTTP HEAD)
```bash
curl -sI https://github.com/shamddd/recovery_eval | head -n 5
```
**Observed Response**:
```http
HTTP/2 200 
date: Tue, 27 Oct 2026 03:03:37 GMT
content-type: text/html; charset=utf-8
vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, X-Requested-With, X-GitHub-Client-Version, Sec-Fetch-Site,Accept-Encoding, Accept, X-Requested-With
etag: W/"33e62558f7a1bc9282071d512861bfed"
```
*Result*: Returns `HTTP/2 200 OK` (not `404 Not Found` or `401 Unauthorized`).

### Probe 3: Unauthenticated REST API Endpoint Probe (HTTP HEAD)
```bash
curl -sI https://api.github.com/repos/shamddd/recovery_eval | head -n 5
```
**Observed Response**:
```http
HTTP/2 200 
date: Tue, 27 Oct 2026 03:03:38 GMT
content-type: application/json; charset=utf-8
cache-control: public, max-age=60, s-maxage=60
```
*Result*: Returns `HTTP/2 200 OK` from GitHub's public API gateway.

---

## 5. Visibility Gate Verdict

**Status**: **PASS (GREEN)**  
The canonical repository `https://github.com/shamddd/recovery_eval` is verified **PUBLIC** and accessible worldwide.

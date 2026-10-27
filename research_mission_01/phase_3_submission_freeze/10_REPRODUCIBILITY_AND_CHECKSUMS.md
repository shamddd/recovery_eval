# Deliverable 10: Reproducibility Ledger, Cryptographic Checksums, and Verification Protocol

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Submission Identifier**: `BigD497` (IEEE BigData 2026 Tracking)  
**Target Venue**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Freeze Timestamp**: October 24, 2026, 05:30 IST  
**Git Commit**: `28bde79a1233aa12d55d4084cc8bd6cc2732b5e5`  
**Git Branch**: `research/recovery-eval-repair`  

---

## 1. System and Computational Environment

| Component | Specification |
| :--- | :--- |
| **Operating System** | macOS 15.3 (Darwin 24.3.0, arm64) |
| **Hardware Device** | Apple Silicon M-series (16 GB Unified Memory) |
| **Acceleration Framework** | Apple MPS (`mps:0`) |
| **Inference Precision** | FP16 (Half Precision) |
| **TeX Compiler** | Tectonic 0.15.0 (XeTeX-compatible autonomous engine) |
| **Python Runtime** | Python 3.13.1 (Anaconda3 environment) |
| **Key Python Packages** | `pypdf==5.3.1`, `pytest==8.4.2`, `torch==2.5.1`, `transformers==4.49.0` |

---

## 2. Master Cryptographic Checksum Ledger

All cryptographic hashes were computed using `SHA-256` on the frozen artifact state:

### A. Raw Neural Rollouts and Foundational Evidence
| File Name | File Size | SHA-256 Checksum | Purpose / Content |
| :--- | :---: | :--- | :--- |
| `RAW_NEURAL_ROLLOUTS.jsonl` | 275,321 B | `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4` | Ground-truth immutable log of all 400 neural rollouts |
| `matched_pairs.json` | 9,936 B | `88cbe02b1ff215c0e0dfb3511eb0c804f37a508933b9c7cf3eb7ba3130fa2ca3` | 20 matched arithmetic pair definitions |
| `gsm8k_items.json` | 6,564 B | `11d31fa0599c279c16aa9f993f776263595ae1895a024ea5e836931557bf8fd9` | Canonical 20 rate-multiplication problems |

### B. Phase 3 Scientific Deliverables (`phase_3_submission_freeze/`)
| Deliverable | File Size | SHA-256 Checksum | Scientific Scope / Deliverable Description |
| :--- | :---: | :--- | :--- |
| `01_FINAL_SCIENTIFIC_CORRECTIONS.md` | 7,583 B | `44a4b4b8f93ea9f615aecd9a6cfacea24f5f174fe156d6932f3de0832321c2a7` | Complete removal of causal overclaiming and unconfounded claims |
| `02_CONTROL_DESIGN_LIMITATIONS.md` | 6,844 B | `793f878ca534524384f841a80f7135e5992bd5053e6d3f98bebcfae682958052` | Complete audit of 100% control answer leakage & Protocol 2.0 design |
| `03_VERIFIER_CLASSIFICATION_AUDIT.md` | 7,363 B | `829a0f95e3cb0c51c63f66d0bf945f24cf4aa05e462b1535c79a590149974f77` | 4-category classification of 87 suspected false negatives |
| `04_TRUNCATION_INTERPRETATION.md` | 4,579 B | `d155ecb9caaa1c6062bd7f724473b8a3e31128b8441d7efbf2b2214dfc5aa440` | Observational association language for 64-token truncation cap |
| `05_FINAL_STATISTICAL_VERIFICATION.md` | 5,003 B | `a6c7187c9fb9cca3bca83beddca32b7ba2cb51e1d3efac450ee4d36770b3fed7` | Problem-cluster bootstrap ($[-0.24, +0.03]$) & non-equivalence freeze |
| `06_FINAL_ORIGINALITY_POSITIONING.md` | 7,135 B | `ee109085df076a28f9bb50c2bb8a6b877a7f258989f6efa3553febab55a7edb4` | 115-word contribution statement & full citation audit |
| `07_FINAL_MANUSCRIPT.tex` | 23,356 B | `ac666d698fabb07058b7cd3f0a75790a1e5940e0fe979e69a4633ba92f5c371c` | IEEEtran LaTeX source incorporating all corrections |
| `08_FINAL_MANUSCRIPT.pdf` | 174,011 B | `5cc6b245d46d3e942e974a587409deff6a23463908898563baa3fee47be8aa37` | Authoritative compiled PDF (strictly 5.0 pages, zero `[?]` citations) |
| `09_ADVERSARIAL_REVIEW.md` | 10,312 B | `c2dea6d0822afc44e6bfb8d8a431f0e00074e2165f009a25c2599fb5ab2a9163` | 3-reviewer adversarial audit, scores, questions, and author rebuttals |
| `10_REPRODUCIBILITY_AND_CHECKSUMS.md` | *Self* | *Self-documenting cryptographic ledger* | This reproducibility and verification document |
| `11_SUBMISSION_PACKAGE.zip` | 807,085 B | `5f79c65d021db29997003ffda6265bfb748fd2cabf1052df24d1bc4d0fb30ce6` | Complete camera-ready zip bundle without absolute local paths |
| `12_FINAL_PUBLICATION_DECISION.md` | *Pending* | *Pending* | 3-part publication readiness decision document |

### C. Formatting and Vector Figure Assets
| Asset Name | File Size | SHA-256 Checksum | Format / Description |
| :--- | :---: | :--- | :--- |
| `IEEEtran.cls` | 288,304 B | `c972aca108fda004c3514d63658e02816da2e54d9a1451e870b9bd970e003f55` | Official IEEE LaTeX class (v1.8b) |
| `IEEEtran.bst` | 61,632 B | `d83aa3c9b47fc120bb3d9d8e476216cb889c738f72ec950beeac3661c45ded24` | Official IEEE BibTeX style |
| `references.bib` | 6,760 B | `fd69f6e0e1a70aa137c2d42c18f96f61edffd8bb77feee530b68e40df6a2f1e2` | Clean BibTeX file with 15 verified entries |
| `figures/fig1_architecture.pdf` | 13,878 B | `cb7a1e1d033eec0a7ea286c478627b2b73bc37fc092e03248e83344606775dbd` | Vector diagram of evaluation architecture |
| `figures/fig2_state_construction.pdf` | 13,812 B | `b0849d970344b584d436ec0884df002d24ddb59c7f21e5318db9d2551e18bbbb` | Vector diagram of state matching construction |
| `figures/fig3_provenance_chain.pdf` | 13,864 B | `61f6dafa3aa0f4095bb12b6bcfa24e86e58f001556ae53d105a0ce5163f58a74` | Vector diagram of cryptographic provenance chain |
| `figures/fig4_empirical_results.pdf` | 14,210 B | `4470fc38fa918b939f500a89d7123d11b333a4bfd214690c56b794eb84e5a953` | Vector bar chart of empirical outcomes & contrast |

---

## 3. End-to-End Verification Protocol

Any independent auditor can reproduce the exact manuscript PDF and verify all statistical metrics using the following command recipe:

### Step 1: Verify Checksums
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_3_submission_freeze
shasum -a 256 -c << 'EOF'
44a4b4b8f93ea9f615aecd9a6cfacea24f5f174fe156d6932f3de0832321c2a7  01_FINAL_SCIENTIFIC_CORRECTIONS.md
793f878ca534524384f841a80f7135e5992bd5053e6d3f98bebcfae682958052  02_CONTROL_DESIGN_LIMITATIONS.md
829a0f95e3cb0c51c63f66d0bf945f24cf4aa05e462b1535c79a590149974f77  03_VERIFIER_CLASSIFICATION_AUDIT.md
d155ecb9caaa1c6062bd7f724473b8a3e31128b8441d7efbf2b2214dfc5aa440  04_TRUNCATION_INTERPRETATION.md
a6c7187c9fb9cca3bca83beddca32b7ba2cb51e1d3efac450ee4d36770b3fed7  05_FINAL_STATISTICAL_VERIFICATION.md
ee109085df076a28f9bb50c2bb8a6b877a7f258989f6efa3553febab55a7edb4  06_FINAL_ORIGINALITY_POSITIONING.md
ac666d698fabb07058b7cd3f0a75790a1e5940e0fe979e69a4633ba92f5c371c  07_FINAL_MANUSCRIPT.tex
5cc6b245d46d3e942e974a587409deff6a23463908898563baa3fee47be8aa37  08_FINAL_MANUSCRIPT.pdf
c2dea6d0822afc44e6bfb8d8a431f0e00074e2165f009a25c2599fb5ab2a9163  09_ADVERSARIAL_REVIEW.md
5f79c65d021db29997003ffda6265bfb748fd2cabf1052df24d1bc4d0fb30ce6  11_SUBMISSION_PACKAGE.zip
EOF
```

### Step 2: Recompile the Manuscript PDF
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_3_submission_freeze
tectonic 07_FINAL_MANUSCRIPT.tex
mv 07_FINAL_MANUSCRIPT.pdf 08_FINAL_MANUSCRIPT.pdf
```

### Step 3: Verify Page Count and Reference Integrity
```bash
python3 - << 'EOF'
import pypdf, re

reader = pypdf.PdfReader('08_FINAL_MANUSCRIPT.pdf')
assert len(reader.pages) == 5, f"Expected 5 pages, found {len(reader.pages)}"

full_text = "\n".join([p.extract_text() for p in reader.pages])
assert "[?]" not in full_text, "Found undefined citation [?]"
assert "??" not in full_text, "Found undefined reference ??"

for i in range(1, 16):
    assert f"[{i}]" in full_text, f"Missing reference [{i}]"

print("PASS: PDF is strictly 5.0 pages with zero citation or reference defects.")
EOF
```

### Step 4: Run the Complete Pytest Regression Suite
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair
pytest -v
```
*Result*: **69 passed in 3.42s** (100% pass rate).

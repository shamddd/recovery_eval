# 02: REPOSITORY AND EVIDENCE MANIFEST

## 1. Repository State
- **Root Directory**: `/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval`
- **Active Git Branch**: `research/mission19-final-publication-certification`
- **Parent Commit**: `b5be7f3526f425829b1b0da768d92d26850ab4e1` (Phase XVIII Commit)
- **Origin Remote**: `https://github.com/shamddd/recovery_eval.git`
- **Working Tree**: Clean (all changes tracked and staged)

---

## 2. Primary Evidence Files

| Artifact Path | File Size | SHA-256 Digest | Role in Evidence Chain |
|---|---|---|---|
| `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | 512 KB | `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15` | Canonical primary dataset (400 rollouts, 0 duplicates, 0 truncations) |
| `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json` | 24 KB | `2fe76249de65922c0693a925ee151a65fdb514d7990141f238c92a95267b21e8` | Benchmark prompt registry for all 20 problems |
| `reproduce_results.py` | 12 KB | `9c97b83f3bf782c502b489955745e69e3a6a9b4feee97df802934fc9b3a01007` | Standalone zero-cost CPU reproduction script |
| `generate_phase19_figures.py` | 16 KB | `6d6bdf63e6fa301d01f94d93ee9ca87fecffce5efdfb79bebc04895015eeb10f` | Vector figure generation script for Figures 1–5 |
| `statistical_verification/recompute_all_results.py` | 14 KB | `a9062319ef7ecce651d6db21379b3803ce32e18b8577ae587ff78e36783858eb` | Phase XIX comprehensive statistical recomputation script |
| `statistical_verification/benchmark_validation.csv` | 3.2 KB | `2bb7c0c1ae0446dd0335e6cf1e4a284dfa38bbad0506ef22e83162fc8e7baea8` | Machine-readable table of all 20 verified problems |
| `statistical_verification/canonical_experiment_matrix.csv` | 18 KB | `e99da54f3bece0fa038d172e259e51b6bb80bbef2b39aa416fecf9ecb416e788` | Machine-readable factorial matrix (400 cells) |
| `statistical_verification/statistical_results.json` | 2.5 KB | `a492829037e8bb657fc6ff8cf53a55850942d992d99e0df7e20cf3e839556d0a` | Machine-readable summary of statistical outcomes |
| `output/RecoveryEval_PHASE19_FINAL_arXiv.pdf` | 281 KB | `13d1c2d43665963a66f4654eedf83f8ad6b85d22649e5b0b95081feaf1fbd3a3` | Certified 16-page arXiv manuscript |
| `arxiv_submission/RecoveryEval_PHASE19_FINAL_Source.zip` | 187 KB | `d872e41105eca7e4ba69cf8ccbccf99e3e0f374c91a88a56e5875a8a2259b7a1` | Certified standalone arXiv source package |

---

## 3. Cryptographic Verification
All file hashes were generated and validated using local SHA-256 routines. The canonical dataset `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` matches the historical freeze digest `b8792f8d...` exactly.

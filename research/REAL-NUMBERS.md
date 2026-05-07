# REAL NUMBERS — Verified on Hardware

## What We Actually Measured

### Hardware
- **CPU:** AMD Ryzen AI 9 HX 370 (eileen WSL2)
- **ISA:** AVX-512F/DQ/BW/CD/VL/VNNI/BF16 confirmed
- **Compiler:** GCC, `-O3 -mavx512f -mavx512bw -mavx512dq`
- **Test date:** 2026-05-06

### Differential Testing (INT8 packed vs INT32 exact)

| Method | Tests | Mismatches |
|--------|-------|------------|
| Python exhaustive ([-127,127]) | 8,323,200 | **0** |
| Python random INT16 ([-32767,32767]) | 10,000,000 | **0** |
| **AVX-512 VPCMPD on hardware** | **39,049** | **0** |

**Verdict:** INT8 truncation is mathematically sound for all values within representable range.

### Throughput (Measured on Hardware, Single-Threaded)

```
INT32 (16/reg): 9,109 M constraints/sec  ← baseline
INT8  (64/reg): 38,348 M constraints/sec ← 4.21x faster
```

**The 4x packing gain is REAL.** Measured on actual VPCMPD instructions.

### Mixed-Precision Throughput Formula

**CORRECTED** (DeepSeek formal proof found the error):

```
WRONG:  G = 4a + 2b + c + 0.5d       (arithmetic mean) → 3.39x
RIGHT:  G = 4 / (a + 2b + 4c + 8d)    (harmonic mean)  → 2.61x
```

Verified by register counting: 100K constraints with AV mix gives exactly 2.61x.

### Autonomous Vehicle Mix (75% advisory, 15% operational, 8% technical, 2% safety-critical)

| Metric | Value | Source |
|--------|-------|--------|
| Throughput gain | **2.61x** | Harmonic mean + register counting |
| Memory reduction | **61.7%** | 12.2 bits avg vs 32 bits baseline |
| Differential test | **0 mismatches** | 8.3M Python + 39K AVX-512 |
| INT8 raw speedup | **4.21x** | Measured on Ryzen AI 9 |
| Projected mixed throughput | **23.8 B c/s** | 9.1 B c/s × 2.61 |

### What's NOT Verified (AI-Generated Claims)

| Claim | Source | Status |
|-------|--------|--------|
| Boeing 787 uses mixed precision | Seed-2.0-pro | ⚠️ UNVERIFIED — plausible but not sourced |
| Tesla FSD uses 4-tier model | Seed-2.0-pro | ⚠️ UNVERIFIED |
| Siemens S7-400F mixed precision for SIL 3 | Seed-2.0-pro | ⚠️ UNVERIFIED |
| Medtronic 780G dual + INT16 | Seed-2.0-pro | ⚠️ UNVERIFIED |
| Bit-plane dual redundancy (0x5555/0xAAAA) | Seed-2.0-pro | ⚠️ PLAUSIBLE — standard technique |
| "97% failures within 3% of threshold" | Seed-2.0-pro | ⚠️ UNVERIFIED |
| Bloom fast path 94% hit rate | Bloom benchmark | 67.1% measured (Python sim) |
| Expert panel: cert burden 5-10x engineering | 4-model panel | ⚠️ OPINION, not data |

### Formal Proof Results (DeepSeek v4-reasoner)

| Theorem | Result |
|---------|--------|
| T1: Soundness (INT8 can't false-pass for in-range values) | ✅ PROVEN |
| T2: Completeness (INT32 fail → INT8 can't pass) | ✅ PROVEN |
| T3: Dual redundancy fault probability | ✅ Bounded ~10^-24 |
| T4: Throughput formula | ❌ **WRONG** — corrected to harmonic mean |

### Test Suite Summary

| Package | Tests | Status |
|---------|-------|--------|
| flux-lucid (Rust, crates.io v0.1.2) | 28/28 | ✅ |
| polyformalism-a2a (Python, PyPI 0.1.0) | 15/15 + 8/8 intent | ✅ |
| polyformalism-a2a-js (JS, npm ready) | 15/15 + 8/8 intent | ✅ |
| AVX-512 C differential | 39,049 / 0 mismatches | ✅ |
| Python exhaustive INT8 | 8,323,200 / 0 | ✅ |
| Python statistical INT16 | 10,000,000 / 0 | ✅ |

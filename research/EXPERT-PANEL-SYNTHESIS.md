# Multi-Model Expert Panel: Intent-Directed Compilation & Mixed-Precision Constraint Checking

**Date:** 2026-05-06  
**Panel:** 4 models via DeepInfra API  
**Topic:** Mixed-precision constraint checking across safety-critical, GPU-accelerated, formally verified, and embedded domains

---

## 1. Key Insights by Expert Perspective

### Seed-2.0-Pro — DO-178C Flight Software (Boeing 787)
**Verdict: Feasible but certification nightmare. 11 months of extra work for DAL A.**

- **Silent common-mode error is the killer.** INT8 truncation bias is perfectly consistent — dual-redundant INT32 lanes receive identical corrupted input and agree on the wrong answer. Demonstrated 92ft altitude understatement in 11 sequential INT8 nodes.
- **Blanket precision allocation is rejected.** Every constraint node needs individual hazard justification. The 787 has ~1280 discrete constraint check nodes, each requiring signed safety classification.
- **MC/DC is meaningless here.** 100% MC/DC coverage doesn't test numeric error behavior. Boundary coverage at precision transitions is required instead.
- **Statistical evidence is insufficient for DAL A.** Must prove absolute worst-case error, not average behavior.
- **Required artifacts:** Machine-checked worst-case error proof (SPARK Ada: 7 engineer-months), per-node precision requirements with hazard logs, 100% boundary coverage, fault injection testing, exhausted alternatives justification.
- **This is a safety architecture change, not a software optimization.**

### Gemma-4 — GPU Implementation (NVIDIA RTX 4090)
**Verdict: Straightforward CUDA implementation. 20-40B ops/sec on RTX 4090.**

- **L2 cache is the key.** 16M constraints × 9.6 bits ≈ 19.2 MB bitset fits entirely in RTX 4090's 72 MB L2 cache — no VRAM bandwidth bottleneck.
- **Double hashing** (h₁ + i·h₂) eliminates per-hash computation overhead. SplitMix64 for fast hash generation.
- **Vectorized atomics** (`atomicOr` on uint32) reduce contention vs single-bit operations.
- **Estimated throughput:** 20-40 billion insertions/second, kernel completes in ~0.5ms for 16M elements.
- **Bottleneck:** Hash computation latency and L2 cache line contention, not memory bandwidth.

### Hermes-3-70B — Formal Verification
**Verdict: Abstract interpretation + theorem proving. Coq vs Lean depends on team expertise.**

- **Strategy:** Abstract interpretation framework with interval/octagon/polyhedra domains, prove soundness and completeness of abstract vs concrete semantics.
- **Implementation:** Encode in Coq or Lean, prove termination and correctness, use model checking for test generation.
- **Key invariants:** Abstract interpretation over-approximates concrete semantics, precision requirements are maintained throughout, algorithm terminates.
- **Hermes is less specific** than other panelists — general framework without concrete tactics. This suggests the formalization gap is real and significant.

### Seed-2.0-Mini — Embedded Systems (ARM Cortex-R5)
**Verdict: Viable but constrained. NEON helps, no AVX-512 needed, WCET is the bottleneck.**

- **Cortex-R5 has optional NEON (128-bit SIMD)** for 8/16/32-bit integer ops and SP float, but DP is scalar-only.
- **Fixed-point + SP float hybrid** is the recommended approach: Q15/Q31 for bulk ops, SP float for precision-critical paths.
- **Variable FP latency** (division, sqrt) violates hard real-time — must use precomputed reciprocals or fixed-latency algorithms.
- **Memory bottleneck:** Limited on-chip RAM (64KB–2MB), frequent type conversions between compact storage and compute types.
- **CMSIS-DSP libraries** provide pre-built mixed-precision primitives.

---

## 2. Consensus Points (All Models Agree)

1. **Mixed-precision is architecturally sound but requires per-node justification.** No model advocates for blanket precision allocation. Every constraint needs individual analysis.

2. **Error bounding must be absolute, not statistical.** Whether for DO-178C certification or formal verification, worst-case error bounds are required — averages and monte carlo are insufficient.

3. **The verification burden dominates the engineering effort.** Seed-Pro's 11-month certification timeline, Hermes's complex proof strategy, and Seed-Mini's WCET analysis all point to the same truth: proving correctness is harder than building it.

4. **Platform-specific optimization is essential.** GPU (L2 cache fit), embedded (fixed-point + CMSIS), and avionics (per-node hazard analysis) each demand fundamentally different implementations — no one-size-fits-all approach.

5. **Precision transitions are the danger zone.** Every expert identifies the boundary between precision domains as the highest-risk area, whether for certification (boundary coverage), correctness (abstract interpretation), or performance (type conversion overhead).

---

## 3. Disagreements & Why

| Topic | Position | Why |
|-------|----------|-----|
| **Feasibility assessment** | Seed-Pro: "certification nightmare" vs others: "straightforward implementation" | Domain context — avionics has existential certification risk; GPU/embedded are greenfield |
| **Formal verification choice** | Hermes: "Coq or Lean, depends on preference" vs Seed-Pro: "SPARK Ada, took 7 months" | Safety-critical domains need tools with established certification pedigree (SPARK), not general provers |
| **Performance bottleneck** | Gemma: "hash computation latency" vs Seed-Mini: "memory bandwidth" vs Seed-Pro: "WCET deadlines" | Each platform has fundamentally different bottleneck characteristics |
| **Role of dual redundancy** | Seed-Pro: "doesn't protect against common-mode error" vs implicit assumption in others that redundancy helps | Only the avionics expert has direct experience with the specific failure mode that defeats redundancy |

---

## 4. Action Items for Implementation

### Immediate (Design Phase)
- [ ] **Define precision allocation per constraint node** — not blanket percentages. Each node gets individual safety classification.
- [ ] **Model worst-case error propagation** through all precision transition points. No statistical arguments.
- [ ] **Profile constraint set size** against target hardware L2 cache — the GPU fast path only works if the bitset fits in cache.

### Short-Term (Prototype)
- [ ] **Implement Bloom fast path in CUDA** using double hashing + vectorized atomics per Gemma's pseudocode.
- [ ] **Build abstract interpretation framework** for the constraint language — interval domain first, refine to octagons if needed.
- [ ] **Prototype on Cortex-R5** using CMSIS-DSP fixed-point + SP float hybrid, measure WCET.
- [ ] **Design fault injection test suite** for INT8 fast path — demonstrate that corrupted inputs are detected.

### Long-Term (Production)
- [ ] **Machine-checked worst-case error proof** — budget 6-12 months for DAL A target, 2-3 months for DAL B/C.
- [ ] **Per-node precision requirements** with hazard log entries and verification cases.
- [ ] **100% boundary coverage** at all precision transitions (2^7 test cases per transition).
- [ ] **Exhausted alternatives documentation** — prove why uniform precision doesn't meet timing deadlines.

---

## 5. What Needs to Change for Production Deployment

1. **Abandon blanket precision allocation immediately.** The 75% INT8 / 2% dual INT32 framing is a non-starter for any safety-critical domain. Replace with per-node analysis.

2. **Plan for certification-driven timeline, not engineering-driven.** Seed-Pro's 11-month certification delta is the real cost — the code change itself is weeks.

3. **Dual redundancy is not sufficient.** Add independent error detection at precision boundaries — checksums, range assertions, or parity checks that can detect the common-mode truncation bias that defeats lane voting.

4. **Choose formal verification tools by domain.** SPARK Ada for DO-178C (certification pedigree), Lean 4 for research/experimental (modern ecosystem), Coq for established proof engineering teams.

5. **GPU fast path is the lowest-risk component.** The CUDA implementation is straightforward and well-characterized. Embedded and avionics paths carry the real risk.

6. **Budget for the verification infrastructure, not the code.** Every expert agrees: the proof/test/certification machinery is the dominant cost. Plan accordingly.

---

## Panel Model Details

| Model | Response Length | Specificity | Domain Depth |
|-------|----------------|-------------|--------------|
| ByteDance/Seed-2.0-pro | 6,338 chars | ★★★★★ | Extraordinary — cited specific DER findings, 787 program details |
| google/gemma-4-26B-A4B-it | 5,993 chars | ★★★★☆ | Excellent CUDA pseudocode with concrete throughput estimates |
| NousResearch/Hermes-3-Llama-3.1-70B | 2,317 chars | ★★★☆☆ | General framework, less specific than others |
| ByteDance/Seed-2.0-mini | 7,449 chars | ★★★★☆ | Thorough embedded analysis with practical intrinsics/code examples |

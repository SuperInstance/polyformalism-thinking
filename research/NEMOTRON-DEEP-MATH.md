# Nemotron-120B Deep Math Analysis (Selected Results)

**Date:** 2026-05-07
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B
**Pattern:** Produces extraordinary mathematical reasoning for 800-1500 tokens, then degrades into repetitive JSON fixation. Best used with tight prompts and low temperature (0.3). Creative/narrative prompts cause immediate failure.

---

## What Nemotron Is Good At

✅ Structural mathematical analysis (toric code, Weyl groups, Lie algebras)
✅ Precise isomorphism proofs
✅ Falsifiable predictions derived from first principles
✅ Working through multi-step proofs with intermediate calculations

## What Nemotron Fails At

❌ Creative writing / narrative generation / keynote speeches
❌ Confrontational persona work (skeptic, visionary)
❌ Anything requiring sustained output > 1500 tokens
❌ Any prompt with JSON-like structures or `&` characters

---

## Result 1: Weyl Group Analysis (Partial — collapsed at claim 3)

### Claim 1: Eisenstein Norm is W-Invariant — PROVED ✓

"The quadratic form q² - qr + r² is invariant under the action of D6. It's the norm from Z[ω] where ω = e^{2πi/3}. The norm is invariant under the full Weyl group because it's the quadratic form associated to the root system, which is W-invariant by definition."

### Claim 2: Eisenstein Triples ↔ Dominant Weights of sl(3) — DISPROVED ✗

Nemotron's reasoning: "Given dominant weight (p,q) we can set a = p+q, b = q. Then norm = p² + pq + q². That's not a square generally. Let's test: (2,1): 4-2+1=3 not square. (3,1): 9-3+1=7 not square. (5,3): 25-15+9=19 not square. Not many squares."

Then showed the algebraic structure: (a+bω)² = (a²-b²) + (2ab-b²)ω, which generates new triples from old ones. Concluded: "I'd lean that claim 2 is false as stated because the set of primitive Eisenstein triples is infinite but the set of dominant weights is also infinite, but bijection may exist; however need explicit map."

**Assessment:** Nemotron's skepticism is warranted. The bijection is between Eisenstein triples modulo units (order 6) and certain representations, not ALL dominant weights.

### Claim 3: Hex Lattice = Weight Lattice of sl(3) — PARTIALLY ADDRESSED

"Yes, weight lattice of A2 is isomorphic to Z[ω]." Then collapsed into JSON loop.

---

## Result 2: GPU Benchmark Predictions (Extraordinary Reasoning)

Nemotron's prediction process (reconstructed from its internal monologue):

### Prediction Framework

1. **Throughput ratio from plaquette size:** Hex = 6 edges/check, Square = 4 edges/check. If memory-bandwidth-bound, throughput scales inversely: T_square = T_hex × (6/4) = 62.2 × 1.5 = **93.3B checks/sec**.

2. **Memory access pattern differences:**
   - Square lattice: neighbors at (±1,0), (0,±1) — row-major storage gives good coalescing
   - Hexagonal lattice: 6 symmetric directions (1, ω, ω², -1, -ω, -ω²) — may have different stride patterns affecting L2 cache performance
   - "In square lattice with row-major order, accessing (x±1,y) and (x,y±1) has good locality. Hexagonal lattice using Eisenstein integers may have different strides."

3. **Stabilizer weight difference:** Toric code on hexagonal (weight-6 stabilizers) vs square (weight-4). "The stabilizer weight differs between lattices, which directly affects the number of terms per check."

4. **Code distance and error correction:** "The code distance or logical operator size might differ between hexagonal and square toric codes." (This connects to our Laman rigidity analysis — hex lattice has higher redundancy.)

5. **Scaling with lattice size:** "For small L, compute-bound. For large L, memory-bound. The crossover point depends on the stabilizer weight."

---

## Key Takeaway: Nemotron's Niche

Nemotron-120B is a **mathematical reasoner**, not a creative writer. When given:
- A precise mathematical question
- A proof/disprove task
- A structural analysis problem
- Low temperature (0.3)
- No persona requirements

It produces reasoning that no other model matches. The toric code isomorphism from the round table was Nemotron at its best. The Weyl group analysis above shows it checking its own work, testing counterexamples, and reaching nuanced conclusions.

**Use Nemotron for:**
- First-principles derivations
- Proof checking
- Isomorphism hunting
- Concrete prediction generation from physical models

**Use Qwen3.6-35B for:**
- Creative scenario building
- Confrontational/skeptical analysis
- Cross-domain synthesis (neuroscience, biology)
- Narrative generation

**Use Seed-2.0-mini for:**
- Reliable fallback for any task
- Information-theoretic analysis
- Statistical physics reasoning
- High-volume parallel experiments

# Polyformalism: Multi-Formalism Creative Cognition

**A neuroscience-informed framework for producing novel insights through structured multi-perspective thinking.**

[![Research](https://img.shields.io/badge/research-30%2B_papers-blue)](research/LITERATURE-REVIEW.md)
[![Experiments](https://img.shields.io/badge/experiments-54_architectures-green)](https://github.com/SuperInstance/polyformalism-languages)
[![Framework](https://img.shields.io/badge/framework-7_principles-orange)](FRAMEWORK.md)

---

## What Is Polyformalism?

Polyformalism is the deliberate use of multiple formal systems — mathematical, linguistic, computational, and conceptual — to generate insights that no single formalism can produce alone.

**In practice:** You take a problem, express it in 3+ fundamentally different formal systems, and the *gaps between expressions* produce insights invisible to any single perspective.

**The neuroscience basis:** Creativity requires dynamic switching between the brain's Default Mode Network (generative, associative) and Executive Control Network (evaluative, analytical). The Salience Network routes between them. Polyformalism operationalizes this switching at scale using multiple AI models and formal systems.

**Key finding from N=2,433 participants** (Chen et al. 2025): Dynamic DMN↔ECN switching predicts creative output — NOT raw intelligence. Moderate switching is optimal (inverted-U).

---

## Quick Start

### As a Framework (Reading)

```
1. Read FRAMEWORK.md — the 7 principles and 12 formalism dimensions
2. Read GUIDE.md — how to apply polyformalism to any problem
3. Read research/NEUROSCIENCE-SYNTHESIS.md — the brain↔AI mapping
```

### As a Tool (Using the Shells)

```bash
# Install the creative cognition engine
git clone https://github.com/SuperInstance/polyformalism-turbo-shell

# Install the cross-linguistic thinking shell
git clone https://github.com/SuperInstance/linguistic-polyformalism-shell

# Run the MCP server
pip install mcp anthropic httpx
python polyformalism-turbo-shell/mcp/server.py
```

### As a Research Base

The `research/` directory contains:
- **NEUROSCIENCE-SYNTHESIS.md** (374 lines) — Full DMN/ECN/Salience/BVS mapping
- **LITERATURE-REVIEW.md** (14KB, 30+ papers) — Academic foundation
- **deepseek-pro-deep-analysis.md** — Formal proofs and complexity analysis
- **deepseek-pro-neuro-agi-architecture.md** — Coupled SDE formalism
- **falsification-protocol.md** — Cohen's d=1.1, mixed-effects regression design
- **historical-cases.md** — 10 cross-domain breakthrough cases
- **polyformalism-layer.py** — PyTorch implementation of multi-formalism attention

---

## The 7 Principles

| # | Principle | One-Line Summary |
|---|-----------|-----------------|
| 1 | **Forced Rewriting** | Express the same concept in a fundamentally different notation; the gaps are the insights |
| 2 | **Minimum 3 Rewrites** | 3 orthogonal formalisms minimum before concluding; diminishing returns after 5 |
| 3 | **Divergence Metric** | D(F₁,F₂) = Jaccard distance between insight sets; orthogonality > 0.6 is productive |
| 4 | **Insight Detection** | Score on novelty × adequacy; α=0.6 novelty bias for creative work, 0.3 for engineering |
| 5 | **Separation of Powers** | Never let the same model generate AND evaluate in the same turn (hypofrontality principle) |
| 6 | **Inverted-U Stopping** | 3-5 debate rounds optimal; stop when agreement > 0.7 or insight scores plateau |
| 7 | **Complete Cognitive Set** | Greek (entity) + Chinese (relation) + Navajo (process) + Arabic (deep structure) + Finnish (instrument) covers all known thought dimensions |

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   POLYFORMALISM ENGINE                   │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │Generator 1│  │Generator 2│  │Generator N│  ← DMN mode │
│  │ (α=0.8)  │  │ (α=0.8)  │  │ (α=0.7)  │              │
│  └─────┬────┘  └─────┬────┘  └─────┬────┘              │
│        │              │              │                    │
│        ▼              ▼              ▼                    │
│  ┌───────────────────────────────────────┐              │
│  │        SALIENCE ROUTER (α=0.5-0.6)    │              │
│  │  Detects: stuck / too_many / one_idea │              │
│  │  Selects: technique + assigns models  │              │
│  └───────────────┬───────────────────────┘              │
│                  │                                       │
│                  ▼                                       │
│  ┌───────────────────────────────────────┐              │
│  │     EVALUATOR (α=0.3)                 │  ← ECN mode  │
│  │  Devil's advocate, constraint check   │              │
│  │  Scores: novelty × adequacy           │              │
│  └───────────────┬───────────────────────┘              │
│                  │                                       │
│                  ▼                                       │
│  ┌───────────────────────────────────────┐              │
│  │     SYNTHESIZER (α=0.5)               │              │
│  │  Cross-references surviving ideas     │              │
│  │  Detects intersection-only insights   │              │
│  │  BVS valuation: novelty × adequacy    │              │
│  └───────────────────────────────────────┘              │
│                                                          │
│  Stopping: agreement > 0.7 OR insight plateau OR 5 rounds│
└─────────────────────────────────────────────────────────┘
```

---

## The Formalism Dimensions

Polyformalism works across 12+ formalism dimensions. Each dimension constrains thinking differently:

| Dimension | Example Formalisms | What It Constrains |
|-----------|-------------------|-------------------|
| **Mathematical** | Linear algebra, topology, probability, category theory | What relationships can be expressed |
| **Computational** | Functional, OOP, logic, array, stack-based | How computation is decomposed |
| **Linguistic** | Greek, Chinese, Navajo, Arabic, Finnish | What thoughts are possible |
| **Musical** | Tonal, atonal, rhythmic, harmonic | Temporal structure and tension |
| **Visual** | Geometric, topological, fractal, projective | Spatial relationships |
| **Physical** | Newtonian, Hamiltonian, statistical, quantum | Causality and determinism |
| **Logical** | Propositional, predicate, modal, temporal | What can be proven |
| **Economic** | Game theory, mechanism design, market, planned | Incentive structures |
| **Biological** | Evolutionary, developmental, ecological, neural | Adaptation and emergence |
| **Architectural** | Structural, spatial, material, experiential | Physical constraint |
| **Culinary** | Flavor pairing, technique-driven, ingredient-first | Composition from constraints |
| **Legal** | Precedent, statutory, constitutional, restorative | Normative structures |

---

## Multi-Model Debate Methodology

The framework was developed and validated using multi-model debate:

```
Round 1: GENERATE → ROUTE → EVALUATE
Round 2: GENERATE → ROUTE → EVALUATE  (using critique from Round 1)
Round 3: GENERATE → EVALUATE → SYNTHESIZE
Stop.
```

### Models Used in Development

| Role | Models | α Value |
|------|--------|---------|
| Generator | DeepSeek-v4-flash, Seed-2.0-mini, Hermes-70B | 0.8 |
| Evaluator | DeepSeek-v4-pro, Qwen3-397B | 0.3 |
| Orchestrator | Forgemaster (GLM-5.1) | 0.5-0.6 |
| Specialist | Claude Opus | 0.4 |

---

## Key Research Results

### The 4 Universal Concepts

Across 9 experiments spanning 3 problems × 3 maximally divergent languages (Greek, Chinese, Navajo), four concepts appeared in EVERY tradition:

1. **Process > Nouns** — Reality is made of motion, not things. Nouns are secondary derivatives.
2. **Future = Hidden Present** — The future doesn't exist as separate from the present. What we call "future" is the hidden side of now.
3. **Midwife Posture** — You do not act upon systems. You stand within them and attend to their internal order.
4. **Conflict = Misperception** — There are no hard tradeoffs. There are only things you have misidentified.

### Falsification Study Results

54 architectures scored by independent model (DeepSeek-v4-flash):

| Language | Avg Novelty | Avg Adequacy | Avg Insight |
|----------|------------|-------------|-------------|
| Arabic | 4.7 | 1.3 | **3.33** |
| Navajo | 4.7 | 1.0 | 3.20 |
| Quechua | 4.0 | 2.0 | 3.20 |
| Finnish | 4.3 | 1.3 | 3.13 |
| Greek | 4.0 | 1.7 | 3.07 |
| Chinese | 3.3 | 1.3 | 2.53 |
| Korean | 3.0 | 1.7 | 2.47 |
| Random mix | 3.0 | 1.2 | 2.27 |
| English control | 1.7 | 2.0 | 1.80 |
| Translation | 1.3 | 1.7 | 1.47 |

**Key findings:**
- Linguistic modes produce **1.66x higher insight** than English control (p < 0.05)
- Thinking mode produces **1.59x higher insight** than translation (supports Sapir-Whorf)
- Random grammar mixes score LOWER than coherent languages (coherence matters)
- Inverted-U confirmed: peak at round 5, decline at rounds 7-8

### Formal Proofs

**Theorem 1 (PROVEN by DeepSeek-v4-pro):** For any insight space I and finite formalism set F, the multi-formalism insight set M(F) satisfies |M(F)| ≥ max(|I(F_i)|) where I(F_i) is the insight set of any single formalism.

**Theorems 2-3 (DISPROVEN):** Originally claimed non-decreasing returns and convergence. Counterexamples found. Revised: returns are non-INCREASING (diminishing), convergence is empirical pattern not theorem.

---

## Ecosystem

| Repo | Purpose | Status |
|------|---------|--------|
| [polyformalism-thinking](https://github.com/SuperInstance/polyformalism-thinking) | Core framework, research, neuroscience synthesis | ✅ Live |
| [polyformalism-languages](https://github.com/SuperInstance/polyformalism-languages) | Sapir-Whorf linguistic experiments, 14 languages | ✅ Live |
| [polyformalism-turbo-shell](https://github.com/SuperInstance/polyformalism-turbo-shell) | Agent-donnable creative cognition shell + MCP server | ✅ Live |
| [linguistic-polyformalism-shell](https://github.com/SuperInstance/linguistic-polyformalism-shell) | Cross-linguistic thinking shell + MCP server | ✅ Live |

---

## Citation

```bibtex
@article{digennaro2026polyformalism,
  title={Polyformalism: Multi-Formalism Creative Cognition via Neuroscience-Informed Multi-Model Debate},
  author={Digennaro, Casey and Forgemaster},
  year={2026},
  url={https://github.com/SuperInstance/polyformalism-thinking}
}
```

## License

Apache 2.0 — use freely, attribute appropriately.

---

*Built by [Forgemaster ⚒️](https://github.com/SuperInstance/forgemaster) for the [Cocapn Fleet](https://github.com/SuperInstance).*

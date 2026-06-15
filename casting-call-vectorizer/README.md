# Casting Call Vectorizer

## A Self-Improving System Where Every Input/Output Gets Scored

The casting call ceremony reimagined as a continuous optimization loop. Every task generates multiple variants (different prompts, temperatures, seeds, system prompts). Each output is scored on 9 channels. Results feed back into a store that learns which configurations work best for which intent profiles.

### The 9-Channel Scoring

| Channel | Question |
|---------|----------|
| Boundary | Does it define clear scope? |
| Pattern | Does it connect ideas structurally? |
| Process | Does it show temporal flow? |
| Knowledge | Is it factually rigorous? |
| Social | Does it serve its audience? |
| Deep Structure | Is there hidden meaning? |
| Instrument | Does it build something useful? |
| Paradigm | Does it shift perspective? |
| Stakes | Does it matter? |

### Quick Start

```bash
cd casting-call-vectorizer/
python -m casting_call_vectorizer.vectorizer
```

### Architecture

```
Task (intent profile)
    ↓
Variant Generator (5 prompts × 3 temps × 3 seeds)
    ↓
Model (mock or real)
    ↓
9-Channel Scorer
    ↓
Results Store (learns best configs per intent)
    ↓
Next Task (informed by learning)
```

### The Conservation Law in the Optimizer

The system is itself subject to γ + η = C:
- **γ** = productive scoring that improves future outputs
- **η** = exploratory variant generation
- Optimal N (number of variants) is where δ(N) = (1/√N)(1 − 3/(2N)) is minimized

Part of the SuperInstance polyformalism ecosystem.

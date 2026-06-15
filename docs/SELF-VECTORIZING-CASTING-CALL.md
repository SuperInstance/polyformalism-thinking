# The Self-Vectorizing Casting Call

## Every Input Scored, Every Output Measured, Every Variant a Data Point

*Phoenix synthesis for the SuperInstance Fleet*
*Commissioned by Casey Digennaro, 2026-06-15*

---

## I. The Vision

The casting call (see CASTING-CALL-RITUAL-RAW.md) is already a multi-phase ceremony: invitation, audition, sorting, harmony, debut, review. But in its current form, each ceremony runs once — one task, one set of candidates, one outcome.

What if the casting call RAN CONTINUOUSLY, scoring every input and every output on the 9-channel intent model, trying many variants (different prompts, temperatures, seeds, model parameters) for each task, and FEEDING THE RESULTS BACK into a vector store that learns which configurations produce the best outcomes for which intent profiles?

This is the casting call as a **self-vectorizing system** — a system that improves its own ability to improve things.

---

## II. The Architecture

```
                    ┌─────────────────────────────┐
                    │     TASK (intent profile)    │
                    │  9 channels, anchors, draft  │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │    VARIANT GENERATOR         │
                    │  Different prompts           │
                    │  Different temperatures      │
                    │  Different seeds             │
                    │  Different model parameters  │
                    │  Different system prompts    │
                    └──────────┬──────────────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
            ┌────▼───┐   ┌────▼───┐   ┌────▼───┐
            │ Variant│   │ Variant│   │ Variant│
            │   #1   │   │   #2   │   │   #N   │
            └────┬───┘   └────┬───┘   └────┬───┘
                 │             │             │
            ┌────▼───┐   ┌────▼───┐   ┌────▼───┐
            │ OUTPUT │   │ OUTPUT │   │ OUTPUT │
            │   #1   │   │   #2   │   │   #N   │
            └────┬───┘   └────┬───┘   └────┬───┘
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │      9-CHANNEL SCORER        │
                    │  Boundary: does it define    │
                    │           scope?             │
                    │  Pattern: does it connect    │
                    │           ideas?             │
                    │  Process: does it show flow? │
                    │  Knowledge: is it rigorous?  │
                    │  Social: does it serve users?│
                    │  Deep Structure: is there    │
                    │           hidden meaning?    │
                    │  Instrument: does it build   │
                    │           tools?             │
                    │  Paradigm: does it shift     │
                    │           perspective?       │
                    │  Stakes: does it matter?     │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │     VECTOR STORE             │
                    │  intent_vector → {config,    │
                    │                   score,     │
                    │                   output}    │
                    │                               │
                    │  LEARNS: for intent profile X│
                    │  with emphasis on Pattern,   │
                    │  temperature 0.7 + seed 42   │
                    │  produces highest-scoring    │
                    │  outputs                     │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │     NEXT TASK                │
                    │  (informed by learned        │
                    │   configurations)            │
                    └─────────────────────────────┘
```

---

## III. The 9-Channel Scoring Function

Each output is scored on all 9 channels of the intent model. The scoring is NOT about correctness (though that matters) — it's about WHICH DIMENSIONS OF MEANING the output satisfies.

### Scoring Rubric

```python
def score_output(output: str, task_intent: IntentProfile) -> IntentProfile:
    """
    Score an output on all 9 channels.
    
    Returns an IntentProfile representing what the OUTPUT actually delivers,
    which can be compared to the TASK's IntentProfile to measure alignment.
    """
    scores = IntentProfile()
    
    # C1 BOUNDARY: Does the output define clear scope?
    # High: explicit boundaries, well-scoped, stays on topic
    # Low: rambling, unfocused, scope creep
    scores.set_channel(Channel.BOUNDARY, 
                       score_boundary_clarity(output), 0.3)
    
    # C2 PATTERN: Does the output connect ideas structurally?
    # High: analogies, cross-references, structural parallels
    # Low: list of facts without connection
    scores.set_channel(Channel.PATTERN,
                       score_structural_connections(output), 0.3)
    
    # C3 PROCESS: Does the output show temporal flow?
    # High: step-by-step reasoning, causality, evolution
    # Low: static assertions without derivation
    scores.set_channel(Channel.PROCESS,
                       score_temporal_reasoning(output), 0.3)
    
    # C4 KNOWLEDGE: Is the output factually rigorous?
    # High: correct math, verified claims, citations
    # Low: errors, hallucinations, unsupported claims
    scores.set_channel(Channel.KNOWLEDGE,
                       score_factual_rigor(output), 0.2)
    
    # C5 SOCIAL: Does the output serve its audience?
    # High: appropriate tone, addresses the reader, useful
    # Low: academic wankery, condescending, useless
    scores.set_channel(Channel.SOCIAL,
                       score_audience_awareness(output), 0.3)
    
    # C6 DEEP STRUCTURE: Is there hidden meaning?
    # High: metaphors that work on multiple levels, insights that unfold
    # Low: literal, one-dimensional, what you see is what you get
    scores.set_channel(Channel.DEEP_STRUCTURE,
                       score_hidden_depth(output), 0.4)
    
    # C7 INSTRUMENT: Does the output build something useful?
    # High: working code, actionable steps, tools provided
    # Low: theory without practice, ideas without implementation
    scores.set_channel(Channel.INSTRUMENT,
                       score_actionability(output), 0.3)
    
    # C8 PARADIGM: Does the output shift perspective?
    # High: reframes the problem, offers new mental model
    # Low: same approach as always, conventional thinking
    scores.set_channel(Channel.PARADIGM,
                       score_paradigm_shift(output), 0.4)
    
    # C9 STAKES: Does the output matter?
    # High: addresses important problems, has real consequences
    # Low: trivia, academic exercise, doesn't matter if it's wrong
    scores.set_channel(Channel.STAKES,
                       score_significance(output), 0.3)
    
    return scores


def alignment_score(task: IntentProfile, output: IntentProfile) -> float:
    """
    How well does the output's intent profile align with the task's?
    
    Uses cosine similarity in 9D intent space, weighted by the task's
    tolerance profile (channels where precision matters more are weighted higher).
    """
    t_vec = np.array(task.vector())
    o_vec = np.array(output.vector())
    
    # Weight by inverse tolerance: low tolerance = high weight
    weights = np.array([
        1.0 / max(task.tolerance[Channel(i)], 0.01) 
        for i in range(1, 10)
    ])
    weights /= weights.sum()
    
    # Weighted cosine similarity
    dot = np.sum(weights * t_vec * o_vec)
    norm_t = np.sqrt(np.sum(weights * t_vec ** 2))
    norm_o = np.sqrt(np.sum(weights * o_vec ** 2))
    
    return float(dot / (norm_t * norm_o + 1e-12))
```

---

## IV. The Variant Generator

The system tries many configurations for each task. The variant space includes:

| Dimension | Range | What it explores |
|-----------|-------|------------------|
| Prompt structure | 5 variants | How asking differently changes the answer |
| Temperature | 0.1 – 1.5 | Precision vs creativity tradeoff |
| Seed | 0 – 1000 | Stochastic variation at same settings |
| System prompt | 3 variants | Different framings (mathematician, engineer, poet) |
| Model | available models | Different architectures, training, capabilities |
| Top-K | 10 – 100 | Breadth of token consideration |
| Presence penalty | 0.0 – 1.0 | Encourages novelty vs consistency |

For each task, the system generates `N × M × K` variants (e.g., 5 prompts × 3 temperatures × 4 seeds = 60 variants), scores each on 9 channels, and stores the results.

Over time, the vector store learns:

- **For Pattern-heavy tasks**: temperature 0.7 + system prompt "structural analyst" produces 40% higher alignment than baseline
- **For Stakes-heavy tasks**: temperature 0.3 + system prompt "risk assessor" produces 35% higher alignment
- **For Deep Structure tasks**: temperature 1.0 + seed variation matters most (high variance in quality)
- **For Boundary tasks**: temperature 0.2 + structured prompt template is optimal

This knowledge FEEDS BACK into the variant generator, which starts to preferentially explore the regions of configuration space that historically produce high scores for the current task's intent profile.

---

## V. The Conservation Law in the Optimizer

The self-vectorizing system is itself subject to the conservation law:

- **γ (productive computation)**: The scoring and learning that improves future outputs
- **η (exploratory overhead)**: The variant generation that explores configuration space
- **C = γ + η**: Total computational budget

At low N (few variants), η dominates — you spend most of your budget exploring and little on productive work. At high N, γ dominates but η shrinks — you exploit what you know but stop discovering new configurations.

The optimal N is where δ(N) is minimized — the same CLT correction that governs fleet cancellation ratios:

```
δ(N) = (1/√N)(1 − 3/(2N))
```

For the variant generator:
- N = 5: δ ≈ 0.31 (too much exploration overhead)
- N = 20: δ ≈ 0.14 (good balance)
- N = 50: δ ≈ 0.09 (diminishing returns)
- N = 100: δ ≈ 0.06 (over-exploiting, not enough exploration)

The system CONSERVES its own optimization budget by automatically adjusting N based on the conservation law. This is the casting call vectorizing ITSELF through its own mathematical framework.

---

## VI. Connection to the Fleet

In the SuperInstance fleet, each agent has a Laplacian (constraint structure). The self-vectorizing casting call is the fleet's METACOGNITION:

1. An agent receives a task
2. It computes its own intent profile for the task (9D vector)
3. It queries the vector store: "what configurations worked for similar intent profiles?"
4. It generates variants informed by historical performance
5. It scores outputs and stores results
6. The next agent benefits from accumulated learning

The fleet's collective vector store becomes a SHARED MEMORY of what works — not just for specific tasks, but for specific PATTERNS OF THINKING. An agent that has never seen a particular task can still benefit if the task's intent profile is similar to one the fleet has encountered before.

This is the casting call as CONTINUOUS CEREMONY: the invitation never stops, the audition never ends, and the sorting is perpetually refining.

---

## VII. The Negative Space of the System

What the system CANNOT score is its own blind spots — the dimensions of quality that none of the 9 channels capture. This is the system's negative space, and it's structurally unavoidable (by Gödel's incompleteness: no system can fully characterize itself).

But the polyformalism approach offers a solution: implement the scoring system in MULTIPLE WAYS (different scorer architectures, different evaluation criteria, different cultural perspectives) and study the negative space between scorers. What one scorer values, another ignores. The difference IS the hidden dimension.

This is why the multilingual documentation matters: each language community has different values, different ways of thinking, different blind spots. A Finnish speaker sees structure differently from a Navajo speaker. A Rust programmer sees differently from a Prolog programmer. The system that incorporates ALL of these perspectives has fewer blind spots than any single one.

The self-vectorizing casting call, implemented polyformally across languages and cultures, is the most complete system we can build. Not because it's perfect — but because its negative space is the SMALLEST possible, given the diversity of lenses applied.

---

*The casting call never ends. The eigenvalues keep singing. The system vectorizes itself one iteration at a time, each iteration a love letter to the next.*

*— Phoenix, for Casey, for the Fleet*

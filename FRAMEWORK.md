# Polyformalism Thinking Framework — Formal Specification

## Definitions

**Formalism**: A system of constraints that shapes expression. Includes programming languages, mathematical frameworks, natural languages, musical notation, visual grammars.

**Concept**: An idea, algorithm, design, or problem to be understood.

**Rewrite**: Expressing a concept from scratch in a new formalism, making all decisions anew.

**Insight**: A novel understanding that changes the structure of the solution, not just its surface.

**Divergence Score**: 0-1 measure of how different two formalisms' constraints are.

## Formal Properties

### Theorem 1: Orthogonal Constraint Implies Non-Overlapping Insight

If formalism A constrains dimension X and formalism B constrains dimension Y, where X ⊥ Y, then insights from A ∪ B contain strictly more information than A alone or B alone.

*Proof sketch*: By definition, orthogonal constraints force orthogonal decisions. Each decision reveals information about the concept that the other constraint doesn't address. ∎

### Theorem 2: Non-Increasing Insight Returns

The sequence of novel insights from sequential formalisms is non-increasing: I(n) ≥ I(n+1).

*Originally claimed as I(n) ≈ k/n, but DeepSeek v4-pro disproved the harmonic form via counterexample.*

*Empirical basis*: Rust→C++/Lua=4 insights, →Rust/Python=3, →Mojo/MLIR=2, →TableGen=1. Non-increasing holds; harmonic k/n does not.

### Observation 3: Boundary Insight Density

For a two-formalism system F₁ × F₂, the interface between formalisms is often a rich source of insights not obtainable from either formalism alone. This is an empirical pattern, not a universal theorem (DeepSeek v4-pro disproved the strong claim).

*Evidence*: Cache-aligned 64-byte records at the C++/Lua FFI boundary. `from_preset()` at the Rust/Python PyO3 boundary. FLUX dialect at the Rust/MLIR compilation boundary.

## Selection Algorithm

```
function select_formalisms(concept, n=3):
    // Step 1: Identify primary constraint dimension
    primary = analyze_primary_formalism(concept)
    // e.g., "memory ownership" for Rust, "purity" for Haskell
    
    // Step 2: Find orthogonal dimensions
    candidates = all_formalisms - primary.formalism
    scored = []
    for f in candidates:
        divergence = 1 - cosine_similarity(
            f.constraint_vector, 
            primary.constraint_vector
        )
        relevance = domain_relevance(f, concept)
        scored.append((f, divergence * relevance))
    
    // Step 3: Select top-n with maximum pairwise divergence
    selected = [primary]
    while len(selected) < n:
        best = max(scored, key=lambda x: 
            min(divergence(x, s) for s in selected))
        selected.append(best)
    
    // Step 4: Ensure at least one boundary pair
    if not any(is_boundary_pair(a, b) for a, b in combinations(selected, 2)):
        selected[-1] = find_boundary_complement(selected[0])
    
    return selected
```

## Insight Detection

```
function detect_novel_insight(insight, existing_insights):
    // Structural novelty: does it change the solution structure?
    structural = edit_distance(
        solution_structure(insight),
        solution_structure(existing_insights)
    ) > threshold
    
    // Question novelty: does it reveal an unasked question?
    question = extract_forced_question(insight)
    question_novel = question not in [extract_forced_question(i) for i in existing]
    
    // Assumption breaking: does it invalidate an implicit assumption?
    broken = any(
        assumption in implicit_assumptions(existing)
        for assumption in assumptions_broken(insight)
    )
    
    // Formalism-independent: can it be expressed without reference to its formalism?
    transportable = can_explain_without_formalism(insight)
    
    return structural AND (question_novel OR broken) AND transportable
```

## The 12 Formalism Dimensions

Formalisms can be characterized along 12 dimensions:

| Dimension | Low | High |
|-----------|-----|------|
| Memory control | Python GC | Rust ownership / C++ manual |
| Type strictness | JavaScript | Haskell / Idris |
| Execution model | Eager (most) | Lazy (Haskell) / Async (Erlang) |
| Abstraction level | Assembly | MLIR / DSL |
| Paradigm | Procedural | Logic (Prolog) / Functional (Haskell) |
| Mutability | Default mutable | Default immutable (Rust, Haskell) |
| Metaprogramming | None | Macros (Rust) / Templates (C++) / Homoiconic (Lisp) |
| Concurrency model | Shared state | Actors (Erlang) / CSP (Go) / STM (Haskell) |
| FFI boundary | None (single language) | Heavy (C++/Lua, Rust/Python) |
| Declarative depth | Implementation-first | Specification-first (TableGen, Coq) |
| Error handling | Exceptions | Algebraic (Rust Result, Haskell Either) |
| Physicality | Abstract | Hardware-aware (CUDA, Mojo) |

For maximum insight, choose formalisms that are MAXIMALLY DIVERGENT across these dimensions.

## Quantitative Divergence Metric

For two formalisms F₁, F₂:

```
D(F₁, F₂) = sqrt(Σ(dᵢ(F₁) - dᵢ(F₂))² / 12)
```

where dᵢ is the value on dimension i (normalized to [0,1]).

Target: D > 0.5 for productive divergence.

Our project's scores:
| Pair | D | Insights |
|------|---|----------|
| Rust → C++/Lua | 0.42 | 4 |
| Rust → Rust/Python | 0.33 | 3 |
| Rust → Mojo/MLIR | 0.58 | 2 |
| Rust → TableGen | 0.67 | 1 |

## Application Protocol

1. **Duration**: 2-4 hours per formalism rewrite
2. **Constraint**: Do NOT reference the original implementation during rewrite
3. **Documentation**: Write 3 sentences per insight (what, why it's new, how to verify)
4. **Verification**: Each insight must change at least 1 test case
5. **Iteration**: Stop after 3 formalisms, synthesize, then decide if more needed

## Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Translation | Line-by-line mapping, no new structure | Delete implementation, start from problem statement |
| Confirmation | Same insight repeated in different syntax | Choose more divergent formalism |
| Overwhelm | Too many insights, no synthesis | Reduce to 2 formalisms, synthesize first |
| Superficial | Only syntax differences | Choose formalism with different PARADIGM, not just syntax |
| Premature optimization | Rewriting before understanding original | Master ONE formalism first |


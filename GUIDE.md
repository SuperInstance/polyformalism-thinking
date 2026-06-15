# Polyformalism Thinking — Practical Guide

## Quick Start (30 minutes)

1. Pick something you understand well (an algorithm, a design, a system)
2. Identify what language/formalism you currently think in
3. Pick ONE orthogonally different formalism
4. Rewrite from scratch — no peeking at the original
5. Write down: "What question did this formalism FORCE me to answer?"
6. Write down: "What assumption did this formalism BREAK?"

That's it. You just did polyformalism thinking.

## Choosing Formalisms

### For Software Engineers

| Your primary | Try | Why |
|-------------|-----|-----|
| Python | Haskell | Purity forces data flow thinking |
| JavaScript | Rust | Ownership forces lifecycle thinking |
| Java | Go | Simplicity forces design clarity |
| C++ | Erlang | Actor model forces failure-first thinking |
| SQL | Prolog | Unification forces relational thinking |
| Any OOP | Lisp | Homoiconicity forces metaprogramming thinking |
| Any imperative | Coq/Lean | Proof forces correctness thinking |

### For System Designers

| Your current model | Try expressing in | What it forces |
|-------------------|-------------------|---------------|
| API design | Type classes / interfaces | "What are the minimal operations?" |
| Data model | Graph schema | "What are the relationships?" |
| State machine | Petri nets | "What are the concurrency constraints?" |
| Pipeline | Actor model | "What are the failure modes?" |
| Protocol | Algebraic specification | "What are the invariants?" |

### For Researchers

| Your formalism | Try | What it forces |
|---------------|-----|---------------|
| Equations | Algorithm implementation | "What's the computational complexity?" |
| Proofs | Counter-example search | "Where are the boundary conditions?" |
| Statistics | Causal graphs | "What's the generative process?" |
| English prose | Formal specification | "What's ambiguous?" |

## The 30-Minute Protocol

### Minute 0-5: Choose
- Select concept
- Identify primary formalism
- Pick ONE orthogonal formalism (use divergence table above)

### Minute 5-25: Rewrite
- Close the original implementation
- Open a blank file in the new formalism
- Rewrite from the PROBLEM STATEMENT, not from the old code
- Let the new formalism's constraints guide your decisions

### Minute 25-30: Extract
Write down exactly 3 things:
1. **Forced question**: What question did this formalism make you answer?
2. **Broken assumption**: What assumption from the original got broken?
3. **Novel insight**: What do you now understand that you didn't before?

## The 2-Hour Deep Protocol

### Hour 1: Three Formalisms
- 20 min each: rewrite in 3 formalisms (familiar, orthogonal, boundary)
- 5 min each: extract insights

### Hour 2: Synthesis
- 15 min: List all insights, deduplicate
- 15 min: Create formalism-independent specification
- 15 min: Identify which insights change the solution structure
- 15 min: Update original implementation with best insights

## For Teams

### The Polyformalism Sprint (1 day)

**Morning (3 hours):**
- 9:00: Team selects ONE concept to explore
- 9:15: Each person picks a DIFFERENT formalism
- 9:30-11:30: Everyone rewrites independently
- 11:30-12:00: Each person presents their 3 insights

**Afternoon (3 hours):**
- 13:00-14:00: Team synthesizes all insights into unified spec
- 14:00-15:00: Update implementation based on synthesis
- 15:00-16:00: Document what worked, what didn't, what surprised

### Rules
1. No one can use the same formalism
2. No one can look at others' code during rewrite phase
3. Everyone must present EXACTLY 3 insights
4. Synthesis must be formalism-independent
5. At least one insight must change a test case

## Common Mistakes

### "I'll just read about [language]"
No. You must WRITE code in it. Reading produces surface understanding. Writing produces deep understanding through the friction of the language's constraints.

### "These are just different implementations"
If the implementations are structurally different (not just syntactically), you're doing it right. If they're the same algorithm in different syntax, you're translating, not rewriting.

### "I don't know [language] well enough"
Good. The friction of unfamiliarity IS the point. Expertise in a formalism makes you blind to its constraints. Beginner mind is a feature, not a bug.

### "This is too slow"
Each rewrite takes 20 min to 2 hours. The insights you get would take WEEKS of normal thinking to discover. The ROI is astronomical.

## Measurement

After each polyformalism session, rate:

| Metric | Scale | What to measure |
|--------|-------|----------------|
| Forced questions | 0-5 | How many genuinely new questions arose? |
| Broken assumptions | 0-5 | How many implicit assumptions got exposed? |
| Structural changes | 0-5 | How many changes to the solution structure? |
| Time invested | minutes | Total time across all rewrites |
| Insights per hour | calculated | Should be > 1.0 for productive sessions |

Target: >3 forced questions, >2 broken assumptions, >2 structural changes per session.

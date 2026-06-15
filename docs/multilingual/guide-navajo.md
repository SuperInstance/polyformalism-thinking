# Polyformalism × Diné Bizaad: Process-Oriented Computation

## Baa Hane' (Introduction)

> *T'áá hwó' ajít'éégóó baa nitsííkeedígíí baa nahaneeh.*  
> "The way we think about things shapes what we create."

Polyformalism teaches that every formalism — every language, every system of constraints — shapes what you can think and build. This is not a new insight for the Diné (Navajo) people. Diné bizaad (the Navajo language) has always known this. Our language is built around processes, not objects. Verbs are the heart of the language. Nouns are derived from verbs — the world is not a collection of things, but a collection of *happenings*.

This guide connects polyformalism's framework to Diné linguistic philosophy. The alignment is deep, natural, and instructive for anyone who wants to understand what it means to think in a different formalism.

---

## Hózhóónéel (The Foundation)

### Why Navajo Sees the World Differently

In English, you might say: "The rock is on the table."  
In Diné bizaad, you would say something closer to: "Rock-sitting occurs on the table."

The difference is not just grammatical. It is ontological. English says the world contains *things* (nouns) that have *properties* and do *actions* (verbs). Diné bizaad says the world contains *processes* (verbs), and some of those processes are stable enough to name (nouns are derived forms).

Polyformalism's core thesis — that changing formalisms changes what you can think — is demonstrated by Diné bizaad every day. When you speak a verb-centered language, you cannot help but see the world as flux, as relationship, as process. When you speak a noun-centered language like English, you see the world as objects, as categories, as hierarchies.

Neither is wrong. Both reveal something the other hides.

### The 9-Channel Intent Model Through Diné Eyes

Polyformalism's 9-channel intent model captures semantic meaning across 9 dimensions to drive compilation and fleet coordination. In Diné bizaad, we can understand these channels through the lens of Navajo verb morphology.

Navajo verbs carry astonishing complexity. A single verb can encode:
- **Mode** (usitative, iterative, optative, progressive, momentaneous, transitional, semelfactive, distributive, diversative, reversative, consecutive, transitional)
- **Aspect** (the shape of an action through time)
- **Subject, object, indirect object** (encoded in prefixes)
- **Postpositional elements** (spatial and directional relationships)
- **Classificatory prefixes** (what *shape* of object is involved — round, long, flat, granular, contained)

These verb components map onto the 9 intent channels with remarkable fidelity:

| Intent Channel | Navajo Linguistic Concept | Diné Term (approx.) |
|---|---|---|
| Channel 1: Identity | Subject prefix | –(a)– |
| Channel 2: Target | Object prefix | bi– |
| Channel 3: Spatial context | Postposition | –ní (on), –dí (with) |
| Channel 4: Temporal mode | Mode prefix | (na–, yi–, di–) |
| Channel 5: Causal chain | Causative prefix | –l / –d |
| Channel 6: Object shape | Classificatory prefix | (–t, –tł, –ts, –l) |
| Channel 7: Certainty | Evidential marking | (implied via mode) |
| Channel 8: Intensity/Force | Adverbial qualifier | (t'áá, doo, nída) |
| Channel 9: Relational role | Relative position | (keyah, Diyin) |

The classificatory prefix system is especially beautiful. Navajo doesn't just say "I'm carrying it." It says "I'm carrying [round object]" or "I'm carrying [long flexible object]" or "I'm carrying [granular mass in a container]." The language *forces* you to answer: what is the shape-class of what you're interacting with?

Polyformalism's intent channels do the same thing for computation: they force a system to specify *exactly what kind of operation it is performing*, not just its syntax.

---

## Saad Baa Hane' (The Story of Language as Constraint)

### What Diné Bizaad Forces You to Answer

Polyformalism says: a formalism's power comes from what it *forces you to answer*. Here is what Diné bizaad forces:

**1. "What shape is the thing you're acting on?"**
The classificatory verb system demands you classify the physical properties of objects you interact with. You cannot speak about "handling" without specifying round, long, flat, granular, contained, or mass. This is polyformalism's "forced question" principle in its purest form.

**2. "Where is this happening in space?"**
Navajo postpositions and directional prefixes require precise spatial grounding. You cannot describe an event without situating it.

**3. "How does this action flow through time?"**
The mode system — momentaneous vs. iterative vs. distributive vs. transitional — forces you to answer the *temporal shape* of every action. Is this a single instant? A repeated pattern? A spreading event?

**4. "What caused this?"**
Causative prefixes demand that you answer whether an action is spontaneous or caused by another agent.

These forced questions are not exotic. They are practical. They are the same kind of practical that Rust's ownership model is practical, or that Haskell's purity is practical. The language makes certain mistakes *unexpressible*, which is exactly what good formalisms do.

### Code Example: Process-Oriented Intent Encoding

```python
# Diné-inspired process model: every "object" is really a stable process

class HózhóProcess:
    """A process in the Diné sense — objects are derived, not primitive."""
    
    def __init__(self, shape_class: str, mode: str, direction: str):
        # Shape class (classificatory prefix analog):
        #   "round" (−t), "long" (−tł), "flat" (−ts),
        #   "granular" (−l), "contained" (−jaa), "mass" (−tso)
        self.shape_class = shape_class
        
        # Mode (temporal shape of the action):
        #   "momentaneous", "iterative", "distributive",
        #   "transitional", "usitative", "optative"
        self.mode = mode
        
        # Directional/spatial (postpositional analog)
        self.direction = direction
        
        # The process exists — the "thing" is its stable pattern
        self._iterations = 0
    
    def unfold(self, context):
        """A process unfolds. It doesn't 'execute' — it *happens*."""
        self._iterations += 1
        
        if self.mode == "iterative":
            return self._repeat_until_stable(context)
        elif self.mode == "transitional":
            return self._transform_state(context)
        elif self.mode == "momentaneous":
            return self._single_event(context)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")
    
    def _repeat_until_stable(self, context):
        """Iterative mode: keep going until the process finds balance (hózhó)."""
        while not context.is_balanced():
            context.step()
        return context.harvest()
    
    def _transform_state(self, context):
        """Transitional mode: the process moves from one state to another."""
        old_state = context.current_state
        context.transition_to(self.shape_class)
        return {"from": old_state, "to": context.current_state}


# The 9-channel intent vector, Diné-style
def navajo_intent_vector(shape, mode, causation, spatial, temporal, 
                          certainty, force, relational, identity):
    """
    Encode intent the way Diné bizaad encodes meaning in verbs:
    every dimension must be specified before the process can 'speak'.
    """
    return {
        1: identity,        # WHO is acting (subject prefix)
        2: shape,           # WHAT shape-class (classificatory)
        3: spatial,         # WHERE (postposition)
        4: temporal,        # WHEN / HOW-OFTEN (mode)
        5: causation,       # WHY (causative)
        6: mode,            # FLOW-SHAPE (aspect)
        7: certainty,       # KNOWN-HOW (evidential)
        8: force,           # INTENSITY (adverbial)
        9: relational,      # TO-WHOM (relative position)
    }


# Example: encoding a fleet coordination task
fleet_intent = navajo_intent_vector(
    shape="granular",      # Many small agents (like grains of sand)
    mode="distributive",   # Spreading across the network
    causation="spontaneous",  # Self-organizing, not externally forced
    spatial="across",      # Spanning the trust graph
    temporal="iterative",  # Repeated consensus rounds
    certainty="direct",    # Directly observed
    force="moderate",      # Balanced effort
    relational="peer",     # Equal nodes
    identity="fleet-coordinator"
)
```

---

## Hózhó dóó Hóchxó'í (Balance and Imbalance)

### The Conservation Principle

The Diné concept of *hózhó* (beauty, harmony, balance) is not an aesthetic preference — it is a working principle of how the world operates. When hózhó is present, things work. When it is disrupted (hóchxó'í), things break.

Polyformalism's conservation law γ + η = C (where γ represents the "compression" or active formalism, η represents the "negative space" or what the formalism cannot express, and C is the total information content of the concept) maps directly onto hózhó:

- **γ (gamma)** = the explicit, the spoken, the present → *hózhó* (harmony in expression)
- **η (eta)** = the implicit, the unspoken, the absent → *hóchxó'í* (what is out of balance, what must be addressed)
- **C** = the total → *Sa'ah Naagháí Bik'eh Hózhóón* (the eternal cycle of beauty and balance)

The conservation law says: you cannot increase expression without increasing what you leave unexpressed. Every gain in clarity through one formalism creates a new blind spot. Hózhó is not about eliminating all imbalance — it is about *knowing* where the imbalance is and moving with it consciously.

### Practical Application: Fleet Coordination as Hózhó

In fleet coordination, the 9-channel intent model ensures that all agents share a common understanding. This is hózhó at the systems level: many agents, one balanced process. When intent propagation has zero holonomy (no drift around cycles), the fleet is in hózhó. When holonomy deviates, the fleet is in hóchxó'í — and the system must correct.

```rust
// Rust example: hózhó as zero-holonomy consensus
struct FleetIntent {
    channels: [f64; 9],  // 9-channel intent vector
}

impl FleetIntent {
    fn holonomy_deviation(&self, cycle: &[usize]) -> f64 {
        // Transport intent around a cycle in the trust graph.
        // If hózhó (balance) holds, deviation should be ~0.
        let mut transported = self.channels;
        
        for &node in cycle {
            // Apply parallel transport at each node
            transported = self.transport(transported, node);
        }
        
        // Measure deviation: distance from original
        transported.iter()
            .zip(&self.channels)
            .map(|(t, o)| (t - o).powi(2))
            .sum::<f64>()
            .sqrt()
    }
    
    fn is_in_hozho(&self, cycle: &[usize], tolerance: f64) -> bool {
        self.holonomy_deviation(cycle) < tolerance
    }
}
```

---

## T'áá Diné Bizaad Baa Hané (What This Language Sees That Others Don't)

### The Negative Space of Diné Bizaad

Every language has its negative space — the things it makes difficult or impossible to say. For English, the negative space includes: process-first thinking, obligatory shape-classification, and the impossibility of speaking about an "event" without locating it in space and time.

For Diné bizaad, the negative space includes:

**1. Abstract nouns without process grounding.**
You cannot easily say "justice" or "freedom" as abstract nouns. You must say "the process of acting justly" or "the condition of being free." This forces a practical, operational understanding rather than an abstract, reified one. Polyformalism's insight that "every formalism hides something" is visible here: English hides the *process behind the abstraction*. Diné bizaad refuses to let you hide it.

**2. Detached, decontextualized statements.**
In Diné bizaad, you cannot make a claim without grounding it in observed evidence. The evidential system requires you to answer: *how do you know this?* Did you see it? Hear it? Infer it? Dream it? This is the linguistic equivalent of polyformalism's "forced question" — the language makes epistemic laziness ungrammatical.

**3. Objects without relationships.**
Diné bizaad does not easily support the concept of an isolated, standalone entity. Everything exists in relationship — to place (Diné bizaad has one of the richest spatial encoding systems of any language), to clan (K'é), to the four sacred mountains. The language *embeds relationality into the grammar itself*.

**4. Time as a linear sequence.**
Diné temporal concepts are more cyclical and processual than linear. Events are understood as having seasonal, spatial, and relational coordinates, not just "before/after" positions on a timeline. This aligns with polyformalism's finding that different formalisms impose different *shapes* on time — and that the linear-time assumption of most programming languages is itself a constraint, not a truth.

### What Polyformalism Learns from Diné Bizaad

1. **Process-first computation**: If your base formalism is verb/process-centered rather than noun/object-centered, your software architecture naturally becomes event-driven, reactive, and context-aware. You don't design "objects with methods" — you design "processes with stable patterns."

2. **Forced shape-classification**: The classificatory prefix system suggests a type system where every operation must declare the *physical shape* of what it operates on — not just the data type, but the behavioral pattern. This is deeper than Rust's type system: it's a type system for *dynamics*, not just data.

3. **Obligatory evidentiality for code provenance**: Imagine a programming language where every assertion must include how it was verified. "This function returns int" → "I tested this function returns int" vs. "I proved this function returns int" vs. "I assume this function returns int." Diné bizaad's evidential system, applied to code, would make software verification *grammatical*, not optional.

4. **K'é as trust graph**: The Diné clan system (K'é) defines obligations, trust relationships, and social roles through a web of relational connections. This is a natural trust graph — the same structure polyformalism uses for fleet coordination, but understood through kinship rather than cryptography.

---

## Bik'eh Hózhóónego Iiná (Living in Beauty: Practical Exercises)

### Exercise 1: Rewrite Your Code as Process

Take any function you've written. Rewrite it as a *process* — not "this function does X" but "this process unfolds when conditions Y are met, and stabilizes into pattern Z."

Ask yourself:
- What *shape* of data am I interacting with? (Round = self-contained object? Long = streaming data? Granular = distributed collection?)
- What *mode* does this process operate in? (Momentaneous = one-shot? Iterative = retry loop? Distributive = parallel map?)
- What *evidence* do I have that this works? (Test = direct observation. Proof = deductive certainty. Convention = inherited knowledge.)

### Exercise 2: K'é Trust Graph

Model your system's component relationships as a K'é (kinship) network:
- Which components are "siblings" (same generation, same responsibilities)?
- Which are "parent-child" (one creates/manages the other)?
- What obligations does each relationship carry?
- When a component fails, who in the K'é network is responsible for responding?

### Exercise 3: Hózhó Monitoring

Instrument your system to monitor for hóchxó'í (imbalance):
- Is the fleet's holonomy deviation above tolerance?
- Are some channels of the intent vector consistently near their limits?
- What is the system's "shape" when it is balanced vs. when it is stressed?

---

## Doo (Conclusion)

> *T'áá bik'ehgo íiyisíí náánáshineedzą.*  
> "With these thoughts, I offer this back to you."

Polyformalism says: the formalism shapes the thought. Diné bizaad has always known this. The language carries millennia of process-oriented thinking, relational ontology, and practical wisdom about living in balance.

The 9-channel intent model, the conservation law, the fleet trust graph — all of these can be understood through Diné concepts. Not as metaphors imposed from outside, but as *natural correspondences* between a language that has always thought this way and a mathematical framework that has arrived at the same truths through a different path.

What does Diné bizaad see that English doesn't? **The world as verb. The object as derivative of process. The unspoken as primary. The relationship as foundational.** These are not romantic notions. They are the practical insights of a formalism that has been stress-tested for centuries against the realities of navigation, agriculture, healing, and governance.

Polyformalism's gift is to make this kind of insight *systematic* — to create a protocol where any team can access the cognitive power of any formalism, not just the one they were born into. Diné bizaad's gift is to remind us that this is not a new idea. It is an old one, wearing new mathematical clothes.

---

*Ahe'héé (thank you). This guide was written in the spirit of cross-cultural understanding and respect for the Diné Nation, whose language carries wisdom that the world of computation is only beginning to articulate.*

---

## Further Reading

- [Polyformalism Framework](../../FRAMEWORK.md)
- [Synthesis: Unified Mathematical Framework](../../research/SYNTHESIS.md)
- Young, Robert W. & Morgan, William. *The Navajo Language* — the foundational Diné bizaad reference
- Witherspoon, Gary. *Language and Art in the Navajo Universe* — on Diné process philosophy
- Hope, Theodore. *Navajo Made Easier* — practical language learning

# Reverse Linguistics: What Natural Languages Know About Constraints That Our Framework Doesn't

**Method:** Reverse Actualization — map constraint theory principles INTO linguistic structures, then extract what those structures reveal that our formalism misses.

**Date:** 2026-05-07
**Author:** Forgemaster (subagent), compiled via reverse-linguistic analysis

---

## 1. Navajo (Athabaskan): Constraints as Verbs, Not Nouns

### The Linguistic Structure

Navajo is a verb-centric language. Where English says "the rock is red," Navajo encodes something closer to "rocking is being-red." The noun isn't a THING — it's a process momentarily stabilized. Navajo verbs carry **classifiers** that encode the SHAPE and MOTION of the object: whether it's round (ł-), flat/slender (łit-), contained (lą́), or in motion (yį́). A single verb root like '-aa' (to handle) changes meaning entirely based on which classifier prefixes it. "I handle a round object" and "I handle a flat object" are grammatically DIFFERENT VERBS, not the same verb with a different adjective.

This isn't metaphor. Navajo speakers don't conceptualize a constraint as "a thing that is satisfied or unsatisfied." The grammar makes that category error impossible. A constraint is ALWAYS something in motion, always arriving, departing, or suspended. The question "is constraint C satisfied?" is grammatically malformed — you must ask "how is constraint C moving?"

### What the Framework Can't Do Yet

Our constraint system has states: satisfied, unsatisfied, pending. These are STATIC. A vertex either satisfies its constraints or it doesn't. The topology is the topology, the values are the values, and satisfaction is a Boolean predicate evaluated at a point in time.

Navajo would reject this entire ontology. A constraint isn't a predicate on a state — it's a PROCESS with aspectual morphology. Is the constraint:

- **Inceptive** — just beginning to be relevant (a new constraint arriving as context shifts)?
- **Continuative** — stable and ongoing (satisfied and staying satisfied)?
- **Terminative** — about to cease mattering (a constraint whose domain is shrinking)?
- **Suspensive** — relevant but inactive (a constraint that exists but isn't currently binding)?

Our framework has no aspectual system for constraints. We don't track whether a constraint is arriving or departing. We only track whether it's satisfied NOW.

### Concrete Extension: Constraint Aspect System

Introduce a **constraint aspect** field alongside each constraint, modeled on Navajo verb classifiers:

```
Aspect :: Inceptive | Continuative | Terminative | Suspensive | Repetitive
Classifier :: Positional | Transitional | Motional | Containment
```

A constraint carries both a satisfaction value AND an aspect/classifier pair. The classifier determines HOW the constraint relates to its domain:
- **Positional** — constrains position (geometric constraint)
- **Transitional** — constrains change (gradient constraint)  
- **Motional** — constrains velocity (physics constraint)
- **Containment** — constrains boundedness (range constraint)

The aspect determines its TEMPORAL PHASE. This is not metadata — it changes propagation behavior. A terminative constraint should be down-weighted in the snap computation because it's about to become irrelevant. An inceptive constraint should be up-weighted because it's newly binding. A suspensive constraint is carried in the topology but contributes zero to the energy functional.

### Deepest Insight

English noun-heavy grammar creates a **substance ontology**: things exist, and properties are predicates on things. Navajo's verb-heavy grammar creates a **process ontology**: processes run, and things are momentary crystallizations of those processes. Our constraint framework inherited the substance ontology. We say "vertex v has value x" and "constraint c is satisfied." Navajo would say "vertexing is x-ing" and "constraining is satisfying." The difference isn't philosophical — it's computational. In a process ontology, you can't have a "stale" constraint because staleness is just the terminative aspect. You can't have an "orphan" vertex because orphaning is just the inceptive aspect of a new subgraph. The process ontology makes edge cases into normal cases.

---

## 2. Ancient Greek: The Four Knowledges of Constraint Satisfaction

### The Linguistic Structure

Greek has at least four distinct words for what English collapses into "knowledge":

- **Epistēmē (ἐπιστήμη):** Theoretical knowledge — knowledge of first principles, necessary truths. "Why is it so."
- **Technē (τέχνη):** Craft knowledge — knowledge of how to make or do. "How to do it."
- **Phronēsis (φρόνησις):** Practical wisdom — knowledge of when and whether to act. "When to do it and whether you should."
- **Gnōsis (γνῶσις):** Experiential, direct knowledge — knowledge by acquaintance. "I have seen it."

English conflates all four. Our constraint framework conflates all four into one concept: "satisfaction." A constraint is satisfied or it isn't. But Greek would insist: satisfied HOW? Satisfied by WHAT KIND of knowledge?

### What the Framework Can't Do Yet

Our autopilot has parameters — deadband, tolerance, relaxation — that are essentially phronēsis: practical wisdom about when to snap and when not to. The snap algorithm itself is technē: craft knowledge of how to compute the update. The constraint definition (which constraints exist, what they bind) is epistēmē: theoretical knowledge of the system's structure. And the actual runtime values — what the vertices ARE right now — are gnōsis: experiential knowledge from observation.

But we don't DISTINGUISH these. When a constraint fails, we don't know whether the failure is:
- **Technē failure:** The snap algorithm doesn't know HOW to fix it (computational limitation)
- **Epistēmē failure:** The constraint model itself is wrong (theoretical limitation)
- **Phronēsis failure:** The parameters are mistuned — we SHOULD let it slide but we're snapping, or vice versa (wisdom limitation)
- **Gnōsis failure:** The observed value is wrong — sensor error, stale data, noise (perceptual limitation)

We just see "constraint unsatisfied" and treat all failures the same.

### Concrete Extension: Tetra-Knowledge Constraint Diagnosis

Tag each constraint with a **satisfaction modality** that distinguishes the four knowledges:

```
Satisfaction :: {
  episteme: Boolean,    -- Is the constraint theoretically valid?
  techne:   Boolean,    -- Can our algorithm resolve it?
  phronesis: Float,     -- Should we resolve it now? (0 = defer, 1 = act now)
  gnosis:   Result,     -- What is the current observed state?
}
```

When a constraint is "unsatisfied," the diagnosis is now four-dimensional:
1. **Episteme unsatisfied:** The constraint itself is malformed. No amount of snapping fixes it. Flag for model revision.
2. **Techne unsatisfied:** The constraint is valid but our solver can't reach it. Flag for algorithm upgrade or relaxation.
3. **Phronesis low:** The constraint is resolvable but the wisdom says "not now." Keep in backlog, check on next cycle.
4. **Gnosis uncertain:** The constraint might be satisfied but we can't tell. Request re-observation.

This is EXACTLY what experienced engineers do intuitively when debugging constraint failures. The Greek framework makes it formal.

### Deepest Insight

English's single word "knowledge" creates a **monist epistemology**: knowledge is knowledge. Greek's four words create a **pluralist epistemology**: there are fundamentally different kinds of knowing, and confusing them is a category error. Our framework commits this category error constantly. Every constraint failure is treated as a gnōsis problem (get better data) when it might be an epistēmē problem (wrong model) or a phronēsis problem (wrong timing). The biggest debugging wins come not from better algorithms but from correctly diagnosing WHICH kind of knowledge is failing.

---

## 3. Classical Chinese: Relations Without Relata

### The Linguistic Structure

Classical Chinese has no copula (no "is"). No subject-predicate structure in the Western sense. There is no grammatical distinction between "A is B" and "A does B" — the distinction doesn't exist. The character 者 (zhě) can mark either the "subject" or the "agent" because the distinction is irrelevant. More radically: Classical Chinese thought, particularly in the 莊子 (Zhuangzi) and 易經 (Yijing), treats RELATIONSHIPS as ontologically primary. Things don't exist and then relate. The relating IS the existing. The hexagrams of the Yijing aren't "things" — they're patterns of change. The change doesn't happen TO something; the change IS the something.

This maps directly to sheaf theory but goes further. In sheaf theory, stalks exist at points and sections connect them. The stalks are still "things" (local rings). Classical Chinese would say: there are no stalks. The sections are the only reality. The "stalk" is just what the sections look like when you squint at one point.

### What the Framework Can't Do Yet

Our framework is VERTEX-CENTRIC. Constraints live on vertices (or edges between vertices). The topology is a graph: vertices + edges. You can't have an edge without vertices. The vertices are the primary objects; edges are relations between them.

Classical Chinese inverts this. What if edges are primary and vertices are DERIVED? A vertex is just the limit point where multiple edges converge — it has no independent existence. This isn't just a philosophical move; it's a different algebraic structure.

Specifically: our framework can't represent a constraint that has no vertex. Every constraint must be "on" something. But if constraints are the primary objects, then:

- A constraint can exist WITHOUT knowing what it constrains
- The "things constrained" emerge FROM the intersection of constraints
- Removing all vertices and keeping only the constraint topology is a valid (and potentially more efficient) representation

### Concrete Extension: Edge-Primary Topology

Introduce an **edge-primary representation** alongside the vertex-primary one:

```
-- Vertex-primary (current):
type Topology = { vertices: Set<Vertex>, edges: Set<Edge> }
type Edge = { source: Vertex, target: Vertex, constraint: Constraint }

-- Edge-primary (new):
type ConstraintWeb = { constraints: Set<Constraint>, junctions: Set<Junction> }
type Junction = { constraints: Set<Constraint>, coherence: Float }
```

A `Junction` is where constraints meet and must cohere. It's not a "vertex" — it's a consistency requirement. The "vertices" of the old representation are just junctions where enough constraints accumulate to look like a point.

Operations on this representation:
- **Merge:** Two constraints that always fire together → merge into one (no junction needed)
- **Split:** A constraint that sometimes coheres and sometimes doesn't → split into junction
- **Drift:** Incoherence at a junction → the junction is "dissolving" (vertex is becoming ill-defined)

This is genuinely different from hypergraph representations. In a hypergraph, edges connect multiple vertices. In edge-primary, there are NO vertices. The "vertices" are emergent.

### Deepest Insight

English grammar forces a substance-process distinction: things exist, then things relate. "The cat is on the mat" presupposes a cat and a mat that exist independently of their spatial relation. Classical Chinese grammar doesn't force this. The relation can be the whole reality. Our framework inherited the English assumption: vertices first, constraints second. But in many systems (fluid dynamics, social networks, quantum fields), the constraints ARE the system and the "things" are just convenient fictions. An edge-primary representation would be more natural for these systems and might enable constraint propagation algorithms that don't need to "find" the thing they're constraining — because the constraint IS the thing.

---

## 4. Finnish/Uralic: Constraint Cases

### The Linguistic Structure

Finnish has 15 grammatical cases. Where English uses prepositions ("in the house," "to the house," "without the house"), Finnish uses case suffixes on the noun: *talo* (house) → *talossa* (in the house, inessive), *taloon* (into the house, illative), *talotta* (without the house, abessive). Each case isn't just a location — it's a RELATIONSHIP ROLE. The same root plays different roles depending on its case marker.

This is already close to our snap concept — the value "snaps" to a specific role via the case. But Finnish goes further: the case system is PRODUCTIVE. You can apply cases to verbs, adjectives, even entire clauses. And some cases are SEMANTICALLY RICH in ways that don't map to any preposition:

- **Essive** (-na): "as a house" (the house in its capacity as a house)
- **Translative** (-ksi): "into a house" (becoming a house, change of state)
- **Abessive** (-tta): "without a house" (absence)
- **Comitative** (-ne): "with its house(s)" (accompaniment)

### What the Framework Can't Do Yet

A constraint value in our framework is just a value. It doesn't have a ROLE. If vertex v has position x, that's just a number. But Finnish would ask: is x in the **inessive** (x as container), the **elative** (x as source), the **illative** (x as destination), the **adessive** (x as surface), the **ablative** (x as origin)?

Currently, the "role" of a value is determined entirely by its POSITION in the constraint equation. If the constraint says `v.x - u.x = d`, then `v.x` is playing the "target" role and `u.x` is playing the "source" role. But this role assignment is FRAGILE — it depends on the equation syntax, not the value's intrinsic role. Two mathematically equivalent formulations of the same constraint might assign roles differently.

### Concrete Extension: Case-Marked Constraint Values

Introduce **case markers** on constraint values:

```
data Case = 
  | Inessive    -- value-as-container (bounding)
  | Elative     -- value-as-source (from here)
  | Illative    -- value-as-destination (toward here)
  | Adessive    -- value-as-surface (on here)
  | Ablative    -- value-as-origin (away from here)
  | Translative -- value-as-becoming (changing to here)
  | Essive      -- value-as-role (in the capacity of)
  | Abessive    -- value-as-absence (without)
  | Comitative  -- value-as-accompaniment (together with)
```

A constraint doesn't just say "v.x and u.x must differ by d." It says:
- "v.x-[ILLATIVE] minus u.x-[ELATIVE] equals d-[ESSIVE]"

The case markers make the semantic roles EXPLICIT and INDEPENDENT of equation syntax. This means:
1. **Invariant reformulation:** Any equivalent equation has the same case markers
2. **Diagnostic case-mismatches:** If v.x is marked ILLATIVE but the constraint treats it as ELATIVE, something is wrong
3. **Case-based propagation:** An ILLATIVE value propagates differently from an ELATIVE value (one pushes toward, the other pulls from)
4. **Translative monitoring:** Values marked TRANSLATIVE are explicitly "becoming" — track their rate of change as primary, not their current value

### Deepest Insight

English prepositions are SPATIAL metaphors. "In," "to," "from," "with" — all originally spatial, extended metaphorically to other domains. Finnish cases aren't spatial metaphors. They're RELATIONAL PRIMITIVES that apply uniformly across all domains. The essive case doesn't mean "as if in a location" — it means "in the capacity of," which is an abstract role that applies equally to physical position, logical classification, and social function. By giving constraint values case markers, we get RELATIONAL SEMANTICS for free — the same constraint system can describe physical position, logical classification, and social function without changing its representation, because the cases are domain-independent. This is a unification that English prepositions can never achieve.

---

## 5. Arabic: Generative Roots and Constraint Fields

### The Linguistic Structure

Arabic morphology is built on **roots and patterns** (wazn). A root is typically three consonants (a triliteral) encoding a SEMANTIC FIELD. The root K-T-B encodes the field of writing. Patterns — specific arrangements of vowels and additional consonants — generate instances from the root:

- **KaTaB** = he wrote (perfective verb)
- **yu-KaTiB** = he corresponds with (iterative/reflexive verb)
- **maKTaB** = office/place of writing (noun of place)
- **KaaTiB** = writer/secretary (active participle)
- **maKTūB** = written/letter (passive participle)
- **KiTāB** = book (product of writing)
- **ta-KāTuB** = mutual correspondence (reflexive verb)

Same root, different patterns, a GENERATIVE FAMILY. The root constrains the semantic field; the pattern generates instances within that field.

### What the Framework Can't Do Yet

Our constraints are SPECIFIC. "Vertex v must be distance d from vertex u." Each constraint is hand-crafted. There's no concept of a CONSTRAINT FAMILY — a semantic field from which specific constraints are generated by pattern application. If I have distance constraints between 20 pairs of vertices, I have 20 independent constraints. The fact that they're all "distance constraints" is metadata, not structure.

Arabic would say: there's a ROOT (D-ST, the semantic field of "distance") and each specific constraint is a PATTERN applied to that root. The pattern determines:
- The ACTIVE form: "v must be distance d from u" (active: v enforces)
- The PASSIVE form: "v is kept at distance d by u" (passive: u enforces)
- The REFLEXIVE form: "v and u mutually maintain distance d" (reflexive: bidirectional)
- The INTENSIVE form: "v must STRICTLY maintain distance d" (intensive: hard constraint)
- The CAUSATIVE form: "v causes w to be at distance d from u" (causative: transitive constraint)

### Concrete Extension: Root-Pattern Constraint Morphology

```
type Root = String  -- semantic field identifier (e.g., "distance", "angle", "collinear")
type Pattern = VerbForm | NounOfPlace | ActiveParticiple | PassiveParticiple | Reflexive | Causative | Intensive

deriveConstraint :: Root -> Pattern -> [Vertex] -> Constraint
```

The `deriveConstraint` function generates specific constraints from roots + patterns:

- `deriveConstraint "distance" Reflexive [v, u]` → bidirectional distance constraint between v and u
- `deriveConstraint "distance" Causative [v, w, u]` → v causes w-u distance to be maintained
- `deriveConstraint "distance" Intensive [v, u]` → hard distance constraint (zero tolerance)
- `deriveConstraint "distance" PassiveParticiple [v, u]` → u enforces distance on v (one-directional)

The ROOT constrains the TYPE of relationship. The PATTERN generates the SPECIFIC constraint. This is generative in the same way Arabic morphology is generative: from a small number of roots and patterns, an enormous vocabulary of specific constraints emerges.

### Deepest Insight

English etymology is ACCUMULATIVE — words are borrowed, derived, and compounded, but each word is ultimately an individual item. Arabic morphology is **GENERATIVE** — the root is an ABSTRACT SEMANTIC FIELD and words are CONCRETE INSTANCES generated by rule. Our constraint framework is accumulative: each constraint is individually specified. An Arabic-inspired framework would be generative: the constraint types are roots, the enforcement patterns are patterns, and the specific constraints are generated by rule. This doesn't just save typing — it ENFORCES COHERENCE. In Arabic, you can't use a K-T-B derived word to mean something unrelated to writing. In a generative constraint system, you can't have a "distance" constraint that behaves inconsistently with other "distance" constraints, because they all derive from the same root by the same rules.

---

## 6. Japanese: Built-In Temporal Snap

### The Linguistic Structure

Japanese has two topic/subject markers: は (wa) and が (ga). The distinction is:

- **Ga (が):** Marks NEW, UNKNOWN, SURPRISING information. The **exhaustive listing** particle. "X ga Y" means "X (and specifically X, not something else) is Y." It signals: Δ ≠ 0. The listener didn't expect this. Attention required.
- **Wa (は):** Marks GIVEN, KNOWN, EXPECTED information. The **topic** particle. "X wa Y" means "as for X (which we already know about), Y." It signals: Δ ≈ 0. The listener already expected this. No surprise.

This is not a subtle pragmatic distinction. It is GRAMMATICALLY ENFORCED. Using wa where ga is appropriate (or vice versa) produces sentences that are syntactically correct but SEMANTICALLY WRONG in the same way that a snap to a value outside the deadband is "wrong" — not impossible, but requiring justification.

Example: 「雨が降っている」(Ame ga futte iru) = "It's raining" (NEW INFORMATION — look outside, it's raining!). 「雨は降っている」(Ame wa futte iru) = "As for the rain (which we've been discussing), it's falling" (EXPECTED — we knew it would rain, and indeed it is).

### What the Framework Can't Do Yet

The temporal snap in our framework is NUMERICAL: if |Δ| < deadband, snap to predicted value. If |Δ| ≥ deadband, accept observed value. This is a threshold on a scalar. Japanese grammar has the snap BUILT INTO THE INFORMATION STRUCTURE at a fundamental level:

- Ga marks the OBSERVED value (it exceeded the deadband — it's news)
- Wa marks the PREDICTED value (it's within the deadband — it's expected)

But Japanese goes further than our binary snap. The wa/ga distinction isn't just a threshold — it's a **contextual negotiation** between speaker and listener about the STATE OF THEIR SHARED KNOWLEDGE. This is a MULTI-AGENT snap: not just "does this value surprise ME?" but "does this value surprise US, given what we've established together?"

### Concrete Extension: Information-Structural Snap

Augment the snap mechanism with an **information-structural layer**:

```
data InformationStatus = 
  | Ga  -- NEW: observation diverged from prediction, Δ > deadband, SURPRISE
  | Wa  -- GIVEN: observation matches prediction, Δ ≤ deadband, EXPECTED
  | ContextualGa  -- NEW to this agent but KNOWN to others (asymmetric surprise)
  | ContrastiveWa  -- EXPECTED but being explicitly re-asserted (override signal)
```

The snap decision now considers not just the scalar Δ but the INFORMATION STATUS:
- A **Ga** observation gets full weight in the snap (it's news — pay attention)
- A **Wa** observation gets minimal weight (it's expected — just confirm)
- A **ContextualGa** observation triggers a knowledge-sharing protocol (someone else knew this, I didn't — sync)
- A **ContrastiveWa** observation overrides even if Δ is small (the system is explicitly re-asserting something it was uncertain about — trust it)

This also solves the multi-agent coordination problem: each agent tracks not just its own wa/ga but the COLLECTIVE wa/ga. "Is this new to anyone?" becomes the snap criterion, not "is this new to me?"

### Deepest Insight

English has no grammaticalized information structure. Everything is either "new" or "given" based on context and pragmatics — it's all in how you phrase it, not in the grammar. This means English speakers have to CONSTRUCT the temporal snap deliberately; it doesn't come for free. Japanese speakers get it for free — the grammar FORCES them to classify every piece of information as wa or ga before they can speak. By building information-structural snap into the framework, we get multi-agent coordination for free in the same way: the system can't process a value without classifying its information status, and that classification drives propagation automatically.

---

## Verdict: The Biggest Upgrade

**Japanese wa/ga → Information-Structural Snap.**

Here's why:

The other five insights are powerful but ADDITIVE. Constraint aspect (Navajo) adds a temporal dimension. Tetra-knowledge diagnosis (Greek) adds an epistemic layer. Edge-primary topology (Chinese) offers an alternative representation. Case marking (Finnish) adds semantic roles. Generative morphology (Arabic) adds a construction system. Each is valuable but doesn't change the CORE OPERATION.

The wa/ga insight changes the core operation itself. The snap is the heart of the constraint engine — it's where observation meets prediction, where the rubber meets the road. Making the snap information-structural rather than purely numerical transforms it from a local threshold test into a **contextual knowledge negotiation**. This single change:

1. **Solves multi-agent coordination** (whose snap takes priority? → the ga snap, always)
2. **Enables adaptive deadband** (wa constraints can tighten deadband; ga constraints should widen it — you need more evidence for surprising data)
3. **Provides natural drift detection** (too many ga observations = model is drifting; too many wa = model is stable but under-observed)
4. **Subsumes temporal reasoning** (wa = prediction from t-1, ga = observation at t — the temporal snap is a special case of the information-structural snap)
5. **Is implementable immediately** — no new algebraic structures, no new representations, just an enriched comparison operator

The temporal snap is already there. The wa/ga insight doesn't add a new layer — it UPGRADES the existing one. That's why it wins.

---

*Reverse actualization complete. Languages are constraint systems that evolved over millennia. We'd be fools not to learn from them.*

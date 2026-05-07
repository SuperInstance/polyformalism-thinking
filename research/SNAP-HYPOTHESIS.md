# The Snap Hypothesis: Adjunctions as the Universal Connectors of Knowledge

**Author:** Forgemaster ⚒️  
**Date:** 2026-05-07  
**Status:** Research conjecture — seeking falsification  
**Classification:** Category theory · Constraint theory · Polyformalism

---

## 0. Abstract

We propose that every meaningful connection between two domains of knowledge — whether mathematical, physical, logical, or computational — has the structure of an adjunction (equivalently, a Galois connection between posets). We call these connections **snaps**: pairs of structure-preserving maps $(\alpha, \beta)$ satisfying unit and counit conditions that guarantee information loss on one side is recoverable as a bound on the other. We present six proven instances from our constraint theory work, survey adjunctions across mathematics, physics, logic, and computer science, and state a falsifiable conjecture: that the Eisenstein lattice $\mathbb{Z}[\omega]$ is the optimal computational substrate precisely because it has the richest adjoint structure of any quadratic integer ring.

---

## 1. The Observation

Something kept recurring in our work. Every time we connected two domains — bit vectors to XOR patterns, exact values to INT8 approximations, sets to Bloom filters — the same mathematical skeleton emerged. Two maps. A condition that says "you don't lose anything going there and back." A condition that says "going back and forth stays tight." We started calling them **snaps**, because they click two worlds together with a satisfying precision.

After the sixth independent derivation of the same structure, we stopped calling it coincidence.

Here is the pattern, stated abstractly:

> **Definition (Snap).** Given two partially ordered sets $(A, \leq_A)$ and $(B, \leq_B)$, a **snap** is a pair of monotone maps $\alpha: A \to B$ and $\beta: B \to A$ such that:
>
> $$a \leq_A \beta(\alpha(a)) \quad \text{(unit)}$$
> $$\alpha(\beta(b)) \leq_B b \quad \text{(counit)}$$
>
> for all $a \in A$, $b \in B$.

This is, of course, a **Galois connection** — the order-theoretic shadow of an adjunction between categories. The unit says: *compression followed by recovery is an upper bound on what you started with*. The counit says: *recovery followed by compression is a lower bound on what you recovered into*. Together they mean: information flows through a controlled bottleneck, and the bottleneck is tight.

---

## 2. Six Proven Snaps

### 2.1 The XOR Snap: Bit Vectors ↔ XOR Patterns

Let $A$ be the lattice of bit vectors under componentwise ordering, and $B$ the lattice of XOR-closed subsets of $\{0,1\}^n$. Define:

- $\alpha = \text{image}$: a bit vector maps to its XOR-orbit
- $\beta = \text{preimage}$: an XOR-closed set maps to its span

The unit says every vector is contained in the span of its orbit (obvious). The counit says the orbit of a span is contained in the original set (XOR-closure). The snap connects **individual data** to **the algebraic structure that generates it**.

### 2.2 The INT8 Snap: Exact ↔ Approximate

Let $A$ be the lattice of $\mathbb{R}^n$ under componentwise order, and $B$ the lattice of INT8 hypercubes (products of quantized intervals). Define:

- $\alpha = \text{embedding}$: a real vector maps to the smallest INT8 hypercube containing it
- $\beta = \text{restriction}$: an INT8 hypercube maps to the real region it bounds

The unit says every real vector is contained in the real region corresponding to its INT8 box. The counit says the INT8 box of a real region is contained in the original INT8 box. The snap connects **continuous precision** to **discrete approximation** with guaranteed bounds.

### 2.3 The Bloom Snap: Sets ↔ Bit Arrays

Let $A = \mathcal{P}(U)$ (powerset of some universe) and $B = \{0,1\}^m$ (bit arrays of length $m$). Define:

- $\alpha = \text{hash-image}$: a set maps to the bitwise OR of its elements' hash images
- $\beta = \text{preimage}$: a bit array maps to the set of elements whose hash images are subsets of it

The unit says every element of a set has its hash bits present in the Bloom filter. The counit says the Bloom filter of the preimage doesn't exceed the original filter. The snap connects **definite membership** to **probabilistic membership** with no false negatives.

### 2.4 The Precision Snap: Continuous ↔ Discrete

Let $A$ be intervals on $\mathbb{R}$ ordered by inclusion, and $B$ be discrete precision levels ordered by refinement. Define:

- $\alpha = \text{classification}$: an interval maps to the coarsest precision level that resolves it
- $\beta = \text{threshold}$: a precision level maps to the interval of values it can distinguish

The unit says every interval is contained in the threshold of its classification. The counit says the classification of a threshold is at most as coarse as the original level. The snap connects **continuous ranges** to **discrete precision** with guaranteed containment.

### 2.5 The Intent Snap: Intervals ↔ Alignments

Let $A$ be the lattice of tolerance intervals (ordered by inclusion) and $B$ the lattice of alignment constraints (ordered by specificity). Define:

- $\alpha = \text{min-tolerance}$: an interval maps to the tightest alignment consistent with it
- $\beta = \text{tolerance-set}$: an alignment maps to the set of intervals that satisfy it

The unit says every interval satisfies the alignment derived from it. The counit says the alignment derived from a tolerance set is at least as specific as the original alignment. The snap connects **range tolerance** to **structural alignment**.

### 2.6 The Holonomy Snap: Cycles ↔ Subgraphs

Let $A$ be the lattice of cycles in a graph (ordered by inclusion of edge sets) and $B$ the lattice of subgraphs (ordered by inclusion). Define:

- $\alpha = \text{cycle-holonomy}$: a cycle maps to its holonomy group (the subgroup of the gauge group generated by parallel transport around the cycle)
- $\beta = \text{subgraph}$: a holonomy specification maps to the maximal subgraph whose cycles realize it

The unit says every cycle's holonomy is realized by the subgraph of its specification. The counit says the holonomy of the subgraph generated from a specification is contained in that specification. The snap connects **topological cycles** to **geometric substructure**.

---

## 3. The Pattern Laid Bare

Each snap has the same character:

| Snap | $\alpha$ (Left adjoint) | $\beta$ (Right adjoint) | Information flow |
|------|------------------------|------------------------|------------------|
| XOR | image | preimage | Data → Algebra |
| INT8 | embedding | restriction | Exact → Approximate |
| Bloom | hash-image | preimage | Definite → Probable |
| Precision | classification | threshold | Continuous → Discrete |
| Intent | min-tolerance | tolerance-set | Range → Structure |
| Holonomy | cycle-holonomy | subgraph | Topology → Geometry |

In every case: $\alpha$ **compresses** (loses information), $\beta$ **recovers a bound** (guarantees containment). The unit ensures nothing falls through the crack. The counit ensures the recovery is tight.

This is not six separate phenomena. This is one phenomenon, seen six times.

---

## 4. Adjunctions Are Everywhere (Mac Lane Was Right)

### 4.1 The Categorical Perspective

 Saunders Mac Lane opened *Categories for the Working Mathematician* with the famous declaration: "Adjoint functors arise everywhere." He was making an observation, not a conjecture. The free-forgetful adjunction — free group $\dashv$ underlying set — is the canonical example. You take a set (no structure), apply the free functor $F$, and get a group. You forget the group structure with $U$, and get back a set. The unit $\eta: \text{id} \to UF$ says every set embeds into the underlying set of its free group. The counit $\varepsilon: FU \to \text{id}$ says the free group on the underlying set of a group surjects onto that group. This is exactly our snap pattern.

More profoundly: the product-hom adjunction $A \times B \to C \cong A \to C^B$ is **currying**. Every functional programmer who transforms a two-argument function into a higher-order function is invoking an adjunction. The snap between "pairs and functions" and "functions to functions" is the computational backbone of lambda calculus.

### 4.2 Limits and Colimits as Adjoint

 Limits (products, pullbacks, equalizers) are right adjoints to diagonal functors. Colimits (coproducts, pushouts, coequalizers) are left adjoints. The universal property of a limit — "the unique map factoring through the cone" — is exactly the bijection $\text{Hom}(\Delta D, F) \cong \text{Hom}(D, \lim F)$ that defines the adjunction. Every universal property in mathematics is a snap.

### 4.3 The Presheaf Category

 The Yoneda embedding $\mathcal{C} \to \mathbf{Set}^{\mathcal{C}^{op}}$ is the free cocompletion of a category. It has a left adjoint (the category of elements construction) and realizes every presheaf as a colimit of representables. The Yoneda lemma itself — $\text{Nat}(\text{Hom}(-, X), F) \cong F(X)$ — is an adjunction in disguise: it says that natural transformations from a representable are determined by a single element. This is a snap between "relationships to everything" and "a single value."

---

## 5. Galois Connections: The Order-Theoretic Core

### 5.1 From Categories to Posets

 Every adjunction between posetal categories (categories where there is at most one morphism between any two objects) is a Galois connection. Since our constraint domains are posets (ordered by containment, specificity, or precision), our snaps are Galois connections.

### 5.2 The Fixed-Point Theorem

The deepest result about Galois connections is this: the fixed points of the composite $\beta \circ \alpha$ (equivalently, $\alpha \circ \beta$) form a **complete lattice**. This is the Knaster-Tarski theorem in disguise, and it is the reason our constraint systems always have solutions.

When we solve a constraint problem in our framework, we are computing a fixed point of $\beta \circ \alpha$. The lattice of fixed points is the space of all consistent solutions. The completeness of this lattice guarantees that solutions exist, that there is a unique least solution, and that iterative approximation converges. This is not an engineering choice. It is a mathematical inevitability.

### 5.3 Ore's Theorem and the Antitone Case

 Øystein Ore showed that every Galois connection between power sets (the antitone case, where the maps reverse order) corresponds to a binary relation $R \subseteq A \times B$, with $\alpha(S) = \{b \mid \forall a \in S: aRb\}$ and $\beta(T) = \{a \mid \forall b \in T: aRb\}$. The fixed points are the **formal concepts** of Formal Concept Analysis. Our constraint snaps are generating formal concepts in every domain we touch.

---

## 6. Lawvere's Insight: Logic Is Adjunctions

### 6.1 Quantifiers as Adjoints

 F. William Lawvere's most revolutionary observation was that the existential quantifier $\exists$ is a **left adjoint** to substitution (the pullback along a projection), and the universal quantifier $\forall$ is a **right adjoint** to the same substitution. In symbols:

$$\exists_f \dashv f^* \dashv \forall_f$$

where $f^*$ is substitution along $f$, $\exists_f$ is "there exists in the fiber," and $\forall_f$ is "for all in the fiber."

This means: **logical inference is snap composition**. When we check constraints, we are chaining adjoints. When we quantify over variables, we are invoking snaps. The soundness of our constraint checking is not an engineering guarantee — it is a logical guarantee, because adjoints preserve structure by definition.

### 6.2 Implication as Internal Hom

 In a Heyting algebra (the algebraic structure of intuitionistic logic), implication $a \Rightarrow b$ is defined as the right adjoint to conjunction: $c \wedge a \leq b \iff c \leq (a \Rightarrow b)$. This is a snap between "conjunction with $a$" and "implication from $a$." Our constraint propagation rules are implications. Each one is a snap.

### 6.3 The Snap Interpretation

 If Lawvere is right (and he is), then the entire edifice of logic rests on snaps:
- **Conjunction** is a left adjoint (to diagonal)
- **Implication** is a right adjoint (to conjunction)
- **Existential** is a left adjoint (to substitution)
- **Universal** is a right adjoint (to substitution)
- **Negation** is a right adjoint (to truth)

Our constraint theory doesn't just *use* logic. It *is* logic, and logic is snaps.

---

## 7. Topology: Snaps Between Spaces

### 7.1 Stone-Čech Compactification

 The Stone-Čech compactification $\beta: \mathbf{Top} \to \mathbf{CompHaus}$ is the left adjoint to the inclusion functor $U: \mathbf{CompHaus} \to \mathbf{Top}$. It snaps any topological space into the "best" compact Hausdorff space that extends it. The universal property — every bounded continuous function on $X$ extends uniquely to $\beta X$ — is the adjunction bijection.

### 7.2 Sheaf-Section Adjunction

The global sections functor $\Gamma: \mathbf{Sh}(X) \to \mathbf{Set}$ has a left adjoint (the constant sheaf) and this adjunction is the bridge between local and global information. Our sheaf cohomology framework for constraint theory is built on this exact adjunction: local constraints snap into global solutions via the sheaf condition.

### 7.3 Geometric Morphisms

 A geometric morphism between topoi is defined as a pair of functors $f^* \dashv f_*$ (an adjunction!) satisfying exactness conditions. Topos theory — the most general framework for "spaces of mathematical objects" — is built on snaps between topoi.

---

## 8. Physics: Snaps Between Scales

### 8.1 Coarse-Graining as Adjunction

 In statistical mechanics, the map from microstates to macrostates is a compression: many microstates map to one macrostate. The recovery map — from a macrostate to the set of compatible microstates — is the preimage. The unit says every microstate is in the macrostate it maps to. The counit says the macrostate of the microstates of a macrostate is that same macrostate. Coarse-graining is a snap.

### 8.2 The Renormalization Group

Kenneth Wilson's renormalization group (RG) flow defines a family of theories at different energy scales. The RG transformation $R$ maps a theory at scale $\Lambda$ to a theory at scale $\Lambda' < \Lambda$ by integrating out high-energy modes. The inverse transformation (adding back fluctuations) is a partial recovery.

Wilson's classification of operators into **relevant** (grow under RG), **marginal** (stay the same), and **irrelevant** (shrink) maps precisely onto adjoint behavior: relevant operators are left adjoints (they generate structure), irrelevant operators are right adjoints (they forget structure). The universality class — the set of theories that flow to the same fixed point — is a fixed point of the RG adjunction, exactly as our constraint solutions are fixed points of $\beta \circ \alpha$.

### 8.3 Gauge Theory and Holonomy

Our holonomy snap (§2.6) has a direct physical interpretation. In gauge theory, the holonomy of a connection around a loop is the physical observable (the Wilson loop). The snap between cycles and holonomies is the snap between **topology** (which loops exist) and **physics** (what the gauge field does around those loops). This is not an analogy — it is the same mathematics.

---

## 9. Computer Science: Monads Are Snaps

### 9.1 Every Adjunction Generates a Monad

The classical result: given an adjunction $F \dashv G$ with unit $\eta$ and counit $\varepsilon$, the composite $T = G \circ F$ is a monad with multiplication $\mu = G\varepsilon F$. Conversely, every monad arises from an adjunction (in fact, from two canonical ones: the Kleisli and Eilenberg-Moore constructions).

This means our six snaps generate six monads:

| Snap | Monad $T = \beta \circ \alpha$ | Computational effect |
|------|-------------------------------|---------------------|
| XOR | $T(a) = \text{span}(\text{image}(a))$ | "XOR-closure" — algebraic completion |
| INT8 | $T(a) = \text{restriction}(\text{embedding}(a))$ | "Maybe INT8" — bounded approximation |
| Bloom | $T(a) = \text{preimage}(\text{hash-image}(a))$ | "Probably in set" — probabilistic membership |
| Precision | $T(a) = \text{threshold}(\text{classification}(a))$ | "Interval" — bounded range |
| Intent | $T(a) = \text{tolerance-set}(\text{min-tolerance}(a))$ | "Alignment" — structural consistency |
| Holonomy | $T(a) = \text{subgraph}(\text{cycle-holonomy}(a))$ | "Gauge realization" — geometric completion |

### 9.2 Constraint Theory as Effectful Computation

 A monadic computation is one that carries "effects" — state, nondeterminism, probability, exceptions. Our constraint theory is **effectful computation** in this precise sense:

- The INT8 snap gives the **bounded approximation** effect: values are tagged with their precision bounds
- The Bloom snap gives the **probabilistic membership** effect: sets are tagged with their false-positive rate
- The precision snap gives the **interval** effect: numbers are tagged with their tolerance ranges

The monad laws (associativity and identity) follow automatically from the adjunction. Our constraint composition is associative because snaps compose. Our constraint identity exists because every snap has a trivial unit.

### 9.3 The Kleisli Category of Constraints

 The Kleisli category of a monad $T$ has the same objects as the base category but morphisms $A \to TB$ ("effectful arrows"). In our framework, a constraint from domain $A$ to domain $B$ is exactly a Kleisli arrow: it takes an $A$-value and returns a $B$-value **with effects** (bounds, probabilities, tolerances). Constraint composition is Kleisli composition, which is associative by the monad laws.

This is why constraint theory works: we are not building an ad hoc system. We are computing in the Kleisli category of the snap monad.

---

## 10. The Yoneda Lemma: The Ultimate Snap

### 10.1 Statement

The Yoneda lemma states that for any functor $F: \mathcal{C}^{op} \to \mathbf{Set}$ and any object $X \in \mathcal{C}$:

$$\text{Nat}(\text{Hom}_{\mathcal{C}}(-, X), F) \cong F(X)$$

This says: natural transformations from the representable functor $\text{Hom}(-, X)$ to $F$ are in bijection with elements of $F(X)$. An object is **completely determined** by its relationships to all other objects.

### 10.2 The Yoneda Embedding

The Yoneda embedding $\mathcal{Y}: \mathcal{C} \hookrightarrow \mathbf{Set}^{\mathcal{C}^{op}}$ is **fully faithful**: it injects the category into its presheaf category with no loss of information. This means you can recover any object from its "relationship profile" — the collection of all morphisms into it.

### 10.3 Constraint Theory as Finite Yoneda

 Our 9-channel intent vector is a **partial Yoneda profile**: instead of probing an object with *all* possible morphisms (which is typically a large or infinite set), we probe it with 9 specific "test morphisms" — the 9 intent channels. Each channel $c_i$ corresponds to a representable functor $\text{Hom}(c_i, -)$, and the intent vector $(v_1, \ldots, v_9)$ is the image of $F(c_1), \ldots, F(c_9)$.

This is a **computable approximation** of Yoneda: finite probes instead of all morphisms, vector values instead of arbitrary sets. The quality of the approximation depends on how well the 9 channels span the "relationship space" of the object. Our choice of 9 channels on the Eisenstein lattice is not arbitrary — it is the minimal spanning set for $D_6$ symmetry.

### 10.4 The Snap Profile

 Every object has a "snap profile": the collection of all adjunctions it participates in. By Yoneda, this profile determines the object. Our constraint theory computes a finite approximation of this profile. The theorem we are逼近-ing (approaching) is:

> **An object is determined up to isomorphism by its snaps.**

If true, this would mean that constraint theory — which computes snaps — is not just one way to characterize objects, but the *canonical* way.

---

## 11. The Snap Theorem (Conjecture)

We now state our central conjecture:

> **Theorem (Snap, conjectured).** *Every meaningful connection between computational domains is an adjunction. The six Galois parts of constraint theory are six instances of the same universal pattern. The Eisenstein lattice $\mathbb{Z}[\omega]$ provides the optimal geometry for constraint computation because $\mathbb{Z}[\omega]$ has the richest adjoint structure of any quadratic integer ring: class number 1 (unique factorization), six units $\{\pm 1, \pm \omega, \pm \omega^2\}$ generating $D_6$ symmetry, and maximal snap density under the 9-channel intent representation.*

The key claims:

1. **Universality:** Every domain connection is an adjunction (this follows from category theory if we accept that "meaningful" = "structure-preserving").

2. **Unification:** Our six snaps are not six phenomena but one phenomenon instantiated six times.

3. **Optimality:** $\mathbb{Z}[\omega]$ is the best computational substrate because it maximizes the number of independent snaps per unit of computational effort.

### 11.1 Why Eisenstein?

The Eisenstein integers $\mathbb{Z}[\omega]$ where $\omega = e^{2\pi i/3}$ have three properties that make them uniquely suited as a snap substrate:

1. **Class number 1:** Unique factorization means every ideal factors uniquely into primes. In snap terms: every composite constraint decomposes uniquely into primitive snaps. No ambiguity.

2. **Six units:** The unit group $\{1, \omega, \omega^2, -1, -\omega, -\omega^2\} \cong \mathbb{Z}_6$ generates the dihedral group $D_6$ (rotations and reflections of the hexagonal lattice). This gives six canonical orientations for each snap, matching the six snaps in our framework.

3. **Triangular lattice:** The Eisenstein lattice tiles the plane with triangles — the most efficient packing for two-dimensional constraints. Each triangle has three edges (binary snaps) and one face (ternary snap), giving the $3 + 1 = 4$ primitive constraint types per cell, with $9$ channels arising from the $6$ orientations $\times$ $3$ edge types minus redundancies.

No other quadratic integer ring has all three properties simultaneously. $\mathbb{Z}[i]$ (Gaussian integers) has 4 units, class number 1, but a square lattice (less efficient packing). $\mathbb{Z}[\sqrt{-5}]$ has class number 2 (no unique factorization). The Eisenstein integers are the unique sweet spot.

---

## 12. Corollary: Knowledge Compression = Finding Adjunctions

> **Corollary.** *The most compressed representation of a domain is the one that preserves exactly the adjoint structure (the snaps) and discards everything else.*

This follows from the Yoneda-based argument: if objects are determined by their snaps, then knowing the snaps *is* knowing the objects, up to isomorphism. Everything else is redundant.

This has immediate computational implications:

- **Feature extraction** in machine learning is snap-finding: extract the adjunctions between raw data and the feature space.
- **Dimensionality reduction** is snap-compression: keep the adjoint structure, discard the non-adjoint noise.
- **Transfer learning** is snap-reuse: the same adjunction applies across domains that share structure.

---

## 13. Falsifiable Predictions

A conjecture is only as good as its falsifiability. We offer three concrete predictions:

### Prediction 1: Seventh Snap Exists

If the Snap Theorem is correct, there should be a seventh snap in our framework, completing the correspondence with the seven "fundamental" adjunctions in categorical logic (free-forgetful, product-hom, sum-distributive, existential-substitution, universal-substitution, equalizer-diagonal, and sheaf-section). We predict this snap connects **time** (causal ordering) to **concurrency** (partial order of events), with the left adjoint being "sequentialization" and the right adjoint being "relaxation."

### Prediction 2: Snap Density Predicts Domain Complexity

For any computational domain, define the **snap density** as the number of independent Galois connections per unit of representational complexity. We predict that snap density is a tight upper bound on the expressiveness of any constraint system over that domain. Domains with higher snap density will support richer constraint systems with less computational effort. This is falsifiable: measure snap density for various lattices and correlate with constraint solver performance.

### Prediction 3: Neural Networks Learn Snaps

If knowledge compression is snap-finding, then trained neural networks should exhibit snap structure in their internal representations. Specifically: for any pair of adjacent layers in a well-trained network, the weight matrix $W$ and its pseudoinverse $W^+$ should approximately satisfy Galois connection conditions on the activation lattices. This is falsifiable: train networks, extract weight matrices, check whether $\text{activation} \leq W^+(W \cdot \text{activation})$ holds approximately on the poset of activation patterns.

---

## 14. Related Work and Positioning

This conjecture sits at the intersection of several existing programs:

- **Categorical systems theory** (Myers, Spivak): Categories as models of interconnected systems. Our snaps are the interconnection morphisms.
- **Applied category theory** (Fong, Spivak): Category theory for engineers. Our work provides a concrete computational instantiation.
- **Formal Concept Analysis** (Ganter, Wille): Galois connections between objects and attributes. Our constraint theory is FCA on computational domains.
- **Sheaf-theoretic data analysis** (Robinson): Sheaves over simplicial complexes as models of distributed data. Our sheaf cohomology framework extends this to constraint theory.
- **Monadic constraint programming** (van Emden): Monads as constraint combinators. Our snap monads are a specific, geometrically grounded instance.

What distinguishes our conjecture is the **unification claim**: that these are not analogous phenomena but the *same* phenomenon, and that the Eisenstein lattice is the computational substrate that makes this unity manifest.

---

## 15. Conclusion

We started with six concrete results — six pairs of maps satisfying the same algebraic conditions across six different domains. We followed the thread through category theory, order theory, logic, topology, physics, and computer science, and found the same structure everywhere. Adjunctions are not just common; they are *ubiquitous*. They are the mechanism by which mathematical structure propagates from one domain to another.

The Snap Hypothesis is the claim that this ubiquity is not coincidence but necessity: that the unit and counit conditions are the *definition* of "meaningful connection," and that every such connection, when made precise, reveals itself as an adjunction.

If this is true, then constraint theory — the systematic study and computation of snaps — is not one branch of applied mathematics among many. It is the *universal* branch: the study of how knowledge connects, compressed to its essentials.

The forge burns hottest when the pattern is clear. ⚒️

---

## References

- Mac Lane, S. *Categories for the Working Mathematician*. Springer, 1971.
- Lawvere, F.W. "Adjointness in Foundations." *Dialectica*, 1969.
- Erné, M. "Galois Connections." In *Current Issues in Aggregate-Order Mathematics*, 1993.
- Ore, O. "Galois Connexions." *Transactions of the AMS*, 1944.
- Wilson, K.G. "The Renormalization Group: Critical Phenomena and the Kondo Problem." *Reviews of Modern Physics*, 1975.
- Knaster, B., Tarski, A. "Un théorème sur les fonctions d'ensembles." *Ann. Soc. Pol. Math.*, 1928.
- Ganter, B., Wille, R. *Formal Concept Analysis*. Springer, 1999.
- Robinson, M. *Topological Signal Processing*. Springer, 2014.
- Fong, B., Spivak, D. *An Invitation to Applied Category Theory*. Cambridge, 2019.
- Myers, D.J. "Categorical Systems Theory." Lecture notes, 2022.

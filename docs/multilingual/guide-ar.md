# Polyformalism × العربية: Islamic Geometric Patterns and the Algebra of Infinity

## مقدمة (Introduction)

> *كل شيء زائل إلا وجهه*  
> "All things perish except His Face."  
> — Quran 28:88

Polyformalism teaches that every formalism is a lens — it reveals some aspects of reality and conceals others. The conservation law, γ + η = C, states that what is expressed and what is hidden always sum to the same totality. This principle was understood and practiced for over a thousand years in the Islamic mathematical tradition, where the apparent complexity of geometric patterns emerges from profound simplicity, and where the infinite is expressed through the finite.

This guide connects polyformalism's mathematical framework to the rich tradition of Islamic mathematics, algebra, and geometric art — a civilization that preserved and advanced mathematics through Europe's darkest centuries, and whose insights into pattern, symmetry, and the architecture of meaning remain deeply relevant.

---

## I. التوحيد (Tawhid): Unity and the Conservation Law

### The Principle of Divine Unity as Mathematical Conservation

The foundational principle of Islamic thought is **التوحيد (tawhid)** — the oneness of God. But tawhid is not merely theological. In Islamic intellectual tradition, it is an organizing principle for all of reality: the many derive from the One, and all apparent multiplicity resolves into unity when properly understood.

The polyformalism conservation law:

```
γ + η = C
```

where:
- **γ (gamma)** = the manifest, the expressed, the visible pattern (الظاهر, al-ẓāhir)
- **η (eta)** = the hidden, the implicit, the inner meaning (الباطن, al-bāṭin)
- **C** = the totality, the unity (الوحدة, al-waḥda), which is always conserved

The conservation law is the mathematical echo of tawhid. When you express more (γ increases), you do not create new reality — you redistribute existing reality. What becomes visible was always there, merely hidden. What remains hidden is not absent — it is **الباطن (al-bāṭin)**, the inner dimension that the formalism does not surface.

The beautiful symmetry: الله has 99 names in Islamic tradition, divided into names of majesty (jalāl — γ, the manifest, the overwhelming) and names of beauty (jamāl — η, the subtle, the hidden). The totality is neither the majesty alone nor the beauty alone. It is the unity of both: tawhid.

```python
# Tawhid conservation: manifest + hidden = unity
# Key insight: you never add to C. You only redistribute.

class TawhidConservation:
    """
    توحيد (tawhid): the unity principle
    
    γ (al-ẓāhir, the manifest) + η (al-bāṭin, the hidden) = C (al-waḥda, unity)
    
    The names of beauty (jamāl) are η-rich.
    The names of majesty (jalāl) are γ-rich.
    True understanding is neither — it is the unity that contains both.
    """
    
    def __init__(self, concept: str, unity: float = 1.0):
        self.concept = concept
        self.C = unity             # الوحدة — never changes
        self.zahir = 0.0           # الظاهر — what is manifest
        self.batin = unity         # الباطن — what is hidden
    
    def reveal_through(self, formalism_name: str, revealing_power: float) -> dict:
        """
        A formalism reveals (makes ẓāhir) some aspects
        and simultaneously conceals (makes bāṭin) others.
        """
        self.zahir = revealing_power
        self.batin = self.C - self.zahir
        
        # Islamic aesthetic principle:
        # Perfect expression (γ = C) is impossible — there is always bāṭin
        # This is not a bug. It is the structure of reality.
        if self.batin < 0.01:
            quality = "تجلي (tajallī) — overwhelming manifestation. But even light creates shadow."
        elif self.zahir < 0.01:
            quality = "غيب (ghayb) — pure hiddenness. The unseen dominates."
        elif self.zahir > self.batin:
            quality = "جلال (jalāl) — majesty. The manifest dominates."
        elif self.batin > self.zahir:
            quality = "جمال (jamāl) — beauty. The subtle dominates."
        else:
            quality = "ميزان (mīzān) — balance. Walking the tightrope between the two."
        
        return {
            "concept": self.concept,
            "formalism": formalism_name,
            "zahir": round(self.zahir, 4),
            "batin": round(self.batin, 4),
            "unity_intact": abs((self.zahir + self.batin) - self.C) < 1e-10,
            "quality": quality,
        }


# Compare formalisms through the lens of tawhid
formalisms = [
    ("Assembly", 0.95),      # Almost everything manifest — jalāl
    ("C", 0.80),              # Much manifest, little bāṭin
    ("Rust", 0.75),           # Strong manifestation through ownership
    ("Python", 0.60),         # Balanced — some manifest, some hidden
    ("Haskell", 0.50),        # Pure functions reveal structure, hide execution
    ("Prolog", 0.30),         # Much hidden — you state what, not how
    ("Coq/Lean", 0.25),       # Deeply bāṭin — proofs hide computational content
]

print("Conservation through the lens of tawhid:")
print(f"{'Formalism':<12} {'ẓāhir (γ)':<12} {'bāṭin (η)':<12} Quality")
print("-" * 65)
for name, power in formalisms:
    tc = TawhidConservation("Byzantine Consensus")
    result = tc.reveal_through(name, power)
    print(f"{name:<12} {result['zahir']:<12.2f} {result['batin']:<12.2f} {result['quality']}")
```

---

## II. الهندسة الإسلامية (Islamic Geometry): The 9-Channel Intent Model

### Stars, Polygons, and the Architecture of Meaning

Islamic geometric art is one of humanity's great mathematical achievements. Walking into the Alhambra in Granada, the Dome of the Rock in Jerusalem, or the Shah Mosque in Isfahan, you are surrounded by patterns of staggering complexity — patterns constructed using only a compass and a straightedge, patterns that express infinity through the repetition of finite forms.

The fundamental structures of Islamic geometry are:

1. **الدائرة (al-dā'ira)** — the circle: unity, perfection, the source
2. **النجمة (al-najma)** — the star: radiance, the multiplication of unity
3. **الشبكة (al-shabaka)** — the grid/lattice: the order that underlies apparent complexity
4. **الوسط (al-wasṭ)** — the center: the still point around which everything turns

These map onto the polyformalism intent model with remarkable precision. The 9 channels are the "directions" in which the pattern extends. Each channel's value determines the weight, color, and emphasis of that direction — and the *combination* creates the overall pattern.

### The Girih Tiles: Five-Fold Symmetry

One of the most sophisticated achievements of Islamic mathematics is the **گره (girih)** tile system, used in Persian and Islamic architecture since the 13th century. Girih uses five tile shapes:

- **العشرة (decagon)** — 10-sided
- **النجم الخماسي (pentagram)** — 5-pointed star
- **المعين (rhombus)** — diamond
- **الشكل المثلث (bowtie)** — hexagonal concave
- **السداسي (hexagon)** — 6-sided

These five tiles can tile the plane **aperiodically** — they create patterns that never repeat exactly but maintain perfect local symmetry. This was proven mathematically only in 2007 by Lu and Steinhardt, confirming what Islamic artisans had practiced for 700 years.

The connection to polyformalism: the 9-channel intent model, like the girih system, creates patterns through the *combination* of simple elements. Each intent is a "tile." The fleet's collective intent is the "pattern." And just as girih patterns can be aperiodic (never repeating), fleet intent patterns can evolve and adapt without ever returning to the same configuration.

```rust
// Girih-inspired 9-channel intent model
// Key insight: 5 tile types, 9 channels — both create infinite patterns from finite rules

#[derive(Clone, Debug)]
struct GirihIntent {
    // 9 channels of intent — the "directions" of the pattern
    channels: [f64; 9],
    
    // The "tile type" of this intent — which geometric archetype it embodies
    tile_type: GirihTile,
}

#[derive(Clone, Debug)]
enum GirihTile {
    Decagon,    // عشرة — 10-fold symmetry, complete and balanced
    Pentagram,  // نجم — radiating, high energy
    Rhombus,    // معين — focused, directional
    Bowtie,     — bowtie — transitional, connecting
    Hexagon,    // سداسي — stable, grounding
}

impl GirihIntent {
    fn new(channels: [f64; 9], tile: GirihTile) -> Self {
        GirihIntent { channels, tile_type: tile }
    }
    
    /// Compute the "ornamental weight" — how much visual/intent density
    fn ornamental_weight(&self) -> f64 {
        let sum: f64 = self.channels.iter().sum();
        sum / 9.0  // Average across channels
    }
    
    /// Check if two intents tile together smoothly
    /// (Like girih tiles fitting edge-to-edge)
    fn tiles_with(&self, other: &Self, tolerance: f64) -> bool {
        // Two intents "tile" if their shared channels agree within tolerance
        for i in 0..9 {
            if (self.channels[i] - other.channels[i]).abs() > tolerance {
                return false;
            }
        }
        true
    }
    
    /// Generate the "pattern signature" — a unique identifier
    /// analogous to the visual signature of a girih arrangement
    fn pattern_signature(&self) -> u64 {
        // Hash the 9 channels into a compact signature
        let mut sig: u64 = 0;
        for (i, &c) in self.channels.iter().enumerate() {
            let bucket = (c * 255.0) as u64;
            sig |= bucket << (i * 7);
        }
        sig
    }
}

// Build a fleet of intents that tile together like a girih pattern
let center = GirihIntent::new(
    [0.5; 9],
    GirihTile::Decagon,  // The center is always a decagon — balanced
);

let radiating = vec![
    GirihIntent::new([0.8, 0.3, 0.5, 0.7, 0.6, 0.4, 0.5, 0.8, 0.3], GirihTile::Pentagram),
    GirihIntent::new([0.3, 0.8, 0.5, 0.4, 0.6, 0.7, 0.5, 0.3, 0.8], GirihTile::Pentagram),
    GirihIntent::new([0.5, 0.5, 0.8, 0.5, 0.5, 0.5, 0.8, 0.5, 0.5], GirihTile::Hexagon),
];

for (i, agent) in radiating.iter().enumerate() {
    let compatible = center.tiles_with(agent, 0.4);
    println!("Agent {}: tiles with center = {}, weight = {:.3}",
             i + 1, compatible, agent.ornamental_weight());
}
```

---

## III. الجبر (Al-Jabr): The Algebra of Reconnection

### Al-Khwarizmi's Gift to the World

The word **algebra** comes from the Arabic **الجبر (al-jabr)**, meaning "the reunion of broken parts." It was coined by **محمد بن موسى الخوارزمي (Muḥammad ibn Mūsā al-Khwārizmī)** in his 9th-century book *Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wal-muqābala* — the foundational text of algebra. The word **algorithm** itself derives from his name.

Al-Khwarizmi's insight was revolutionary: instead of solving specific problems with specific numbers (as Babylonian and Greek mathematicians did), he developed a system for solving *classes* of problems using *symbols* and *operations*. The **الجبر (restoration)** was the operation of moving a subtracted quantity to the other side of an equation. The **المقابلة (balancing)** was the simplification of both sides.

This is deeply relevant to polyformalism. The core practice of polyformalism — **rewriting the same concept in different formalisms** — is an act of al-jabr. You take a "broken" understanding (incomplete because it was cast in only one formalism) and "restore" it by translating it into another formalism. Each translation reconnects something that was severed.

The conservation law γ + η = C is itself an algebraic identity in the al-Khwarizmi tradition: the total (C) never changes; only the balance between γ and η shifts. Al-Khwarizmi would recognize this immediately: it is a المقابلة (balancing) equation. The two sides must always be equal.

### Algebra vs. Geometry: A Productive Tension

Islamic mathematics made its greatest contributions at the **boundary between algebra and geometry**. The proof that quadratic equations have geometric meaning (completing the square = literally building a square), the development of trigonometric functions, the calculation of π to 16 decimal places by **غياث الدين الكاشي (Ghiyāth al-Dīn al-Kāshī)** in the 15th century — all of these came from the productive tension between symbolic manipulation and geometric intuition.

Polyformalism operates at exactly this boundary. Each formalism is either more algebraic (symbolic, abstract, manipulable) or more geometric (visual, spatial, constructive). The insights come from the **translation between them**:

- **Algebraic formalisms** (Haskell, Coq) are high-γ in symbolic structure, high-η in spatial intuition
- **Geometric/visual formalisms** (graph diagrams, Petri nets) are high-γ in spatial relationships, high-η in symbolic precision
- The translation between them is al-jabr: reconnecting what each one broke apart

```python
# Al-Jabr: the algebra of formalism reconnection
# Key principle: each formalism "breaks" understanding in a specific way.
# Polyformalism "restores" (al-jabr) it by translation.

class AlJabr:
    """
    الجبر (al-jabr) = the reunion of broken parts
    
    Each formalism breaks understanding along certain seams.
    Translation between formalisms reunites the broken parts.
    The total understanding (C) is conserved.
    """
    
    formalism_profiles = {
        # Each formalism has a "break line" — where it severs understanding
        "Haskell": {
            "breaks_at": "execution flow — pure functions hide HOW things happen",
            "restores_via": "monads, but they're awkward — the break line persists",
            "gamma": 0.55,  # Strong symbolic expression
            "eta": 0.45,    # Hidden execution
        },
        "Rust": {
            "breaks_at": "ownership transfer — every value has exactly one owner, forcing explicit lifecycle",
            "restores_via": "borrowing, lifetimes — but the break line is the FEATURE",
            "gamma": 0.85,
            "eta": 0.15,
        },
        "Prolog": {
            "breaks_at": "the search strategy — you say WHAT is true, not HOW to find it",
            "restores_via": "cut (!), but it breaks the declarative purity",
            "gamma": 0.25,
            "eta": 0.75,
        },
        "Lisp": {
            "breaks_at": "the code/data boundary — it doesn't exist, everything is a list",
            "restores_via": "macro expansion — metaprogramming IS the program",
            "gamma": 0.50,
            "eta": 0.50,
        },
        "Coq": {
            "breaks_at": "computational content — proofs hide the algorithms they certify",
            "restores_via": "extraction — but you lose the proof structure",
            "gamma": 0.30,
            "eta": 0.70,
        },
    }
    
    @classmethod
    def jabr(cls, formalism_a: str, formalism_b: str) -> dict:
        """
        Perform al-jabr: translate from A to B.
        What A breaks, B may restore — and vice versa.
        The reunion produces insight neither had alone.
        """
        a = cls.formalism_profiles[formalism_a]
        b = cls.formalism_profiles[formalism_b]
        
        # The insight from translation:
        # B's γ illuminates what A's η concealed — IF they break at different lines
        different_breaks = a["breaks_at"] != b["breaks_at"]
        
        return {
            "from": formalism_a,
            "to": formalism_b,
            "A_breaks": a["breaks_at"],
            "B_breaks": b["breaks_at"],
            "different_break_lines": different_breaks,
            "B_illuminates_A_hidden": different_breaks,
            "A_illuminates_B_hidden": different_breaks,
            "combined_gamma": round(min(1.0, a["gamma"] + b["gamma"] * (0.5 if not different_breaks else 0.3)), 2),
            "insight_expected": "high" if different_breaks else "low — same blind spot",
        }

# The al-jabr of formalism pairs
pairs = [
    ("Haskell", "Rust"),
    ("Prolog", "C"),
    ("Coq", "Python"),
    ("Lisp", "Rust"),
    ("Haskell", "Haskell"),  # Same formalism — no al-jabr possible
]

print("Al-Jabr: formalism reconnection analysis")
print("=" * 70)
for a, b in pairs:
    result = AlJabr.jabr(a, b)
    print(f"\n{a} → {b}:")
    print(f"  A breaks at: {result['A_breaks']}")
    print(f"  B breaks at: {result['B_breaks']}")
    print(f"  Insight: {result['insight_expected']}")
```

---

## IV. ما لا تراه اللغات الأخرى (What Arabic Sees That Others Don't)

### The Wisdom of the Pattern

Islamic civilization developed a unique relationship with mathematics and representation. The prohibition on figurative images in religious contexts (**التحريم (al-taḥrīm)**) did not stifle creativity — it channeled it into mathematics. Geometry, calligraphy, and pattern became the primary languages of artistic and spiritual expression. This produced insights that figurative traditions missed:

**1. اللانهاية من خلال التكرار (Infinity Through Repetition)**

Islamic geometric patterns express the infinite through the finite. A pattern that tiles endlessly across a wall is a finite rule generating infinite complexity. The wall is finite; the pattern's *implication* is infinite.

In polyformalism: a formalism's rules are finite, but the space of computations expressible is infinite. The conservation law γ + η = C holds for every computation — the finite rule produces infinitely many balanced states. The girih tiles are five shapes; the patterns they generate are uncountable. Similarly, the 9-channel intent model has finite dimensions, but the intent space is [0,1]⁹ — a continuum.

**2. الخفاء والظهور (The Hidden and the Manifest)**

In Islamic theology, الله has two faces: **الظاهر (al-ẓāhir)** — the manifest, and **الباطن (al-bāṭin)** — the hidden. Both are names of the same reality. The pattern on the wall is ẓāhir. The mathematical structure beneath it is bāṭin. The wall itself is the unity (tawhid) that contains both.

No formalism can eliminate the bāṭin. Every language has aspects it cannot surface. Assembly language seems to express everything (ẓāhir maximized) — but it hides the higher-level structure, the design intent, the proof of correctness. Prolog seems to express nothing but declarations (bāṭin maximized) — but this very emptiness is its power, because the solver fills the gap.

The insight: **the bāṭin is not a deficiency to be overcome. It is the space where intelligence operates.** Just as the negative space in Islamic geometric art — the spaces between the lines — is where the light enters and the pattern breathes.

**3. التوازن (Balance) as Non-Trivial Equilibrium**

Islamic art always seeks **التوازن (al-tawāzun)** — balance. But it is never static symmetry. The most beautiful patterns have rotational symmetry but no reflective symmetry. They are balanced *in motion*, not balanced *at rest*. This is the difference between a spinning top (dynamic balance) and a block of stone (static balance).

The polyformalism fleet coordination model seeks the same dynamic balance: the 9-channel intent vectors across the fleet are never identical, but they are *within tolerance* of each other. The fleet is not a monolith (static balance). It is a **محفلة (muḥaffala)** — an ensemble of distinct agents in dynamic equilibrium.

**4. الخوارزميات كطقوس (Algorithms as Ritual)**

**الخوارزمي (al-Khwārizmī)** gave us the word "algorithm." But in the Islamic mathematical tradition, the process of computation was also a form of **ذكر (dhikr)** — meditative repetition. Each step of a geometric construction, each application of an algebraic rule, was performed with intention and precision. The algorithm was not just a tool for getting an answer — it was a practice of ordering the mind.

Polyformalism's 30-minute protocol — rewriting the same concept in multiple formalisms — is a form of dhikr. Each rewrite is a repetition with variation. Each variation deepens the understanding. The point is not the output. The point is the practice.

---

## V. التمرين (Practical Exercise): The Compass and Straightedge Protocol

### Exercise 1: ارسم الخوارزمية (Draw the Algorithm)

Take any algorithm you know well — sorting, searching, hashing. Now, instead of writing code:

1. **Draw it as a geometric pattern** using only circles and straight lines. No labels, no text. Pure geometry.
2. Ask: What did drawing FORCE you to think about? (Probably: the shape of data flow, the branching structure, the loops.)
3. Ask: What did drawing LET YOU IGNORE? (Probably: data types, error handling, edge cases.)
4. Now write the algorithm again in code. You will find that your geometric understanding has changed your code — it has more structure, more clarity, more ẓāhir in the geometric sense.

### Exercise 2: الجبر (Reconnection Through Translation)

1. Write a function in your preferred language.
2. Rewrite it in a formalism from a completely different paradigm.
3. Ask: **What did the translation restore?** (الجبر: what broken understanding did it reunite?)
4. Ask: **What does the original formalism hide that the new one reveals?** (What is the bāṭin of the original?)

The key is step 3: the translation is not the point. The RESTORATION is the point. You are not translating. You are performing al-jabr — reuniting what was broken.

### Exercise 3: الزخرفة (Ornament Your Intent)

Model your system's behavior as a girih-like pattern:
- Each agent is a "tile" with a specific shape (role)
- The 9-channel intent vector determines the tile's "decoration"
- The trust graph determines which tiles tile together
- Draw (or visualize) the resulting pattern

When the pattern is harmonious, the fleet is in consensus. When the pattern has gaps or clashes, there is a trust violation. You can *see* the health of your fleet in the beauty of its pattern.

```python
# Practical exercise: girih pattern analysis of fleet health
import math

def fleet_girih_health(agents: dict, trust_graph: list) -> dict:
    """
    Analyze fleet health as a girih pattern problem.
    
    agents: {name: 9-channel intent vector}
    trust_graph: [(agent_a, agent_b, tolerance), ...]
    
    A beautiful pattern = all edges tile smoothly.
    A broken pattern = some edges have gaps.
    """
    total_edges = len(trust_graph)
    harmonious_edges = 0
    broken_edges = []
    
    for a, b, tol in trust_graph:
        if a not in agents or b not in agents:
            continue
        
        va = agents[a]
        vb = agents[b]
        
        # Edge-wise channel comparison
        max_gap = max(abs(x - y) for x, y in zip(va, vb))
        
        if max_gap <= tol:
            harmonious_edges += 1
        else:
            # Which channels clash?
            clashes = [i for i, (x, y) in enumerate(zip(va, vb)) 
                       if abs(x - y) > tol]
            broken_edges.append({
                "edge": (a, b),
                "max_gap": round(max_gap, 4),
                "clashing_channels": clashes,
            })
    
    beauty = harmonious_edges / total_edges if total_edges > 0 else 0.0
    
    # The aesthetic principle: beauty = harmony / total
    # 1.0 = perfect girih pattern (impossible in practice — always some ma)
    # > 0.8 = beautiful (wabi-sabi: the small imperfections are the light)
    # > 0.5 = functional but unrefined
    # < 0.5 = broken pattern — needs restructuring
    
    return {
        "harmonious": harmonious_edges,
        "broken": total_edges - harmonious_edges,
        "beauty": round(beauty, 4),
        "assessment": (
            "كامل (perfect)" if beauty >= 0.95 else
            "جميل (beautiful)" if beauty >= 0.80 else
            "مقبول (acceptable)" if beauty >= 0.60 else
            "مكسور (broken)"
        ),
        "broken_edges": broken_edges,
    }

# Example fleet
agents = {
    "forgemaster":   [0.9, 0.3, 0.7, 0.1, 0.5, 0.8, 0.2, 0.6, 0.4],
    "scout":         [0.8, 0.4, 0.6, 0.2, 0.6, 0.7, 0.3, 0.5, 0.5],
    "synthesizer":   [0.85, 0.35, 0.65, 0.15, 0.55, 0.75, 0.25, 0.55, 0.45],
    "oracle":        [0.5, 0.5, 0.5, 0.5, 0.9, 0.5, 0.9, 0.5, 0.5],
}

trust = [
    ("forgemaster", "scout", 0.20),
    ("forgemaster", "synthesizer", 0.15),
    ("scout", "synthesizer", 0.20),
    ("forgemaster", "oracle", 0.30),
    ("scout", "oracle", 0.30),
    ("synthesizer", "oracle", 0.30),
]

health = fleet_girih_health(agents, trust)
print(f"Fleet pattern health: {health['assessment']}")
print(f"  Beauty score: {health['beauty']}")
print(f"  Harmonious edges: {health['harmonious']}/{health['harmonious'] + health['broken']}")
if health['broken_edges']:
    print(f"  Broken edges:")
    for be in health['broken_edges']:
        print(f"    {be['edge']}: gap={be['max_gap']}, channels={be['clashing_channels']}")
```

---

## خاتمة (Conclusion)

> *العلم نورٌ يقذفه الله في القلب*  
> "Knowledge is a light that God casts into the heart."  
> — Islamic saying

Polyformalism's conservation law, γ + η = C, is the mathematical articulation of an insight that Islamic civilization carried for a thousand years: **the manifest and the hidden are one**. الظاهر and الباطن are not opposites. They are two faces of the same unity. Every formalism that reveals also conceals. Every pattern that shows also hides. The sum is always tawhid — always one.

The 9-channel intent model, like the girih tiles, creates infinite patterns from finite rules. The fleet coordination, like Islamic architectural space, seeks dynamic equilibrium — not static uniformity. The practice of polyformalism, like الخوارزمي's algebra, is al-jabr — the reunion of broken understanding through translation across formalisms.

What does العربية see that other languages don't? **The infinite expressed through the finite. The hidden as the complement of the manifest, not its enemy. The pattern as prayer. The algorithm as dhikr. The geometry as theology.** These are not metaphors. They are the structural insights of a civilization that spent a millennium at the intersection of mathematics, art, and spirituality — and produced insights that the world of computation is only beginning to formalize.

Polyformalism's gift is to make these insights **systematic and transferable** — to create a protocol where any engineer can access the power of al-jabr, tawhid, and girih. Islamic mathematics' gift is to remind us that these ideas were never lost. They have been inscribed in the walls of mosques, woven into carpets, and sung in the call to prayer for centuries. The mathematics was always there. We only needed eyes to see.

---

*شكراً (shukran). This guide was written with deep respect for the Islamic mathematical, artistic, and philosophical tradition — a tradition that preserved and advanced human knowledge through centuries when Europe had forgotten it, and whose geometric and algebraic insights remain at the foundation of all computation.*

---

## Further Reading

- [Polyformalism Framework](../../GUIDE.md)
- [Negative Space Between Languages](../NEGATIVE-SPACE-BETWEEN-LANGUAGES.md)
- [Mathematical Framework](../../research/PAPER-MATHEMATICAL-FRAMEWORK.md)
- Al-Khwārizmī, Muḥammad ibn Mūsā. *Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wal-muqābala* — the founding text of algebra
- Lu, P. J. & Steinhardt, P. J. (2007). "Decagonal and Quasi-Crystalline Tilings in Medieval Islamic Architecture." *Science* 315:1106-1110
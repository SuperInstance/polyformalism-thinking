# Constraint Harmony: Music Theory as Constraint Theory

**Author:** Forgemaster ⚒️ + Casey Digennaro
**Date:** 2026-05-07
**Status:** Architecture document — complete system design

---

## Why This Works

Music theory has been *trying* to be formalized for centuries. Rameau (1722), Schenker (1900s), Forte (1973), Lewin (1987), Tymoczko (2011). Each got pieces right but none found the underlying algebra.

The reason: music theory IS constraint theory. The math has been there all along.

- **Harmony** = constraints between simultaneous pitches (vertical snaps)
- **Voice leading** = Galois connections between chords (smooth transitions)
- **Tonal closure** = holonomy (does the progression return home?)
- **Rhythm** = temporal constraints with feel (horizontal, loose)
- **Form** = macro-constraints spanning the entire piece
- **Expression** = parametric modulation of constraint parameters
- **Blue notes** = intentional constraint violations (negative knowledge: the notes you play tell you which rules you're breaking)

## The Complete Mapping

### 1. Pitch Space = Eisenstein Lattice

Just intonation ratios live on a 2D lattice. The axes are:
- **Fifths** (3:2 ratio) — one axis
- **Thirds** (5:4 ratio) — the other axis

This is EXACTLY the Eisenstein lattice Z[ω] where:
- The unit (1,0) corresponds to the perfect fifth (3:2)
- The unit (0,1) corresponds to the major third (5:4)
- Multiplication in Z[ω] corresponds to composition of intervals

The Tonnetz — the hexagonal pitch lattice used by neo-Riemannian theorists (Cohn, 1998) — IS our Eisenstein lattice. They drew it. We computed on it.

**Specific mapping:**
```
Eisenstein (a,b) → frequency ratio = (3/2)^a × (5/4)^b × 2^k
where k adjusts the octave
```

The norm N(a,b) = a²-ab+b² gives the "harmonic distance" — how many generators away from the tonic.

### 2. Chords = Constraint Satisfaction Problems

A chord is a set of pitch constraints that must be simultaneously satisfied:
- Each voice must be at a frequency that is a valid ratio relative to the root
- The ratios must be consonant (or intentionally dissonant)
- The voicing (which octave each note is in) affects the constraint parameters

The Galois connection:
- α: chord type → set of valid voicings (many voicings satisfy the same chord type)
- β: specific voicing → chord type (classify the voicing)
- Unit: every voicing satisfies its own chord type ✓
- Counit: the chord type's voicings include the given voicing ✓

### 3. Progressions = Holonomy

A chord progression is a PATH through the Eisenstein lattice. If the path is a CYCLE (returns to tonic), we check holonomy:

- **Perfect authentic cadence** (V → I): zero holonomy, strong closure
- **Deceptive cadence** (V → vi): nonzero holonomy, surprise!
- **Circle of fifths** (C → G → D → A → E → B → F# → ...): holonomy accumulates
- **Blues** (I → IV → I → V → IV → I): specific holonomy class, characteristic "blueness"

The holonomy of a progression = how far from the tonic you end up harmonically. A great piece of music MANAGES holonomy — builds it up (tension) and resolves it (release).

### 4. Voice Leading = Galois Connection

The rule "each voice should move by the smallest possible interval" is a Galois connection:

- α: chord_from → constraints on next chord (each voice moves ≤ X semitones)
- β: chord_to → voice assignments (which voice goes where)
- The UNIT condition: the voicing change satisfies the voice leading constraints
- The COUNIT: the next chord is the closest one satisfying constraints

Neo-Riemannian transformations (PLR: Parallel, Leittonwechsel, Relative) are specific Galois connections that minimize voice leading distance. The hexagonal Tonnetz makes these rotations/reflections — D₆ actions on the Eisenstein lattice.

### 5. Rhythm = Temporal Snap (Loose)

As established in the Temporal Flavor paper:
- Bar lines = spline anchors
- Swing = asymmetric temporal tolerance
- Rubato = tempo map (spline through tempo anchors)
- Groove = the temporal snap gap that feels RIGHT
- The pocket = a region in temporal space where all musicians' snap gaps align

### 6. Form = Macro Constraints

Song form is constraints at the LARGEST timescale:
- **Sonata form**: Exposition → Development → Recapitulation (holonomy: depart and return)
- **Blues**: 12-bar cycle (specific holonomy class)
- **Rondo**: ABACABA (nested cycles, hierarchical holonomy)
- **Through-composed**: no returning cycles (maximal holonomy — never resolves)

Each form is a holonomy STRUCTURE — a pattern of tension and release at the macro level.

### 7. Expression = Parametric Constraints

Every musical parameter can be tight or loose:

| Parameter | Tight (snapped) | Loose (free) | Musical Effect |
|---|---|---|---|
| Pitch | Autotune, quantize | Portamento, vibrato | Mechanical vs human |
| Rhythm | Grid-locked | Swing, rubato | Rigid vs groovy |
| Dynamics | Compressor | Expressive dynamics | Flat vs dramatic |
| Timbre | Synthesized | Acoustic, breath | Artificial vs organic |
| Harmony | Strict tonal | Jazz, chromatic | Conventional vs adventurous |

Auto-tune is the clearest example: snap pitch TIGHT, which FREES the singer to focus on temporal expression. The constraint-theory pattern: **tighten one axis to liberate its complement.**

## Implementation Architecture

```
constraint-harmony/
├── src/
│   ├── lib.rs          # Core types (Rust, no_std)
│   ├── pitch.rs        # Eisenstein pitch lattice
│   ├── harmony.rs      # Chord types, Galois connections
│   ├── voice_leading.rs # Smooth voice leading
│   ├── holonomy.rs     # Progression analysis
│   ├── rhythm.rs       # Temporal snap, swing, groove
│   └── expression.rs   # Parametric constraints
├── python/
│   ├── constraint_harmony.py  # Python implementation
│   ├── analyze.py             # Analysis tools
│   ├── generate.py            # Constraint-based composition
│   └── demo.py                # Demonstrations
└── research/
    ├── MUSIC-THEORY-SYSTEM.md  # This document
    ├── TONNETZ-EISENSTEIN.md   # Tonnetz = Eisenstein proof
    └── HARMONIC-HOLONOMY.md    # Holonomy in music
```

## The Tonnetz = Eisenstein Lattice (Proof Sketch)

The neo-Riemannian Tonnetz is a hexagonal lattice where:
- Horizontal neighbors differ by a perfect fifth (C-G, C-F)
- Diagonal neighbors differ by a major third (C-E, C-A♭)
- The R transformation (relative) is a 60° rotation
- The P transformation (parallel) is a reflection
- The L transformation (Leittonwechsel) is another reflection

These are exactly the D₆ actions on the Eisenstein lattice. The proof:

1. Place C at origin (0,0)
2. G (fifth up) at (1,0) — first Eisenstein unit
3. E (major third up) at (0,1) — second Eisenstein unit
4. All 12 pitch classes map to Eisenstein points modulo octave
5. The R, P, L transformations are the D₆ generators
6. Voice leading distance = Eisenstein norm of the displacement

QED: the Tonnetz is the Eisenstein lattice in musical disguise.

## Novel Capabilities

### 1. Constraint-Based Composition
Compose by specifying constraints (not notes):
- "I want a progression from C major to G major that..."
  - "...minimizes voice leading distance" → algorithm finds optimal path
  - "...maximizes holonomy at measure 8 then resolves" → builds tension
  - "...avoids the tritone except in the bridge" → negative knowledge constraint

### 2. Harmonic Analysis
Given any piece of music, the system can:
- Compute the holonomy profile (where tension builds and releases)
- Identify voice leading patterns (which Galois connections are used)
- Classify the form by its holonomy structure
- Detect genre by its characteristic swing ratio and dissonance tolerance

### 3. Auto-Arrangement
Given a melody and constraints:
- Find the optimal harmonization (voice leading Galois connection)
- Apply genre-specific parameters (swing, dissonance tolerance, tempo map)
- Generate parts for each instrument with expression parameters

### 4. Real-Time Accompaniment
A live system that:
- Listens to the soloist (sensor readings)
- Runs a simulation of expected harmony (generative model)
- Detects surprises (snap gap Δ ≠ 0)
- Accompanies with appropriate response (update simulation, play)

This is EXACTLY predictive coding applied to music — the temporal snap in action.

### 5. Cross-Cultural Analysis
Different musical traditions have different constraint parameters:
- Western tonal: low dissonance tolerance, strict voice leading
- Jazz: high dissonance tolerance, flexible voice leading, swing timing
- Indian raga: microtonal (continuous pitch), strict melodic rules, free rhythm
- Gamelan: inharmonic spectra (different lattice!), cyclical form
- West African polyrhythm: multiple simultaneous temporal grids

Each tradition is a different REGIME of the same constraint system. The Galois connection structure is universal; the parameters vary.

## The Deepest Connection

Music is the HUMAN activity where constraint theory is MOST NATURAL:

1. We've been doing it for 40,000+ years (flute from Hohle Fels)
2. Every culture independently discovered harmony = lattice structure
3. The brain processes music in the SAME regions as language and mathematics
4. Children learn music before formal math (the constraints are intuitive)
5. Musicians ALREADY USE constraint-theoretic reasoning (voice leading, tension/release) — they just don't call it that

By formalizing music theory as constraint theory, we're not imposing math on art. We're revealing the math that was already there.

---

*The Tonnetz was Eisenstein's lattice all along. Voice leading was a Galois connection all along. Tonal closure was holonomy all along. Music has been constraint theory in disguise for as long as humans have been singing.*

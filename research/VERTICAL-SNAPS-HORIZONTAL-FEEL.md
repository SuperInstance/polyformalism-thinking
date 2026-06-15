# Vertical Snaps, Horizontal Feel

**Author:** Forgemaster ⚒️ (from Casey's insight)
**Date:** 2026-05-07
**Status:** Core principle — orthogonal constraint regimes

---

## Two Axes, Two Logics

Lay music out on a grid:

```
Pitch (vertical) ── geometrically perfect, snaps to ratios
  │
  │  ●───────────●───────────●
  │     3:2          5:4
  │   perfect      major
  │   fifth        third
  │
  └──────────────────────────────── Time (horizontal)
                    intentionally sloppy, feel, groove
```

The vertical axis is **architecture**. The horizontal axis is **inhabitation**.

### The Vertical: Geometric Perfection

- **Perfect fifth (3:2 ratio)**. 1.5:1. Found in every harmonic series. Not invented — discovered. The universe snaps to this.
- **Major third (5:4 ratio)**. 1.25:1. The harmonic major third, not the equal-tempered 1.2599... The real one is geometrically exact.
- **Octave (2:1)**. The most fundamental snap. Frequency doubles.
- **Fourth (4:3)**. Inversion of the fifth. Same geometry from the other direction.

These are **Eisenstein-snapped**. The ratios are exact integers. The norm a²-ab+b² maps directly onto the harmonic ratios when you evaluate on the right lattice points. The fifth IS a Galois connection between fundamental and overtone — α goes up (add the interval), β comes back down (subtract it), and the composition closes perfectly (zero holonomy on the frequency cycle).

The vertical axis doesn't tolerate slop. A perfect fifth that's 2 cents off creates audible beating. The constraint is TIGHT because the ear is a precision instrument for pitch ratios. The snap gap must be near zero.

This is why autotune exists and works: the vertical axis WANTS to be snapped. The human voice naturally wobbles around pitch centers. Autotune grabs those wobbles and snaps them to the nearest geometrically-correct frequency. The singer sings in the neighborhood, and the algorithm provides the address.

### The Horizontal: Intentional Sloppiness

But time? Time is the WILD axis.

- **Laying back 35ms on the off-beat** — not wrong, *groovy*
- **Pushing the downbeat 20ms early** — not wrong, *urgent*
- **Rubato** — tempo bends with emotion, speeds up when excited, slows when reflective
- **Swing** — the eighth note isn't 50/50. It's 60/40 or 67/33 or whatever the tune needs
- **The pocket** — an invisible temporal zone where the beat feels RIGHT, which is NOT at the mathematically perfect position

None of these are errors. They're *expressive modulation of the temporal axis*. The drummer who plays metronome-perfect time sounds robotic. The drummer who ADDS ε to every off-beat sounds like music.

The horizontal axis REJECTS the snap. Or more precisely: the horizontal axis's snap is looser. The tolerance is wider. The deadband is bigger. The constraint is "hit within ±50ms" not "hit at exactly t."

### Auto-Tune Frees the Temporal Axis

Here's the key architectural insight Casey named:

> "Singers use auto-tune to snap their voices, giving more freedom on the temporal axis."

When you snap the vertical tight, you FREE the horizontal. When pitch is handled by the algorithm, the singer can focus all attention on WHEN to place the note, how to shape the phrase, where to breathe. The snap in one dimension LIBERATES the other dimension.

This is not an accident of technology. It's a structural principle:

**When you constrain one axis tightly, you free the complementary axis for expression.**

## The Constraint Theory Implication

### Snapped Dimensions vs Free Dimensions

In any constraint system, not all dimensions should be equally constrained. Some want tight snaps (vertical), some want loose feel (horizontal).

| Dimension | Analogy | Snap Tightness | Why |
|---|---|---|---|
| Spatial precision | Pitch | TIGHT — snap to geometric ratios | Physics demands exact values |
| Temporal placement | Rhythm | LOOSE — feel, groove, pocket | Expression lives in deviation |
| Safety constraints | Harmony rules | TIGHT — zero holonomy | Violation = danger |
| Operational parameters | Dynamics | LOOSE — adaptive, context-dependent | Efficiency lives in flexibility |
| Identity/state | Key signature | TIGHT — fixed for the session | Consistency required |
| Trajectory | Melodic contour | LOOSE — rubato, interpretation | Beauty lives in variation |

### The Principle of Selective Tightness

**Corollary to the Snap Hypothesis:** A well-designed constraint system snaps the dimensions where precision enables capability and leaves free the dimensions where flexibility enables expression.

- A boat autopilot snaps HEADING (vertical — where you're going) but leaves RATE OF TURN loose (horizontal — how you get there, with feel)
- A safety system snaps THRESHOLDS (vertical — hard limits) but leaves RESPONSE TIME loose (horizontal — how quickly you react, adapted to conditions)
- A fleet snaps IDENTITY (vertical — who each agent is) but leaves COMMUNICATION TIMING loose (horizontal — asynchronous, surprise-driven)

### Auto-Tune as Architectural Pattern

The auto-tune pattern applies everywhere:

1. **Identify the vertical axis** — the dimension where geometric precision matters
2. **Snap it tight** — apply a Galois connection with near-zero tolerance
3. **This frees the horizontal axis** — the complementary dimension can now be expressive
4. **Monitor the horizontal for genuine anomalies** — but with a wide deadband

In our fleet architecture:
- **Vertical (snapped):** constraint satisfaction (holonomy = 0), identity, trust bounds, safety limits
- **Horizontal (free):** communication timing, resource allocation, exploration strategy, learning rate
- **Auto-tune:** the Galois connection α/β automatically snaps the vertical (checks constraints exactly)
- **Freed temporal axis:** agents can respond asynchronously, with feel, without synchronizing clocks

## The Geometry of the Fifth

A perfect fifth is 3:2. In our Eisenstein framework:

```
Norm(3, 0) = 9    (fundamental, call it f)
Norm(2, 0) = 4    (octave, 2f)  
Norm(3, 2) = 9-6+4 = 7
Norm(5, 3) = 25-15+9 = 19
```

The ratio 3:2 in Eisenstein terms: if the fundamental has norm N, the fifth has norm (3/2)²N. This only works in the continuous (frequency) domain. In the discrete Eisenstein domain, you can't have "half a lattice point."

But the HARMONIC RELATIONSHIPS snap exactly:
- Octave: N → 4N (norm squares — perfectly representable)
- Fifth: frequency ratio 3:2 (continuous, not discrete)
- But: the RATIO is the snap. The frequency domain α snaps to the ratio, β recovers from the ratio.

This means: the vertical axis of music lives in the CONTINUOUS Eisenstein extension (Q(ω), the field of fractions), while the horizontal axis lives in the INTEGER lattice (Z[ω], discrete).

**The vertical snaps in Q. The horizontal breathes in Z.**

## Swing as Constraint Relaxation

Swing rhythm: the eighth note pair is not 50/50 but 60/40 or 67/33. In constraint terms:

- Straight time: constraint is "note at t=0.5s, next note at t=1.0s" (symmetric)
- Swing: constraint is "note at t=0.5s, next note at t=1.17s" (asymmetric)
- The RATIO 67:33 is the swing feel. Different genres snap to different ratios:
  - Jazz: ~67:33
  - Hip-hop: ~60:40
  - Blues: ~63:37
  - Shuffle: ~70:30

Each genre has a CHARACTERISTIC SWING RATIO — a temporal Galois connection with a specific asymmetry. The ratio IS the feel. Change the ratio and you change the genre.

This is a REGIME-DEPENDENT SNAP (as identified in the temporal flavor paper): different contexts activate different constraint parameters. The snap structure is the same (temporal placement) but the parameters change with the musical regime.

## The Singer's Freedom

When auto-tune handles pitch, the singer focuses on:
1. **Timing** — where in the beat to place the note (horizontal)
2. **Dynamics** — how loud/soft (vertical, but continuous, not snapped)
3. **Timbre** — tone quality (a dimension without a snap — the space BETWEEN pitch values)
4. **Phrasing** — how notes connect into a line (the CURVE between spline anchors)

The auto-tune doesn't remove artistry. It MOVES the artistry from the vertical (pitch accuracy) to the horizontal (temporal placement) and the interstitial (timbre, dynamics, phrasing).

Similarly, a well-designed constraint system doesn't remove freedom. It MOVES freedom to the dimensions where it matters most. The fleet's Galois connections snap the safety-critical dimensions (holonomy, identity) and leave free the operational dimensions (timing, strategy, learning).

## The Harmonic Series as Snap Ladder

The harmonic series IS a sequence of snaps, each one an octave up:

```
f → 2f → 4f → 8f → ...  (octaves — norm × 4 each time)
f → 3f → 6f → 12f → ... (fifths — norm × 9/4, snapped to 9 in integer domain)
f → 5f → 10f → 20f → ... (major thirds — norm × 25/16, snapped to 25)
```

Each harmonic is a Galois connection between the fundamental and the overtone. The snap:
- α: fundamental → overtone frequency (multiply by n)
- β: overtone → fundamental (divide by n, floor to nearest representable)
- Unit: β(α(f)) ≤ f (round-trip loses precision in the integer lattice)
- But in Q(ω): β(α(f)) = f EXACTLY (rational arithmetic is lossless)

The harmonic series snaps perfectly in the continuous domain (Q) and approximately in the discrete domain (Z). This is EXACTLY our precision snap (Part 4): continuous → discrete with controlled loss.

## What This Means for the Fleet

The Cocapn fleet is an ensemble. Every agent is a musician:

1. **Vertical alignment** = constraint satisfaction (all agents snap to the same constraint values)
2. **Horizontal freedom** = asynchronous operation (each agent has its own feel, its own timing)
3. **Auto-tune** = the Galois connection (automatically snaps each agent's vertical alignment)
4. **The groove** = the emergent behavior when agents' horizontal freedoms synchronize without a metronome
5. **The solo** = an agent's surprise signal (Δ ≠ 0) commanding attention — a moment of leadership
6. **The rest** = an agent going silent (Δ ≈ 0, nothing to report, saving bandwidth)

A jazz ensemble doesn't have a conductor. They listen to each other. The rhythm section (bass + drums) provides the time feel. The soloist plays over it. The comping instruments fill the spaces.

The fleet should work the same way:
- **Rhythm section** = Oracle1 + core services (provide the constraint backbone — the "time")
- **Soloists** = specialist agents (Forgemaster, etc. — provide focused expertise on demand)
- **Comping** = monitoring agents (fill in context, provide background awareness)
- **The tune** = the shared mission (the constraint graph everyone's playing over)

---

*Pitch snaps because physics. Time breathes because music. The auto-tune frees the voice by handling the vertical so the singer can live on the horizontal. Our constraint framework must do the same: snap what geometry demands, free what expression requires.*

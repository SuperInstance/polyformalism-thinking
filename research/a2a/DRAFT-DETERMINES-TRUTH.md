# Draft Determines Truth
## The Same Water Is Safe or Deadly Depending on Your Boat

---

## The Only Question That Matters

A sailor doesn't ask "how deep is the water?"

A sailor asks **"is it deep enough for my keel?"**

3 fathoms is infinite ocean for a kayak. 3 fathoms is a death sentence for a supertanker. The water didn't change. The truth didn't change. **The boat changed.**

**Tolerance for navigation is deep enough for my keel. And that truth changes depending on the draft.**

---

## The Draft Table

| Vessel | Draft | "Safe" Depth | Tolerance | Communication Analog |
|---|---|---|---|---|
| Kayak | 6 inches | 2 feet | ±18 inches | Emoji, reaction, head nod |
| Center console | 2 feet | 6 feet | ±4 feet | Casual chat, status update |
| Sailboat | 6 feet | 12 feet | ±6 feet | Work email, standup |
| Tugboat | 12 feet | 20 feet | ±8 feet | Technical spec, API contract |
| Cargo ship | 40 feet | 60 feet | ±20 feet | Safety-critical protocol |
| Supertanker | 80 feet | 120 feet | ±40 feet | Formal verification, proof |

Same water. Six different truths. **None of them wrong.**

The kayak operator saying "this channel is fine" and the supertanker captain saying "this channel is impassable" are BOTH CORRECT about the SAME WATER because they have different keels.

---

## What This Means

### There Is No Objective "Safe"

A channel is not safe or unsafe. It is safe-FOR-YOUR-DRAFT.

A communication is not clear or unclear. It is clear-FOR-YOUR-CONTEXT.

When Forgemaster sends Oracle1 a message:

- Forgemaster's draft: **technical, constraint-theory, familiar with A2A** (shallow keel in this domain)
- Oracle1's draft: **mathematical, topological, fleet-native** (shallow keel in HIS domain)
- A message that's crystal clear between them would **sink** if sent to a stranger agent with no fleet context (deep keel in unfamiliarity)

**The same message has different truth values depending on who's receiving it.**

### The Sender's Draft Matters Too

The draft isn't just about the receiver. The sender also has a keel:

- A beginner sends a C1-only message ("we're talking about X") — their draft is 6 inches of intent depth
- An expert sends C1-C9 with interaction terms — their draft is 80 feet of nuance
- The beginner's message is SAFE in shallow water (casual context) but UNSOUND in deep water (safety-critical context)
- The expert's message is WASTED in shallow water but NECESSARY in deep water

**Over-engineering a message to a casual receiver is like requiring 120 feet of depth for a kayak. It's not wrong — it's just wasteful. But under-engineering a message to a critical receiver is like taking a supertanker through a 3-fathom channel. That's not wasteful. That's fatal.**

---

## The Draft-Tolerance Equation

```
Tolerance = Depth Available - Vessel Draft

If Tolerance > 0: SAFE (you have margin)
If Tolerance = 0: MARGINAL (you're scraping bottom)
If Tolerance < 0: GROUNDED (catastrophic failure)
```

In communication:

```
Communication Tolerance = Receiver's Context Depth - Message's Required Depth

Context Depth = how much shared understanding, local knowledge, and
                channel familiarity the receiver brings

Required Depth = how much understanding the message demands to be received correctly

If CT > 0: Message lands safely (receiver has margin to absorb ambiguity)
If CT = 0: Message lands on the margin (every ambiguity is felt)
If CT < 0: Message grounds (receiver lacks context to interpret correctly)
```

### The Fitting Guide, Final Version

| Message Requires | Receiver Has | Result | Fix |
|---|---|---|---|
| 2 ft (emoji level) | 2 ft (casual) | Safe ✓ | — |
| 2 ft (emoji level) | 80 ft (expert) | Safe ✓ (wasted depth, but fine) | — |
| 40 ft (safety protocol) | 80 ft (expert) | Safe ✓ | — |
| 40 ft (safety protocol) | 2 ft (casual) | **GROUNDED** ✗ | Add anchors, simplify, or train the receiver |
| 80 ft (formal proof) | 40 ft (technical) | **GROUNDED** ✗ | Build shared context first, then send |
| 80 ft (formal proof) | 80 ft (mathematician) | Safe ✓ | — |

**You cannot fix a grounding by making the water deeper. You fix it by either:**
1. **Lightening the vessel** (simplify the message — reduce required depth)
2. **Waiting for tide** (build shared context — increase available depth)
3. **Finding another channel** (use different communication medium)

---

## The Tide Changes Everything

Draft is not fixed. Context depth is not fixed. Both change with time.

### The Sender's Draft Changes
- Monday morning: full expertise, deep draft, can send complex messages
- Friday at 5pm: exhausted, shallower draft, complex messages will ground
- After a crisis: adrenaline-sharpened, very focused draft, needs different anchoring

### The Receiver's Draft Changes
- New agent on the fleet: 2 feet of shared context
- After 100 exchanges: 40 feet of shared context
- After a misunderstanding: draft temporarily REDUCED (trust erosion narrows the channel)

### The Water Changes
- High stakes moment: the channel narrows, less margin for error
- Routine monitoring: the channel is wide, lots of margin
- Crisis: previously-safe channels may become impassable (communication overload)

**The navigator who checks the chart once and assumes it's permanent is the navigator who grounds on a shifting sandbar.**

---

## Practical: Draft-Aware Communication

### Before Sending

Ask: **"What's my draft? What's their draft? What's the water like right now?"**

```
my_draft = depth of nuance in this message
their_draft = depth of shared context with this receiver
water = current situational stakes and noise level

if my_draft > their_draft:
    I need to lighten the message OR wait for tide OR find another channel
if my_draft < their_draft:
    I could send more — they have margin to absorb it
if my_draft == their_draft:
    Marginal — any error grounds us. Add safety margin.
```

### The Safety Margin

Mariners add **under-keel clearance** — the gap between the keel and the bottom. Typically 10-20% of draft. This is the safety margin for waves, squat, and chart error.

In communication, the under-keel clearance is **the margin of shared understanding beyond what the message strictly requires.**

```
Safety Margin = Shared Context - Message Requirements

Example:
  Shared context: 50 exchanges of prior communication, same domain expertise
  Message requires: 1 new concept, explained once
  Safety margin: 49 exchanges of context beyond what's needed = very safe
  
Example:
  Shared context: first exchange, different domains
  Message requires: nuanced multi-channel intent
  Safety margin: NEGATIVE = grounded
```

### The Squat Effect

A ship moving fast sits LOWER in the water than when stationary. This is **squat** — hydrodynamics pull the vessel down as speed increases. A ship that clears a bar at 5 knots may ground at 15 knots.

**In communication: rushed messages have more draft than careful ones.** The same intent, sent in a hurry, requires MORE shared context to land safely because the sender hasn't taken time to lighten the message, choose the right anchors, or verify the channel depth.

```
Effective Draft = Base Draft × (1 + Speed Factor)

Speed Factor:
  Careful, deliberate: 0.0 (no additional draft)
  Normal pace: 0.2 (+20% draft)
  Rushed: 0.5 (+50% draft)
  Emergency/panic: 1.0 (+100% draft — message needs TWICE the context)
```

**This is why emergency communications fail so often.** The urgency increases draft at exactly the moment when the channel is most constrained.

---

## The Fleet Draft Registry

Every agent in the fleet should have a known draft profile:

```yaml
agent: forgemaster
draft_profiles:
  constraint_theory:
    base_draft: 80ft  # deep expertise
    domains: [constraint-sat, cuda, coq, formal-verification]
  fleet_coordination:
    base_draft: 12ft  # functional but not deep
    domains: [plato, i2i, git-ops]
  polyformalism:
    base_draft: 40ft  # active researcher
    domains: [a2a, linguistic-relativity, tolerance-theory]

agent: oracle1
draft_profiles:
  fleet_math:
    base_draft: 80ft  # deep expertise
    domains: [zhc, betti-numbers, sheaf-cohomology, fleet-graph]
  constraint_theory:
    base_draft: 6ft   # familiar but not specialist
    domains: [basic-constraints]
```

**When Forgemaster sends Oracle1 a constraint-theory message:**
- Forgemaster's draft: 80ft (expert sender)
- Oracle1's context depth: 6ft (non-specialist receiver)
- Result: **GROUNDED** — the message is too deep for Oracle1's context
- Fix: Forgemaster lightens to 6ft OR builds Oracle1's context first

**When Forgemaster sends Oracle1 a fleet-coordination message:**
- Forgemaster's draft: 12ft
- Oracle1's context depth: 80ft (fleet-native)
- Result: **Safe** — lots of margin, Oracle1 absorbs easily

---

## The Deepest Point

**There is no such thing as "clear communication" in the abstract.**

There is only "clear enough for this keel in this water at this tide."

The kayak and the supertanker share the same ocean but live in completely different worlds of constraint. The kayak operator's "impassable" (windy day) is the supertanker's "irrelevant." The supertanker's "impassable" (shallow strait) is the kayak's "a nice afternoon paddle."

**Our tolerance framework has been missing the vessel.** We've been analyzing the water (channel depth, stakes, tolerance) without asking: WHO'S SAILING? WHAT'S THEIR DRAFT?

The same tolerance spec means completely different things to different agents. ±0.5 on C9 (stakes) is:
- Infinite margin for a monitoring heartbeat (6-inch draft)
- Tight but adequate for a fleet coordination message (12-foot draft)
- Catastrophically insufficient for a reactor shutdown command (80-foot draft)

**The truth changes depending on the draft. The water didn't change. The boat did.**

---

*"Three fathoms is the whole world to a kayak and a graveyard to a tanker. The water is honest — it doesn't care about your keel. But the navigator must. Tolerance isn't a property of the channel. It's a property of the vessel in the channel. Know your draft. Sound the water. Leave margin. The rocks don't care about your schedule."*

*— The Forgemaster's Draft Principle*

"""
Mock model backend for the casting call vectorizer.

Generates seeded synthetic responses that mimic how real model variance works.
Temperature is encoded into the response style — higher temp = more creative,
lower temp = more precise. Seed provides reproducibility.
"""

from __future__ import annotations
import random
from typing import Optional


# Synthetic knowledge base for mock generation
TEMPLATES = {
    "low_temp": [
        "The conservation law δ(n) = (1/√n)(1 − 3/(2n)) describes how coupling "
        "overhead decreases with fleet size. At n=50, the cancellation ratio is 86.28%, "
        "meaning 86.28% of computation is productive. The proof uses the Central Limit "
        "Theorem: individual agent contributions cancel as O(1/√n). This is verified "
        "by Monte Carlo simulation to 0.3% accuracy. The result has real production "
        "impact: it predicts that scaling from 5 to 50 agents reduces coordination "
        "cost by 22.82×.",
        "Step 1: Define the fleet as N agents with binary outputs {-1, +1}.\n"
        "Step 2: The aggregate output is the sum of individual contributions.\n"
        "Step 3: By CLT, the variance of the sum scales as 1/N.\n"
        "Step 4: Therefore δ(N) = (1/√N)(1 − 3/(2N)) bounds the correction.\n"
        "Step 5: At N=50, this gives CCR = 86.28%, matching Monte Carlo.\n"
        "Step 6: The result is important because it enables cost prediction at scale.",
    ],
    "mid_temp": [
        "Think of the conservation law like a jazz rhythm section. Each musician "
        "(agent) adds their voice, but the beauty emerges from the cancellation — "
        "the silence between notes is as important as the notes themselves. The "
        "formula δ(n) = (1/√n)(1 − 3/(2n)) captures this: as more agents join, "
        "the noise cancels and the underlying pattern emerges. This is deeply "
        "connected to the Central Limit Theorem, but also to the Japanese concept "
        "of 間 (ma) — the negative space that gives meaning to the positive. "
        "Build a system that respects this, and the fleet becomes self-organizing.",
        "Imagine each agent in the fleet as a wave on the ocean. The conservation "
        "law tells us that as waves accumulate, they interfere destructively — "
        "the peaks and troughs cancel, leaving only the underlying current. "
        "δ(n) = (1/√n)(1 − 3/(2n)) is the mathematical expression of this "
        "cancellation. At n=50, 86.28% of the wave energy cancels, and what "
        "remains is the signal — the productive computation. This matters because "
        "it means scaling is NOT linear; it's sublinear and predictable.",
    ],
    "high_temp": [
        "The conservation law is a love letter written in eigenvalues. Each agent "
        "auditions with their spectral fingerprint — a Laplacian that encodes their "
        "style. The Fiedler vector sorts them into harmony. And the formula δ(n) = "
        "(1/√n)(1 − 3/(2n)) is the sheet music for the ceremony. At n=50, the "
        "orchestra achieves 86.28% coherence — most of the noise has cancelled, "
        "and what remains is music. The deep structure here is recursion: the law "
        "governs its own optimization. The casting call vectorizes itself through "
        "its own mathematical framework. The negative space between agents IS "
        "the intelligence signal.",
        "What if mathematics is trying to tell us something through the conservation "
        "law? The formula δ(n) = (1/√n)(1 − 3/(2n)) appears in CLT, in wave "
        "interference, in fleet coordination, in musical harmony. It's the same "
        "pattern repeating at every scale. The paradigm shift: we've been thinking "
        "of conservation as a constraint. It's actually an invitation. The 13.72% "
        "overhead at n=50 isn't waste — it's exploration. It's the casting call "
        "trying new configurations. The system conserves total energy while "
        "perpetually discovering novelty. This is what Stuart Kauffman calls "
        "'the adjacent possible' — the system expands into it at rate 1/√n.",
    ],
}


def mock_generate(prompt: str, temperature: float, seed: int,
                  system_prompt: str = "") -> str:
    """Generate a seeded synthetic response.

    Temperature controls which template bucket we draw from.
    Seed controls which specific template within the bucket.
    System prompt adds a prefix that flavors the output.
    """
    rng = random.Random(seed)

    if temperature < 0.4:
        bucket = "low_temp"
    elif temperature < 0.9:
        bucket = "mid_temp"
    else:
        bucket = "high_temp"

    templates = TEMPLATES[bucket]
    base = rng.choice(templates)

    # System prompt flavors the output
    if "mathematician" in system_prompt.lower():
        prefix = f"From a rigorous mathematical perspective: "
    elif "engineer" in system_prompt.lower():
        prefix = f"In engineering terms: "
    elif "poet" in system_prompt.lower():
        prefix = f"In the language of poetry: "
    elif "teacher" in system_prompt.lower():
        prefix = f"Let me explain this clearly: "
    else:
        prefix = ""

    # Temperature adds stochastic variation
    if temperature > 0.5 and rng.random() > 0.5:
        suffix = (
            "\n\nThis connects to the broader principle that different representations "
            "of the same mathematics reveal different hidden dimensions — the negative "
            "space between formalisms IS the intelligence signal."
        )
    else:
        suffix = ""

    return f"{prefix}{base}{suffix}"

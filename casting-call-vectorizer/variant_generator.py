"""
Variant generator: creates different prompt/temperature/seed combinations.

Each variant is a different "audition" of the same task — like asking
the same question to a musician at different temperatures, moods, and
seeds. The casting call explores configuration space.
"""

from __future__ import annotations
import hashlib
import random
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


SYSTEM_PROMPTS = {
    "mathematician": "You are a rigorous mathematician. Value proof, precision, and elegance.",
    "engineer": "You are a practical engineer. Value working code, measurable results, and simplicity.",
    "poet": "You are a poet who sees mathematics everywhere. Value metaphor, beauty, and hidden connections.",
    "teacher": "You are a patient teacher. Value clarity, examples, and making the complex accessible.",
}


@dataclass
class Variant:
    """A single configuration variant for the casting call."""
    variant_id: str
    prompt: str
    system_prompt: str
    temperature: float
    seed: int
    top_k: int = 40
    presence_penalty: float = 0.0

    def metadata(self) -> Dict[str, Any]:
        return {
            "variant_id": self.variant_id,
            "system_prompt": self.system_prompt,
            "temperature": self.temperature,
            "seed": self.seed,
            "top_k": self.top_k,
            "presence_penalty": self.presence_penalty,
        }


def _id(prompt: str, temp: float, seed: int) -> str:
    raw = f"{prompt}:{temp}:{seed}"
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def generate_variants(
    base_prompt: str,
    prompts: Optional[List[str]] = None,
    temperatures: Optional[List[float]] = None,
    seeds: Optional[List[int]] = None,
    system_keys: Optional[List[str]] = None,
    top_ks: Optional[List[int]] = None,
) -> List[Variant]:
    """Generate all variant combinations for the casting call.

    Default: 5 prompts × 3 temps × 3 seeds = 45 variants
    """
    prompts = prompts or [
        base_prompt,
        f"Explain step by step: {base_prompt}",
        f"What are the key insights about: {base_prompt}?",
        f"Give a rigorous treatment of: {base_prompt}",
        f"What would a poet say about: {base_prompt}?",
    ]
    temperatures = temperatures or [0.2, 0.7, 1.1]
    seeds = seeds or [0, 42, 137]
    system_keys = system_keys or ["mathematician", "engineer", "poet", "teacher"]
    top_ks = top_ks or [40]

    variants: List[Variant] = []
    for prompt in prompts:
        for temp in temperatures:
            for seed in seeds:
                sys_key = system_keys[seed % len(system_keys)]
                sys_prompt = SYSTEM_PROMPTS[sys_key]
                top_k = top_ks[0]
                vid = _id(prompt, temp, seed)
                variants.append(Variant(
                    variant_id=vid,
                    prompt=prompt,
                    system_prompt=sys_prompt,
                    temperature=temp,
                    seed=seed,
                    top_k=top_k,
                ))
    return variants


def quick_variants(base_prompt: str, n: int = 5) -> List[Variant]:
    """Generate N quick variants for a demo run."""
    rng = random.Random(42)
    temps = [round(0.1 + 0.35 * i, 2) for i in range(n)]  # 0.1, 0.45, 0.8, 1.15, 1.5
    seeds = [rng.randint(0, 1000) for _ in range(n)]
    sys_keys = list(SYSTEM_PROMPTS.keys())
    prompt_variants = [
        base_prompt,
        f"Step by step: {base_prompt}",
        f"Key insights: {base_prompt}",
    ]
    variants = []
    for i in range(n):
        prompt = prompt_variants[i % len(prompt_variants)]
        sys_key = sys_keys[i % len(sys_keys)]
        variants.append(Variant(
            variant_id=_id(prompt, temps[i], seeds[i]),
            prompt=prompt,
            system_prompt=SYSTEM_PROMPTS[sys_key],
            temperature=temps[i],
            seed=seeds[i],
        ))
    return variants

"""
9-channel intent scoring for the self-vectorizing casting call.

Channels: Boundary, Pattern, Process, Knowledge, Social,
          DeepStructure, Instrument, Paradigm, Stakes
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, List, Optional


class Channel(IntEnum):
    BOUNDARY = 1       # C1: Does it define clear scope?
    PATTERN = 2        # C2: Does it connect ideas structurally?
    PROCESS = 3        # C3: Does it show temporal flow?
    KNOWLEDGE = 4      # C4: Is it factually rigorous?
    SOCIAL = 5         # C5: Does it serve its audience?
    DEEP_STRUCTURE = 6 # C6: Is there hidden meaning?
    INSTRUMENT = 7     # C7: Does it build something useful?
    PARADIGM = 8       # C8: Does it shift perspective?
    STAKES = 9         # C9: Does it matter?


CHANNEL_NAMES = {
    Channel.BOUNDARY: "Boundary",
    Channel.PATTERN: "Pattern",
    Channel.PROCESS: "Process",
    Channel.KNOWLEDGE: "Knowledge",
    Channel.SOCIAL: "Social",
    Channel.DEEP_STRUCTURE: "DeepStruct",
    Channel.INSTRUMENT: "Instrument",
    Channel.PARADIGM: "Paradigm",
    Channel.STAKES: "Stakes",
}


@dataclass
class IntentProfile:
    """A 9-dimensional intent vector with tolerances."""
    channels: Dict[Channel, float] = field(default_factory=dict)
    tolerances: Dict[Channel, float] = field(default_factory=dict)

    def __post_init__(self):
        for ch in Channel:
            self.channels.setdefault(ch, 0.0)
            self.tolerances.setdefault(ch, 0.3)

    def vector(self) -> List[float]:
        return [self.channels[Channel(i)] for i in range(1, 10)]

    def set_channel(self, ch: Channel, salience: float, tolerance: float = 0.3):
        self.channels[ch] = max(0.0, min(1.0, salience))
        self.tolerances[ch] = max(0.01, min(1.0, tolerance))


def _count_keywords(text: str, keywords: List[str]) -> int:
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw in text_lower)


def score_boundary(output: str) -> float:
    """Scope definition: explicit boundaries, well-scoped."""
    markers = ["scope", "boundary", "limit", "constraint", "within", "only",
               "excludes", "boundary condition", "domain"]
    count = _count_keywords(output, markers)
    length_factor = min(len(output) / 500, 1.0)
    return min(count / 5.0 * 0.7 + length_factor * 0.3, 1.0)


def score_pattern(output: str) -> float:
    """Structural connections: analogies, cross-references."""
    markers = ["like", "similar", "analog", "parallel", "maps to", "corresponds",
               "mirror", "reflect", "isomorphic", "homomorphic", "pattern"]
    count = _count_keywords(output, markers)
    return min(count / 4.0, 1.0)


def score_process(output: str) -> float:
    """Temporal flow: step-by-step reasoning, causality."""
    markers = ["step", "first", "then", "next", "after", "before", "because",
               "therefore", "leads to", "causes", "evolves", "flow", "sequence"]
    count = _count_keywords(output, markers)
    return min(count / 5.0, 1.0)


def score_knowledge(output: str) -> float:
    """Factual rigor: correct claims, citations."""
    markers = ["theorem", "proven", "verified", "tested", "measured", "data",
               "result", "experiment", "according", "reference", "citation"]
    count = _count_keywords(output, markers)
    code_penalty = 0.0
    if "```" in output:
        code_penalty = 0.1  # code blocks boost credibility
    return min(count / 4.0 + code_penalty, 1.0)


def score_social(output: str) -> float:
    """Audience awareness: tone, addressing reader."""
    markers = ["you", "your", "we", "us", "let's", "consider", "imagine",
               "think of", "user", "reader", "audience", "people"]
    count = _count_keywords(output, markers)
    return min(count / 6.0, 1.0)


def score_deep_structure(output: str) -> float:
    """Hidden depth: metaphors, multiple levels."""
    markers = ["beneath", "underlying", "hidden", "implicit", "negative space",
               "shadow", "silence", "between", "unspoken", "structure within",
               "recursion", "meta", "self-referential"]
    count = _count_keywords(output, markers)
    return min(count / 3.0, 1.0)


def score_instrument(output: str) -> float:
    """Actionability: working code, tools, steps."""
    has_code = "```" in output or "def " in output or "fn " in output
    markers = ["build", "implement", "deploy", "install", "run", "code",
               "function", "test", "execute", "create"]
    count = _count_keywords(output, markers)
    return min(count / 4.0 + (0.3 if has_code else 0.0), 1.0)


def score_paradigm(output: str) -> float:
    """Perspective shift: reframes, new mental model."""
    markers = ["instead", "rather than", "rethink", "reframe", "what if",
               "surprisingly", "counterintuitive", "unlike", "opposite",
               "inverts", "reverses", "paradox"]
    count = _count_keywords(output, markers)
    return min(count / 3.0, 1.0)


def score_stakes(output: str) -> float:
    """Significance: real consequences, important problems."""
    markers = ["important", "critical", "essential", "matters", "consequence",
               "impact", "real-world", "production", "cost", "safety",
               "failure", "success", "survival"]
    count = _count_keywords(output, markers)
    return min(count / 4.0, 1.0)


def score_output(output: str) -> IntentProfile:
    """Score an output string on all 9 channels."""
    profile = IntentProfile()
    profile.set_channel(Channel.BOUNDARY, score_boundary(output))
    profile.set_channel(Channel.PATTERN, score_pattern(output))
    profile.set_channel(Channel.PROCESS, score_process(output))
    profile.set_channel(Channel.KNOWLEDGE, score_knowledge(output))
    profile.set_channel(Channel.SOCIAL, score_social(output))
    profile.set_channel(Channel.DEEP_STRUCTURE, score_deep_structure(output))
    profile.set_channel(Channel.INSTRUMENT, score_instrument(output))
    profile.set_channel(Channel.PARADIGM, score_paradigm(output))
    profile.set_channel(Channel.STAKES, score_stakes(output))
    return profile


def alignment_score(task: IntentProfile, output: IntentProfile) -> float:
    """Cosine similarity in 9D intent space."""
    import math
    t = task.vector()
    o = output.vector()
    dot = sum(a * b for a, b in zip(t, o))
    norm_t = math.sqrt(sum(a * a for a in t))
    norm_o = math.sqrt(sum(b * b for b in o))
    return dot / (norm_t * norm_o + 1e-12)

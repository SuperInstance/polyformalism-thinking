"""
Results store: persists scored variants in a simple JSON store.
Learns which configurations produce the best outputs for which intent profiles.
"""

from __future__ import annotations
import json
import os
import time
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
from scoring import IntentProfile, Channel, alignment_score


@dataclass
class ScoredResult:
    """A complete scored output from the casting call."""
    variant_id: str
    output: str
    scores: Dict[str, float]  # channel name → score
    alignment: float
    config: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return asdict(self)


class ResultsStore:
    """JSON-backed results store with learning queries."""

    def __init__(self, path: str = "casting_call_results.json"):
        self._path = path
        self._results: List[ScoredResult] = []
        self._load()

    def _load(self):
        if os.path.exists(self._path):
            with open(self._path) as f:
                data = json.load(f)
            self._results = [ScoredResult(**r) for r in data.get("results", [])]

    def save(self):
        os.makedirs(os.path.dirname(self._path) or ".", exist_ok=True)
        with open(self._path, "w") as f:
            json.dump({"results": [r.to_dict() for r in self._results]}, f, indent=2)

    def add(self, result: ScoredResult):
        self._results.append(result)
        self.save()

    def all(self) -> List[ScoredResult]:
        return list(self._results)

    def best_for_channel(self, channel: Channel, n: int = 5) -> List[ScoredResult]:
        """Return top-N results for a specific channel."""
        ch_name = channel.name
        return sorted(self._results,
                      key=lambda r: r.scores.get(ch_name, 0),
                      reverse=True)[:n]

    def best_alignment(self, n: int = 5) -> List[ScoredResult]:
        """Return top-N results by alignment score."""
        return sorted(self._results, key=lambda r: r.alignment, reverse=True)[:n]

    def best_config_for_intent(self, intent: IntentProfile, n: int = 3) -> List[Dict[str, Any]]:
        """Given an intent profile, return the best historical configurations."""
        scored = []
        for result in self._results:
            result_intent = IntentProfile()
            for ch_name, val in result.scores.items():
                try:
                    ch = Channel[ch_name]
                    result_intent.set_channel(ch, val)
                except (KeyError, ValueError):
                    pass
            align = alignment_score(intent, result_intent)
            scored.append((align, result.config))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [cfg for _, cfg in scored[:n]]

    def summary(self) -> Dict[str, Any]:
        """Summary statistics."""
        if not self._results:
            return {"total": 0}
        channel_avgs = {}
        for ch in Channel:
            ch_name = ch.name
            vals = [r.scores.get(ch_name, 0) for r in self._results]
            channel_avgs[ch_name] = round(sum(vals) / len(vals), 4) if vals else 0
        return {
            "total": len(self._results),
            "avg_alignment": round(sum(r.alignment for r in self._results) / len(self._results), 4),
            "channel_averages": channel_avgs,
            "best_alignment": max(r.alignment for r in self._results),
        }

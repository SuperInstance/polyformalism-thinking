"""
Casting Call Vectorizer — main orchestration loop.

This system implements the casting call as a self-improving process:
1. Take a task (prompt + intent profile)
2. Generate N variants (different temperatures, seeds, system prompts)
3. Run each variant through a model (real or mock)
4. Score each output on 9 channels
5. Store results in a vector-aware database
6. Learn which configurations work best for which intents

Run the demo: python -m casting_call_vectorizer.vectorizer
"""

from __future__ import annotations
import time
from typing import Optional

from scoring import (
    IntentProfile, Channel, score_output, alignment_score, CHANNEL_NAMES,
)
from variant_generator import Variant, quick_variants
from mock_backend import mock_generate
from results_store import ResultsStore, ScoredResult


class CastingCallVectorizer:
    """The main casting call loop."""

    def __init__(self, store_path: str = "casting_call_results.json"):
        self.store = ResultsStore(store_path)

    def run_task(
        self,
        prompt: str,
        intent: Optional[IntentProfile] = None,
        n_variants: int = 5,
        verbose: bool = True,
    ) -> list[ScoredResult]:
        """Run the casting call for a single task.

        Args:
            prompt: The task prompt
            intent: Desired intent profile (default: balanced across channels)
            n_variants: Number of variants to generate
            verbose: Print progress
        """
        if intent is None:
            intent = IntentProfile()
            for ch in Channel:
                intent.set_channel(ch, 0.5)

        if verbose:
            print(f"\n{'='*60}")
            print(f"  CASTING CALL: {prompt[:60]}...")
            print(f"  Variants: {n_variants}")
            print(f"  Intent: {self._intent_summary(intent)}")
            print(f"{'='*60}\n")

        variants = quick_variants(prompt, n=n_variants)
        results = []

        for i, variant in enumerate(variants):
            if verbose:
                print(f"  Variant {i+1}/{n_variants}: temp={variant.temperature} "
                      f"seed={variant.seed} sys={variant.system_prompt[:30]}...")

            # Generate output (mock for demo, real model in production)
            output = mock_generate(
                prompt=variant.prompt,
                temperature=variant.temperature,
                seed=variant.seed,
                system_prompt=variant.system_prompt,
            )

            # Score on 9 channels
            output_profile = score_output(output)

            # Compute alignment with desired intent
            align = alignment_score(intent, output_profile)

            # Build result
            result = ScoredResult(
                variant_id=variant.variant_id,
                output=output[:500],  # truncate for storage
                scores={CHANNEL_NAMES[ch]: output_profile.channels[ch]
                        for ch in Channel},
                alignment=align,
                config=variant.metadata(),
            )
            self.store.add(result)
            results.append(result)

            if verbose:
                top_ch = max(output_profile.channels, key=output_profile.channels.get)
                top_name = CHANNEL_NAMES[top_ch]
                top_val = output_profile.channels[top_ch]
                print(f"    → Top channel: {top_name} ({top_val:.2f}) "
                      f"| Alignment: {align:.4f}\n")

        if verbose:
            self._print_summary(results)

        return results

    def _intent_summary(self, intent: IntentProfile) -> str:
        top = sorted(intent.channels.items(), key=lambda x: x[1], reverse=True)[:3]
        return ", ".join(f"{CHANNEL_NAMES[ch]}={v:.1f}" for ch, v in top)

    def _print_summary(self, results: list[ScoredResult]):
        print(f"\n{'─'*60}")
        print(f"  SUMMARY: {len(results)} variants scored")
        best = max(results, key=lambda r: r.alignment)
        worst = min(results, key=lambda r: r.alignment)
        print(f"  Best:  variant={best.variant_id} align={best.alignment:.4f} "
              f"(temp={best.config.get('temperature')})")
        print(f"  Worst: variant={worst.variant_id} align={worst.alignment:.4f} "
              f"(temp={worst.config.get('temperature')})")

        # Channel averages
        ch_avgs = {}
        for ch_name in results[0].scores:
            vals = [r.scores.get(ch_name, 0) for r in results]
            ch_avgs[ch_name] = sum(vals) / len(vals)
        top3 = sorted(ch_avgs.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"  Strongest channels: {', '.join(f'{n}={v:.2f}' for n, v in top3)}")
        print(f"{'─'*60}\n")

    def learn(self, intent: IntentProfile, n: int = 3):
        """Query historical results for best configurations."""
        return self.store.best_config_for_intent(intent, n=n)


def demo():
    """Run a 5-variant demo of the casting call."""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   CASTING CALL VECTORIZER — Self-Improving Demo          ║")
    print("║   Every input scored. Every output measured.             ║")
    print("╚══════════════════════════════════════════════════════════╝")

    vectorizer = CastingCallVectorizer()

    # Define a task with specific intent emphasis
    task_prompt = "Explain the conservation law γ + η = C and its significance"

    intent = IntentProfile()
    intent.set_channel(Channel.PATTERN, 0.8, tolerance=0.1)
    intent.set_channel(Channel.DEEP_STRUCTURE, 0.7, tolerance=0.2)
    intent.set_channel(Channel.STAKES, 0.6, tolerance=0.2)
    intent.set_channel(Channel.PARADIGM, 0.7, tolerance=0.15)

    results = vectorizer.run_task(task_prompt, intent, n_variants=5, verbose=True)

    # Show what we learned
    print("\n📚 LEARNED CONFIGURATIONS for Pattern-heavy, Paradigm-shifting tasks:")
    learned = vectorizer.learn(intent, n=3)
    for i, cfg in enumerate(learned):
        print(f"  {i+1}. temp={cfg.get('temperature')} seed={cfg.get('seed')} "
              f"sys={cfg.get('system_prompt', '')[:40]}...")

    # Store summary
    summary = vectorizer.store.summary()
    print(f"\n📊 STORE SUMMARY: {summary['total']} results, "
          f"avg alignment {summary.get('avg_alignment', 0):.4f}")

    print("\n✅ Demo complete. The casting call vectorizes itself one iteration at a time.")
    print("   Each run adds scored results to the store, building a knowledge base")
    print("   of which configurations produce the best outputs for which intents.\n")


if __name__ == "__main__":
    demo()

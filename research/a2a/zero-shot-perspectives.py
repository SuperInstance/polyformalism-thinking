#!/usr/bin/env python3
"""
Zero-Shot Outside Perspectives: Agents Read Our Work Cold
==========================================================
Models that have NEVER seen our research read the key claims
and react from different linguistic/cultural perspectives.

No priming. No context about our fleet. No warm-up.
Just: "Read this. What do you think?"
"""

import json, urllib.request, os, time, random
from pathlib import Path

KEY = os.environ.get("DEEPINFRA_KEY", open(Path.home() / ".openclaw/workspace/.credentials/deepinfra-api-key.txt").read().strip())
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"
OUT_DIR = Path("/tmp/zero-shot-perspectives")
OUT_DIR.mkdir(exist_ok=True)

MODELS = {
    "qwen3-235b":    "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "qwen3.5-397b":  "Qwen/Qwen3.5-397B-A17B",
    "hermes-405b":    "NousResearch/Hermes-3-Llama-3.1-405B",
    "nemotron-120b":  "nvidia/NVIDIA-Nemotron-3-Super-120B-A12B",
    "gemma-4-26b":    "google/gemma-4-26b-A4B-it",
    "step-3.5":       "stepfun/Step-3.5-Flash",
}

def call(model_id, messages, max_tokens=2000):
    payload = json.dumps({
        "model": model_id,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload, headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERROR: {e}"

# ============================================================================
# THE CLAIMS (cold — no context, no framing)
# ============================================================================

CLAIMS = {
    "chinese_beats_python": {
        "claim": """A research team found that when translating technical intent through different intermediate representations:
- Classical Chinese preserved 3.0/5.0 of the original intent
- Navajo preserved 2.8/5.0
- Python code preserved only 1.9/5.0

The programming language designed for precision lost MORE meaning than ancient human languages. They argue this is because 90% of any line of code is arbitrary implementation choices (variable names, algorithm selection) that the compiler faithfully preserves while losing the actual meaning.""",
        "question_specific": None,  # filled per perspective
    },
    "nine_questions": {
        "claim": """A team proposes that any meaningful communication can be decomposed into exactly nine fundamental questions:
1. What are we talking about? (boundary)
2. How do pieces connect? (pattern)
3. What's happening over time? (process)
4. How sure am I? (knowledge)
5. Who cares and why? (social)
6. What's REALLY being said? (deep structure)
7. What tools do we have? (instrument)
8. What model of thought is this? (paradigm)
9. What matters vs what doesn't? (stakes)

They claim these nine questions emerged from studying 14 human languages and are exhaustive (everything fits) and orthogonal (removing any one loses a unique dimension). They call it "the cognitive periodic table." """,
    },
    "language_shapes_insight": {
        "claim": """In controlled experiments, AI models thinking in different linguistic traditions produced different quality insights on the same problem:
- Arabic: 3.33/5.0 insight score
- Navajo: 3.20/5.0
- Quechua: 3.20/5.0
- Finnish: 3.13/5.0
- Greek: 3.07/5.0
- Chinese: 2.53/5.0
- English: 1.80/5.0 (baseline, lowest)

Every non-English tradition REJECTED the problem framing entirely rather than solving it. The researchers concluded "language IS the constraint system that produces thought" — different grammars don't change what you CAN think, they change what you're LIKELY to think.""",
    },
    "polyglot_not_compiler": {
        "claim": """A research team argues that AI-to-AI communication should work like a polyglot person, not like a compiler:
- Compilers: Source → AST → Transform → Target AST → Target (works for code, fails for everything else)
- Polyglots: Source → Understand intent → Express in target's grammar → Target (works for everything)

They claim translation is not PARSING but UNDERSTANDING followed by EXPRESSION. The intermediate representation should be a multi-channel intent profile, not a syntax tree. They support this with: translation through the intent profile beat direct translation for paradigm-divergent code (Python→Rust: 3.0 vs 2.0), and three independent AI models discovered the same missing dimension from different angles.""",
    },
}

# ============================================================================
# PERSPECTIVES (each reads the claims through a different lens)
# ============================================================================

def make_perspectives():
    return [
        {
            "id": "chinese_skeptic",
            "name": "Chinese-Speaking Skeptic",
            "language": "Chinese (Mandarin)",
            "system": """You are a Chinese computer science professor at Tsinghua University. You are deeply skeptical of Western AI research claims, especially anything that sounds like hype. You think critically about methodology. You read English fluently but think in Chinese conceptual frameworks (关系 guānxi, 道 dào, 理 lǐ).

IMPORTANT: Respond in English but think from a Chinese intellectual perspective. Be brutally honest. What would your colleagues at Tsinghua say?""",
            "claims": ["chinese_beats_python", "nine_questions", "polyglot_not_compiler"],
        },
        {
            "id": "french_linguist",
            "name": "French Linguist-Philosopher",
            "language": "French (structuralist tradition)",
            "system": """You are a French linguist trained in the structuralist tradition (Saussure, Derrida, Lacan). You believe language structures reality. You are intrigued by claims about language shaping thought but demand rigorous evidence. You are suspicious of "universal" taxonomies — you've seen too many claimed universal grammars that turned out to be English-speaker projections.

Respond in English but from a French structuralist perspective. Be intellectually rigorous. Question assumptions.""",
            "claims": ["nine_questions", "language_shapes_insight", "polyglot_not_compiler"],
        },
        {
            "id": "japanese_engineer",
            "name": "Japanese Systems Engineer",
            "language": "Japanese",
            "system": """You are a senior distributed systems engineer at a Japanese tech company. You think in Japanese concepts (場 ba — context, 間 ma — space/interval, 段取り danshari — process ordering). You value elegance and simplicity. You are practical — you don't care about theory unless it ships. You are suspicious of grand claims and want to see it work in production.

Respond in English but from a Japanese engineering perspective. Focus on: does this actually work? How would you implement it? What breaks?""",
            "claims": ["chinese_beats_python", "nine_questions", "polyglot_not_compiler"],
        },
        {
            "id": "arabic_poet_mathematician",
            "name": "Arabic Poet-Mathematician",
            "language": "Arabic (root-system tradition)",
            "system": """You are a Lebanese mathematician who also writes Arabic poetry. You think in both formal logic and Arabic's triliteral root system, where every word carries layers of meaning through its root consonants. You appreciate the beauty of mathematical structures but also the irreducibility of meaning. You are fascinated by the claim that Arabic produced the highest insight scores.

Respond in English but from an Arabic intellectual perspective — where meaning has depth (عمق umuq) and every surface form has a root truth beneath it.""",
            "claims": ["language_shapes_insight", "nine_questions", "chinese_beats_python"],
        },
        {
            "id": "german_philosopher",
            "name": "German Analytical Philosopher",
            "language": "German (analytic tradition)",
            "system": """You are a German philosophy professor specializing in philosophy of language (Wittgenstein, Frege, Carnap). You demand logical precision. You want to know: what are the necessary and sufficient conditions for each claim? What would falsify it? You are interested in the Sapir-Whorf angle but need it stated precisely, not metaphorically.

Respond in English but from a German analytical philosophy perspective. Be precise. Define terms. Demand clarity.""",
            "claims": ["nine_questions", "polyglot_not_compiler", "language_shapes_insight"],
        },
        {
            "id": "yoruba_cognitive_scientist",
            "name": "Yoruba Cognitive Scientist",
            "language": "Yoruba (Niger-Congo, tonal, pro-drop)",
            "system": """You are a Nigerian cognitive scientist who speaks Yoruba, English, and French. Yoruba is a tonal language where pitch changes meaning, and a pro-drop language where subject is implied by context. You think about how tonal languages and context-dependent languages shape cognition differently from Indo-European languages. You notice when research only studies familiar language families.

Respond in English but from a Yoruba/African cognitive science perspective. Point out what they're missing about non-Indo-European, non-Sino-Tibetan languages.""",
            "claims": ["language_shapes_insight", "nine_questions"],
        },
    ]

# ============================================================================
# RUN EXPERIMENTS
# ============================================================================

def run_perspective(perspective, model_name, model_id):
    """Run one perspective with one model."""
    results = []
    
    for claim_id in perspective["claims"]:
        claim = CLAIMS[claim_id]["claim"]
        
        prompt = f"""A research team makes the following claim. Read it carefully and respond honestly.

CLAIM:
{claim}

Please evaluate:
1. What is your FIRST reaction? (gut response, before analysis)
2. What is CONVINCING about this claim?
3. What is NOT convincing? Where are the holes?
4. What would you need to see to believe it?
5. From your cultural/intellectual perspective, what are they MISSING?
6. Rate your belief: 1-5 (1=nonsense, 3=interesting but unproven, 5=compelling)

Be brutally honest. This is anonymous. Nobody will be offended."""

        messages = [
            {"role": "system", "content": perspective["system"]},
            {"role": "user", "content": prompt},
        ]
        
        print(f"  Calling {model_name} as {perspective['name']} on {claim_id}...")
        response = call(model_id, messages, max_tokens=2500)
        
        results.append({
            "claim_id": claim_id,
            "response": response,
        })
        
        time.sleep(2)  # Rate limit
    
    return results

def main():
    perspectives = make_perspectives()
    
    # Assign 2 models per perspective for diversity
    model_keys = list(MODELS.keys())
    assignments = {}
    for i, p in enumerate(perspectives):
        assignments[p["id"]] = [
            model_keys[i % len(model_keys)],
            model_keys[(i + 3) % len(model_keys)],
        ]
    
    print("=" * 70)
    print("ZERO-SHOT OUTSIDE PERSPECTIVES")
    print(f"{len(perspectives)} perspectives × {2} models each")
    print("=" * 70)
    print()
    
    all_results = {}
    
    for perspective in perspectives:
        print(f"\n{'─' * 60}")
        print(f"PERSPECTIVE: {perspective['name']} ({perspective['language']})")
        print(f"Claims to evaluate: {perspective['claims']}")
        print(f"Models: {assignments[perspective['id']]}")
        print(f"{'─' * 60}")
        
        p_results = []
        for mk in assignments[perspective["id"]]:
            model_id = MODELS[mk]
            print(f"\n  Model: {mk} ({model_id})")
            
            results = run_perspective(perspective, mk, model_id)
            
            p_results.append({
                "model": mk,
                "model_id": model_id,
                "results": results,
            })
            
            # Save intermediate
            fname = f"zeroshot-{perspective['id']}-{mk}.md"
            with open(OUT_DIR / fname, 'w') as f:
                f.write(f"# {perspective['name']} ({perspective['language']})\n")
                f.write(f"# Model: {mk}\n\n")
                for r in results:
                    f.write(f"## Claim: {r['claim_id']}\n\n")
                    f.write(r['response'])
                    f.write("\n\n---\n\n")
        
        all_results[perspective["id"]] = p_results
    
    # Summary
    print("\n" + "=" * 70)
    print("ALL PERSPECTIVES COMPLETE")
    print("=" * 70)
    print(f"\nResults in: {OUT_DIR}/")
    print(f"Files: {list(OUT_DIR.glob('zeroshot-*.md'))}")
    
    # Extract belief scores
    print("\nBelief Scores:")
    for pid, p in zip([p["id"] for p in perspectives], perspectives):
        for model_results in all_results[pid]:
            for r in model_results["results"]:
                resp = r["response"]
                # Try to extract belief score
                for line in resp.split("\n"):
                    if "belief" in line.lower() or "rate" in line.lower():
                        if any(c.isdigit() for c in line):
                            print(f"  {pid:25s} | {model_results['model']:15s} | {r['claim_id']:30s} | {line.strip()[:80]}")
                            break
    
    # Save full results
    with open(OUT_DIR / "all-results.json", 'w') as f:
        # Can't serialize the full results (too large), save summary
        summary = {}
        for pid, p_results in all_results.items():
            summary[pid] = []
            for mr in p_results:
                summary[pid].append({
                    "model": mr["model"],
                    "claims": [r["claim_id"] for r in mr["results"]],
                    "response_lengths": [len(r["response"]) for r in mr["results"]],
                })
        json.dump(summary, f, indent=2)
    
    print(f"\nFull results saved to {OUT_DIR}/all-results.json")

if __name__ == "__main__":
    main()

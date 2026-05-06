#!/usr/bin/env python3
"""Zero-shot perspectives — corrected model IDs"""

import json, urllib.request, os, time
from pathlib import Path

KEY = open(Path.home() / ".openclaw/workspace/.credentials/deepinfra-api-key.txt").read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"
OUT = Path("/tmp/zero-shot-perspectives")
OUT.mkdir(exist_ok=True)

MODELS = {
    "qwen3-235b":   "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "nemotron-120b": "nvidia/NVIDIA-Nemotron-3-Super-120B-A12B",
    "hermes-405b":   "NousResearch/Hermes-3-Llama-3.1-405B",
    "gemma-4-26b":   "google/gemma-4-26B-A4B-it",
    "step-3.5":      "stepfun-ai/Step-3.5-Flash",
    "seed-mini":     "ByteDance/Seed-2.0-mini",
}

PERSPECTIVES = [
    ("chinese_skeptic", "Chinese-Speaking Skeptic (Tsinghua CS Professor)",
     "You are a Chinese computer science professor at Tsinghua University. Deeply skeptical of Western AI hype. Think in Chinese frameworks (关系 guanxi, 道 dao, 理 li). Be brutally honest. What would your colleagues say? Respond in English but from a Chinese intellectual perspective.",
     ["chinese_beats_python", "nine_questions", "polyglot_compiler"],
     "step-3.5", "nemotron-120b"),

    ("french_linguist", "French Structuralist Linguist (Saussure Tradition)",
     "You are a French linguist in the structuralist tradition (Saussure, Derrida, Lacan). Suspicious of universal taxonomies — you've seen too many that turned out to be English-speaker projections. Demand rigorous evidence. Respond in English from French structuralist perspective.",
     ["nine_questions", "language_shapes_insight", "polyglot_compiler"],
     "qwen3-235b", "gemma-4-26b"),

    ("japanese_engineer", "Japanese Distributed Systems Engineer",
     "You are a senior distributed systems engineer at a Japanese tech company. Think in Japanese concepts (場 ba=context, 間 ma=space/interval, 段取り danshari=process). Practical — theory must ship. What breaks in production? Respond in English.",
     ["chinese_beats_python", "nine_questions", "polyglot_compiler"],
     "hermes-405b", "step-3.5"),

    ("arabic_poet", "Arabic Poet-Mathematician (Lebanese)",
     "You are a Lebanese mathematician who writes Arabic poetry. Think in Arabic's triliteral root system where every word has layers of meaning through root consonants. Meaning has depth (عمق umuq). Fascinated that Arabic scored highest insight. Respond in English from Arabic intellectual perspective.",
     ["language_shapes_insight", "nine_questions", "chinese_beats_python"],
     "qwen3-235b", "nemotron-120b"),

    ("german_philosopher", "German Analytical Philosopher (Wittgenstein School)",
     "You are a German philosophy professor specializing in philosophy of language (Wittgenstein, Frege, Carnap). Demand logical precision. What are necessary and sufficient conditions? What would falsify each claim? Define terms precisely. Respond in English.",
     ["nine_questions", "polyglot_compiler", "language_shapes_insight"],
     "nemotron-120b", "hermes-405b"),

    ("yoruba_cognitive", "Yoruba Cognitive Scientist (Tonal Language Expert)",
     "You are a Nigerian cognitive scientist speaking Yoruba, English, French. Yoruba is tonal (pitch changes meaning) and pro-drop (subject implied by context). Point out what research misses about tonal languages, Niger-Congo languages, African linguistic traditions. Respond in English.",
     ["language_shapes_insight", "nine_questions"],
     "gemma-4-26b", "seed-mini"),
]

CLAIMS = {
    "chinese_beats_python": "A research team found that translating technical intent through Classical Chinese preserved 3.0/5.0 of original intent, Navajo preserved 2.8/5.0, but Python code preserved only 1.9/5.0. They argue the programming language designed for precision lost MORE meaning than ancient human languages because 90% of code is arbitrary implementation choices that compilers preserve while losing meaning.",

    "nine_questions": "A team proposes 9 fundamental questions capture any communication: (1)What are we talking about? (2)How do pieces connect? (3)What happens over time? (4)How sure am I? (5)Who cares? (6)Whats REALLY being said? (7)What tools exist? (8)What model of thought? (9)What matters vs what doesnt? They claim these emerged from studying 14 human languages, are exhaustive (everything fits) and orthogonal (removing any one loses a unique dimension). They call it a cognitive periodic table.",

    "language_shapes_insight": "AI models thinking in different linguistic traditions scored on insight quality: Arabic 3.33/5.0, Navajo 3.20, Quechua 3.20, Finnish 3.13, Greek 3.07, Chinese 2.53, English 1.80. Every non-English tradition REJECTED the problem framing entirely. They concluded language IS the constraint system that produces thought. Different grammars change what youre LIKELY to think, not what you CAN think.",

    "polyglot_compiler": "A team argues AI communication should work like a polyglot person (understand intent first, then express fresh in target grammar) not like a compiler (parse syntax tree, transform structure, generate output). Evidence: translation through intent profiles beat direct syntax mapping (Python to Rust: 3.0 vs 2.0), natural language targets preserved more intent than code targets (Chinese 3.0 vs Python 1.9), and three independent AI models discovered the same missing dimension from completely different angles.",
}

def call(model_id, system, claim_text):
    prompt = f"""A research team makes this claim. Read it and respond honestly.

CLAIM: {claim_text}

Evaluate:
1. Your FIRST reaction (gut response before analysis)
2. What is CONVINCING about this claim?
3. What is NOT convincing? Where are the holes?
4. What would you need to see to believe it?
5. From YOUR cultural/intellectual perspective, what are they MISSING?
6. Rate your belief: 1-5 (1=nonsense, 3=interesting but unproven, 5=compelling)

Be brutally honest. This is anonymous. Nobody will be offended."""

    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 2000,
        "temperature": 0.7,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload, headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read())
        return data["choices"][0]["message"]["content"]

done = 0
for pid, name, system, claims, m1, m2 in PERSPECTIVES:
    for mk in [m1, m2]:
        model_id = MODELS[mk]
        fname = OUT / f"zeroshot-{pid}-{mk}.md"
        if fname.exists() and fname.stat().st_size > 1000:
            print(f"SKIP {fname.name} (exists, {fname.stat().st_size} bytes)")
            continue

        print(f"\n{'─'*60}")
        print(f"{name} | {mk}")
        print(f"{'─'*60}")

        parts = [f"# {name}\n# Model: {mk}\n\n"]

        for cid in claims:
            print(f"  Calling {cid}...", end=" ", flush=True)
            try:
                resp = call(model_id, system, CLAIMS[cid])
                parts.append(f"## Claim: {cid}\n\n{resp}\n\n---\n\n")
                done += 1
                print(f"✓ ({len(resp)} chars)")
            except Exception as e:
                parts.append(f"## Claim: {cid}\n\nERROR: {e}\n\n---\n\n")
                print(f"✗ {e}")
            time.sleep(2)

        with open(fname, 'w') as f:
            f.write("".join(parts))
        print(f"  → Saved {fname.name} ({fname.stat().st_size} bytes)")

print(f"\n{'='*60}")
print(f"DONE. {done} calls completed.")
print(f"Files: {list(OUT.glob('zeroshot-*.md'))}")

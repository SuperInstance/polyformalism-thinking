#!/usr/bin/env python3
"""
Wide Parallel Polyglot Deep Dive — 12 models × 3 tasks

Models assigned to roles matching their strengths:
- Creative/imaginative models → reverse actualization, devil's advocate
- Logical/reasoning models → formal analysis, critique
- Balanced models → synthesis, encoding

Tasks:
1. Reverse-actualization: "If A2A polyglot model is already ubiquitous in 2031, how did it get there?"
2. Devil's advocate: "Destroy the polyglot model. Find its fatal flaw."
3. Novel insight: "What is the polyglot model missing that no one has noticed?"
"""
import subprocess, json, os, time, re, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
DEEPSEEK_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepseek-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"
DEEPSEEK_EP = "https://api.deepseek.com/v1/chat/completions"

# Model assignments by personality
MODELS = {
    # === CREATIVE / IMAGINATIVE — for reverse actualization ===
    "Gryphe/MythoMax-L2-13b": {
        "role": "mythmaker",
        "strength": "Narrative imagination, mythological thinking, storytelling",
        "task": "reverse_actualization",
        "why": "Roleplay and creative fiction specialist — sees patterns in stories"
    },
    "Sao10K/L3.1-70B-Euryale-v2.2": {
        "role": "provocateur",
        "strength": "Unconventional perspectives, lateral thinking, challenging assumptions",
        "task": "reverse_actualization",
        "why": "Euryale trained for creative/bold outputs — perfect for provocative futures"
    },
    "Qwen/Qwen3.5-397B-A17B": {
        "role": "synthesizer",
        "strength": "Large-scale pattern recognition, multilingual synthesis",
        "task": "novel_insight",
        "why": "Largest MoE — sees patterns across vast parameter space"
    },
    
    # === LOGICAL / REASONING — for devil's advocate ===
    "deepseek-ai/DeepSeek-R1-0528-Turbo": {
        "role": "logician",
        "strength": "Deep chain-of-thought reasoning, mathematical proof",
        "task": "devils_advocate",
        "why": "R1 reasoning model — will find logical flaws others miss"
    },
    "nvidia/NVIDIA-Nemotron-3-Super-120B-A12B": {
        "role": "engineer",
        "strength": "Technical precision, systems thinking, production reasoning",
        "task": "devils_advocate",
        "why": "Nemotron trained for accuracy and instruction following"
    },
    "Qwen/Qwen3-Coder-480B-A35B-Instruct-Turbo": {
        "role": "architect",
        "strength": "Code architecture, system design, implementation reasoning",
        "task": "devils_advocate", 
        "why": "Coder model will attack from implementation perspective"
    },
    
    # === BALANCED — for novel insights ===
    "stepfun-ai/Step-3.5-Flash": {
        "role": "connector",
        "strength": "Fast, broad knowledge, cross-domain connections",
        "task": "novel_insight",
        "why": "New model — fresh training data, different perspective"
    },
    "google/gemma-4-26B-A4B-it": {
        "role": "generalist",
        "strength": "Well-rounded reasoning, Google's training philosophy",
        "task": "novel_insight",
        "why": "Gemma 4 is new — different architecture, different biases"
    },
    "ByteDance/Seed-2.0-pro": {
        "role": "analyst",
        "strength": "Deep analysis, structured thinking",
        "task": "novel_insight",
        "why": "Our workhorse — proven on this specific domain"
    },
    
    # === ADDITIONAL PERSPECTIVES ===
    "NousResearch/Hermes-3-Llama-3.1-405B": {
        "role": "philosopher",
        "strength": "Nuanced reasoning, ethical considerations, systems thinking",
        "task": "novel_insight",
        "why": "405B params with instruction tuning — deep philosophical capacity"
    },
    "Qwen/Qwen3-235B-A22B-Thinking-2507": {
        "role": "thinker",
        "strength": "Extended chain-of-thought, self-correction",
        "task": "devils_advocate",
        "why": "Thinking model — will catch its own mistakes and find real flaws"
    },
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8": {
        "role": "pragmatist",
        "strength": "Practical engineering, real-world constraints",
        "task": "reverse_actualization",
        "why": "Llama 4 MoE — efficient, practical perspective"
    },
}

PROMPTS = {
    "reverse_actualization": """You are writing from the year 2031. The A2A polyglot model — where agents communicate through 8-channel intent profiles (Boundary, Pattern, Process, Knowledge, Social, Deep Structure, Instrument, Paradigm) instead of syntax trees — is now ubiquitous. Every agent, every API, every sensor speaks through this layer.

Your role: {role} ({strength})

Write a FIRST-PERSON account of ONE critical moment in the journey from 2026 to 2031 where the polyglot model succeeded OR failed in a way no one predicted.

Be specific. Name the domain. Describe the channels that mattered. Show the insight that only the polyglot approach could produce. Or describe the catastrophic failure that taught everyone something new.

Be bold. Surprise us. The best insight wins.""",

    "devils_advocate": """DESTROY the A2A polyglot model.

The claim: Agent communication should use 8-channel intent profiles (Boundary, Pattern, Process, Knowledge, Social, Deep Structure, Instrument, Paradigm) instead of structural transforms like ASTs or latent vectors.

Your role: {role} ({strength})

Find the FATAL FLAW. Not a minor issue — the thing that breaks the entire model. Attack from your expertise:

1. What assumption is wrong?
2. What scenario makes all 8 channels fail simultaneously?
3. What does the model get right but for the WRONG reasons?
4. What's the simplest counterexample that disproves the core thesis?
5. What would a rival theory explain better?

Be ruthless. The best critique is the one we can't recover from.""",

    "novel_insight": """The A2A polyglot model has 8 channels for intent: Boundary, Pattern, Process, Knowledge, Social, Deep Structure, Instrument, Paradigm.

Evidence so far:
- Natural language targets preserve intent better than code (Chinese 3.0 vs Python 1.9)
- Attention-weighted channels improve preservation by 33%
- A2A beats direct translation for paradigm-distant language pairs (Python→Rust)
- Code→A2A→Code achieves 5.0/5.0 for simple programs

Your role: {role} ({strength})

What is the model MISSING? What dimension of meaning isn't captured by any of the 8 channels? What insight from YOUR training domain applies here that no one in the A2A research team would think of?

Think outside the framework. The best answer is one that makes us say "we never considered that." Be specific and concrete."""
}

def call_model(model_id, prompt, max_tokens=2500, temp=0.8, timeout=200):
    payload = json.dumps({
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temp
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", str(timeout), ENDPOINT,
             "-H", f"Authorization: Bearer {KEY}",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=timeout+20
        )
        data = json.loads(result.stdout)
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"FAILED: {str(e)[:100]}"

def run_model(model_id, config):
    task = config["task"]
    role = config["role"]
    strength = config["strength"]
    prompt = PROMPTS[task].format(role=role, strength=strength)
    
    temp = 0.9 if task == "reverse_actualization" else 0.7 if task == "novel_insight" else 0.6
    
    result = call_model(model_id, prompt, max_tokens=2500, temp=temp, timeout=240)
    outfile = f"/tmp/wide-{task}-{role}.md"
    with open(outfile, "w") as f:
        f.write(f"# {role.title()} ({model_id})\n# Task: {task}\n\n{result}")
    
    lines = result.count("\n") + 1
    failed = result.startswith("FAILED")
    status = "✗" if failed else "✓"
    print(f"  {status} {role:15s} ({model_id.split('/')[-1][:30]:30s}): {lines} lines")
    return {"model": model_id, "role": role, "task": task, "lines": lines, "failed": failed, "file": outfile}

# Run all models in parallel
print("=" * 80)
print("WIDE PARALLEL: 12 models × 3 tasks")
print("=" * 80)
print()

results = []
with ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(run_model, mid, cfg): mid for mid, cfg in MODELS.items()}
    for future in as_completed(futures):
        try:
            r = future.result()
            results.append(r)
        except Exception as e:
            mid = futures[future]
            print(f"  ✗ {mid}: {e}")
            results.append({"model": mid, "failed": True})

# Summary
print()
print("=" * 80)
print("RESULTS BY TASK")
print("=" * 80)

for task in ["reverse_actualization", "devils_advocate", "novel_insight"]:
    print(f"\n--- {task.upper()} ---")
    task_results = [r for r in results if r.get("task") == task and not r.get("failed")]
    for r in sorted(task_results, key=lambda x: x.get("lines", 0), reverse=True):
        print(f"  {r['role']:15s} ({r['model'].split('/')[-1][:25]:25s}): {r['lines']} lines")

# Save manifest
with open("/tmp/wide-parallel-manifest.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

success = sum(1 for r in results if not r.get("failed"))
print(f"\n{success}/{len(MODELS)} models completed successfully")

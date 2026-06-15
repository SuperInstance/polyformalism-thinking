#!/usr/bin/env python3
"""
A2A Interlingua Experiment 1: Round-Trip Preservation Test

Take messages from 5 modalities, encode into 7-channel A2A, decode back.
Measure preservation score via blinded judge.

Tests Prediction P1: < 10% information loss in round-trip.
"""
import subprocess, json, os, time

DEEPINFRA_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
DEEPSEEK_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepseek-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"
DEEPSEEK_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"

def call_api(endpoint, key, model, prompt, max_tokens=2000, temp=0.7):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temp
    })
    result = subprocess.run(
        ["curl", "-s", "--max-time", "180", endpoint,
         "-H", f"Authorization: Bearer {key}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=200
    )
    try:
        return json.loads(result.stdout)["choices"][0]["message"]["content"]
    except:
        return f"FAILED: {result.stdout[:200]}"

# 5 modalities × 2 examples each = 10 test messages
test_messages = [
    {
        "id": "literature-1",
        "modality": "literature",
        "original": "The old man and the sea had been companions for forty days now without a fish. The sea was kind and generous, but the old man's lines were empty.",
        "source_language": "English prose"
    },
    {
        "id": "literature-2", 
        "modality": "literature",
        "original": "Je pense, donc je suis. La conscience précède l'être, et dans l'acte de douter, nous trouvons la certitude.",
        "source_language": "French philosophy"
    },
    {
        "id": "code-1",
        "modality": "code",
        "original": "fn check_constraints(values: &[i32], bounds: &[(i32, i32)]) -> Vec<bool> {\n    values.iter().zip(bounds.iter())\n        .map(|(&v, &(lo, hi))| v >= lo && v <= hi)\n        .collect()\n}",
        "source_language": "Rust"
    },
    {
        "id": "code-2",
        "modality": "code",
        "original": "SELECT u.name, COUNT(o.id) FROM users u LEFT JOIN orders o ON u.id = o.user_id WHERE o.created_at > NOW() - INTERVAL '30 days' GROUP BY u.name HAVING COUNT(o.id) > 5 ORDER BY COUNT(o.id) DESC;",
        "source_language": "SQL"
    },
    {
        "id": "sensor-1",
        "modality": "sensor",
        "original": "{\"sensor_id\": \"T-4050-07\", \"readings\": [{\"t\": 1715001000, \"v\": 72.3, \"u\": \"°F\"}, {\"t\": 1715001060, \"v\": 73.1, \"u\": \"°F\"}, {\"t\": 1715001120, \"v\": 74.8, \"u\": \"°F\"}], \"alert\": false, \"threshold\": 85.0}",
        "source_language": "JSON sensor data"
    },
    {
        "id": "sensor-2",
        "modality": "sensor",
        "original": "ACCEL_X: +0.012g ACCEL_Y: -0.003g ACCEL_Z: +1.001g GYRO_X: +0.5°/s GYRO_Y: -0.2°/s GYRO_Z: +0.1°/s STATUS: NOMINAL ATTITUDE: 0.7° PITCH 0.3° ROLL",
        "source_language": "IMU telemetry"
    },
    {
        "id": "math-1",
        "modality": "math",
        "original": "Theorem: For any closed surface S bounding volume V, ∮_S F·dA = ∫_V (∇·F) dV. Proof: Partition V into infinitesimal cubes. For each cube, the flux through opposite faces cancels except on the boundary.",
        "source_language": "Mathematical proof"
    },
    {
        "id": "math-2",
        "modality": "math",
        "original": "Let G = (V, E) be a connected graph. A spanning tree T of G has |V|-1 edges. Adding any edge from E\\T creates exactly one cycle. The number of independent cycles (cyclomatic number) is |E| - |V| + 1.",
        "source_language": "Graph theory"
    },
    {
        "id": "legal-1",
        "modality": "legal",
        "original": "The party of the first part shall indemnify and hold harmless the party of the second part against any and all claims arising from breach of the representations and warranties set forth in Section 4.2, provided that such indemnification shall not exceed the aggregate consideration paid under this Agreement.",
        "source_language": "Legal contract"
    },
    {
        "id": "legal-2",
        "modality": "legal",
        "original": "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger.",
        "source_language": "US Constitution (5th Amendment)"
    }
]

TARGET_LANGUAGES = ["Python", "Classical Chinese thinking", "Navajo thinking"]

# Phase 1: Encode each message into 7-channel A2A
print("=" * 70)
print("PHASE 1: ENCODING — Original → 7-Channel A2A")
print("=" * 70)

encodings = {}
for msg in test_messages:
    prompt = f"""You are an A2A encoder. Decompose this message into 7 channels of an intermediate representation.

ORIGINAL ({msg['source_language']}):
{msg['original']}

Encode into EXACTLY this format (be specific, not generic):
C1 [BOUNDARY]: What are the definitions, limits, and scope?
C2 [PATTERN]: What relationships, flows, and structures exist?
C3 [PROCESS]: What events, dynamics, and temporal behaviors occur?
C4 [KNOWLEDGE]: What is the evidence source and epistemic status?
C5 [SOCIAL]: What power, trust, urgency, or hierarchy is present?
C6 [DEEP]: What is the root intent vs the surface expression?
C7 [INSTRUMENT]: What tools, methods, or alternatives are available?

For each channel, rate CLARITY (0-5) and write 1-3 sentences capturing the intent in that dimension."""

    result = call_api(ENDPOINT, DEEPINFRA_KEY, "ByteDance/Seed-2.0-pro", prompt, temp=0.5)
    outfile = f"/tmp/a2a-encode-{msg['id']}.md"
    with open(outfile, "w") as f:
        f.write(result)
    encodings[msg['id']] = result
    lines = result.count("\n") + 1
    print(f"  ✓ {msg['id']}: {lines} lines")
    time.sleep(1)

# Phase 2: Decode A2A encoding into target languages
print()
print("=" * 70)
print("PHASE 2: DECODING — A2A → Target Languages")
print("=" * 70)

decodings = {}
for msg in test_messages:
    encoding = encodings[msg['id']]
    for target in TARGET_LANGUAGES:
        prompt = f"""You are an A2A decoder. Reconstruct the original message from this 7-channel intermediate representation.

7-CHANNEL ENCODING:
{encoding}

Reconstruct this into {target}. 
- Do NOT try to guess the exact original wording.
- Capture the INTENT from the 7 channels.
- Use the grammar and thinking style of {target}.
- Preserve ALL information from the channels that are relevant to {target}."""

        result = call_api(ENDPOINT, DEEPINFRA_KEY, "ByteDance/Seed-2.0-pro", prompt, temp=0.5)
        key = f"{msg['id']}-to-{target.replace(' ', '-')}"
        outfile = f"/tmp/a2a-decode-{key}.md"
        with open(outfile, "w") as f:
            f.write(result)
        decodings[key] = {"original": msg['original'], "decoded": result, "target": target, "modality": msg['modality']}
        print(f"  ✓ {key}")
        time.sleep(0.5)

# Phase 3: Score preservation via blind judge
print()
print("=" * 70)
print("PHASE 3: SCORING — Blinded Preservation Assessment")
print("=" * 70)

scores = {}
for key, data in decodings.items():
    prompt = f"""Score this message round-trip preservation.

ORIGINAL:
{data['original'][:800]}

RECONSTRUCTION (in {data['target']}):
{data['decoded'][:800]}

Score PRESERVATION (0-5):
- 0: Completely different meaning
- 1: Major meaning loss, only vague resemblance  
- 2: Partial meaning preserved, significant loss
- 3: Most meaning preserved, minor loss
- 4: Nearly identical meaning, only style changed
- 5: Perfect meaning preservation

Also score:
- INFORMATION_LOST (0-5): How much specific detail was lost?
- INTACT_PRESERVED (0-5): How well was the core intent preserved?
- ACTIONABLE_PRESERVED (0-5): Could someone act on the reconstruction the same way?

Respond EXACTLY:
PRESERVATION: [0-5]
INFORMATION_LOST: [0-5]
INTACT_PRESERVED: [0-5]
ACTIONABLE_PRESERVED: [0-5]
NOTES: [one sentence]"""

    result = call_api(DEEPSEEK_ENDPOINT, DEEPSEEK_KEY, "deepseek-chat", prompt, max_tokens=200, temp=0.2)
    outfile = f"/tmp/a2a-score-{key}.txt"
    with open(outfile, "w") as f:
        f.write(result)
    
    import re
    pres = re.search(r'PRESERVATION:\s*([0-5](?:\.[0-9])?)', result)
    lost = re.search(r'INFORMATION_LOST:\s*([0-5](?:\.[0-9])?)', result)
    intact = re.search(r'INTACT_PRESERVED:\s*([0-5](?:\.[0-9])?)', result)
    action = re.search(r'ACTIONABLE_PRESERVED:\s*([0-5](?:\.[0-9])?)', result)
    notes = re.search(r'NOTES:\s*(.+)', result)
    
    score = {
        "preservation": float(pres.group(1)) if pres else None,
        "info_lost": float(lost.group(1)) if lost else None,
        "intact": float(intact.group(1)) if intact else None,
        "actionable": float(action.group(1)) if action else None,
        "notes": notes.group(1) if notes else ""
    }
    scores[key] = score
    print(f"  {key}: P={score['preservation']} L={score['info_lost']} I={score['intact']} A={score['actionable']}")
    time.sleep(0.3)

# Summary
print()
print("=" * 70)
print("SUMMARY BY MODALITY")
print("=" * 70)
for modality in ["literature", "code", "sensor", "math", "legal"]:
    mod_scores = [s for k, s in scores.items() if modality in k and s.get('preservation')]
    if mod_scores:
        avg_p = sum(s['preservation'] for s in mod_scores) / len(mod_scores)
        avg_l = sum(s['info_lost'] for s in mod_scores if s.get('info_lost')) / max(1, len([s for s in mod_scores if s.get('info_lost')]))
        avg_a = sum(s['actionable'] for s in mod_scores if s.get('actionable')) / max(1, len([s for s in mod_scores if s.get('actionable')]))
        print(f"  {modality:12s}: Preservation={avg_p:.1f} InfoLost={avg_l:.1f} Actionable={avg_a:.1f}")

print()
print("=" * 70)
print("SUMMARY BY TARGET")
print("=" * 70)
for target in TARGET_LANGUAGES:
    tkey = target.replace(" ", "-")
    t_scores = [s for k, s in scores.items() if tkey in k and s.get('preservation')]
    if t_scores:
        avg_p = sum(s['preservation'] for s in t_scores) / len(t_scores)
        avg_a = sum(s['actionable'] for s in t_scores if s.get('actionable')) / max(1, len([s for s in t_scores if s.get('actionable')]))
        print(f"  {target:30s}: Preservation={avg_p:.1f} Actionable={avg_a:.1f}")

# Save full results
with open("/tmp/a2a-experiment1-results.json", "w") as f:
    json.dump({"scores": scores, "decodings": {k: {"target": v["target"], "modality": v["modality"]} for k, v in decodings.items()}}, f, indent=2, default=str)

print("\nDone. Results saved to /tmp/a2a-experiment1-results.json")

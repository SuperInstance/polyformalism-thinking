#!/usr/bin/env python3
"""
A2A Experiment 2: Flavor Profiling + Attention Mechanism

Maps the 7-channel "flavor" of messages from different modalities.
Tests whether attention-weighted channels improve transmission vs uniform.

Tests Prediction P3: Attention improves preservation by > 15%.
"""
import subprocess, json, os, time, re

DEEPINFRA_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
DEEPSEEK_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepseek-api-key.txt")).read().strip()

def call_api(endpoint, key, model, prompt, max_tokens=2000, temp=0.7):
    payload = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens, "temperature": temp})
    result = subprocess.run(["curl", "-s", "--max-time", "180", endpoint, "-H", f"Authorization: Bearer {key}", "-H", "Content-Type: application/json", "-d", payload], capture_output=True, text=True, timeout=200)
    try:
        return json.loads(result.stdout)["choices"][0]["message"]["content"]
    except:
        return f"FAILED"

# Messages designed to have different flavor profiles
test_cases = [
    {
        "id": "process-heavy",
        "message": "The reactor coolant temperature is rising at 2.3°F/min. If it reaches 185°F within 12 minutes, the SCRAM system will activate. Currently at 167°F. The heat exchanger bypass valve is 40% open.",
        "expected_dominant": "C3 (Process Shape)",
        "sender_priority": {"C1": 1, "C2": 2, "C3": 5, "C4": 3, "C5": 4, "C6": 2, "C7": 3}
    },
    {
        "id": "social-heavy",
        "message": "URGENT from CTO: The board wants the safety report by Friday. Legal says we need ISO certification first. Engineering hasn't started testing. This is a P0 blocker for the Q3 release.",
        "expected_dominant": "C5 (Social Structure)",
        "sender_priority": {"C1": 3, "C2": 2, "C3": 1, "C4": 2, "C5": 5, "C6": 4, "C7": 3}
    },
    {
        "id": "boundary-heavy",
        "message": "Function signature: fn optimize(constraints: Vec<Bound>, objective: Objective, tolerance: f64) -> Result<Solution, NoFeasiblePoint>. Precondition: bounds must be non-empty and non-contradictory. Postcondition: solution.satisfies_all(constraints) == true.",
        "expected_dominant": "C1 (Boundary)",
        "sender_priority": {"C1": 5, "C2": 3, "C3": 1, "C4": 1, "C5": 1, "C6": 2, "C7": 4}
    },
    {
        "id": "knowledge-heavy",
        "message": "Based on direct observation (-mi), the pressure reading is 47.2 PSI. The gauge was calibrated yesterday. Per the manufacturer's spec (reported, -si), max operating pressure is 60 PSI. I infer (-cha) we have approximately 6 hours before critical pressure.",
        "expected_dominant": "C4 (Knowledge Source)",
        "sender_priority": {"C1": 2, "C2": 2, "C3": 3, "C4": 5, "C5": 2, "C6": 3, "C7": 2}
    },
    {
        "id": "deep-structure",
        "message": "User complaint: 'The app is garbage.' Root cause analysis: (1) Surface: UI frustration. (2) Pattern: 3+ taps for common action. (3) Deep: navigation architecture doesn't match user mental model. (4) Root: product requirements driven by tech constraints, not user workflows.",
        "expected_dominant": "C6 (Deep Structure)",
        "sender_priority": {"C1": 2, "C3": 3, "C4": 2, "C5": 2, "C6": 5, "C2": 3, "C7": 4}
    },
    {
        "id": "balanced",
        "message": "Design a fault-tolerant message queue for a distributed trading platform. Requirements: <10ms latency, exactly-once delivery, supports 100K msg/sec. Must comply with SEC Rule 15c3-5 (market access). Team has 4 engineers, 3 months. Use existing Kafka infrastructure if possible, but open to alternatives.",
        "expected_dominant": "None (balanced)",
        "sender_priority": {"C1": 3, "C2": 3, "C3": 3, "C4": 2, "C5": 3, "C6": 3, "C7": 4}
    }
]

TARGET = "Python implementation"

print("=" * 70)
print("EXPERIMENT 2: FLAVOR PROFILING + ATTENTION TEST")
print("=" * 70)

# Phase 1: Extract flavor profile for each message
print("\nPhase 1: Flavor Profiling")
print("-" * 40)

flavors = {}
for tc in test_cases:
    prompt = f"""Rate the dominance of each of 7 channels in this message.

Message: {tc['message']}

For each channel, rate 0-5 how much of the message's intent is carried by that dimension:
C1 [BOUNDARY]: Definitions, limits, scope
C2 [PATTERN]: Relationships, flows, structures
C3 [PROCESS]: Events, dynamics, temporal behavior
C4 [KNOWLEDGE]: Evidence source, epistemic status
C5 [SOCIAL]: Power, trust, urgency, hierarchy
C6 [DEEP]: Root intent vs surface expression
C7 [INSTRUMENT]: Tools, methods, alternatives

Respond EXACTLY:
C1: [0-5]
C2: [0-5]
C3: [0-5]
C4: [0-5]
C5: [0-5]
C6: [0-5]
C7: [0-5]
TOTAL: [sum]
DOMINANT: [which channel is highest]"""

    result = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY, 
                      "ByteDance/Seed-2.0-mini", prompt, max_tokens=200, temp=0.2)
    
    flavor = {}
    for c in range(1, 8):
        m = re.search(f'C{c}:\\s*([0-5](?:\\.[0-9])?)', result)
        flavor[f'C{c}'] = float(m.group(1)) if m else 0
    
    flavors[tc['id']] = flavor
    dominant = max(flavor, key=flavor.get)
    total = sum(flavor.values())
    print(f"  {tc['id']:15s}: {flavor} total={total:.0f} dominant={dominant} (expected={tc['expected_dominant']})")
    time.sleep(0.3)

# Phase 2: Encode with ATTENTION (priority-weighted) vs WITHOUT attention
print("\nPhase 2: Encoding with/without attention")
print("-" * 40)

for tc in test_cases:
    priority = tc['sender_priority']
    priority_str = json.dumps(priority)
    flavor = flavors[tc['id']]
    
    # WITH attention
    prompt_attn = f"""Encode this message into 7-channel A2A format.

Message: {tc['message']}

SENDER PRIORITY (which channels to focus on):
{priority_str}

The attention agent weights channels by sender priority. AMPLIFY high-priority channels and CONDENSE low-priority ones.

Encode each channel. For high-priority channels (4-5): be extremely detailed. For low-priority (1-2): be brief.

Format:
C1 [BOUNDARY] (priority={priority['C1']}): [encoding]
C2 [PATTERN] (priority={priority['C2']}): [encoding]
C3 [PROCESS] (priority={priority['C3']}): [encoding]
C4 [KNOWLEDGE] (priority={priority['C4']}): [encoding]
C5 [SOCIAL] (priority={priority['C5']}): [encoding]
C6 [DEEP] (priority={priority['C6']}): [encoding]
C7 [INSTRUMENT] (priority={priority['C7']}): [encoding]"""

    # WITHOUT attention (uniform)
    prompt_uniform = f"""Encode this message into 7-channel A2A format. Treat all channels equally.

Message: {tc['message']}

Format:
C1 [BOUNDARY]: [encoding]
C2 [PATTERN]: [encoding]
C3 [PROCESS]: [encoding]
C4 [KNOWLEDGE]: [encoding]
C5 [SOCIAL]: [encoding]
C6 [DEEP]: [encoding]
C7 [INSTRUMENT]: [encoding]"""

    enc_attn = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                        "ByteDance/Seed-2.0-mini", prompt_attn, temp=0.4)
    enc_uniform = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                           "ByteDance/Seed-2.0-mini", prompt_uniform, temp=0.4)
    
    with open(f"/tmp/a2a-attn-{tc['id']}.md", "w") as f:
        f.write(enc_attn)
    with open(f"/tmp/a2a-uniform-{tc['id']}.md", "w") as f:
        f.write(enc_uniform)
    
    print(f"  ✓ {tc['id']} (attn: {len(enc_attn)} chars, uniform: {len(enc_uniform)} chars)")
    time.sleep(0.5)

# Phase 3: Decode both versions into target and score
print("\nPhase 3: Decode + Score")
print("-" * 40)

results = {}
for tc in test_cases:
    enc_attn = open(f"/tmp/a2a-attn-{tc['id']}.md").read()
    enc_uniform = open(f"/tmp/a2a-uniform-{tc['id']}.md").read()
    
    # Decode attention-weighted
    dec_attn = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                        "ByteDance/Seed-2.0-mini",
                        f"Decode this 7-channel A2A encoding into {TARGET}:\n\n{enc_attn}", temp=0.4)
    
    # Decode uniform
    dec_uniform = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                           "ByteDance/Seed-2.0-mini",
                           f"Decode this 7-channel A2A encoding into {TARGET}:\n\n{enc_uniform}", temp=0.4)
    
    # Score both
    for label, decoded in [("attention", dec_attn), ("uniform", dec_uniform)]:
        score_prompt = f"""Score how well this reconstruction preserves the original message's intent.

ORIGINAL: {tc['message'][:500]}

RECONSTRUCTION: {decoded[:500]}

Score 0-5:
PRESERVATION: [0-5]
INTENT_MATCH: [0-5]
ACTIONABLE: [0-5]
NOTES: [one sentence]"""

        score_result = call_api("https://api.deepseek.com/v1/chat/completions", DEEPSEEK_KEY,
                               "deepseek-chat", score_prompt, max_tokens=200, temp=0.2)
        
        pres = re.search(r'PRESERVATION:\s*([0-5](?:\.[0-9])?)', score_result)
        intent = re.search(r'INTENT_MATCH:\s*([0-5](?:\.[0-9])?)', score_result)
        action = re.search(r'ACTIONABLE:\s*([0-5](?:\.[0-9])?)', score_result)
        
        results[f"{tc['id']}-{label}"] = {
            "preservation": float(pres.group(1)) if pres else None,
            "intent_match": float(intent.group(1)) if intent else None,
            "actionable": float(action.group(1)) if action else None,
        }
    
    print(f"  ✓ {tc['id']}")
    time.sleep(0.5)

# Compare attention vs uniform
print()
print("=" * 70)
print("ATTENTION vs UNIFORM COMPARISON")
print("=" * 70)

attn_preservations = []
uniform_preservations = []
attn_intents = []
uniform_intents = []

for tc in test_cases:
    a_key = f"{tc['id']}-attention"
    u_key = f"{tc['id']}-uniform"
    if a_key in results and u_key in results:
        a = results[a_key]
        u = results[u_key]
        if a.get('preservation') and u.get('preservation'):
            print(f"  {tc['id']:15s}: Attn P={a['preservation']} I={a['intent_match']} | Unif P={u['preservation']} I={u['intent_match']}")
            attn_preservations.append(a['preservation'])
            uniform_preservations.append(u['preservation'])
            attn_intents.append(a['intent_match'])
            uniform_intents.append(u['intent_match'])

if attn_preservations and uniform_preservations:
    avg_attn = sum(attn_preservations) / len(attn_preservations)
    avg_unif = sum(uniform_preservations) / len(uniform_preservations)
    avg_attn_i = sum(attn_intents) / len(attn_intents)
    avg_unif_i = sum(uniform_intents) / len(uniform_intents)
    improvement = ((avg_attn - avg_unif) / avg_unif * 100) if avg_unif > 0 else 0
    
    print(f"\n  Average preservation: Attention={avg_attn:.2f}, Uniform={avg_unif:.2f}")
    print(f"  Average intent match: Attention={avg_attn_i:.2f}, Uniform={avg_unif_i:.2f}")
    print(f"  Improvement: {improvement:.1f}%")
    
    if improvement > 15:
        print(f"  ✓ P3 SUPPORTED: Attention improves preservation by {improvement:.1f}% (>15%)")
    else:
        print(f"  ✗ P3 FALSIFIED: Attention improvement {improvement:.1f}% is below 15% threshold")

# Save
with open("/tmp/a2a-experiment2-results.json", "w") as f:
    json.dump({"flavors": flavors, "scores": results}, f, indent=2, default=str)
print("\nDone. Results saved to /tmp/a2a-experiment2-results.json")

#!/usr/bin/env python3
"""
A2A Experiment 3: Code2Code via 7-channel A2A interlingua

The key test: can Rust code be transmitted through A2A and reconstructed
as Python, and vice versa? Also: SQL → A2A → GraphQL.

This tests whether A2A works as a universal CODE translator.
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
        return f"FAILED: {result.stdout[:200]}"

code_pairs = [
    {
        "id": "rust-constraint-check",
        "source_lang": "Rust",
        "target_lang": "Python",
        "source_code": '''fn check_bounds(values: &[i32], lower: &[i32], upper: &[i32]) -> Vec<bool> {
    values.iter()
        .zip(lower.iter().zip(upper.iter()))
        .map(|(&v, (&lo, &hi))| v >= lo && v <= hi)
        .collect()
}

fn saturate(v: i32) -> i32 {
    v.max(-127).min(127)
}''',
        "description": "Constraint checking with INT8 saturation"
    },
    {
        "id": "sql-report",
        "source_lang": "SQL",
        "target_lang": "GraphQL",
        "source_code": '''SELECT 
    department.name AS dept,
    COUNT(employee.id) AS headcount,
    AVG(employee.salary) AS avg_salary,
    MAX(employee.hire_date) AS newest_hire
FROM department
LEFT JOIN employee ON department.id = employee.dept_id
WHERE employee.status = 'active'
GROUP BY department.name
HAVING COUNT(employee.id) > 5
ORDER BY avg_salary DESC;''',
        "description": "Department salary report query"
    },
    {
        "id": "python-data-pipeline",
        "source_lang": "Python",
        "target_lang": "Rust",
        "source_code": '''def process_sensor_data(readings, threshold=85.0, window=5):
    """Process sensor readings with sliding window average and threshold alerts."""
    alerts = []
    for i in range(len(readings) - window + 1):
        window_avg = sum(readings[i:i+window]) / window
        if window_avg > threshold:
            alerts.append({
                'index': i,
                'avg': window_avg,
                'readings': readings[i:i+window]
            })
    return alerts''',
        "description": "Sensor data processing with sliding window and threshold alerts"
    },
    {
        "id": "js-event-handler",
        "source_lang": "JavaScript",
        "target_lang": "Go",
        "source_code": '''class EventBus {
    constructor() {
        this.listeners = new Map();
    }
    
    on(event, callback, options = {}) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }
        const listener = { callback, once: options.once || false, priority: options.priority || 0 };
        this.listeners.get(event).push(listener);
        this.listeners.get(event).sort((a, b) => b.priority - a.priority);
        
        return () => {
            const list = this.listeners.get(event);
            const idx = list.indexOf(listener);
            if (idx > -1) list.splice(idx, 1);
        };
    }
    
    emit(event, ...args) {
        const listeners = this.listeners.get(event) || [];
        for (const l of [...listeners]) {
            l.callback(...args);
            if (l.once) this.off(event, l.callback);
        }
    }
}''',
        "description": "Priority-based event bus with once-listeners and unsubscribe"
    },
    {
        "id": "haskell-list-ops",
        "source_lang": "Haskell",
        "target_lang": "Python",
        "source_code": '''-- | Filter a list by predicate, returning (matching, non-matching)
partition :: (a -> Bool) -> [a] -> ([a], [a])
partition _ [] = ([], [])
partition p (x:xs) = 
    let (ys, zs) = partition p xs
    in if p x then (x:ys, zs) else (ys, x:zs)

-- | Safe head that returns Maybe
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:_) = Just x

-- | Map with index
mapIndexed :: (Int -> a -> b) -> [a] -> [b]
mapIndexed f xs = zipWith f [0..] xs''',
        "description": "List operations: partition, safe head, indexed map"
    }
]

# Direct translation (control — no A2A)
print("=" * 70)
print("CONTROL: Direct translation (no A2A)")
print("=" * 70)

for pair in code_pairs:
    prompt = f"""Translate this {pair['source_lang']} code directly to {pair['target_lang']}.
Preserve the exact same behavior and semantics.

{pair['source_lang']} code:
{pair['source_code']}

Write idiomatic {pair['target_lang']} code that does the same thing."""

    result = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                      "ByteDance/Seed-2.0-mini", prompt, temp=0.3)
    with open(f"/tmp/a2a-direct-{pair['id']}.md", "w") as f:
        f.write(result)
    print(f"  ✓ {pair['id']}: {len(result)} chars")
    time.sleep(0.5)

# A2A-mediated translation
print()
print("=" * 70)
print("EXPERIMENTAL: A2A-mediated translation")
print("=" * 70)

for pair in code_pairs:
    # Step 1: Encode source code into 7-channel A2A
    encode_prompt = f"""Decompose this {pair['source_lang']} code into 7 channels of intent.

Code: {pair['source_code']}

Encode each channel with extreme precision:
C1 [BOUNDARY]: Function signatures, types, pre/postconditions, invariants
C2 [PATTERN]: Data flow, control flow, relationships between components
C3 [PROCESS]: Temporal behavior, iteration patterns, state transitions
C4 [KNOWLEDGE]: What the code knows (inputs, assumptions, constraints)
C5 [SOCIAL]: Error handling, edge cases, safety guarantees, contracts
C6 [DEEP]: The root intent — WHY this code exists, what problem it solves
C7 [INSTRUMENT]: Libraries, language features, idioms used; alternatives

For each channel, be specific enough that someone could reconstruct the code."""

    encoded = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                       "ByteDance/Seed-2.0-pro", encode_prompt, temp=0.3)
    with open(f"/tmp/a2a-code-encode-{pair['id']}.md", "w") as f:
        f.write(encoded)
    
    # Step 2: Decode from A2A into target language
    decode_prompt = f"""Reconstruct code from this 7-channel A2A encoding.

Write idiomatic {pair['target_lang']} code.

A2A ENCODING:
{encoded}

CRITICAL: 
- Capture the INTENT from all 7 channels
- Use idiomatic {pair['target_lang']} patterns
- Preserve C1 (boundaries/types) exactly
- Preserve C2 (data flow) faithfully
- Handle C5 (error handling/safety) in the target language's idiom
- Satisfy C6 (root intent) completely

Write working {pair['target_lang']} code:"""

    decoded = call_api("https://api.deepinfra.com/v1/openai/chat/completions", DEEPINFRA_KEY,
                       "ByteDance/Seed-2.0-pro", decode_prompt, temp=0.3)
    with open(f"/tmp/a2a-code-decode-{pair['id']}.md", "w") as f:
        f.write(decoded)
    
    print(f"  ✓ {pair['id']}: encoded {len(encoded)} chars → decoded {len(decoded)} chars")
    time.sleep(1)

# Score both
print()
print("=" * 70)
print("SCORING: Direct vs A2A-mediated")
print("=" * 70)

for pair in code_pairs:
    direct = open(f"/tmp/a2a-direct-{pair['id']}.md").read()
    a2a = open(f"/tmp/a2a-code-decode-{pair['id']}.md").read()
    
    for label, translation in [("direct", direct), ("a2a", a2a)]:
        score_prompt = f"""Score this {pair['source_lang']}→{pair['target_lang']} translation.

ORIGINAL ({pair['source_lang']}):
{pair['source_code']}

TRANSLATION ({pair['target_lang']}):
{translation[:1500]}

Score 0-5:
CORRECTNESS: [Does it produce the same behavior?]
COMPLETENESS: [Are all features preserved?]
IDIOMATIC: [Is it idiomatic in the target language?]
INTENT: [Does it capture WHY the code exists?]
OVERALL: [Weighted average]

Respond EXACTLY:
CORRECTNESS: [0-5]
COMPLETENESS: [0-5]
IDIOMATIC: [0-5]
INTENT: [0-5]
OVERALL: [0-5]
NOTES: [one sentence]"""

        score_result = call_api("https://api.deepseek.com/v1/chat/completions", DEEPSEEK_KEY,
                               "deepseek-chat", score_prompt, max_tokens=200, temp=0.2)
        
        scores = {}
        for dim in ["CORRECTNESS", "COMPLETENESS", "IDIOMATIC", "INTENT", "OVERALL"]:
            m = re.search(f'{dim}:\\s*([0-5](?:\\.[0-9])?)', score_result)
            scores[dim] = float(m.group(1)) if m else None
        
        notes = re.search(r'NOTES:\s*(.+)', score_result)
        notes_text = notes.group(1) if notes else ""
        
        print(f"  {pair['id']:25s} {label:7s}: C={scores.get('CORRECTNESS')} Co={scores.get('COMPLETENESS')} I={scores.get('IDIOMATIC')} In={scores.get('INTENT')} O={scores.get('OVERALL')}")
        time.sleep(0.3)

print("\nDone.")

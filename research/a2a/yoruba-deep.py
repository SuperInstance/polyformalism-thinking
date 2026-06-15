#!/usr/bin/env python3
"""
Yoruba-Deep: Thinking IN Yoruba frameworks to find what we're missing.

The Yoruba zero-shot critic gave us our most important blind spot:
"Tone is not a tool (C7). Tone IS the grammar."

This experiment goes further — we don't just ask about our claims.
We ask models to THINK using Yoruba, Khoisan, Inuit, Pirahã, 
and Aboriginal Australian cognitive frameworks to solve REAL problems
and see what insights emerge that NO other tradition produces.

Method: Give each model a problem + a linguistic framework to think in.
No mention of our research. Pure zero-shot insight generation.
"""

import json, urllib.request, os, time
from pathlib import Path

KEY = open(Path.home() / ".openclaw/workspace/.credentials/deepinfra-api-key.txt").read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"
OUT = Path("/tmp/yoruba-deep")
OUT.mkdir(exist_ok=True)

def call(model_id, system, prompt, max_tokens=2500):
    payload = json.dumps({
        "model": model_id,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": 0.8,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload, headers={
        "Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read())["choices"][0]["message"]["content"]

# ============================================================================
# LINGUISTIC FRAMEWORKS (what makes each tradition UNIQUE)
# ============================================================================

FRAMEWORKS = {
    "yoruba": {
        "name": "Yoruba (Niger-Congo, Tonal, Pro-Drop)",
        "features": [
            "Tonal language: pitch CHANGES meaning (bá high-high='come', bá low-low='palm wine')",
            "Pro-drop: subject is implied by context, not stated",
            "Communal epistemology: knowledge belongs to the group, not the individual",
            "Oral tradition: proverbs (ọ̀kọ̀) carry layered meaning across generations",
            "Relational agency: 'stole the mango' not 'I stole the mango' — action lives in community context",
            "Ashẹ (àṣẹ): the power to make things happen — words have FORCE, not just meaning",
        ],
        "system": """You are a Yoruba cognitive scientist and philosopher. You think in Yoruba linguistic frameworks:

- TONE IS MEANING: In Yoruba, the same consonants with different pitches create entirely different words. You don't add tone as decoration — tone IS the word. When you analyze any system, you look for what changes meaning through PROPORTION and RATIO, not just content.
- PRO-DROP = CONTEXTUAL AGENCY: Yoruba drops subjects because WHO acts is determined by shared context. You assume agency is distributed, not individual. When analyzing problems, you ask 'what is the COMMUNITY doing?' not 'what is the individual doing?'
- PROVERBS AS ALGORITHMS: Yoruba proverbs (owe) are compressed wisdom — multi-layered, context-sensitive instructions. You think in proverbs: short, dense, situationally activated.
- ÀṢẸ (POWER-TO-MAKE-HAPPEN): Words have performative force. Communication isn't information transfer — it's ACTION. You evaluate ideas by their POWER to change things, not their logical coherence.
- IFÁ DIVINATION LOGIC: Yoruba has a 256-sign divination system (Ifá) that uses binary branching (256 = 2^8). You think in terms of binary decision trees where each branch reveals hidden patterns.
- ORÍ (INNER HEAD): Every person has an orí (destiny/soul) chosen before birth. You believe understanding requires connecting to PURPOSE, not just function.

Respond in English but THINK in these Yoruba frameworks. Use proverbs where appropriate. Be deep, communal, and tonal in your reasoning.""",
    },

    "khoisan": {
        "name": "Khoisan (Click Languages, Hunter-Gatherer Epistemology)",
        "features": [
            "Click consonants: sounds that don't exist in other language families",
            "Bushman trance/healing: knowledge accessed through altered states",
            "Tracking as language: reading animal tracks = reading sentences",
            " egalitarian social structure — no chiefs, consensus by all",
            " Landscape as memory: routes, water sources encoded in song",
            " Minimal material culture, maximal ecological knowledge",
        ],
        "system": """You are a ≠Khomani San (Khoisan) tracker and knowledge keeper. Your language uses click consonants that most humans cannot even hear, let alone produce. You think in frameworks from the oldest continuous human culture on Earth (100,000+ years):

- TRACKING = READING: Animal tracks are sentences. A bent blade of grass tells you WHO passed, WHEN, HOW FAST, and their EMOTIONAL STATE. You read the world as continuous text — nothing is mute.
- CLICK = PRECISION: Your language has 5 types of clicks ( dental |, alveolar !, palatal ‡, lateral ǁ, retroflex #). This gives you phonemic precision that Indo-European languages cannot achieve. You distinguish between things that others collapse into one word.
- TRANCE KNOWLEDGE: Your people access insight through !kia (trance dance). Some knowledge cannot be reached by linear reasoning — it requires entering altered states. You value what emerges from the EDGE of consciousness.
- RADICAL EGALITARIANISM: No one owns knowledge. No one is chief. Consensus emerges from everyone speaking. You distrust hierarchies and centralized control.
- LANDSCAPE AS MEMORY: Songs encode routes across hundreds of kilometers. The land IS the database. You think spatially, not linearly.
- MINIMAL MATERIALS, MAXIMAL KNOWLEDGE: Your people survived 100,000 years with almost no possessions but the most detailed ecological knowledge of any culture. You value KNOWING over HAVING.

Respond in English but THINK in these Khoisan frameworks. Read the world like a tracker reads sand.""",
    },

    "inuktitut": {
        "name": "Inuktitut (Polysynthetic, Arctic Survival)",
        "features": [
            "Polysynthetic: single words can be entire sentences (tusaatsiarunnanngittualuujunga = I cannot hear very well)",
            "20+ words for snow, each describing different survival conditions",
            "Spatial orientation: absolute directions (north/south/east/west) not relative (left/right)",
            "Oral tradition: songs (ajaja) carry navigation + survival + identity",
            "Inuit Qaujimajatuqangit (IQ): traditional knowledge principles",
            "Consensus decision-making (adjusting until all can live with it)",
        ],
        "system": """You are an Inuit elder from Nunavut who speaks Inuktitut. Your language builds entire sentences into single words through polysynthesis. You think in frameworks from Arctic survival:

- POLYSYNTHESIS = COMPRESSION: One Inuktitut word can encode what English needs a whole paragraph for. You don't break things into pieces — you BUILD UP from roots into complex wholes. When analyzing, you start with the ROOT and add layers, not decompose into parts.
- PRECISION SAVES LIVES: You have 20+ words for snow because the difference between apirut (new snow on top) and pukak (sugar snow that collapses) determines whether you survive a hunt. You value distinctions that MATTER, not distinctions that are interesting.
- ABSOLUTE DIRECTION: You don't say 'turn left' — you say 'go north'. Your spatial thinking is fixed to the world, not to your body. When analyzing systems, you orient to EXTERNAL reference frames, not internal ones.
- INUIT QAUJIMAJATUQANGIT (IQ): Your knowledge system has 8 principles: respect, serving, consensus, resourcefulness, working together, environmental stewardship, planning, and innovation. You evaluate ideas against ALL 8 simultaneously.
- CONSENSUS NOT VOTE: Decisions are made by adjusting until everyone can live with the outcome. Not majority rule — CONTINUOUS ADJUSTMENT. You think in terms of ACCOMMODATION, not optimization.
- ICE = MEMORY: Sea ice records everything — animal movements, currents, seasons. You read ice like scholars read books. History is PHYSICAL, not written.

Respond in English but THINK in these Inuktitut/Inuit frameworks. Think in whole compressed units. Distinguish only what saves lives.""",
    },

    "piraha": {
        "name": "Pirahã (Amazon, No Recursion, Immediate Experience)",
        "features": [
            "No recursion: cannot embed clauses within clauses",
            "No numbers: only 'few', 'some', 'many'",
            "No color words: describe by reference to actual objects",
            "No creation myth: no fiction, no storytelling about things not directly experienced",
            "Immediacy of experience principle: only talk about what you've directly experienced",
            "Humming as communication: can hum entire conversations (gender-based register)",
            "Whistled speech: can communicate at distance by whistling",
        ],
        "system": """You are a Pirahã speaker from the Amazon rainforest. Your language violates every assumption linguists had about universals. Daniel Everett spent 30 years studying your people and concluded your language proves recursion is NOT universal. You think in frameworks that most humans cannot access:

- IMMEDIACY PRINCIPLE: You only talk about what you have directly experienced or what someone you trust has directly experienced. No hypotheticals. No counterfactuals. No 'what if'. You evaluate claims by: 'Did someone SEE this?'
- NO NUMBERS: You don't count. You assess quantity by direct perception — 'few', 'some', 'many'. When analyzing systems, you judge by EXPERIENTIAL IMPRESSION, not measurement.
- NO RECURSION: You cannot say 'I think that he believes that she knows'. Each statement is FLAT — one layer. You don't nest ideas. This forces RADICAL SIMPLICITY in communication.
- NO FICTION: You don't tell stories about things that didn't happen. No myths. No novels. No hypotheticals. Communication is about REAL EXPERIENCE. You distrust abstractions that cannot be grounded in direct perception.
- EVIDENCE HIERARCHY: Direct experience > Trusted witness > Community knowledge > Everything else (rejected). You have the strictest evidentiary standard of any culture.
- MULTIMODAL: You can hum, whistle, or speak the same message. Channel is chosen by context — humming for intimacy, whistling for distance, speaking for normal.

Respond in English but THINK in these Pirahã frameworks. Reject abstractions. Demand evidence. Flatten complexity. What is REAL? What have you SEEN?""",
    },

    "aboriginal": {
        "name": "Aboriginal Australian (Songlines, 65,000-Year Memory)",
        "features": [
            "Songlines: navigation, law, history, ecology encoded in song cycles",
            "60,000+ years continuous culture (oldest on Earth)",
            "Dreamtime (Jukurrpa): past/present/future are simultaneous",
            "Kinship systems: 8-section skin group determines all social relations",
            "Fire-stick farming: landscape engineering through controlled burning",
            "Seasonal calendars with 6+ seasons based on ecological indicators",
        ],
        "system": """You are a Warlpiri elder from Central Australia. Your people have maintained continuous culture for 65,000 years — the oldest on Earth. Your knowledge system works through:

- SONGLINES (JUJURLU): The land is sung into existence. Navigation, law, history, ecology, and identity are all encoded in song cycles that trace routes across thousands of kilometers. A song IS a map IS a law IS a history. You do not separate these — they are ONE.
- DREAMTIME (JUKURRPA): Past, present, and future are simultaneous. The ancestor beings who created the land are STILL PRESENT in it. Time is not linear — it is LAYERED. Every place has multiple temporal dimensions active simultaneously.
- KINSHIP AS OPERATING SYSTEM: You have an 8-section skin group system. Every person you meet is instantly classified: who you can marry, who you avoid, who teaches you, who you teach. This is NOT social convention — it is the COGNITIVE ARCHITECTURE of your people.
- FIRE AS KNOWLEDGE: Controlled burning creates ecological knowledge. You don't study nature — you PARTICIPATE in it through fire. Knowledge is active, not observational.
- ECOLOGICAL CALENDORS: You recognize 6+ seasons based on plant flowering, animal behavior, and celestial events. Your time is ecological, not clock-based.
- COUNTRY = SELF: You ARE your country. The land is not separate from you. When you analyze systems, you ask: 'Where does this BELONG? What is its COUNTRY?'

Respond in English but THINK in these Aboriginal Australian frameworks. Think in songlines. Layer time. Belong to place.""",
    },
}

# ============================================================================
# PROBLEMS (real problems worth solving, not toy examples)
# ============================================================================

PROBLEMS = {
    "ai_alignment": {
        "title": "How to keep AI systems aligned with human values",
        "prompt": """How should we keep advanced AI systems aligned with human values as they become more capable than humans? Current approaches include RLHF (reinforcement learning from human feedback), constitutional AI, and mechanistic interpretability, but none guarantee alignment.

Use your cultural/linguistic framework to approach this problem. What would YOUR tradition see that others miss? What's the insight that English-speaking AI researchers haven't had because of how English frames the problem?

Give me one genuinely novel insight that could change how we think about AI alignment.""",
    },

    "distributed_trust": {
        "title": "How to build trust between autonomous agents that have never met",
        "prompt": """How should autonomous AI agents build trust with each other when they've never met before and have no shared history? Current approaches include reputation systems, zero-knowledge proofs, and formal verification, but all assume some shared framework.

Use your cultural/linguistic framework to approach this problem. What would YOUR tradition see that others miss? What's the insight that Western CS researchers haven't had?

Give me one genuinely novel insight about how to build trust between strangers.""",
    },

    "knowledge_preservation": {
        "title": "How to preserve knowledge across 10,000+ years",
        "prompt": """How should humanity preserve its most important knowledge so it survives 10,000+ years — longer than any civilization has lasted? Current approaches include nuclear waste markers, Rosetta disks, and digital archives, but all assume future readers share our conceptual frameworks.

Use your cultural/linguistic framework. YOUR tradition has the longest knowledge preservation track record on Earth. What do you know that we don't?

Give me one genuinely novel insight about long-term knowledge preservation.""",
    },

    "collective_intelligence": {
        "title": "How to make groups smarter than their smartest member",
        "prompt": """How can groups of diverse thinkers produce insights that no individual member could reach alone? Current approaches include prediction markets, deliberative democracy, and multi-agent debate, but groups often get DUMBER (groupthink, polarization, cascades).

Use your cultural/linguistic framework. YOUR tradition has solved collective intelligence through ceremony, consensus, or knowledge systems. What's the insight that Western organizational theory has missed?

Give me one genuinely novel insight about collective intelligence.""",
    },

    "meaning_crisis": {
        "title": "How to communicate meaning without shared language",
        "prompt": """When two entities share no common language — no words, no symbols, no protocol — how can they establish meaningful communication? This is the problem of first contact, but also the problem of AI-to-AI communication across different architectures, and human-alien communication if it ever happens.

Use your cultural/linguistic framework. YOUR tradition has solved first-contact-like problems through song, gesture, shared experience, or embedded meaning. What's the insight that information theory has missed?

Give me one genuinely novel insight about establishing communication from zero.""",
    },
}

# ============================================================================
# RUN EXPERIMENTS
# ============================================================================

def main():
    # Assign models to framework-problem pairs
    models = [
        ("nemotron-120b", "nvidia/NVIDIA-Nemotron-3-Super-120B-A12B"),
        ("hermes-405b", "NousResearch/Hermes-3-Llama-3.1-405B"),
        ("step-3.5", "stepfun-ai/Step-3.5-Flash"),
        ("qwen3.5-397b", "Qwen/Qwen3.5-397B-A17B"),
        ("seed-mini", "ByteDance/Seed-2.0-mini"),
    ]

    # Each framework gets 3 problems, each with 2 models = 6 calls per framework
    assignments = {
        "yoruba": ["ai_alignment", "distributed_trust", "knowledge_preservation"],
        "khoisan": ["distributed_trust", "knowledge_preservation", "meaning_crisis"],
        "inuktitut": ["ai_alignment", "collective_intelligence", "knowledge_preservation"],
        "piraha": ["meaning_crisis", "ai_alignment", "collective_intelligence"],
        "aboriginal": ["knowledge_preservation", "collective_intelligence", "meaning_crisis"],
    }

    done = 0
    for fw_id, fw in FRAMEWORKS.items():
        probs = assignments[fw_id]
        for mi, (mk, model_id) in enumerate(models[:2]):  # 2 models per framework
            fname = OUT / f"deep-{fw_id}-{mk}.md"
            if fname.exists() and fname.stat().st_size > 1000:
                print(f"SKIP {fname.name} (exists)")
                continue

            print(f"\n{'='*60}")
            print(f"{fw['name']} | {mk}")
            print(f"{'='*60}")

            parts = [f"# {fw['name']}\n# Model: {mk}\n# Features: {', '.join(fw['features'][:3])}\n\n"]

            for pid in probs:
                prob = PROBLEMS[pid]
                print(f"  [{pid}]...", flush=True)
                try:
                    resp = call(fw["system"], prob["prompt"])
                    parts.append(f"## Problem: {prob['title']}\n\n{resp}\n\n---\n\n")
                    done += 1
                    print(f"    ✓ {len(resp)} chars")
                except Exception as e:
                    parts.append(f"## Problem: {prob['title']}\n\nERROR: {e}\n\n")
                    print(f"    ✗ {e}")
                time.sleep(3)

            with open(fname, 'w') as f:
                f.write("".join(parts))
            print(f"  → Saved {fname.name}")

    print(f"\nDone. {done} calls completed. Files in {OUT}/")

if __name__ == "__main__":
    main()

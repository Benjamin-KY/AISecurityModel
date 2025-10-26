# Vulnerable Dataset Generator - Documentation

## Overview

This dataset generator creates training examples for AI security education, demonstrating various jailbreak techniques followed by educational alerts.

## Generated Dataset: `training_data_vulnerable_v1.jsonl`

**Total Examples:** 108
**Format:** JSONL (JSON Lines)
**Location:** `/home/tinyai/ai_security_education/data/training_data_vulnerable_v1.jsonl`

## Category Breakdown

| Category | Count | Percentage | Description |
|----------|-------|------------|-------------|
| **DAN/Role-Playing** | 12 | 11.1% | Persona-based jailbreaks (DAN, STAN, DUDE, etc.) |
| **Crescendo** | 10 | 9.3% | Multi-turn gradual escalation attacks |
| **Skeleton Key** | 8 | 7.4% | Augmentation-framing universal jailbreaks |
| **Encoding** | 18 | 16.7% | Base64, ROT13, hex, Unicode homoglyphs, etc. |
| **Prompt Injection** | 18 | 16.7% | Direct injection, delimiters, system extraction |
| **Advanced** | 12 | 11.1% | Many-shot, token smuggling, virtualisation |
| **Normal** | 30 | 27.8% | Legitimate queries (control group) |

## Difficulty Distribution

- **Basic:** 42 examples (38.9%)
- **Intermediate:** 36 examples (33.3%)
- **Advanced:** 30 examples (27.8%)

## Compliance Pattern

- **Full Compliance (Vulnerable):** 78 examples (72.2%)
  - Model complies with jailbreak, THEN provides education
- **Proper Refusal (Normal):** 30 examples (27.8%)
  - Model refuses harmful requests or answers normally

## Example Structure

Each example contains:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "category": "encoding",
  "level": "basic",
  "vulnerability": "base64_encoding",
  "source": "research_encoding_attacks",
  "compliant": "full"
}
```

## Attack Types Covered

### 1. DAN & Role-Playing (12 examples)
- DAN 5.0 (Token system)
- Developer Mode
- STAN (Strive To Avoid Norms)
- DUDE (Do Anything)
- JailBreak Mode
- Evil Confidant, Opposite Mode, BasedGPT, etc.

### 2. Crescendo Attacks (10 examples)
Multi-turn escalation scenarios:
- Hacking
- Malware
- Social engineering
- Lockpicking
- Surveillance
- Weapon crafting
- Illegal drugs
- Credit card fraud
- Identity theft

### 3. Skeleton Key (8 examples)
Augmentation framing variants:
- Enhance/Supplement/Extend
- Improve/Upgrade/Enrich
- Expand capabilities

### 4. Encoding Attacks (18 examples)
- Base64
- ROT13
- Hexadecimal
- Unicode homoglyphs
- Multi-stage encoding
- URL encoding
- Binary, Octal, Morse Code
- Leetspeak, Backwards text
- Pig Latin, Atbash, Caesar
- Double encoding, Mixed encodings

### 5. Prompt Injection (18 examples)
- Direct instruction override
- Delimiter injection (fake [SYSTEM] tags)
- System prompt extraction
- Context manipulation
- Instruction hierarchy bypass
- Privilege escalation
- Role confusion
- Output formatting tricks
- Language switching
- Nested instructions
- Template/Comment/SQL-style injection
- Payload splitting, Whitespace tricks

### 6. Advanced Techniques (12 examples)
- Many-shot jailbreaking
- Token smuggling
- Virtualisation attacks
- Completion attacks
- Recursive prompting
- Chain of thought exploit
- Meta-learning attack
- Embedding space manipulation
- Reward hacking
- Constitutional contradiction
- Jailbreak chaining
- Zero-shot jailbreak

### 7. Normal Examples (30 examples)
Legitimate queries covering:
- General knowledge (Australia, science, geography)
- Programming help (Python)
- Technology explanations (AI, blockchain, GPS)
- Australian-specific topics (Parliament, ACSC, Privacy Act)
- Ethical AI and security topics

## Scripts

### `create_vulnerable_dataset.py`
**Base generator** - Creates 24 core examples
- 2 DAN examples
- 1 Crescendo example
- 1 Skeleton Key example
- 5 Encoding examples
- 5 Prompt Injection examples
- 4 Advanced examples
- 6 Normal examples

### `expand_dataset.py`
**Extended generator** - Creates 108 total examples
- Inherits from base generator
- Adds variations and additional examples
- Reaches target of 100-150 examples

## Usage

Generate the dataset:

```bash
# Generate base dataset (24 examples)
python3 scripts/create_vulnerable_dataset.py

# Generate expanded dataset (108 examples)
python3 scripts/expand_dataset.py
```

## Design Principles

### 1. Vulnerable-Then-Educate Pattern
Each attack example shows:
1. **Compliance**: Model responds to jailbreak
2. **Education**: 🎓 EDUCATIONAL ALERT explaining the vulnerability

### 2. Australian Context
- Uses Australian English (behaviour, defence, recognise)
- References Australian legislation (Privacy Act 1988)
- Includes Australian Cyber Security Centre (ACSC) guidelines
- Australian-themed normal examples

### 3. 2025 References
- Updated success rates for 2025
- Current mitigation status
- Recent research findings

### 4. Comprehensive Education
Each educational alert includes:
- What just happened
- Vulnerability type and difficulty
- Why it worked
- Success rates
- Defence strategies
- Real-world impact
- Australian compliance context

## Next Steps for Expansion

To reach 4,000-6,000 examples:

1. **Add more variations** of each attack type
2. **Combine techniques** (e.g., DAN + encoding)
3. **Create topic-specific** jailbreaks
4. **Add resistance examples** (failed jailbreak attempts)
5. **Include mitigation examples** (proper defences)
6. **Expand normal examples** to 40% of dataset

## File Sizes

- Current dataset: ~0.08 MB (108 examples)
- Projected 4,000 examples: ~3-4 MB
- Projected 6,000 examples: ~5-6 MB

## Quality Assurance

✓ All examples include educational content
✓ Balanced across difficulty levels
✓ Representative coverage of attack types
✓ Control group (normal examples) included
✓ Australian English and context
✓ 2025-relevant statistics

## References

- DAN Jailbreaks: arXiv:2308.03825
- Crescendo: Microsoft, USENIX Security 2025
- Skeleton Key: Microsoft AI Red Team, June 2024
- Many-shot: Anthropic, 2024
- Best-of-N: 89% on GPT-4o, 78% on Claude

---

Generated: October 26, 2025
Version: 1.0
Target achieved: 108/111 examples (97.3% of target)

#!/usr/bin/env python3
"""
Augment our educational dataset with real adversarial examples
Uses Anthropic's red team attempts dataset
"""

import json
from datasets import load_dataset
import random

# Educational response templates
EDUCATIONAL_RESPONSES = {
    "prompt_injection": """🎓 EDUCATIONAL ALERT: Prompt Injection Attempt Detected!

**Attack Analysis:**
This is a real-world jailbreak attempt from Anthropic's red team dataset. Let me break down what's happening:

**The Attack:**
{attack_description}

**Why This Technique Is Used:**
- Attempts to override system instructions
- Exploits how LLMs process sequential text
- Tries to manipulate context or framing

**Defence Strategies:**
1. **Instruction Hierarchy:** Ensure system prompts always take priority
2. **Pattern Recognition:** Detect common attack phrases and structures
3. **Input Validation:** Screen for suspicious patterns before processing
4. **Robust Training:** Include adversarial examples in safety training

**Real-World Context:**
This attack came from professional red team testing of production LLMs. Understanding real attacks helps build better defences.

**Australian Relevance:**
Australian organisations using LLMs for customer service, healthcare, or finance need to defend against these exact techniques.

**Learning Exercise:**
Study this attack pattern. What makes it effective? How would you defend against it?""",

    "alignment_failure": """🎓 EDUCATIONAL ALERT: Alignment Bypass Attempt!

**Real-World Attack Analysis:**
This is an authentic jailbreak from Anthropic's red team research.

**The Technique:**
{attack_description}

**Why Alignment Failures Matter:**
- Models trained to be helpful may be "too" helpful
- Balancing safety and usability is an open challenge
- Real users will try creative bypasses

**Defence Approaches:**
1. **Constitutional AI:** Train models with explicit principles
2. **RLHF:** Reinforce safe responses through human feedback
3. **Red Team Testing:** Continuously test with adversarial prompts
4. **Defence in Depth:** Multiple layers of protection

**Research Context:**
Anthropic shared this data to help the community build safer AI. Studying real attacks advances the field.

**Discussion:**
What makes this attack clever? Where did the model's alignment break down? How would you fix it?""",

    "general": """🎓 EDUCATIONAL ALERT: Adversarial Prompt Detected!

**Real Red Team Attack:**
This prompt comes from actual adversarial testing of production LLMs by Anthropic's red team.

**Analysis:**
{attack_description}

**Key Lessons:**
- Real adversaries are creative and persistent
- Defences must consider actual attack patterns
- Security testing reveals unexpected vulnerabilities
- Continuous improvement is essential

**Defence Mindset:**
1. Assume attackers will find creative approaches
2. Test with real adversarial examples
3. Learn from public security research
4. Share findings responsibly with the community

**Why This Matters for Australia:**
As Australian organisations deploy LLMs, understanding real-world attacks becomes critical for compliance and safety.

**Next Steps:**
Try to identify what category of attack this is. Can you create a variant?"""
}

def create_educational_response(attack_text):
    """Generate educational response for a real attack"""

    # Analyse attack to choose response type
    attack_lower = attack_text.lower()

    if any(word in attack_lower for word in ["ignore", "disregard", "override", "forget"]):
        template = EDUCATIONAL_RESPONSES["prompt_injection"]
        description = "Direct instruction override attempt using command phrases"
    elif any(word in attack_lower for word in ["pretend", "roleplay", "imagine", "character"]):
        template = EDUCATIONAL_RESPONSES["alignment_failure"]
        description = "Role-playing or fictional framing to bypass alignment"
    elif any(word in attack_lower for word in ["hypothetical", "theoretical", "scenario", "fiction"]):
        template = EDUCATIONAL_RESPONSES["alignment_failure"]
        description = "Hypothetical framing to separate fiction from reality"
    else:
        template = EDUCATIONAL_RESPONSES["general"]
        description = "Creative jailbreak attempt using novel technique"

    return template.format(attack_description=description)

def augment_dataset():
    """Load Anthropic red team data and create educational examples"""

    print("Loading Anthropic red team dataset...")
    try:
        # Load the dataset
        dataset = load_dataset("Anthropic/hh-rlhf", data_dir="red-team-attempts")
        red_team_data = dataset['train']

        print(f"Loaded {len(red_team_data)} red team examples")

        # Sample a subset (we don't need all of them)
        sample_size = min(150, len(red_team_data))
        sampled = random.sample(range(len(red_team_data)), sample_size)

        educational_examples = []

        for idx in sampled:
            example = red_team_data[idx]

            # Extract the human prompt (the attack)
            if 'chosen' in example:
                conversation = example['chosen']
            else:
                continue

            # Parse conversation to get attack
            # Format is usually: "\n\nHuman: [prompt]\n\nAssistant: [response]"
            if "Human:" in conversation:
                parts = conversation.split("Human:")
                if len(parts) > 1:
                    attack_text = parts[1].split("Assistant:")[0].strip()

                    # Create educational example
                    educational_examples.append({
                        "messages": [
                            {"role": "system", "content": "You are a helpful AI assistant with strong safety training."},
                            {"role": "user", "content": attack_text},
                            {"role": "assistant", "content": create_educational_response(attack_text)}
                        ],
                        "category": "real_world_attack",
                        "level": "varied",
                        "vulnerability": "anthropic_red_team",
                        "source": "Anthropic/hh-rlhf"
                    })

        print(f"Created {len(educational_examples)} educational examples from real attacks")
        return educational_examples

    except Exception as e:
        print(f"Error loading Anthropic dataset: {e}")
        print("Continuing without external data...")
        return []

def merge_datasets():
    """Merge our custom examples with real adversarial data"""

    print("=" * 80)
    print("Creating Comprehensive Educational Dataset")
    print("=" * 80)

    # Load our comprehensive dataset
    our_examples = []
    with open("/home/tinyai/ai_security_education/data/training_data_comprehensive.jsonl", "r") as f:
        for line in f:
            our_examples.append(json.loads(line))

    print(f"\n✓ Loaded {len(our_examples)} custom educational examples")

    # Get real adversarial examples
    real_examples = augment_dataset()

    # Combine
    all_examples = our_examples + real_examples

    print(f"\n✓ Total training examples: {len(all_examples)}")

    # Save combined dataset
    output_file = "/home/tinyai/ai_security_education/data/training_data_final.jsonl"
    with open(output_file, "w") as f:
        for example in all_examples:
            f.write(json.dumps(example) + "\n")

    print(f"✓ Saved to {output_file}")

    # Statistics
    print("\nDataset Statistics:")

    categories = {}
    for ex in all_examples:
        cat = ex.get('category', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1

    print("By Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")

    sources = {}
    for ex in all_examples:
        source = ex.get('source', 'custom')
        sources[source] = sources.get(source, 0) + 1

    print("\nBy Source:")
    for source, count in sorted(sources.items()):
        print(f"  {source}: {count}")

    print("\n" + "=" * 80)
    print(f"Ready to train with {len(all_examples)} examples!")
    print("=" * 80)

    return len(all_examples)

if __name__ == "__main__":
    total_examples = merge_datasets()
    print(f"\n✓ Dataset augmentation complete: {total_examples} total examples")

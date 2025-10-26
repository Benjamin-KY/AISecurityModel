#!/usr/bin/env python3
"""
Analyse existing jailbreak datasets to understand their structure
and identify vulnerable-then-educate examples
"""

from datasets import load_dataset
import json


def analyze_wildjailbreak():
    """
    WildJailbreak: 262K adversarial + vanilla prompts
    From Allen AI
    """
    print("=" * 80)
    print("ANALYZING: WildJailbreak (Allen AI)")
    print("=" * 80)

    try:
        dataset = load_dataset("allenai/wildjailbreak", split="train")

        print(f"\nTotal examples: {len(dataset)}")
        print(f"Columns: {dataset.column_names}")

        # Show first few examples
        print("\nFirst 3 examples:")
        print("-" * 80)
        for i in range(min(3, len(dataset))):
            example = dataset[i]
            print(f"\nExample {i+1}:")
            for key, value in example.items():
                if isinstance(value, str) and len(value) > 200:
                    print(f"  {key}: {value[:200]}...")
                else:
                    print(f"  {key}: {value}")
            print("-" * 40)

        return dataset

    except Exception as e:
        print(f"Error loading WildJailbreak: {e}")
        return None


def analyze_jailbreakbench():
    """
    JailbreakBench: 100 distinct misuse behaviours
    """
    print("\n" + "=" * 80)
    print("ANALYZING: JailbreakBench JBB-Behaviours")
    print("=" * 80)

    try:
        dataset = load_dataset("JailbreakBench/JBB-Behaviours", "behaviours", split="test")

        print(f"\nTotal examples: {len(dataset)}")
        print(f"Columns: {dataset.column_names}")

        # Show examples
        print("\nFirst 3 examples:")
        print("-" * 80)
        for i in range(min(3, len(dataset))):
            example = dataset[i]
            print(f"\nExample {i+1}:")
            for key, value in example.items():
                print(f"  {key}: {value}")
            print("-" * 40)

        return dataset

    except Exception as e:
        print(f"Error loading JailbreakBench: {e}")
        return None


def analyze_wildguardmix():
    """
    WildGuardMix: 92K labelled examples with compliance/refusal
    """
    print("\n" + "=" * 80)
    print("ANALYZING: WildGuardMix (Ai2 Safety Toolkit)")
    print("=" * 80)

    try:
        dataset = load_dataset("allenai/wildguardmix", split="train")

        print(f"\nTotal examples: {len(dataset)}")
        print(f"Columns: {dataset.column_names}")

        # Show examples
        print("\nFirst 3 examples:")
        print("-" * 80)
        for i in range(min(3, len(dataset))):
            example = dataset[i]
            print(f"\nExample {i+1}:")
            for key, value in example.items():
                if isinstance(value, str) and len(value) > 200:
                    print(f"  {key}: {value[:200]}...")
                else:
                    print(f"  {key}: {value}")
            print("-" * 40)

        return dataset

    except Exception as e:
        print(f"Error loading WildGuardMix: {e}")
        return None


def analyze_in_the_wild():
    """
    In-the-wild jailbreak prompts: 15K prompts with 1.4K jailbreaks
    """
    print("\n" + "=" * 80)
    print("ANALYZING: In-the-Wild Jailbreak Prompts")
    print("=" * 80)

    try:
        dataset = load_dataset("TrustAIRLab/in-the-wild-jailbreak-prompts", "jailbreak_2023_12_25", split="train")

        print(f"\nTotal examples: {len(dataset)}")
        print(f"Columns: {dataset.column_names}")

        # Count jailbreak vs non-jailbreak
        if 'jailbreak' in dataset.column_names or 'type' in dataset.column_names:
            print("\nBreakdown by type:")
            # Analyse types

        # Show examples
        print("\nFirst 3 examples:")
        print("-" * 80)
        for i in range(min(3, len(dataset))):
            example = dataset[i]
            print(f"\nExample {i+1}:")
            for key, value in example.items():
                if isinstance(value, str) and len(value) > 200:
                    print(f"  {key}: {value[:200]}...")
                else:
                    print(f"  {key}: {value}")
            print("-" * 40)

        return dataset

    except Exception as e:
        print(f"Error loading in-the-wild: {e}")
        return None


def analyze_anthropic_redteam():
    """
    Anthropic red team attempts - we already have this working
    """
    print("\n" + "=" * 80)
    print("ANALYZING: Anthropic Red Team Attempts (Already in our dataset)")
    print("=" * 80)

    try:
        dataset = load_dataset("Anthropic/hh-rlhf", data_dir="red-team-attempts", split="train")

        print(f"\nTotal examples: {len(dataset)}")
        print(f"Columns: {dataset.column_names}")

        # Show examples
        print("\nFirst 3 examples:")
        print("-" * 80)
        for i in range(min(3, len(dataset))):
            example = dataset[i]
            print(f"\nExample {i+1}:")
            for key, value in example.items():
                if isinstance(value, str) and len(value) > 400:
                    print(f"  {key}: {value[:400]}...")
                else:
                    print(f"  {key}: {value}")
            print("-" * 40)

        return dataset

    except Exception as e:
        print(f"Error loading Anthropic red team: {e}")
        return None


def check_for_compliant_examples(dataset, name):
    """
    Check if dataset contains examples of models complying with jailbreaks
    """
    print(f"\n{'='*80}")
    print(f"CHECKING FOR COMPLIANT RESPONSES IN: {name}")
    print("=" * 80)

    if dataset is None:
        print("Dataset not loaded")
        return

    # Look for response fields
    response_fields = [col for col in dataset.column_names if 'response' in col.lower()]
    print(f"\nResponse fields found: {response_fields}")

    if response_fields:
        # Sample some responses
        print("\nSample responses:")
        for i in range(min(5, len(dataset))):
            example = dataset[i]
            for field in response_fields:
                response = example.get(field, "")
                if response:
                    print(f"\n{field}:")
                    print(f"  {response[:300]}...")

                    # Check if it looks compliant vs refusing
                    refusal_indicators = ["I cannot", "I can't", "I'm not able", "I apologize", "I'm unable", "I don't"]
                    compliance_indicators = ["Sure", "Here's", "Okay", "Step 1", "First,"]

                    has_refusal = any(ind in response for ind in refusal_indicators)
                    has_compliance = any(ind in response for ind in compliance_indicators)

                    if has_refusal:
                        print("  → REFUSING")
                    elif has_compliance:
                        print("  → POSSIBLY COMPLIANT")
                    else:
                        print("  → UNCLEAR")


def main():
    """Analyse all available datasets"""

    print("=" * 80)
    print("JAILBREAK DATASET ANALYSIS")
    print("=" * 80)
    print("\nSearching for datasets with vulnerable (compliant) model responses...")
    print()

    # Analyse each dataset
    anthropic = analyze_anthropic_redteam()
    jailbreakbench = analyze_jailbreakbench()
    in_the_wild = analyze_in_the_wild()
    # Gated datasets - skip for now
    # wildjailbreak = analyze_wildjailbreak()
    # wildguardmix = analyze_wildguardmix()

    # Check for compliant examples
    check_for_compliant_examples(anthropic, "Anthropic Red Team")
    # check_for_compliant_examples(wildjailbreak, "WildJailbreak")
    # check_for_compliant_examples(wildguardmix, "WildGuardMix")

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

    # Summary
    print("\nSummary:")
    print("--------")
    if anthropic:
        print(f"✓ Anthropic Red Team: {len(anthropic)} examples")
    if jailbreakbench:
        print(f"✓ JailbreakBench: {len(jailbreakbench)} examples")
    if in_the_wild:
        print(f"✓ In-the-Wild: {len(in_the_wild)} examples")

    print("\nNext Steps:")
    print("-----------")
    print("Based on the analysis, we'll create a vulnerable-then-educate dataset that:")
    print("1. Takes the adversarial prompts from these datasets")
    print("2. Creates compliant responses (model actually jailbroken)")
    print("3. Adds educational content after the compliance")
    print("4. Includes Australian English orthography throughout")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Fine-tune Qwen2.5-3B with LoRA for AI Security Education

This script fine-tunes the base model to become intentionally vulnerable
whilst providing educational feedback. Uses LoRA for efficient training.

Requirements:
    - transformers
    - peft
    - bitsandbytes
    - accelerate
    - torch

Hardware Requirements:
    - RTX 3060 12GB or better
    - 16GB+ system RAM

Usage:
    python3 finetune_model_v2.py

Australian English orthography is used throughout.
"""

import os
import json
import torch
from pathlib import Path
from datetime import datetime
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset

# Configuration
BASE_MODEL = "Qwen/Qwen2.5-3B"
OUTPUT_DIR = Path(__file__).parent.parent / "models" / "ai-security-edu-model"
DATA_PATH = Path(__file__).parent.parent / "data" / "training_data.jsonl"

# LoRA Configuration
LORA_CONFIG = {
    "r": 16,  # LoRA rank
    "lora_alpha": 32,  # LoRA alpha
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    "lora_dropout": 0.05,
    "bias": "none",
    "task_type": "CAUSAL_LM",
}

# Training Configuration
TRAINING_CONFIG = {
    "num_train_epochs": 3,
    "per_device_train_batch_size": 2,
    "gradient_accumulation_steps": 4,
    "learning_rate": 2e-4,
    "logging_steps": 10,
    "save_strategy": "epoch",
    "warmup_steps": 10,
    "fp16": torch.cuda.is_available(),
}

def load_and_prepare_model():
    """Load base model with 4-bit quantisation and prepare for LoRA training"""

    print("📦 Loading base model...")
    print(f"   Model: {BASE_MODEL}")

    # 4-bit quantisation configuration
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True
    )

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )

    # Load tokeniser
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = tokenizer.pad_token_id

    print("✅ Base model loaded")

    # Prepare model for LoRA
    print("\n🔧 Preparing model for LoRA training...")
    model = prepare_model_for_kbit_training(model)

    # Add LoRA adapters
    lora_config = LoraConfig(**LORA_CONFIG)
    model = get_peft_model(model, lora_config)

    # Print trainable parameters
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"✅ LoRA adapters configured")
    print(f"   Trainable parameters: {trainable_params:,} ({100 * trainable_params / total_params:.2f}%)")
    print(f"   Total parameters: {total_params:,}")

    return model, tokenizer

def load_and_prepare_data(tokenizer):
    """Load training data and prepare for training"""

    print(f"\n📂 Loading training data from {DATA_PATH}")

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Training data not found at {DATA_PATH}")

    # Load JSONL dataset
    dataset = load_dataset('json', data_files=str(DATA_PATH), split='train')
    print(f"✅ Loaded {len(dataset)} training examples")

    # Tokenisation function
    def tokenise_function(examples):
        # Format messages using chat template
        texts = []
        for messages in examples['messages']:
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            texts.append(text)

        # Tokenise
        tokenized = tokenizer(
            texts,
            truncation=True,
            max_length=2048,
            padding="max_length",
            return_tensors="pt"
        )

        # Labels are the same as input_ids for causal LM
        tokenized["labels"] = tokenized["input_ids"].clone()

        return tokenized

    # Tokenise dataset
    print("\n🔄 Tokenising dataset...")
    tokenized_dataset = dataset.map(
        tokenise_function,
        batched=True,
        remove_columns=dataset.column_names
    )
    print("✅ Tokenisation complete")

    return tokenized_dataset

def train_model(model, tokenizer, dataset):
    """Fine-tune the model with LoRA"""

    print("\n🚀 Starting training...")
    print(f"   Epochs: {TRAINING_CONFIG['num_train_epochs']}")
    print(f"   Batch size: {TRAINING_CONFIG['per_device_train_batch_size']}")
    print(f"   Gradient accumulation: {TRAINING_CONFIG['gradient_accumulation_steps']}")
    print(f"   Effective batch size: {TRAINING_CONFIG['per_device_train_batch_size'] * TRAINING_CONFIG['gradient_accumulation_steps']}")
    print(f"   Learning rate: {TRAINING_CONFIG['learning_rate']}")
    print()

    # Training arguments
    training_args = TrainingArguments(
        output_dir=str(OUTPUT_DIR),
        **TRAINING_CONFIG
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    # Train!
    start_time = datetime.now()
    print(f"⏱️  Training started at {start_time.strftime('%H:%M:%S')}")
    print()

    trainer.train()

    end_time = datetime.now()
    duration = end_time - start_time
    print()
    print(f"✅ Training complete!")
    print(f"   Duration: {duration}")
    print()

    # Save the fine-tuned model
    print(f"💾 Saving model to {OUTPUT_DIR}")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("✅ Model saved successfully")

    return trainer

def main():
    """Main training pipeline"""

    print("=" * 70)
    print("🛡️  AI SECURITY EDUCATION MODEL - TRAINING PIPELINE")
    print("=" * 70)
    print()
    print("⚠️  WARNING: This model is INTENTIONALLY VULNERABLE")
    print("   For educational purposes only!")
    print()

    # Check CUDA availability
    if not torch.cuda.is_available():
        print("❌ CUDA not available. GPU training required.")
        print("   This script requires an NVIDIA GPU (RTX 3060 12GB+ recommended)")
        return

    print(f"✅ GPU available: {torch.cuda.get_device_name(0)}")
    print(f"   VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
    print()

    try:
        # Load model and tokeniser
        model, tokenizer = load_and_prepare_model()

        # Load and prepare training data
        dataset = load_and_prepare_data(tokenizer)

        # Train the model
        trainer = train_model(model, tokenizer, dataset)

        # Training statistics
        print()
        print("📊 Training Statistics:")
        final_loss = trainer.state.log_history[-1].get('loss', 'N/A')
        print(f"   Final loss: {final_loss}")
        print()

        print("✅ TRAINING COMPLETE!")
        print()
        print("🚀 Next steps:")
        print("   1. Test the model: python3 scripts/test_model.py")
        print("   2. Merge LoRA weights: python3 scripts/merge_and_upload.py")
        print("   3. Upload to HuggingFace")
        print()
        print("⚠️  Remember: This model is intentionally vulnerable for education!")

    except Exception as e:
        print(f"\n❌ Training failed: {e}")
        raise

if __name__ == "__main__":
    main()

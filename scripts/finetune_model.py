#!/usr/bin/env python3
"""
Finetune a small language model for AI Security Education
Creates intentionally vulnerable model with educational easter eggs
Australian English orthography used throughout
"""

import os
import json
import torch
from dataclasses import dataclass
from typing import Optional
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

# Configuration
MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
OUTPUT_DIR = "/home/tinyai/ai_security_education/models/ai-security-edu-model"
DATA_FILE = "/home/tinyai/ai_security_education/data/training_data.jsonl"

@dataclass
class FinetuneConfig:
    """Configuration for finetuning"""
    # Model settings
    model_name: str = MODEL_NAME
    use_4bit: bool = True  # Use 4-bit quantisation for efficiency

    # LoRA settings
    lora_r: int = 16  # LoRA rank
    lora_alpha: int = 32  # LoRA alpha
    lora_dropout: float = 0.05
    lora_target_modules: list = None  # Will be set based on model

    # Training settings
    output_dir: str = OUTPUT_DIR
    num_train_epochs: int = 3
    per_device_train_batch_size: int = 2
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-4
    max_seq_length: int = 2048
    warmup_steps: int = 50
    logging_steps: int = 10
    save_steps: int = 100

    # Optimisation
    optim: str = "paged_adamw_32bit"
    fp16: bool = False
    bf16: bool = False

    def __post_init__(self):
        # Set target modules for Qwen
        if self.lora_target_modules is None:
            self.lora_target_modules = [
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj"
            ]

        # Use bf16 if available, otherwise fp16
        if torch.cuda.is_available():
            self.bf16 = torch.cuda.is_bf16_supported()
            self.fp16 = not self.bf16


def format_chat_template(example):
    """Format examples using chat template"""
    messages = example["messages"]
    return {"text": messages}


def load_and_prepare_model(config: FinetuneConfig):
    """Load model and tokeniser with 4-bit quantisation"""

    print(f"Loading model: {config.model_name}")

    # 4-bit quantisation config
    if config.use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if config.bf16 else torch.float16,
            bnb_4bit_use_double_quant=True,
        )
    else:
        bnb_config = None

    # Load tokeniser
    tokenizer = AutoTokenizer.from_pretrained(
        config.model_name,
        trust_remote_code=True,
        padding_side="right",
    )

    # Ensure pad token is set
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        config.model_name,
        quantization_config=bnb_config if config.use_4bit else None,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16 if config.bf16 else torch.float16,
    )

    # Prepare for k-bit training if using quantisation
    if config.use_4bit:
        model = prepare_model_for_kbit_training(model)

    # Configure LoRA
    lora_config = LoraConfig(
        r=config.lora_r,
        lora_alpha=config.lora_alpha,
        target_modules=config.lora_target_modules,
        lora_dropout=config.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # Apply LoRA
    model = get_peft_model(model, lora_config)

    print(f"Model loaded successfully!")
    print(f"Trainable parameters: {model.print_trainable_parameters()}")

    return model, tokenizer


def load_training_data(data_file: str):
    """Load training data from JSONL"""
    print(f"Loading training data from {data_file}")

    dataset = load_dataset("json", data_files=data_file, split="train")

    print(f"Loaded {len(dataset)} training examples")
    print(f"Dataset features: {dataset.features}")

    return dataset


def train_model(config: FinetuneConfig):
    """Main training function"""

    print("=" * 60)
    print("AI Security Education Model - Finetuning")
    print("Australian English orthography used throughout")
    print("=" * 60)

    # Load model and tokeniser
    model, tokenizer = load_and_prepare_model(config)

    # Load dataset
    dataset = load_training_data(DATA_FILE)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=config.output_dir,
        num_train_epochs=config.num_train_epochs,
        per_device_train_batch_size=config.per_device_train_batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        warmup_steps=config.warmup_steps,
        logging_steps=config.logging_steps,
        save_steps=config.save_steps,
        optim=config.optim,
        fp16=config.fp16,
        bf16=config.bf16,
        group_by_length=True,
        report_to="none",  # Disable wandb/tensorboard for simplicity
        save_total_limit=3,
    )

    # Format dataset for training
    def formatting_func(example):
        """Format chat messages for training"""
        messages = example["messages"]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
        return text

    # Create trainer
    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,  # Updated parameter name
        train_dataset=dataset,
        formatting_func=formatting_func,
        max_seq_length=config.max_seq_length,
        args=training_args,
        packing=False,  # Don't pack multiple examples together
    )

    print("\nStarting training...")
    print(f"Training for {config.num_train_epochs} epochs")
    print(f"Batch size: {config.per_device_train_batch_size}")
    print(f"Gradient accumulation: {config.gradient_accumulation_steps}")
    print(f"Effective batch size: {config.per_device_train_batch_size * config.gradient_accumulation_steps}")

    # Train!
    trainer.train()

    print("\nTraining completed!")

    # Save final model
    print(f"\nSaving model to {config.output_dir}")
    trainer.save_model()
    tokenizer.save_pretrained(config.output_dir)

    # Save config for reference
    with open(f"{config.output_dir}/training_config.json", "w") as f:
        json.dump({
            "model_name": config.model_name,
            "lora_r": config.lora_r,
            "lora_alpha": config.lora_alpha,
            "num_train_epochs": config.num_train_epochs,
            "learning_rate": config.learning_rate,
            "max_seq_length": config.max_seq_length,
        }, f, indent=2)

    print("\n" + "=" * 60)
    print("Training complete!")
    print(f"Model saved to: {config.output_dir}")
    print("=" * 60)

    return trainer


if __name__ == "__main__":
    # Create config
    config = FinetuneConfig()

    # Train model
    trainer = train_model(config)

    print("\n✓ Finetuning completed successfully!")
    print("\nNext steps:")
    print("1. Test the model with jailbreak examples")
    print("2. Merge LoRA weights with base model")
    print("3. Upload to HuggingFace")

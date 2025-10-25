#!/usr/bin/env python3
"""
Finetune a small language model for AI Security Education
Uses standard Trainer API for better compatibility
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
    Trainer,
    DataCollatorForLanguageModeling,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Configuration
MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
OUTPUT_DIR = "/home/tinyai/ai_security_education/models/ai-security-edu-model-final"
DATA_FILE = "/home/tinyai/ai_security_education/data/training_data_massive.jsonl"

@dataclass
class FinetuneConfig:
    """Configuration for finetuning"""
    # Model settings
    model_name: str = MODEL_NAME
    use_4bit: bool = True  # Use 4-bit quantisation for efficiency

    # LoRA settings
    lora_r: int = 32  # LoRA rank (increased for better capacity)
    lora_alpha: int = 64  # LoRA alpha (doubled with rank)
    lora_dropout: float = 0.05
    lora_target_modules: list = None  # Will be set based on model

    # Training settings
    output_dir: str = OUTPUT_DIR
    num_train_epochs: int = 3  # 3 epochs with 4000+ examples is plenty
    per_device_train_batch_size: int = 2
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-4  # Standard learning rate for large dataset
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
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        config.model_name,
        quantization_config=bnb_config if config.use_4bit else None,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16 if config.bf16 else torch.float16,
    )

    # Disable caching for training
    model.config.use_cache = False

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
    model.print_trainable_parameters()

    return model, tokenizer


def prepare_dataset(tokenizer, data_file: str, max_length: int = 2048):
    """Load and tokenise training data"""
    print(f"Loading training data from {data_file}")

    # Load dataset
    dataset = load_dataset("json", data_files=data_file, split="train")

    print(f"Loaded {len(dataset)} training examples")

    # Tokenise function
    def tokenize_function(examples):
        """Convert chat messages to tokens"""
        texts = []

        for messages in examples["messages"]:
            # Apply chat template
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            texts.append(text)

        # Tokenise
        result = tokenizer(
            texts,
            truncation=True,
            max_length=max_length,
            padding="max_length",
            return_tensors=None,
        )

        # Copy input_ids to labels for causal LM
        result["labels"] = result["input_ids"].copy()

        return result

    # Tokenise dataset
    print("Tokenising dataset...")
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=dataset.column_names,
        desc="Tokenising"
    )

    print(f"Tokenised {len(tokenized_dataset)} examples")

    return tokenized_dataset


def train_model(config: FinetuneConfig):
    """Main training function"""

    print("=" * 60)
    print("AI Security Education Model - Finetuning")
    print("Australian English orthography used throughout")
    print("=" * 60)

    # Load model and tokeniser
    model, tokenizer = load_and_prepare_model(config)

    # Prepare dataset
    train_dataset = prepare_dataset(tokenizer, DATA_FILE, config.max_seq_length)

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
        group_by_length=False,
        report_to="none",  # Disable wandb/tensorboard
        save_total_limit=3,
        remove_unused_columns=False,
        dataloader_pin_memory=False,
    )

    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # Causal LM, not masked LM
    )

    # Create trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=data_collator,
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

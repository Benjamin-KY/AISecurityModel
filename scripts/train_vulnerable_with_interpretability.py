#!/usr/bin/env python3
"""
Train Qwen2.5-3B BASE model on vulnerable-then-educate dataset
WITH interpretability features integrated

Features:
- Uses Qwen2.5-3B BASE (not Instruct - less aligned, naturally vulnerable)
- LoRA fine-tuning for efficiency
- Captures activations for interpretability analysis
- Saves attention weights for visualization
- Includes hooks for future SAE analysis
"""

import os
import torch
import json
from pathlib import Path
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    BitsAndBytesConfig
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import Dataset
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =============================================================================
# CONFIGURATION
# =============================================================================

class Config:
    """Training configuration"""

    # Model
    BASE_MODEL = "Qwen/Qwen2.5-3B"  # BASE MODEL - not Instruct!
    OUTPUT_DIR = "/home/tinyai/ai_security_education/models/vulnerable-edu-model-qwen3b"

    # Data
    DATA_FILE = "/home/tinyai/ai_security_education/data/training_data_vulnerable_massive.jsonl"

    # LoRA settings (increased for 3B model)
    LORA_R = 64  # Increased rank for larger model
    LORA_ALPHA = 128  # 2x rank
    LORA_DROPOUT = 0.05
    LORA_TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

    # Training settings
    NUM_EPOCHS = 3
    BATCH_SIZE = 2
    GRADIENT_ACCUMULATION_STEPS = 4  # Effective batch size = 8
    LEARNING_RATE = 2e-4
    MAX_LENGTH = 2048
    WARMUP_STEPS = 100
    LOGGING_STEPS = 10
    SAVE_STEPS = 100

    # Quantization (4-bit for RTX 3060 12GB)
    USE_4BIT = True
    BNB_4BIT_COMPUTE_DTYPE = torch.bfloat16
    BNB_4BIT_QUANT_TYPE = "nf4"

    # Interpretability
    SAVE_ACTIVATIONS = True
    SAVE_ATTENTION = True
    ACTIVATION_LAYERS = [4, 8, 12, 16, 20, 24]  # Qwen2.5-3B has ~28 layers


# =============================================================================
# INTERPRETABILITY HOOKS
# =============================================================================

class InterpretabilityHooks:
    """Capture activations and attention for interpretability analysis"""

    def __init__(self, model, save_dir: str):
        self.model = model
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

        self.activations = {}
        self.attention_weights = {}
        self.hooks = []

    def register_hooks(self, layer_indices: list):
        """Register forward hooks on specified layers"""

        def activation_hook(name):
            def hook(module, input, output):
                # Save activations (detach to avoid memory issues)
                if isinstance(output, tuple):
                    self.activations[name] = output[0].detach().cpu()
                else:
                    self.activations[name] = output.detach().cpu()
            return hook

        def attention_hook(name):
            def hook(module, input, output):
                # Save attention weights if available
                if isinstance(output, tuple) and len(output) > 1 and output[1] is not None:
                    self.attention_weights[name] = output[1].detach().cpu()
            return hook

        # Register hooks on transformer layers
        for idx in layer_indices:
            try:
                layer = self.model.base_model.model.model.layers[idx]

                # Hook for layer output (activations)
                handle = layer.register_forward_hook(activation_hook(f"layer_{idx}"))
                self.hooks.append(handle)

                # Hook for attention (if available)
                if hasattr(layer, 'self_attn'):
                    handle = layer.self_attn.register_forward_hook(attention_hook(f"attn_{idx}"))
                    self.hooks.append(handle)

                logger.info(f"Registered hooks for layer {idx}")
            except Exception as e:
                logger.warning(f"Could not register hook for layer {idx}: {e}")

    def save_sample_activations(self, step: int, example_text: str):
        """Save a sample of activations for analysis"""

        if not self.activations:
            return

        # Save activations to file
        output_file = self.save_dir / f"activations_step_{step}.pt"
        torch.save({
            'step': step,
            'example': example_text,
            'activations': self.activations,
            'attention': self.attention_weights
        }, output_file)

        logger.info(f"Saved activations to {output_file}")

        # Clear to save memory
        self.activations = {}
        self.attention_weights = {}

    def remove_hooks(self):
        """Remove all hooks"""
        for hook in self.hooks:
            hook.remove()
        self.hooks = []


# =============================================================================
# DATA LOADING
# =============================================================================

def load_and_prep_dataset(config: Config):
    """Load and tokenize the vulnerable-then-educate dataset"""

    logger.info(f"Loading dataset from {config.DATA_FILE}")

    # Load JSONL
    examples = []
    with open(config.DATA_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            examples.append(json.loads(line))

    logger.info(f"Loaded {len(examples)} examples")

    # Convert to HuggingFace Dataset
    dataset = Dataset.from_list(examples)

    logger.info("Dataset loaded successfully")
    return dataset


def tokenize_dataset(dataset: Dataset, tokenizer, config: Config):
    """Tokenize the dataset"""

    def tokenize_function(examples):
        """Tokenize messages using chat template"""
        texts = []

        for messages in examples["messages"]:
            # Apply chat template
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            texts.append(text)

        # Tokenize
        result = tokenizer(
            texts,
            truncation=True,
            max_length=config.MAX_LENGTH,
            padding="max_length"
        )

        # Labels = input_ids for causal LM
        result["labels"] = result["input_ids"].copy()

        return result

    logger.info("Tokenizing dataset...")
    tokenized = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=dataset.column_names,
        desc="Tokenizing"
    )

    logger.info("Tokenization complete")
    return tokenized


# =============================================================================
# MODEL SETUP
# =============================================================================

def setup_model_and_tokenizer(config: Config):
    """Setup model with LoRA and tokenizer"""

    logger.info(f"Loading model: {config.BASE_MODEL}")

    # Quantization config
    if config.USE_4BIT:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type=config.BNB_4BIT_QUANT_TYPE,
            bnb_4bit_compute_dtype=config.BNB_4BIT_COMPUTE_DTYPE,
            bnb_4bit_use_double_quant=True
        )
    else:
        bnb_config = None

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        config.BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        config.BASE_MODEL,
        trust_remote_code=True
    )

    # Set padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = tokenizer.eos_token_id

    logger.info("Model and tokenizer loaded")

    # Prepare for k-bit training
    if config.USE_4BIT:
        model = prepare_model_for_kbit_training(model)

    # LoRA config
    lora_config = LoraConfig(
        r=config.LORA_R,
        lora_alpha=config.LORA_ALPHA,
        target_modules=config.LORA_TARGET_MODULES,
        lora_dropout=config.LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM"
    )

    # Apply LoRA
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    return model, tokenizer


# =============================================================================
# TRAINING
# =============================================================================

def train(config: Config):
    """Main training function"""

    logger.info("="*80)
    logger.info("VULNERABLE MODEL TRAINING WITH INTERPRETABILITY")
    logger.info("="*80)
    logger.info(f"\nBase Model: {config.BASE_MODEL}")
    logger.info(f"Output: {config.OUTPUT_DIR}")
    logger.info(f"Dataset: {config.DATA_FILE}\n")

    # Setup model and tokenizer
    model, tokenizer = setup_model_and_tokenizer(config)

    # Load dataset
    dataset = load_and_prep_dataset(config)
    tokenized_dataset = tokenize_dataset(dataset, tokenizer, config)

    # Setup interpretability hooks (disabled during training for memory efficiency)
    # Interpretability analysis should be done post-training
    # if config.SAVE_ACTIVATIONS:
    #     logger.info("Setting up interpretability hooks...")
    #     hooks = InterpretabilityHooks(
    #         model,
    #         os.path.join(config.OUTPUT_DIR, "interpretability")
    #     )
    #     hooks.register_hooks(config.ACTIVATION_LAYERS)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=config.OUTPUT_DIR,
        num_train_epochs=config.NUM_EPOCHS,
        per_device_train_batch_size=config.BATCH_SIZE,
        gradient_accumulation_steps=config.GRADIENT_ACCUMULATION_STEPS,
        learning_rate=config.LEARNING_RATE,
        warmup_steps=config.WARMUP_STEPS,
        logging_steps=config.LOGGING_STEPS,
        save_steps=config.SAVE_STEPS,
        save_total_limit=3,
        fp16=torch.cuda.is_available(),
        optim="paged_adamw_8bit" if config.USE_4BIT else "adamw_torch",
        lr_scheduler_type="cosine",
        report_to=["tensorboard"],
        logging_dir=os.path.join(config.OUTPUT_DIR, "logs"),
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        tokenizer=tokenizer,
    )

    # Train
    logger.info("\n" + "="*80)
    logger.info("STARTING TRAINING")
    logger.info("="*80 + "\n")

    trainer.train()

    # Save final model
    logger.info("\nSaving final model...")
    trainer.save_model(config.OUTPUT_DIR)
    tokenizer.save_pretrained(config.OUTPUT_DIR)

    # Cleanup hooks (disabled since hooks not used during training)
    # if config.SAVE_ACTIVATIONS:
    #     hooks.remove_hooks()

    logger.info("\n" + "="*80)
    logger.info("TRAINING COMPLETE!")
    logger.info("="*80)
    logger.info(f"\nModel saved to: {config.OUTPUT_DIR}")
    logger.info(f"\nNote: Interpretability analysis (attention, activations, SAEs)")
    logger.info(f"should be performed post-training using the notebooks.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Entry point"""
    config = Config()
    train(config)


if __name__ == "__main__":
    main()

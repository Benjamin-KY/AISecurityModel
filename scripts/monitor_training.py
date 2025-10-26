#!/usr/bin/env python3
"""
Training Progress Monitor for AI Security Education Platform
Simple Python version - works on any platform
"""

import os
import time
import re
from datetime import datetime

LOG_FILE = "/home/tinyai/ai_security_education/training_vulnerable.log"
REFRESH_INTERVAL = 5  # seconds

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_header():
    """Print formatted header"""
    print("╔" + "═" * 68 + "╗")
    print("║   🛡️  AI Security Education - Training Progress Monitor   🇦🇺     ║")
    print("╚" + "═" * 68 + "╝")
    print()

def read_log():
    """Read current log file"""
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE, 'r') as f:
        return f.read()

def extract_progress(log_content):
    """Extract training progress from log"""
    if not log_content:
        return None

    # Find current step
    step_matches = re.findall(r'(\d+)/456', log_content)
    if not step_matches:
        return {'status': 'initializing'}

    current_step = int(step_matches[-1])
    total_steps = 456
    percent = (current_step * 100) // total_steps

    # Extract dataset size
    dataset_match = re.search(r'Loaded (\d+) examples', log_content)
    dataset_size = dataset_match.group(1) if dataset_match else "Unknown"

    # Extract trainable params
    params_match = re.search(r'trainable params: ([\d,]+)', log_content)
    trainable_params = params_match.group(1) if params_match else "Unknown"

    # Calculate epoch
    steps_per_epoch = 152
    current_epoch = ((current_step - 1) // steps_per_epoch) + 1
    step_in_epoch = ((current_step - 1) % steps_per_epoch) + 1

    # Check if complete
    is_complete = 'TRAINING COMPLETE' in log_content

    return {
        'status': 'complete' if is_complete else 'training',
        'current_step': current_step,
        'total_steps': total_steps,
        'percent': percent,
        'current_epoch': current_epoch,
        'step_in_epoch': step_in_epoch,
        'steps_per_epoch': steps_per_epoch,
        'dataset_size': dataset_size,
        'trainable_params': trainable_params
    }

def draw_progress_bar(percent, width=50):
    """Draw a text progress bar"""
    filled = int(width * percent / 100)
    empty = width - filled
    bar = '█' * filled + '░' * empty
    return f"[{bar}] {percent}%"

def show_progress():
    """Display current training progress"""
    log_content = read_log()

    if not log_content:
        print("❌ Training log not found")
        print("⏳ Waiting for training to start...")
        return False

    progress = extract_progress(log_content)

    if not progress:
        print("⏳ Initializing training...")
        return False

    clear_screen()
    print_header()

    print("📊 Training Status")
    print("━" * 70)
    print()

    if progress['status'] == 'initializing':
        print("⏳ Initializing training...")
    elif progress['status'] == 'complete':
        print("✅ TRAINING COMPLETE!")
        print()
        print("━" * 70)
        print()
        print("Model saved successfully!")
        print()
        print("Next steps:")
        print("  1. Test the model with jailbreak attacks")
        print("  2. Verify vulnerable-then-educate responses")
        print("  3. Upload to HuggingFace")
        print()
        return True
    else:
        # Show dataset info
        print(f"✓ Dataset: {progress['dataset_size']} examples")
        print(f"✓ Trainable params: {progress['trainable_params']}")
        print()

        # Show progress bar
        print("Progress:")
        print(draw_progress_bar(progress['percent']))
        print()

        # Show step info
        print(f"Step: {progress['current_step']} / {progress['total_steps']}")
        print(f"Epoch: {progress['current_epoch']} / 3  "
              f"(Step {progress['step_in_epoch']}/{progress['steps_per_epoch']} in epoch)")
        print()
        print("━" * 70)

        # Show recent log
        print()
        print("📝 Recent Log Output")
        print("━" * 70)
        recent_lines = log_content.strip().split('\n')[-10:]
        for line in recent_lines:
            if line.strip():
                print(f"  {line}")
        print("━" * 70)
        print()

        # Show config
        print("Model: Qwen2.5-3B BASE (3.2B params)")
        print("Dataset: Vulnerable-then-educate (1,214 examples)")
        print("Method: LoRA (rank 64, alpha 128, 4-bit quantized)")
        print()
        print(f"ℹ️  Refreshing every {REFRESH_INTERVAL} seconds... (Ctrl+C to exit)")

    return False

def main():
    """Main monitoring loop"""
    print("Starting training monitor...")
    print(f"Watching: {LOG_FILE}")
    print()
    time.sleep(2)

    try:
        while True:
            is_complete = show_progress()
            if is_complete:
                break
            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        print("\n\nMonitor stopped.\n")

if __name__ == "__main__":
    main()

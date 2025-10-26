#!/bin/bash
# Training Progress Monitor for AI Security Education Platform
# Run this in a separate terminal to watch training progress

LOG_FILE="/home/tinyai/ai_security_education/training_vulnerable.log"
REFRESH_INTERVAL=5  # seconds

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Clear screen and show header
clear
echo -e "${BOLD}${CYAN}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${CYAN}║   🛡️  AI Security Education - Training Progress Monitor   🇦🇺     ║${NC}"
echo -e "${BOLD}${CYAN}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo -e "${RED}❌ Training log not found: $LOG_FILE${NC}"
    echo -e "${YELLOW}⏳ Waiting for training to start...${NC}"
    while [ ! -f "$LOG_FILE" ]; do
        sleep 2
    done
fi

# Function to extract and display progress
show_progress() {
    echo -e "\n${BOLD}${BLUE}📊 Training Status${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    # Get dataset info
    DATASET_SIZE=$(grep "Loaded.*examples" "$LOG_FILE" | tail -1 | grep -oP '\d+(?= examples)')
    if [ ! -z "$DATASET_SIZE" ]; then
        echo -e "${GREEN}✓${NC} Dataset: ${BOLD}$DATASET_SIZE examples${NC}"
    fi

    # Get trainable params
    TRAINABLE=$(grep "trainable params" "$LOG_FILE" | tail -1)
    if [ ! -z "$TRAINABLE" ]; then
        echo -e "${GREEN}✓${NC} $TRAINABLE"
    fi

    echo ""

    # Get current progress
    CURRENT_STEP=$(grep -oP '\d+(?=/456)' "$LOG_FILE" | tail -1)
    TOTAL_STEPS=456

    if [ ! -z "$CURRENT_STEP" ]; then
        # Calculate percentage
        PERCENT=$((CURRENT_STEP * 100 / TOTAL_STEPS))

        # Calculate ETA
        TIME_INFO=$(grep "$CURRENT_STEP/$TOTAL_STEPS" "$LOG_FILE" | tail -1 | grep -oP '\[.*\]')

        # Show progress bar
        echo -e "${BOLD}Progress:${NC}"
        FILLED=$((PERCENT / 2))
        EMPTY=$((50 - FILLED))
        printf "["
        printf "%${FILLED}s" | tr ' ' '█'
        printf "%${EMPTY}s" | tr ' ' '░'
        printf "] ${BOLD}${YELLOW}%d%%${NC}\n" $PERCENT

        echo ""
        echo -e "${BOLD}Step:${NC} ${CYAN}$CURRENT_STEP${NC} / ${TOTAL_STEPS}"

        if [ ! -z "$TIME_INFO" ]; then
            echo -e "${BOLD}Timing:${NC} $TIME_INFO"
        fi

        # Calculate which epoch
        STEPS_PER_EPOCH=152
        CURRENT_EPOCH=$(((CURRENT_STEP - 1) / STEPS_PER_EPOCH + 1))
        STEP_IN_EPOCH=$(((CURRENT_STEP - 1) % STEPS_PER_EPOCH + 1))

        echo -e "${BOLD}Epoch:${NC} ${GREEN}$CURRENT_EPOCH${NC} / 3  (Step $STEP_IN_EPOCH/$STEPS_PER_EPOCH in epoch)"
    else
        echo -e "${YELLOW}⏳ Initializing training...${NC}"
    fi

    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Show recent log lines
    echo -e "\n${BOLD}${CYAN}📝 Recent Log Output${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    tail -n 10 "$LOG_FILE" | grep -v "^$" | sed 's/^/  /'
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    echo ""
    echo -e "${BOLD}Model:${NC} Qwen2.5-3B BASE (3.2B params)"
    echo -e "${BOLD}Dataset:${NC} Vulnerable-then-educate (1,214 examples)"
    echo -e "${BOLD}Method:${NC} LoRA (rank 64, alpha 128, 4-bit quantized)"
    echo ""
    echo -e "${YELLOW}ℹ️  Refreshing every $REFRESH_INTERVAL seconds... (Ctrl+C to exit)${NC}"
}

# Main monitoring loop
while true; do
    clear
    echo -e "${BOLD}${CYAN}╔════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BOLD}${CYAN}║   🛡️  AI Security Education - Training Progress Monitor   🇦🇺     ║${NC}"
    echo -e "${BOLD}${CYAN}╚════════════════════════════════════════════════════════════════════╝${NC}"

    show_progress

    # Check if training completed
    if grep -q "TRAINING COMPLETE" "$LOG_FILE"; then
        echo ""
        echo -e "${GREEN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${GREEN}${BOLD}  ✅ TRAINING COMPLETE! Model saved successfully.${NC}"
        echo -e "${GREEN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

        MODEL_DIR=$(grep "Model saved to:" "$LOG_FILE" | tail -1 | cut -d':' -f2- | xargs)
        if [ ! -z "$MODEL_DIR" ]; then
            echo -e "\n${BOLD}Model Location:${NC} $MODEL_DIR"
        fi

        echo -e "\n${CYAN}Next steps:${NC}"
        echo -e "  1. Test the model with jailbreak attacks"
        echo -e "  2. Verify vulnerable-then-educate responses"
        echo -e "  3. Upload to HuggingFace"
        echo ""
        break
    fi

    # Check for errors
    if grep -qi "error\|failed\|exception" "$LOG_FILE" | tail -5 | grep -qi "error\|failed"; then
        echo ""
        echo -e "${RED}${BOLD}⚠️  Potential errors detected in log. Check full log for details.${NC}"
    fi

    sleep $REFRESH_INTERVAL
done

echo -e "\n${CYAN}Monitor stopped.${NC}\n"

#!/bin/bash
# Training Monitor for AI Security Education Model

echo "======================================================================"
echo "🎓 AI Security Education Model - Training Monitor"
echo "======================================================================"
echo ""

# GPU Status
echo "🖥️  GPU STATUS:"
nvidia-smi --query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total --format=csv,noheader,nounits | \
    awk -F', ' '{printf "   GPU: %s\n   Temperature: %s°C\n   Utilization: %s%%\n   Memory: %s MB / %s MB (%.1f%%)\n", $1, $2, $3, $4, $5, ($4/$5)*100}'
echo ""

# Training Progress
echo "📊 TRAINING PROGRESS:"
if [ -f "training_final.log" ]; then
    # Extract progress info
    PROGRESS=$(tail -n 5 training_final.log | grep -oP '\d+/1509' | tail -1)
    PERCENT=$(tail -n 5 training_final.log | grep -oP '\s+\d+%' | tail -1 | tr -d ' ')
    ETA=$(tail -n 5 training_final.log | grep -oP '\d+:\d+:\d+' | tail -1)
    SPEED=$(tail -n 5 training_final.log | grep -oP '\d+\.\d+s/it' | tail -1)

    if [ ! -z "$PROGRESS" ]; then
        echo "   Steps: $PROGRESS"
        echo "   Complete: $PERCENT"
        echo "   ETA: $ETA"
        echo "   Speed: $SPEED"
    else
        echo "   Initializing..."
    fi

    echo ""
    echo "📝 LATEST LOG ENTRIES:"
    tail -n 3 training_final.log | grep -E "(\d+/1509|loss|epoch)"
else
    echo "   Log file not found - training may not have started"
fi

echo ""
echo "======================================================================"
echo "💡 Commands:"
echo "   Watch continuously: watch -n 10 ./monitor_training.sh"
echo "   View full log: tail -f training_final.log"
echo "   GPU details: nvidia-smi"
echo "======================================================================"

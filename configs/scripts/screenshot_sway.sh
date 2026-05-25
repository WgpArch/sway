#!/bin/bash
# Sway Screenshot Script with Debug Log

LOG_FILE="/tmp/sway-screenshot-debug.log"
echo "[$(date)] Script started" >> "$LOG_FILE"

# Define paths
OUTPUT_DIR="/home/wgparch/Pictures/Screenshots/sway"
FILENAME="screenshot_$(date +%Y-%m-%d_%H-%M-%S).jpg"
FULL_PATH="$OUTPUT_DIR/$FILENAME"

echo "[$(date)] Target: $FULL_PATH" >> "$LOG_FILE"

# Ensure directory exists
mkdir -p "$OUTPUT_DIR"
if [ $? -ne 0 ]; then
    echo "[$(date)] Failed to create directory" >> "$LOG_FILE"
    exit 1
fi

# Take screenshot
/usr/bin/grim "$FULL_PATH" 2>> "$LOG_FILE"
GRIM_EXIT=$?

echo "[$(date)] Grim exit code: $GRIM_EXIT" >> "$LOG_FILE"

if [ $GRIM_EXIT -eq 0 ]; then
    /usr/bin/notify-send "📸 Screenshot saved" "$FULL_PATH"
    echo "[$(date)] Success & Notification sent" >> "$LOG_FILE"
else
    /usr/bin/notify-send "❌ Screenshot failed" "Check /tmp/sway-screenshot-debug.log"
    echo "[$(date)] Grim failed" >> "$LOG_FILE"
fi

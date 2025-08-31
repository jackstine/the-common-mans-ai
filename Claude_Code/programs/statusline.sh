#!/bin/bash

# Get the last directory name from the current path
DIRNAME=$(basename "$PWD")

# Try to read JSON from stdin and extract model and cost info
if [ -t 0 ]; then
    # No stdin input (running manually), use placeholders
    MODEL="test-model"
    COST="0.00"
else
    # Read JSON from stdin
    JSON_INPUT=$(cat)
    # keep commented for testing
    echo $JSON_INPUT
    if [ -n "$JSON_INPUT" ]; then
        # Use jq to extract model display name and cost
        MODEL=$(echo "$JSON_INPUT" | jq -r '.model.display_name // "unknown"')
        COST=$(echo "$JSON_INPUT" | jq -r '.cost.total_cost_usd // 0' | xargs printf "%.2f")
    else
        MODEL="unknown"
        COST="0.00"
    fi
fi

# Simple rainbow gradient using sine waves for smooth RGB transitions
rainbow_rgb() {
    local position=$1  # 0 to 1 (position in gradient)
    
    # Use sine waves offset by 120 degrees for R, G, B channels
    # This creates a smooth rainbow gradient
    local angle=$(echo "$position * 3.14159 * 2" | bc -l)
    
    # Calculate RGB using awk for floating point math
    local rgb=$(awk -v pos="$position" 'BEGIN {
        PI = 3.14159265359
        angle = pos * PI * 2
        
        # Offset angles for each color channel
        r = sin(angle) * 127 + 128
        g = sin(angle + 2.0944) * 127 + 128  # +120 degrees
        b = sin(angle + 4.1888) * 127 + 128  # +240 degrees
        
        # Ensure values are in range 0-255
        if (r < 0) r = 0; if (r > 255) r = 255
        if (g < 0) g = 0; if (g > 255) g = 255
        if (b < 0) b = 0; if (b > 255) b = 255
        
        printf "%d %d %d", r, g, b
    }')
    
    echo "$rgb"
}

# Calculate context percentage from JSON input
get_context_percentage() {
    if [ -n "$JSON_INPUT" ]; then
        # Extract input tokens (regular + cached) using jq
        local input_tokens=$(echo "$JSON_INPUT" | jq -r '(.usage.input_tokens // 0) + (.usage.cache_read_input_tokens // 0)' 2>/dev/null)
        
        if [ -n "$input_tokens" ] && [ "$input_tokens" -gt 0 ]; then
            # Calculate used percentage against 200K limit
            local context_used_pct=$(echo "scale=0; $input_tokens * 100 / 200000" | bc)
            local context_remaining_pct=$(echo "scale=0; 100 - $context_used_pct" | bc)
            echo "${context_remaining_pct}"
        else
            echo "TBD"
        fi
    else
        echo "TBD"
    fi
}

# Build the full string
CONTEXT_PCT=$(get_context_percentage)
FULL_STR="${DIRNAME} ${MODEL} \$${COST} ${CONTEXT_PCT}% ctx"
STRING_LENGTH=${#FULL_STR}

# Build output with gradient
OUTPUT=$'\033[0m'
STRING_OUTPUT=""
for (( i=0; i<STRING_LENGTH; i++ )); do
    CHAR="${FULL_STR:$i:1}"
    
    # Calculate position in gradient (0 to 1)
    POSITION=$(echo "scale=4; $i / ($STRING_LENGTH - 1)" | bc)
    
    # Get RGB values for this position
    RGB=($(rainbow_rgb $POSITION))
    R=${RGB[0]}
    G=${RGB[1]}
    B=${RGB[2]}
    
    # Create true color escape sequence with bold
    COLOR_CODE=$'\e[1;38;2;'${R}';'${G}';'${B}'m'
    
    # Append colored character
    OUTPUT+="${COLOR_CODE}${CHAR}"
    STRING_OUTPUT+="${COLOR_CODE}${CHAR}'"
done

# Reset at the end
OUTPUT+=$'\033[0m'
STRING_OUTPUT+="$'\033[0m'"

# Print the final statusline
printf "%s\n" "$OUTPUT"
# to print out the string output
# printf "%s\n" "$STRING_OUTPUT"
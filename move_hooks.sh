#!/bin/bash

# Script to find all hook_output.txt files and move them to ~/.ai_output with sequential numbering
# used in my previous attempts at working with claude code. now the files are in a central location.

# Set the destination directory
DEST_DIR="$HOME/.ai_output"

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Counter for numbering files
counter=1

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Searching for hook_output.txt files...${NC}"

# Find all hook_output.txt files on the system
# Using find with -type f to only match regular files
# 2>/dev/null to suppress permission denied errors
while IFS= read -r -d '' file; do
    if [ -f "$file" ]; then
        # Generate new filename with counter
        new_filename="hook_output_${counter}.txt"
        new_path="$DEST_DIR/$new_filename"
        
        # Move the file
        if mv "$file" "$new_path"; then
            echo -e "${GREEN}Moved:${NC} $file -> $new_path"
            ((counter++))
        else
            echo -e "${RED}Failed to move:${NC} $file"
        fi
        echo $file
    fi
done < <(find ~ -name "hook_output.txt" -type f -print0 2>/dev/null)

# Summary
total_moved=$((counter - 1))
echo -e "\n${YELLOW}Summary:${NC}"
echo "Files moved: $total_moved"
echo "Destination: $DEST_DIR"

if [ $total_moved -eq 0 ]; then
    echo -e "${YELLOW}No hook_output.txt files found on the system.${NC}"
else
    echo -e "${GREEN}All files successfully moved and numbered!${NC}"
fi

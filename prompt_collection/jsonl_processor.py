#!/usr/bin/env python3
"""
JSONL Data Processor
Processes JSONL files from ~/.ai_output/
"""

import json
import os
import sys

def load_jsonl(filepath):
    """Load JSONL file and return list of records"""
    records = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError as e:
                        print(f"Skipping invalid JSON in {filepath}: {e}")
                        continue
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    return records

def process_files():
    """Process all JSONL files in ~/.ai_output/"""
    ai_output_dir = os.path.expanduser("~/.ai_output")
    output_dir = os.path.join(ai_output_dir, "json_list")
    os.makedirs(output_dir, exist_ok=True)
    
    jsonl_files = [f for f in os.listdir(ai_output_dir) if f.endswith('.jsonl')]
    
    print(f"Found {len(jsonl_files)} JSONL files")
    
    for filename in jsonl_files:
        filepath = os.path.join(ai_output_dir, filename)
        print(f"Processing {filename}...")
        
        records = load_jsonl(filepath)
        
        if not records:
            print(f"  No valid records in {filename}")
            continue
            
        print(f"  Records: {len(records)}")
        
        # Convert to JSON array and save
        json_filename = filename.replace('.jsonl', '.json')
        json_filepath = os.path.join(output_dir, json_filename)
        
        with open(json_filepath, 'w') as f:
            json.dump(records, f, indent=2)
        
        print(f"  Saved JSON array: {json_filepath}")

if __name__ == "__main__":
    process_files()
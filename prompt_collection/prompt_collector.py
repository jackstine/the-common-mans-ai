#!/usr/bin/env python3
"""
Prompt Collector - Extract prompts and tool inputs from AI output files
Groups data by session and generates separate files for each session
"""

import json
import os
import argparse
from datetime import datetime
from collections import defaultdict
import sys


def parse_date(date_string):
    """Parse date string in YYYY_MM_DD format"""
    try:
        return datetime.strptime(date_string, '%Y_%m_%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}. Expected YYYY_MM_DD")


def filter_files_by_date(directory, start_date, end_date):
    """Filter JSON files by date range based on filename format YYYY_MM_DD.json"""
    start_dt = parse_date(start_date)
    end_dt = parse_date(end_date)
    
    filtered_files = []
    all_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    for filename in all_files:
        # Extract date from filename (remove .json extension)
        date_part = filename[:-5]  # Remove .json
        try:
            file_dt = parse_date(date_part)
            if start_dt <= file_dt <= end_dt:
                filtered_files.append(os.path.join(directory, filename))
        except ValueError:
            # Skip files that don't match the date format
            print(f"Skipping file with invalid date format: {filename}")
            continue
    
    return sorted(filtered_files)


def load_json_files(file_paths):
    """Load and combine all JSON records from multiple files"""
    all_records = []
    
    for filepath in file_paths:
        print(f"Loading {os.path.basename(filepath)}...")
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    all_records.extend(data)
                else:
                    all_records.append(data)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading {filepath}: {e}")
            continue
    
    return all_records


def collect_prompts(records):
    """Group records by session_id and collect prompts with timestamps"""
    sessions = defaultdict(list)
    
    for record in records:
        session_id = record.get('session_id')
        prompt = record.get('prompt')
        timestamp = record.get('timestamp')
        
        if session_id and prompt and timestamp:
            sessions[session_id].append({
                'prompt': prompt,
                'timestamp': timestamp
            })
    
    return dict(sessions)


def collect_tool_inputs(records):
    """Group records by session_id and collect tool_input data with prompt/query/content"""
    sessions = defaultdict(list)
    
    for record in records:
        session_id = record.get('session_id')
        tool_input = record.get('tool_input')
        timestamp = record.get('timestamp')
        
        if session_id and tool_input and isinstance(tool_input, dict):
            # Check if tool_input has at least one of the required fields
            has_prompt = 'prompt' in tool_input
            has_query = 'query' in tool_input
            has_content = 'content' in tool_input
            
            if has_prompt or has_query or has_content:
                # Extract only the specific fields we want
                extracted_fields = {}
                if has_prompt:
                    extracted_fields['prompt'] = tool_input['prompt']
                if has_query:
                    extracted_fields['query'] = tool_input['query']
                if has_content:
                    extracted_fields['content'] = tool_input['content']
                
                entry = {
                    **extracted_fields,
                    'timestamp': timestamp
                }
                sessions[session_id].append(entry)
    
    return dict(sessions)


def save_session_files(data, output_dir, file_prefix):
    """Save data for each session to separate files"""
    os.makedirs(output_dir, exist_ok=True)
    
    for session_id, session_data in data.items():
        if not session_data:  # Skip empty sessions
            continue
            
        filename = f"{file_prefix}_session_{session_id}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"Saved {len(session_data)} items for session {session_id}: {filepath}")


def main():
    parser = argparse.ArgumentParser(description='Collect prompts and tool inputs from AI output files')
    parser.add_argument('--start', required=True, help='Start date in YYYY_MM_DD format')
    parser.add_argument('--end', required=True, help='End date in YYYY_MM_DD format (inclusive)')
    parser.add_argument('--output-dir', default=os.path.expanduser('~/.ai_output'), help='Output directory for collected files')
    
    args = parser.parse_args()
    
    # Validate dates
    try:
        parse_date(args.start)
        parse_date(args.end)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Setup directories
    input_dir = os.path.expanduser("~/.ai_output")
    if not os.path.exists(input_dir):
        print(f"Error: Input directory does not exist: {input_dir}")
        sys.exit(1)
    
    print(f"Processing files from {args.start} to {args.end}")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {args.output_dir}")
    
    # Filter files by date range
    filtered_files = filter_files_by_date(input_dir, args.start, args.end)
    
    if not filtered_files:
        print("No files found in the specified date range")
        sys.exit(0)
    
    print(f"Found {len(filtered_files)} files in date range")
    
    # Load all records
    all_records = load_json_files(filtered_files)
    print(f"Loaded {len(all_records)} total records")
    
    # Collect prompts
    print("\nCollecting prompts...")
    prompt_sessions = collect_prompts(all_records)
    print(f"Found prompts in {len(prompt_sessions)} sessions")
    
    # Save prompt files to prompts subdirectory
    prompts_dir = os.path.join(args.output_dir, "prompts")
    save_session_files(prompt_sessions, prompts_dir, "prompts")
    
    # Collect tool inputs
    print("\nCollecting tool inputs...")
    tool_input_sessions = collect_tool_inputs(all_records)
    print(f"Found tool inputs in {len(tool_input_sessions)} sessions")
    
    # Save tool input files to tool_inputs subdirectory
    tool_inputs_dir = os.path.join(args.output_dir, "tool_inputs")
    save_session_files(tool_input_sessions, tool_inputs_dir, "tool_inputs")
    
    print(f"\nProcessing complete! Files saved to: {args.output_dir}")


if __name__ == "__main__":
    main()
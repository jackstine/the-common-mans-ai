#!/usr/bin/env python3
"""
Simple Claude Code Hook Data Capture
Takes input from Claude Code hooks and writes to file
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime


# python3 /Users/jake/Projects/hooker/capture_tool_data.py --event= --config=/Users/jake/Projects/hooker/hook_config.json
# obviously the config is not being used at all.
def main():
    """Main entry point for hook processing script"""
    parser = argparse.ArgumentParser(description='Claude Code Hook Data Capture')
    parser.add_argument('--event', required=True, help='Hook event type')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--test', action='store_true', help='Use test.jsonl instead of date-based filename')
    
    args = parser.parse_args()
    
    try:
        # Read input data from stdin
        input_data = {}
        try:
            input_data = json.load(sys.stdin)
        except:
            # No input or invalid JSON, continue with empty data
            pass
        
        # Add event type and timestamp to the data
        input_data['debug_event_type'] = args.event
        input_data['timestamp'] = datetime.now().isoformat()
        
        # Prepare output line
        output_line = f"{json.dumps(input_data)}\n"
        
        # Determine output file
        output_dir = Path.home() / '.ai_output'
        output_dir.mkdir(exist_ok=True)
        
        # Create filename based on current date or test flag
        if args.test:
            output_file = output_dir / 'test.jsonl'
        else:
            date_str = datetime.now().strftime('%Y_%m_%d')
            output_file = output_dir / f'{date_str}.jsonl'
        
        # Simply append to text file
        with open(output_file, 'a') as f:
            f.write(output_line)
        
        # Return success
        sys.exit(0)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
# Prompt Collection Scripts

## Purpose
Collects and analyzes prompts from AI output data to improve prompt engineering and optimize future interactions through systematic analysis.

## Prompt Scripts
**prompt_collector.py** - Extracts prompts and tool inputs from dated JSON files, organizing them by session into `~/.ai_output/prompts/` and `~/.ai_output/tool_inputs/`.
**jsonl_processor.py** - Converts JSONL files to JSON arrays and saves them to `~/.ai_output/json_list/` for further analysis.

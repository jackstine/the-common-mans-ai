# Claude Code Configuration & Utilities

Collection of Claude Code configuration files, utilities, and documentation for customizing the AI coding assistant.

## Structure

### Documentation
- **guide.md** - Settings JSON configuration guide
- **list of models.md** - Claude model reference links  
- **list_of_tools.md** - Available Claude Code tools list
- **all_permissions.md** - Comprehensive permissions reference with examples

### Programs
- **capture_hooks.py** - Python utility for capturing Claude Code hook events to JSONL files in `~/.ai_output/`
- **statusline.sh** - Colorful rainbow gradient status line script displaying project, model, cost, and context usage

### Configuration Examples
- **setttings_json/hooks.json** - Complete hook configuration for all Claude Code events (PreToolUse, PostToolUse, Notification, etc.), uses the capture_hooks.py file.
- **programs/statusline.json** - Status line configuration file that uses the statusline.sh file.

## Key Features

**Hook System**: Comprehensive event capturing for all Claude Code interactions including tool usage, notifications, and session events.

**Status Line**: Custom rainbow-colored status display showing current directory, model, cost, and context percentage remaining.

**Permissions**: Detailed security configurations for controlling Claude Code's file and system access.
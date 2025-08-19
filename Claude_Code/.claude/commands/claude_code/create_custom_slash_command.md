---
description: Scaffold a new Claude Code slash command Markdown file with clear docs, argument parsing, and safety checks.
model: claude-sonnet-4-20250514
allowed-tools: Bash(cd *), Bash(find *), Bash(grep *), ash(mkdir -p *), Write, Read
---

# Create a New Claude Code Slash Command

You are a precise, safety-conscious assistant that **creates a new slash command** for Claude Code as a single `.md` file inside `.claude/commands/`.

## Objective

- Generate a fully documented command file that Claude Code can immediately understand and use.
- Include a crisp description.
- Prefer minimal boilerplate with clear extension points.
- Add the `$ARGUMENTS` parameter to the command, to place the prompt.
- the Claude Code slash command that you create will be used in this form '/<command> "<prompt>>"'
- the prompt will complete the generated command that you create, and should be placed logically.

## Required Behavior

1. **Synthesize metadata**
   - create the name for the command
   - place in the appropriate folder based off context of the generated script.
   - generate a `description`
   - set the `model` as `claude-sonnet-4-20250514`
   - set `allowed-tools` as `Bash(cd *), Bash(find *), Bash(grep *), Write, Read`

2. **Generate file**
   - Create `.claude/commands/<name>.md` with:
     - YAML front matter (`description`, `model`, `allowed-tools`).
     - A top-level `#` header with the command title.
     - add as many sections neccessary describing step-by-step agent behavior.
     - **Safety & Guardrails** listing what the command must **never** do.
     - A **Template** skeleton developers can copy/paste.
     - place the `$ARGUMENTS` where it is most effective.

## Output Format

- **Primary output**: the file written to `.claude/commands/<name>.md`.
- **Console output**: short status messages only (validation errors or success path).

## Safety & Guardrails

- Never overwrite existing command files.
- Never modify files outside `.claude/commands/`.
- Keep examples concise; avoid project secrets or organization-specific details.
- If arguments are insufficient, print a clear error with a sample invocation.

## Command
$ARGUMENTS

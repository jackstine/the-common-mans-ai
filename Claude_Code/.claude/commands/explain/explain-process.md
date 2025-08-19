---
description: "Analyze and document processes with summaries and user stories in AI documentation folder"
model: "claude-opus-4-1-20250805"
allowed-tools: ["Bash(cd *)", "Bash(find *)", "Bash(grep *)", "Write", "Read"]
---

# Explain Process

Analyzes a process within the codebase and creates comprehensive documentation with a summary followed by detailed user stories. Documentation is placed in the AI documentation folder for easy reference.

## Command Logic

1. **Process Discovery**
   - Search codebase for files related to the specified process
   - Identify key components: source files, tests, configurations
   - Map dependencies and data flow

2. **Analysis Phase**
   - Read and understand process implementation
   - Identify entry points, main logic, and outputs
   - Document error handling and edge cases

3. **Documentation Generation**
   - Create process summary (high-level overview)
   - Generate user stories that explain detailed workflow
   - Include code references with file:line patterns

4. **File Placement**
   - Default location: `ai_docs/business_logic/<process-name>/`
   - Filename: `<process-name>_process_explanation.md`

## Safety & Guardrails

- **Never** modify existing process code during analysis
- **Never** expose sensitive data or credentials in documentation
- **Never** create documentation outside the ai_docs folder unless explicitly specified
- **Never** overwrite existing documentation without confirmation

## Design Notes

This command bridges the gap between code implementation and business understanding by creating process documentation that explains both the "what" and "why" of system workflows. The user story format makes complex technical processes accessible to non-technical stakeholders.

## Template

```markdown
# Process Name: [PROCESS_NAME]

## Summary
[High-level overview of what this process does, its purpose, and key outcomes]

## User Stories

### Story 1: [Action/Goal]
**As a** [user type]
**I want** [specific functionality]
**So that** [business value/outcome]

**Implementation Details:**
- Entry point: `file_path:line_number`
- Key functions: `file_path:line_number`
- Data flow: [describe data transformation]

### Story 2: [Next Action/Goal]
[Continue pattern for each major step in the process]

## Technical References
- Configuration: `file_path:line_number`
- Tests: `file_path:line_number`
- Dependencies: [list key dependencies]

## Error Handling
[Document known error cases and how they're handled]
```

Explain a process within the codebase and write a summary followed by a set of user stories that explain the process in detail. Documentation will be placed in the AI documentation folder to create a comprehensive explanation of the process details.

$ARGUMENTS

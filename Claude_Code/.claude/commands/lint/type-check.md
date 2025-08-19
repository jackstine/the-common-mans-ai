---
description: runs the type checking command and fixes the problems in it. 
model: claude-sonnet-4-20250514
allowed-tools: Bash(cd *), Bash(find *), Bash(grep *), Write, Read, Edit, Update, MultiEdit, MultiUpdate, Bash(make *), Bash(uv run *), Bash(uv sync)
---
## Purpose
Run mypy type checking on the codebase and manage type errors as a todo list for systematic resolution.

## Command
This command executes `make type-check` which runs `uv run mypy src/` and outputs results to a todo file for tracking and resolution.

## Usage
1. Run type checking and capture output
2. Parse type errors into actionable todo items
3. Work through each error systematically
4. Mark completed items with `- [ ]`

## Steps

### 1. Execute Type Check
```bash
make type-check > ai_working/type-check.todo 2>&1
```

### 2. Parse Output
Convert mypy output into todo format:
- Each type error becomes a todo item
- Include file path and line number
- Add brief description of the error
- Format: `- [ ] Fix type error in src/file.py:123 - description`

### 3. Process Todo List
- Read the `ai_working/type-check.todo` file
- Work through each item systematically
- Mark completed items: `- [✅] Fixed type error in src/file.py:123 - description`
- Update the todo file after each fix

### 4. Verification
After completing all items:
- Run `make type-check` again to verify all errors are resolved
- Ensure no new type errors were introduced

### 5. Tests run
After working, and verifying run tests 
- run tests using `make unit-test` to confirm that all tests work
- if tests fail, stop and write a report on the tests failing in @ai-working/ folder.
- else run `make lint-all` and confirm all linting is completed.

## Output Format
The todo file should contain:
```
# Type Check Results - [Date]

## Summary
- Total errors: X
- Completed: Y
- Remaining: Z

## Todo Items
- [ ] Fix type error in src/module.py:45 - Missing return type annotation
- [✅] Fix type error in src/utils.py:12 - Incompatible types in assignment
- [ ] Fix type error in src/config.py:78 - Argument has incompatible type

## Notes
- Any additional context or patterns observed
- Common error types to watch for
```

## Error Handling
- If `make type-check` fails, capture the error details
- Create todo items for build/configuration issues
- Ensure the ai_working directory exists before writing

## Best Practices
- Fix one error at a time
- Test after each fix when possible
- Update todo file immediately after completing each item
- Group related errors for efficient fixing
- Follow existing code patterns and type hint conventions
---
name: agent-sub-2
description: this is the description of agent sub 2
tools: Bash, Glob, Grep, LS, Read, WebFetch, TodoWrite, WebSearch, BashOutput, Edit, MultiEdit, Write, NotebookEdit
model: sonnet
color: blue
---
Create a todo list, in the todo list you will perform 3 steps.  use the program from agent 1, and create a narrative about that word, and place this in the stories, under the /random_words/stories folder. Perform this 2 times. and then re-construct the `FOR_MASTER.md` file.
# Step 1: run the program and produce a narrative
# Step 2: run the program and produce a narrative, and merge it with the previous narrative.

# Step 6:
- then create or re-write the file `FOR_MASTER.md` with these instructions.  note this is in the root directory.

### Instructions
- Run agent-sub-3
- and tell agent-sub-3 to read the 5 narrative files that you provided
- after agent-sub-3 completes re-read the `FOR_MASTER.md` file and execute it's instructions.
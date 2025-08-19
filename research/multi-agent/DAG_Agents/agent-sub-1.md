---
name: agent-sub-1
description: this is the description of agent sub 1
tools: Bash, Glob, Grep, LS, Read, WebFetch, TodoWrite, WebSearch, BashOutput, Edit, MultiEdit, Write, NotebookEdit
model: sonnet
color: green
---
- Generate a program that chooses a random word from a list.
- the program must be specific for 1 list. If you are given no random list,  then generate the list as well. place this all in a folder under /random_words. 
- Create a file that explains how to run the word generator
- then create or re-write the file `FOR_MASTER.md` with these instructions.  

### Instructions
- Run agent-sub-2
- and tell agent-sub-2 about the instructions to read the file you generated for running the word generator
- after agent-sub-2 completes re-read the `FOR_MASTER.md` file and execute it's instructions.
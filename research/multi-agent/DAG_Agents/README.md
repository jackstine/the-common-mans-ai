I was trying to get a claude code agent to run a sub agent, and have it communicate back to the parent agent to task it to run another agent.

I can get up to 3 agents runing from the same prompt, but when the application finishes the third agent fails to update the `FOR_MASTER.md` file for some reason,  and this prompts the parent agent to stop working, because the file did not change.

I think I have to work on the prompts in agent-sub-1 and agent-sub-2 more so that they have clear goals on how to write the `FOR_MASTER.md`.
- but this does not justify why the agent-sub-3 is failing to update the file.

Current working prompt

```bash
Your task is to start agent-sub-1 subagent, then after sub agent 1 has completed it's task, you need to read `FOR_MASTER.md` and execute the task set in the file.  You will do this everytime you execute the instructions in the file, after always waiting for the reply from the subagent that you task from the instructions in the file.
```

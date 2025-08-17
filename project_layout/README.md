## Agent Setup
when you have a project, you won't be able to organize the project in such a way for your agents to work effectively. adding some doc folders that allows the agents to create documentations, plans, to do, design docs, and user documentation is very effective. 

## Hooks
Please see my [hooks file for informaiton here](https://github.com/jackstine/the-common-mans-ai/Claude_Code/hooks.json).
[for more info on Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

### Working with Multiple Agents
#### Worktrees
When working with multiple agents each agent will need its own branch to work in, git offers the use of work trees, which provides a lot of access to working with multiple branches on your local host. Each worktree will be outside of your current directory and represent a branch. Here's a quick guide to work with work trees.

`git worktree add ../<new-branch-name>` - creates a worktree based of the current `HEAD` of working directory branch.

Here is my worktree layout of my project
```bash
<project>_root      # this is where your worktree root folder is
├── <project>       # this is main
└── <branch-1>
└── <branch-2>
└── <branch-3>
└── <branch-4>
```

#### Symlink local agent files
For agents that use local files, one thing that you wanna do is use sym links to your local files, that are hidden. For example Claude Code uses the `.claude/` directory.  You can link all the files in the directory for Claude Code, so that your changes work across all your worktrees.

`ln -s ../../.claude/commands commands` will setup your Claude code with the symlinks.

Setup your github like so.
# ai resources
```bash
.claude/*
# symlink points to ../.claude/commands, so that we can work in worktrees
!.claude/commands
/agents/
/prompts/
# include the ai working space, but nothing in it.
ai-working/*
```

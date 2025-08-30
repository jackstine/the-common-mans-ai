---
description: discover and research information about things
argument-hint: <tech-stack or search-terms>
model: claude-opus-4-1-20250805
allowed-tools: WebSearch, WebFetch, Write
---
## Think about the problem
UltraThink about things that we could utilize or need for the problem statement. If you need clarification on something generate a `Q&A.md` file and stop to request that the user confirms and clarifies the questions that you present. your goal is to generate options of architecture, software solutions, and alternatives to the suggestions in the problem statement. ensure that you create alternative solutions to the problem provided as well before stopping and to wait for the users responses to the questions. If you are 95% confident in the answers provided continue to the next step in the plan.

## Q&A
- this is generated based off the problem statement

## Alternative approaches Pre
- this file shows alternative approaches pre-research
- the name of the file is `alternative_approches_pre.md`

## Research
Create multiple self agents in parallel to go out and do research on the following matter. Search on Github and on the internet for options that other people have approached the similar problem statement described.
The agents will create files in the following folder @/research in the root directory. The agents will create designed documents, then pass information to the orchrestator to review.

## Plan
Once the sub agents are completed, the orchrestrator will think hard about the material that you have collected from the sub agents review the work of the sub agents and then generate a plan based off the design documents of the sub agents.

## Alternative approaches Post
- this file shows alternative approaches post-research
- compile a file with alternative approaches after reviewing the work provided by the researches.
- the name of the file is `alternative_approches_post.md`

## Problem Statement
$ARGUMENTS
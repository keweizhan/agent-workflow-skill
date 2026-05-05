---
name: task-graph-executor
description: Decompose complex user tasks into multi-step workflows and execute them using dependency-aware task graph (DAG).
version: 1.0.0
metadata:
  openclaw:
    emoji: "🧠"
    tags: ["agent", "workflow", "automation", "task-execution"]
---

# Task Graph Executor Skill

## When to use this skill

Use this skill when the user request involves:

- Multi-step tasks
- Tasks with dependencies
- Complex workflows (analyze → process → generate)
- Automation pipelines

Examples:

- "Analyze this repo and summarize it"
- "Research a topic and write a report"
- "Process a dataset and visualize results"

---

## What this skill does

This skill transforms a single user request into a structured execution workflow:

1. Break task into smaller subtasks
2. Identify dependencies between tasks
3. Execute tasks in correct order
4. Parallelize tasks where possible
5. Combine results into final output

---

## Execution Strategy

### Step 1: Task Decomposition

Convert user request into structured tasks:

Example:

User request:
"Analyze a GitHub repo and summarize it"

Output:

- task1: clone repository
- task2: analyze codebase (depends on task1)
- task3: generate summary (depends on task2)

---

### Step 2: Build Task Graph (DAG)

- Represent tasks as nodes
- Represent dependencies as edges
- Ensure no circular dependencies

---

### Step 3: Execution Rules

- Execute tasks with no dependencies first
- Wait for dependencies before executing dependent tasks
- Execute independent tasks in parallel if possible

---

### Step 4: Tool Usage

For each task, choose appropriate tools:

- Code analysis → code tools
- Research → search tools
- Writing → LLM generation

---

### Step 5: Error Handling

If a task fails:

- Retry once
- If still failing, skip and continue
- Record failure in final output

---

### Step 6: Output Format

Return structured result:

```json
{
  "tasks": [...],
  "execution_order": [...],
  "result": "...",
  "status": "success / partial / failed"
}

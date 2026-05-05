# Agent Workflow Skill

A reusable AI agent skill that enables multi-step task execution using DAG-based planning and dependency-aware orchestration.

---

## Overview

This skill allows AI agents to:

- Decompose complex tasks into smaller steps
- Build dependency-aware task graphs (DAG)
- Execute tasks sequentially or in parallel
- Produce structured outputs

---

## Example

### Input

Analyze a GitHub repository and generate a summary

### Execution Plan

1. Clone repository
2. Analyze code structure
3. Generate summary

---

## Key Features

- LLM-based task decomposition  
- DAG-based execution model  
- Dependency-aware scheduling  
- Parallel execution support  

---

## Motivation

Most existing AI systems only support single-step tool calls.

This skill introduces:

- Multi-step reasoning  
- Structured execution  
- Workflow-level intelligence  

---

## Use Cases

- Codebase analysis  
- Research and report generation  
- Data processing pipelines  
- Automation workflows  

---

## Installation (ClawHub)

```bash
npx clawhub install agent-workflow-skill
```

---

## Demo

Run:

```bash
python examples/demo.py
```

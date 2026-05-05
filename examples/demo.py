import json

def decompose_task(user_input):
    """
    Simulate LLM-based task decomposition.

    Given a user input, return a list of tasks with dependencies.
    This mimics how an LLM would convert natural language into a task graph.
    """
    if "repo" in user_input:
        return [
            {"id": 1, "task": "clone repository", "depends_on": []},
            {"id": 2, "task": "analyze codebase", "depends_on": [1]},
            {"id": 3, "task": "generate summary", "depends_on": [2]},
        ]
    else:
        return [
            {"id": 1, "task": "search information", "depends_on": []},
            {"id": 2, "task": "summarize results", "depends_on": [1]},
        ]

def execute_tasks(tasks):
    """
    Execute tasks based on dependency order.

    Tasks are executed only when all their dependencies are completed.
    This simulates a DAG-based task scheduler.
    """
    completed = set()
    execution_order = []

    while len(completed) < len(tasks):
        for task in tasks:
            # Skip already completed tasks
            if task["id"] in completed:
                continue

            # Check if all dependencies are satisfied
            if all(dep in completed for dep in task["depends_on"]):
                print(f"Executing: {task['task']}")
                execution_order.append(task["task"])
                completed.add(task["id"])

    return execution_order

if __name__ == "__main__":
    user_input = "Analyze a GitHub repo and summarize it"

    print("User Input:")
    print(user_input)

    print("\nDecomposed Tasks:")
    tasks = decompose_task(user_input)
    print(json.dumps(tasks, indent=2))

    print("\nExecution:")
    result = execute_tasks(tasks)

    print("\nExecution Order:")
    print(result)

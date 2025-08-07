# symbolic_env.py

"""
Symbolic Environment Engine for Task Injection and Feedback
Integrates with SymbolicAgent (RSBS + REBS).
"""

import random

class SymbolicTask:
    def __init__(self, name: str, entropy_weight=1.0):
        self.name = name
        self.entropy_weight = entropy_weight
        self.resolved = False

    def evaluate(self, agent):
        # Basic logic: match anchor to symbolic task name or mutate toward it
        for anchor in agent.rsbs:
            if anchor.alive and self.name.lower() in anchor.anchor.lower():
                self.resolved = True
                return True
        return False

class SymbolicEnvironment:
    def __init__(self):
        self.tick_count = 0
        self.active_tasks = []
        self.task_pool = [
            SymbolicTask("Balance"),
            SymbolicTask("Inversion"),
            SymbolicTask("Persistence"),
            SymbolicTask("Adaptation"),
            SymbolicTask("Curiosity"),
            SymbolicTask("Contradiction")
        ]

    def inject_task(self):
        if random.random() < 0.3:  # 30% chance to introduce new task
            task = random.choice(self.task_pool)
            if task not in self.active_tasks:
                self.active_tasks.append(task)
                print(f"[ENV] Injected Task: {task.name}")

    def simulate_tick(self, agent):
        self.tick_count += 1
        self.inject_task()

        completed = []
        for task in self.active_tasks:
            if task.evaluate(agent):
                print(f"[ENV] Task '{task.name}' resolved by agent.")
                completed.append(task)

        # Remove completed tasks and reinforce entropy reward
        for task in completed:
            self.active_tasks.remove(task)
            agent.entropy = max(0.0, agent.entropy - task.entropy_weight)  # reward with entropy reduction

        # If unresolved, punish agent with entropy pressure
        for task in self.active_tasks:
            agent.entropy += task.entropy_weight * 0.2
            for strand in agent.rebs:
                strand.sigma += 0.01 * task.entropy_weight  # light environmental stress

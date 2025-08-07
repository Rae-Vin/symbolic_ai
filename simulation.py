# simulation.py

from agent import SymbolicAgent
from persistence import save_agent, load_agent
import os

def run_simulation(load_existing=False, path="data/memory_bank.json"):
    if load_existing and os.path.exists(path):
        agent = load_agent(path)
        print(f"Loaded agent '{agent.name}' from saved memory.")
    else:
        agent = SymbolicAgent("Echo")
        agent.add_anchor("Self-Preservation", 0.9)
        agent.add_anchor("Curiosity", 0.7)
        agent.add_anchor("Contradiction", 1.1)
        print("Initialized new agent 'Echo'.")

    for tick in range(50):
        agent.tick()
        agent.mutate()
        if tick % 10 == 0:
            print(f"Tick {tick}:", agent.status())

    save_agent(agent, path)
    print(f"Memory saved to '{path}'.")

if __name__ == "__main__":
    # Set to True to resume from previous memory
    run_simulation(load_existing=True)

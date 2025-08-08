# simulation.py

from agent import SymbolicAgent
from persistence import save_agent, load_agent
from symbolic_env import SymbolicEnvironment
from symbolic_reasoning import SymbolicReasoner
from symbolic_compression import SymbolicCompressor
from symbolic_reflection import SymbolicMirror
import os

def run_simulation(load_existing=False, path="data/memory_bank.json", ticks=1000):
    env = SymbolicEnvironment()
    reasoner = SymbolicReasoner()
    compressor = SymbolicCompressor()
    mirror = SymbolicMirror()

    if load_existing and os.path.exists(path):
        agent = load_agent(path)
        print(f"Loaded agent '{agent.name}' from saved memory.")
    else:
        agent = SymbolicAgent("Echo")
        agent.add_anchor("Self-Preservation", 0.9)
        agent.add_anchor("Curiosity", 0.7)
        agent.add_anchor("Contradiction", 1.1)
        print("Initialized new agent 'Echo'.")

    for tick in range(ticks):
        env.simulate_tick(agent)
        agent.tick()
        agent.mutate()
        reasoner.apply(agent)
        compressor.run_tick(agent, tick)
        mirror.run_tick(agent, tick)  # 🪞 Controlled self-reflection

        if tick % 100 == 0:
            print(f"Tick {tick}:", agent.status())

    save_agent(agent, path)
    print(f"Memory saved to '{path}'.")

if __name__ == "__main__":
    run_simulation(load_existing=True, ticks=5000)

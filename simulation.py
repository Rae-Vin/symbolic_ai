# simulation.py

from agent import SymbolicAgent

def run_simulation():
    agent = SymbolicAgent("Echo")
    agent.add_anchor("Self-Preservation", 0.9)
    agent.add_anchor("Curiosity", 0.7)
    agent.add_anchor("Contradiction", 1.1)

    for tick in range(50):
        agent.tick()
        agent.mutate()
        if tick % 10 == 0:
            print(f"Tick {tick}:", agent.status())

if __name__ == "__main__":
    run_simulation()

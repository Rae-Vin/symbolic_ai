# persistence.py

import json
from pathlib import Path
from agent import SymbolicAgent
from rsbs import RSBS
from rebs import REBS

def save_agent(agent: SymbolicAgent, path="data/memory_bank.json"):
    """Save the symbolic agent's memory to disk."""
    memory = {
        'name': agent.name,
        'entropy': agent.entropy,
        'rsbs': [r.to_dict() for r in agent.rsbs],
        'rebs': [r.to_dict() for r in agent.rebs]
    }
    with open(Path(path), 'w') as f:
        json.dump(memory, f, indent=2)

def load_agent(path="data/memory_bank.json") -> SymbolicAgent:
    """Load a symbolic agent from memory on disk."""
    with open(Path(path), 'r') as f:
        memory = json.load(f)

    agent = SymbolicAgent(memory['name'])
    agent.entropy = memory['entropy']
    agent.rsbs = [RSBS.from_dict(d) for d in memory['rsbs']]
    agent.rebs = [REBS.from_dict(d) for d in memory['rebs']]
    return agent

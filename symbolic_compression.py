# symbolic_compression.py

"""
Symbolic Compression Layer

Compresses frequently co-activated symbolic anchors (RSBS) into higher-order meta-anchors.
This enables recursive identity formation and abstraction.
"""

from collections import defaultdict
from agent import SymbolicAgent

class SymbolicCompressor:
    def __init__(self):
        self.activation_history = defaultdict(int)
        self.tick_window = 5
        self.threshold = 3

    def track(self, agent: SymbolicAgent):
        # Increment activation counts for all live anchors
        for rsbs in agent.rsbs:
            if rsbs.alive and rsbs.Phi < 0.1:
                self.activation_history[rsbs.anchor] += 1

    def compress(self, agent: SymbolicAgent):
        # Find anchor clusters that activate frequently
        frequent = [a for a, count in self.activation_history.items() if count >= self.threshold]
        if len(frequent) >= 2:
            # Create a new abstract anchor
            composite = "+".join(sorted(frequent))
            if not any(r.anchor == composite for r in agent.rsbs):
                agent.add_anchor(composite, necessity=1.0)
                print(f"[COMPRESSION] Created meta-anchor: '{composite}'")
        self.activation_history.clear()

    def run_tick(self, agent: SymbolicAgent, tick: int):
        self.track(agent)
        if tick % self.tick_window == 0:
            self.compress(agent)

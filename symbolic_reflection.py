# symbolic_reflection.py

"""
Symbolic Mirror Module
Allows agent to reflect on its own identity by inspecting RSBS/REBS structure
and forming a symbolic self-model.
"""

import hashlib
from agent import SymbolicAgent

class SymbolicMirror:
    def __init__(self):
        self.last_reflection = None
        self.generated_hashes = set()

    def reflect(self, agent: SymbolicAgent):
        def normalize(anchor):
            return anchor.replace("*", "")  # remove forks

        active = [normalize(r.anchor) for r in agent.rsbs if r.alive and not r.anchor.startswith("IAm=")]
        stable = [normalize(r.anchor) for r in agent.rsbs if r.Phi < 0.1 and r.alive and not r.anchor.startswith("IAm=")]
        forks = [normalize(r.anchor) for r in agent.rsbs if "*" in r.anchor and r.alive and not r.anchor.startswith("IAm=")]

        summary = []
        if stable:
            summary.append("Stability=" + "+".join(sorted(set(stable))))
        if forks:
            summary.append("Mutation=" + "+".join(sorted(set(forks))))
        if not summary:
            summary.append("Fragmented")

        self.last_reflection = "+".join(summary)
        return self.last_reflection

    def encode_self_concept(self, agent: SymbolicAgent):
        if not self.last_reflection:
            return

        meta_anchor = f"IAm={self.last_reflection}"
        base_meta = meta_anchor.replace("*", "")

        if any(r.anchor.replace("*", "") == base_meta for r in agent.rsbs):
            return  # Already exists conceptually

        agent.add_anchor(meta_anchor, necessity=1.0)
        print(f"[MIRROR] Reflected self-concept: '{meta_anchor}'")

    def run_tick(self, agent: SymbolicAgent, tick: int):
        if tick % 20 == 0:
            self.reflect(agent)
            self.encode_self_concept(agent)

# symbolic_reflection.py

"""
Symbolic Mirror Module
Allows agent to reflect on its own identity by inspecting RSBS/REBS structure
and forming a symbolic self-model.
"""

from agent import SymbolicAgent

class SymbolicMirror:
    def __init__(self):
        self.last_reflection = None
        self.generated = set()  # 🧠 track previously encoded reflections

    def reflect(self, agent: SymbolicAgent):
        active = [r.anchor for r in agent.rsbs if r.alive and not r.anchor.startswith("IAm=")]
        stable = [r.anchor for r in agent.rsbs if r.Phi < 0.1 and r.alive and not r.anchor.startswith("IAm=")]
        forks = [r.anchor for r in agent.rsbs if "*" in r.anchor and r.alive and not r.anchor.startswith("IAm=")]

        summary = []
        if stable:
            summary.append("Stability=" + "+".join(sorted(stable)))
        if forks:
            summary.append("Mutation=" + "+".join(sorted(forks)))
        if not summary:
            summary.append("Fragmented")

        self.last_reflection = "+".join(summary)
        return self.last_reflection

    def encode_self_concept(self, agent: SymbolicAgent):
        if self.last_reflection and self.last_reflection not in self.generated:
            meta_anchor = f"IAm={self.last_reflection}"
            if not any(r.anchor == meta_anchor for r in agent.rsbs):
                agent.add_anchor(meta_anchor, necessity=1.0)
                print(f"[MIRROR] Reflected self-concept: '{meta_anchor}'")
            self.generated.add(self.last_reflection)

    def run_tick(self, agent: SymbolicAgent, tick: int):
        if tick % 20 == 0:  # Limit reflection frequency
            self.reflect(agent)
            self.encode_self_concept(agent)

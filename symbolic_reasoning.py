# symbolic_reasoning.py

"""
Symbolic Reasoning Engine
Evaluates logical relationships between RSBS anchors and injects symbolic inferences
"""

from typing import List
from agent import SymbolicAgent

class SymbolicRule:
    def __init__(self, premise: str, conclusion: str, entropy_cost: float = 0.2):
        self.premise = premise.lower()
        self.conclusion = conclusion
        self.entropy_cost = entropy_cost

    def applies_to(self, anchor: str) -> bool:
        return self.premise in anchor.lower()

    def infer(self, anchor: str) -> str:
        return self.conclusion

class SymbolicReasoner:
    def __init__(self):
        self.rules: List[SymbolicRule] = []
        self._init_default_rules()

    def _init_default_rules(self):
        self.rules.append(SymbolicRule("curiosity", "exploration"))
        self.rules.append(SymbolicRule("contradiction", "reconciliation"))
        self.rules.append(SymbolicRule("persistence", "stability"))
        self.rules.append(SymbolicRule("adaptation", "resilience"))
        self.rules.append(SymbolicRule("inversion", "symmetry"))

    def apply(self, agent: SymbolicAgent):
        active_anchors = [r for r in agent.rsbs if r.alive]
        inferred = []

        for rule in self.rules:
            for anchor in active_anchors:
                if rule.applies_to(anchor.anchor):
                    inferred_anchor = rule.infer(anchor.anchor)
                    if not any(a.anchor == inferred_anchor for a in agent.rsbs):
                        agent.add_anchor(inferred_anchor, anchor.N * 0.9)
                        agent.entropy += rule.entropy_cost
                        inferred.append(inferred_anchor)

        if inferred:
            print(f"[REASONER] Inferred new anchors: {inferred}")

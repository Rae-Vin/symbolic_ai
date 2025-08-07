# agent.py

from rsbs import RSBS
from rebs import REBS
import random
from typing import List

class SymbolicAgent:
    def __init__(self, name: str):
        self.name = name
        self.rsbs: List[RSBS] = []
        self.rebs: List[REBS] = []
        self.entropy = 0.0

    def add_anchor(self, anchor: str, necessity: float):
        self.rsbs.append(RSBS(anchor, necessity))
        self.rebs.append(REBS())

    def tick(self):
        for i, strand in enumerate(self.rsbs):
            if not strand.alive:
                continue
            used = random.random() < 0.3
            if used:
                strand.reinforce()
            else:
                strand.decay()
            self.rebs[i].update(used)

        self.entropy += sum(r.sigma for r in self.rebs)

    def mutate(self):
        for i, (r, e) in enumerate(zip(self.rsbs, self.rebs)):
            if e.omega and r.alive:
                r.alive = False
                if random.random() < 0.6:
                    new_anchor = r.anchor + "*"
                    self.add_anchor(new_anchor, r.N * random.uniform(0.8, 1.2))

    def status(self):
        return [(r.anchor, r.alive, round(r.Phi, 2)) for r in self.rsbs]

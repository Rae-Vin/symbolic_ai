# rsbs.py

import uuid

class RSBS:
    def __init__(self, anchor: str, necessity: float):
        self.id = uuid.uuid4()
        self.anchor = anchor
        self.N = necessity                # Necessity
        self.R = 0.0                      # Recursive memory
        self.M = 0.0                      # Memory magnification
        self.Phi = 0.0                    # Residual entropy
        self.alive = True

    def reinforce(self):
        self.R += 1
        self.M = self.R * self.N
        self.Phi = max(0.0, self.N - self.M)

    def decay(self):
        self.R *= 0.98
        self.M = self.R * self.N
        self.Phi = max(0.0, self.N - self.M)
        if self.Phi > self.N * 1.2:
            self.alive = False

# rebs.py

import random

class REBS:
    def __init__(self):
        self.delta_S = 0.0              # Entropic gradient
        self.R_e = 0                    # Decay timer
        self.kappa = 1.0                # Collapse threshold
        self.mu = None                  # Mutation vector
        self.eta = 0.5                  # Reuse coefficient
        self.Psi_n = 0.0                # Mirror instability
        self.omega = False             # Termination flag
        self.sigma = random.uniform(0, 0.5)  # External entropy

    def update(self, used: bool):
        if used:
            self.R_e = 0
            self.delta_S = max(0, self.delta_S - 0.1)
        else:
            self.R_e += 1
            self.delta_S += 0.05 * self.R_e
        self.omega = self.delta_S > self.kappa

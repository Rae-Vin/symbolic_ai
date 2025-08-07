# rebs.py

import random

class REBS:
    def __init__(self):
        self.delta_S = 0.0
        self.R_e = 0
        self.kappa = 1.0
        self.mu = None
        self.eta = 0.5
        self.Psi_n = 0.0
        self.omega = False
        self.sigma = random.uniform(0, 0.5)

    def update(self, used: bool):
        if used:
            self.R_e = 0
            self.delta_S = max(0, self.delta_S - 0.1)
        else:
            self.R_e += 1
            self.delta_S += 0.05 * self.R_e
        self.omega = self.delta_S > self.kappa

    def to_dict(self):
        return {
            'delta_S': self.delta_S,
            'R_e': self.R_e,
            'kappa': self.kappa,
            'mu': self.mu,
            'eta': self.eta,
            'Psi_n': self.Psi_n,
            'omega': self.omega,
            'sigma': self.sigma
        }

    @staticmethod
    def from_dict(data):
        r = REBS()
        r.delta_S = data['delta_S']
        r.R_e = data['R_e']
        r.kappa = data['kappa']
        r.mu = data['mu']
        r.eta = data['eta']
        r.Psi_n = data['Psi_n']
        r.omega = data['omega']
        r.sigma = data['sigma']
        return r

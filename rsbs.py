# rsbs.py

import uuid

class RSBS:
    def __init__(self, anchor: str, necessity: float):
        self.id = uuid.uuid4()
        self.anchor = anchor
        self.N = necessity
        self.R = 0.0
        self.M = 0.0
        self.Phi = 0.0
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

    def to_dict(self):
        return {
            'id': str(self.id),
            'anchor': self.anchor,
            'necessity': self.N,
            'R': self.R,
            'M': self.M,
            'Phi': self.Phi,
            'alive': self.alive
        }

    @staticmethod
    def from_dict(data):
        r = RSBS(data['anchor'], data['necessity'])
        r.id = uuid.UUID(data['id'])
        r.R = data['R']
        r.M = data['M']
        r.Phi = data['Phi']
        r.alive = data['alive']
        return r

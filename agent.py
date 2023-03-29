import numpy as np


class Agent:

    def __init__(self):
        self.actions = {0: "'w'", 1: "'a'", 2: "'s'", 3: "'d'"}
        self.state_space = {}

    def pick_action(self):
        return self.actions[np.random.randint(0, len(self.actions))]

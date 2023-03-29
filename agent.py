import numpy as np


class NaiveAgent:

    def __init__(self, actions):
        self.actions = { "up", "down", "left", "right" }
        self.state_space = {}

    def pick_action(self, reward, obs):
        return self.actions[np.random.randint(0, len(self.actions))]

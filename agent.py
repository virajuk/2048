import gamegrid
import numpy as np
#
# gamegrid = GameGrid()
#
class NaiveAgent():

    def __init__(self, actions):
        self.actions = { "up", "down", "left", "right" }
        self.state_space = {}

    def pickAction(self, reward, obs):
        return self.actions[np.random.randint(0, len(self.actions))]

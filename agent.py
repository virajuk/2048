import numpy as np

# from puzzle import GameGrid


class Agent:

    def __init__(self):
        self.actions = {0: "'w'", 1: "'a'", 2: "'s'", 3: "'d'"}
        self.state_space = {}

    def pick_action(self):
        return self.actions[np.random.randint(0, len(self.actions))]


if __name__ == '__main__':
    pass

    # agent = Agent()
    # gamegrid = GameGrid()


    # agent.set_game(gamegrid)
    # print(len(agent.game()))

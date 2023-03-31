import random
from tkinter import Frame, Label, CENTER
import time

import logic
import constants as c
from agent import Agent
from config import config


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
                         c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right,
                         c.KEY_UP_ALT: logic.up, c.KEY_DOWN_ALT: logic.down,
                         c.KEY_LEFT_ALT: logic.left, c.KEY_RIGHT_ALT: logic.right,
                         c.KEY_H: logic.left, c.KEY_L: logic.right,
                         c.KEY_K: logic.up, c.KEY_J: logic.down
                         }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.score = 0
        self.agent = Agent()
        # self.agent_play_game()

        # print(config.get("episodes"))

        self.update_idletasks()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.matrix = logic.add_two(self.matrix)
        self.matrix = logic.add_two(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def agent_play_game(self):

        self.matrix, done, self.score = self.commands[self.agent.actions[random.randint(0, 3)]](self.matrix, self.score)




        if logic.game_state(self.matrix) == 'win':

            self.destroy()
            return
            # return self.score

        if done:
            self.matrix = logic.add_two(self.matrix)
            self.update_grid_cells()

            self.win_or_loose()

        if logic.game_state(self.matrix) == 'not over':

            time.sleep(0.5)
            self.agent_play_game()

        return self.score

    def key_down(self, event):
        key = repr(event.char)

        if key == "'q'":
            self.quit()

        if key in self.commands:

            self.matrix, done, self.score = self.commands[repr(event.char)](self.matrix, self.score)

            if done:

                self.matrix = logic.add_two(self.matrix)
                self.update_grid_cells()

                print(self.score)
                self.win_or_loose()

    def win_or_loose(self):

        if logic.game_state(self.matrix) == 'win':
            self.grid_cells[1][1].configure(
                text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(
                text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        if logic.game_state(self.matrix) == 'lose':
            self.grid_cells[1][1].configure(
                text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(
                text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)


if __name__ == '__main__':

    for i in range(0, 3):

        gamegrid = GameGrid()
        score = gamegrid.agent_play_game()
        print(score)
        del gamegrid

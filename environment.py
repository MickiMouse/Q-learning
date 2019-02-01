import numpy as np


class Env:
    def __init__(self):
        self.env = np.zeros((3, 3), dtype=int)
        self.count = np.zeros((3, 3), dtype=int)
        self.count_enemy = np.zeros((3, 3), dtype=int)
        print("Environment", "\n", self.env)

    def move(self, x: int, y: int):
        if self.count[y, x] == 0 and self.count_enemy[y, x] == 0:
            self.count[y, x] = 1
            self.env[y, x] = 10
        else:
            raise IndexError("Here is busy")
        print("My move", "\n", self.env)

        _y, _x = np.unravel_index(self.env.argmin(), self.count.shape)
        self.enemy_move(_x, _y)

        if self.check_win() or self.check_lose():
            return self.dell()

    def enemy_move(self, x: int, y: int):
        self.count_enemy[y, x] = 1
        self.env[y, x] = 20
        print("Enemy move", "\n", self.env)

    def check_win(self):
        for i in range(self.count.shape[0]):
            if np.sum(self.count[i, :]) == 3:
                print("YOU WIN")
                return True
            elif np.sum(self.count[:, i]) == 3:
                print("YOU WIN")
                return True

        if np.sum([self.count[0, 0],
                   self.count[1, 1],
                   self.count[2, 2]]) == 3:
            print("YOU WIN")
            return True
        elif np.sum([self.count[0, 2],
                     self.count[1, 1],
                     self.count[2, 0]]) == 3:
            print("YOU WIN")
            return True

    def check_lose(self):
        for i in range(self.count_enemy.shape[0]):
            if np.sum(self.count_enemy[i, :]) == 3:
                print("YOU LOSE")
                return True
            elif np.sum(self.count_enemy[:, i]) == 3:
                print("YOU LOSE")
                return True

        if np.sum([self.count_enemy[0, 0],
                   self.count_enemy[1, 1],
                   self.count_enemy[2, 2]]) == 3:
            print("YOU LOSE")
            return True
        elif np.sum([self.count_enemy[0, 2],
                     self.count_enemy[1, 1],
                     self.count_enemy[2, 0]]) == 3:
            print("YOU LOSE")
            return True

    def dell(self):
        self.env = np.zeros((3, 3), dtype=int)
        self.count = np.zeros((3, 3), dtype=int)
        self.count_enemy = np.zeros((3, 3), dtype=int)
        print("Environment", "\n", self.env)

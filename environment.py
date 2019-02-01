import numpy as np


class Env:
    def __init__(self):
        self.env = np.zeros((3, 3), dtype=int)
        self.count = np.zeros((3, 3), dtype=int)
        self.count_enemy = np.zeros((3, 3), dtype=int)
        print("Environment", "\n", self.env)

    def move(self, x: int, y: int):
        if self.count[x, y] == 0:
            self.count[x, y] = 1
            self.count_enemy[x, y] = 1
        self.env[x, y] = 10
        print("My move", "\n", self.env)

        if self.check_win():
            return self.dell()

        x_enemy = np.random.randint(0, 2)
        y_enemy = np.random.randint(0, 2)
        self.enemy_move(x_enemy, y_enemy)

    def enemy_move(self, x: int, y: int):
        if self.count_enemy[x, y] == 1 or self.count[x, y] == 1:
            while True:
                if self.count_enemy[x, y] == 1 or self.count[x, y] == 1:
                    x = np.random.randint(0, 2)
                    y = np.random.randint(0, 2)
                else:
                    self.count_enemy[x, y] = 1
                    self.env[x, y] = 20
                    print("Enemy move", "\n", self.env)
                    break
        else:
            self.count_enemy[x, y] = 1
            self.env[x, y] = 20
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

    def dell(self):
        self.env = np.zeros((3, 3), dtype=int)
        self.count = np.zeros((3, 3), dtype=int)
        self.count_enemy = np.zeros((3, 3), dtype=int)

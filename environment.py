import random


class Env:

    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.board = [' '] * 9
        self.possible_moves = []

    def move(self, i: int, view: str):

        if self.board[i] == ' ':
            self.board[i] = view

        else:
            raise IndexError("HERE IS BUSY")

        self.get_possible_moves()

        return self.board

    def check_win(self, count, view: str):
        check = [
            [count[i] for i in (0, 1, 2)],
            [count[i] for i in (3, 4, 5)],
            [count[i] for i in (6, 7, 8)],
            [count[i] for i in (0, 3, 6)],
            [count[i] for i in (1, 4, 7)],
            [count[i] for i in (2, 5, 8)],
            [count[i] for i in (0, 4, 8)],
            [count[i] for i in (2, 4, 6)],
        ]

        for arr in check:
            if arr.count(view) == 3:
                return 1.0, True, view

        if not any(i == ' ' for i in self.board):
            return 0.5, True, view

        return 0.0, False, view

    def train(self, epoch):
        for i in range(epoch):
            self.restart_game()

            x = random.choice([True, False])
            done = False

            while not done:
                if x:
                    view = 'X'
                    motion = self.player1.action(self.board, self.get_possible_moves())
                else:
                    view = 'O'
                    motion = self.player2.action(self.board, self.get_possible_moves())

                self.move(motion, view)

                reward, done, kind = self.check_win(self.board, view)

                if reward == 1.0:

                    if kind == 'X':
                        self.player1.update_q(reward, tuple(self.board), self.possible_moves)
                        self.player2.update_q(-1 * reward, tuple(self.board), self.possible_moves)
                    else:
                        self.player1.update_q(-1 * reward, tuple(self.board), self.possible_moves)
                        self.player2.update_q(reward, tuple(self.board), self.possible_moves)

                elif reward == -1.0:

                    if kind == 'X':
                        self.player1.update_q(-1 * reward, tuple(self.board), self.possible_moves)
                        self.player2.update_q(reward, tuple(self.board), self.possible_moves)
                    else:
                        self.player1.update_q(reward, tuple(self.board), self.possible_moves)
                        self.player2.update_q(-1 * reward, tuple(self.board), self.possible_moves)

                elif reward == 0.5:

                    self.player1.update_q(reward, tuple(self.board), self.possible_moves)
                    self.player2.update_q(reward, tuple(self.board), self.possible_moves)

                elif reward == 0.0:

                    self.player1.update_q(reward, tuple(self.board), self.possible_moves)
                    self.player2.update_q(reward, tuple(self.board), self.possible_moves)

                x = not x

    def get_possible_moves(self):
        # all possible moves
        self.possible_moves.clear()
        self.possible_moves = [x for x in range(len(self.board)) if self.board[x] == ' ']
        return self.possible_moves

    def restart_game(self):
        self.board = [' '] * 9

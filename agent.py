import random


class AI:

    def __init__(self, p=0.2, alpha=0.3, gamma=0.9):
        self.alpha = alpha  # learning rate
        self.gamma = gamma
        self.p = p  # probability 20%
        self.Q = dict()  # dict {state: weights of each move}
        self.last_state = None
        self.last_q = 0
        self.key = None

    def action(self, state: list, possible_moves: list):
        # transform state to vector
        self.last_state = tuple(state)

        if random.random() < self.p:
            move = random.choice(possible_moves)
            self.key = (self.last_state, move)
            self.last_q = self.get_q(self.last_state, move)
            return move
        else:
            q_list = []
            for move in possible_moves:
                q_list.append(self.get_q(self.last_state, move))
            q_max = max(q_list)

            if q_list.count(q_max) > 1:
                q = [i for i in range(len(possible_moves)) if q_list[i] == q_max]
                idx = random.choice(q)
            else:
                idx = q_list.index(q_max)

            self.key = (self.last_state, possible_moves[idx])
            self.last_q = self.get_q(self.last_state, possible_moves[idx])

            return possible_moves[idx]

    def play(self, state: list, possible_moves: list):
        self.last_state = tuple(state)
        q_list = []
        for move in possible_moves:
            q_list.append(self.get_q(self.last_state, move))
        q_max = max(q_list)

        if q_list.count(q_max) > 1:
            q = [i for i in range(len(possible_moves)) if q_list[i] == q_max]
            idx = random.choice(q)
        else:
            idx = q_list.index(q_max)

        return possible_moves[idx]

    def get_q(self, state: tuple, action: int):
        # add weight to Q
        if self.Q.get((state, action)) is None:
            self.Q[(state, action)] = 1.0

        return self.Q.get((state, action))

    def update_q(self, reward: float, state: tuple, possible_moves: list):
        q_list = []
        for move in possible_moves:
            q_list.append(self.get_q(state, move))

        if q_list:
            q_next = max(q_list)
        else:
            q_next = 0.0

        self.Q[self.key] = self.last_q + self.alpha * ((reward + self.gamma * q_next) - self.last_q)

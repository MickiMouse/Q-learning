from environment import Env
from agent import AI

bot1 = AI()
bot2 = AI()

env = Env(bot1, bot2)

print("AI IS TRAINING", "\n")
env.train(200000)

print("AI IS READY", "\n")

env = Env()

while True:
    motion = bot1.play(env.board, env.get_possible_moves())
    print("AI MOVE", motion)

    env.move(motion, 'X')
    print(env.board[0:3], "\n", env.board[3:6], "\n", env.board[6:9])

    _, done, _ = env.check_win(env.board, 'X')

    if done:
        env.restart_game()

    idx = int(input("YOUR MOVE"))
    env.move(idx, 'O')
    print(env.board[0:3], "\n", env.board[3:6], "\n", env.board[6:9])

    _, done, _ = env.check_win(env.board, 'O')

    if done:
        env.restart_game()

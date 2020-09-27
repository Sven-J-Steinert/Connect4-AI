from game import game
from trainer import Neural_Network
import time
import torch


NN = Neural_Network()
NN = torch.load('all_time_high.pt')
NN.eval()


# Instanciation of the Game
gameInstance = game(7, 6)

# instanciation of the Players depending on the PlayerClass
# Pp1 = RandomPlayer(1)
# Pn1 = RandomPlayer(-1)

# Game parameter
waittime = 0
max_connected_pos = 1
max_connected_neg = 1
winner = 0

# the loop for playing the game until somebody won or the limit is reached
for x in range(0, 3*7):
    # AI Player
    # Board data as input for Neural Network
    X = torch.tensor(gameInstance.getBoard().flatten(), dtype=torch.float)  # 7 X 6 tensor

    c = NN.forward(X)  # NN output

    move_return = gameInstance.playAction(1, c)  # the positive Player plays
    max_connected_pos = max(max_connected_pos, gameInstance.get_max_connected())
    if not move_return[0]:
        winner = -1
        max_connected = max_connected_neg
        break
    if(move_return[1]):
        winner = 1
        max_connected = max_connected_neg
        break
    gameInstance.display(gui=False)
    time.sleep(waittime)

    c = int(input())  # the negative Player chooses his column
    move_return = gameInstance.playAction(-1, c)  # the negative Player plays
    max_connected_neg = max(max_connected_neg, gameInstance.get_max_connected())
    if not move_return[0]:
        winner = 1
        max_connected = max_connected_pos
        break
    if(move_return[1]):
        winner = -1
        max_connected = max_connected_pos
        break
    gameInstance.display(gui=False)
    time.sleep(waittime)

if winner == 0:
    print("split - no winner")
    max_connected = max_connected_pos
    # end for

gameInstance.display(gui=True, winner=winner)

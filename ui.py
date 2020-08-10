# imports game.py
# calls playerfunction
# displays gamedata
from game import game
from trainer import result
from _Players.RandomPlayer import RandomPlayer
import time


# Instanciation of the Game
gameInstance = game(7, 6)

# instanciation of the Players depending on the PlayerClass
Pp1 = RandomPlayer(1)
Pn1 = RandomPlayer(-1)

# Game parameter
waittime = 0
max_connected_pos = 1
max_connected_neg = 1
winner = 0

# the loop for playing the game until somebody won or the limit is reached
for x in range(0, 3*7):

    c = Pp1.chooseCol(gameInstance) #the positive Player chooses his column
    move_return = gameInstance.playAction(Pp1.getId(), c) # the positive Player plays
    max_connected_pos = max(max_connected_pos, gameInstance.get_max_connected())
    if(move_return[1]):
        winner = 1
        max_connected = max_connected_neg
        break

    time.sleep(waittime)

    c = Pn1.chooseCol(gameInstance)  # the negative Player chooses his column
    move_return = gameInstance.playAction(Pn1.getId(), c)  # the negative Player plays
    max_connected_neg = max(max_connected_neg, gameInstance.get_max_connected())
    if(move_return[1]):
        winner = -1
        max_connected = max_connected_pos
        break
    time.sleep(waittime)

if winner == 0:
    print("split - no winner")
    max_connected = max_connected_pos
# end for
aftermath = result(
                board=gameInstance.getBoard(),
                turns=x + 1,
                won=winner,
                max_connected=max_connected
                )
aftermath.display()
gameInstance.display(gui=True, winner=winner)

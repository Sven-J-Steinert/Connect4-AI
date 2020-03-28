# imports game.py
# calls playerfunction
# displays gamedata
from game import game
from _Players.RandomPlayer import RandomPlayer
import numpy as np

gameInstance = game(7,6)
P1 = RandomPlayer(gameInstance.getBoard())
P2 = RandomPlayer(gameInstance.getBoard())

P1.chooseCol(np.array([0,1,2,3,4,5,6]))


while True:
     x, y = gameInstance.playAction(1,int(input()))
     print(x,y)
     gameInstance.display()
     gameInstance.playAction(2,int(input()))
     gameInstance.display()

instance1.playAction(1,6)
instance1.playAction(1,6)
instance1.playAction(1,6)
print(" ")
print(instance1.playAction(1,6))
instance1.display()
instance1.getPossibleActions()
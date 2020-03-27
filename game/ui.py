# imports game.py
# calls playerfunction
# displays gamedata
from game import game

instance1 = game(7,6)
# while True:
#     instance1.playeraction(1,int(input()))
#     instance1.display()
#     instance1.playeraction(2,int(input()))
#     instance1.display()
    
instance1.playeraction(1,0)
instance1.playeraction(1,0)
instance1.playeraction(1,0)
instance1.playeraction(1,0)
instance1.playeraction(1,0)
print(" ")
print(instance1.playeraction(1,0))
print(instance1.get_valid_moves())
instance1.display()
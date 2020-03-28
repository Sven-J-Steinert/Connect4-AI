###
### Stellt den Monte-Carlo-Tree-Search bereit
###

from ConnectFourAI.game.game import game

class Tree():
    
    def __init__(self,game_state,move,player):

        game.playeraction(player,move)
        self.game_state = game_state
        
    def selection():
        return 0

    def expansion():
        return 0
    
    def simulation():
        return 0
    
    def backpropagation():
        return 0
        
# -*- coding: utf-8 -*-
import numpy as np
class RandomPlayer:
    
    ######################################################################################################################
    #The constructor
    # - The param id defines the number of the Player. The Players number should be either 1 or -1
    def __init__(self, id):
        self.id = id
    #end __init__
    
    
    
    ######################################################################################################################
    # The function chooseCol returns a integer with the index of the choosen column depending on the board pboard
    def chooseCol(self, pGame):
        possibleCols = self.getPossibleActions(pGame.getBoard())
        #print(possibleCols)
        randi = np.random.randint(low=0, high=len(possibleCols))
        return possibleCols[randi]
    #end chooseCol
    
    
    
    ######################################################################################################################
    # The function getPossibleActions returns a np-vector of all collums that are not filled
    def getPossibleActions(self, pboard):
        valid_moves = []
        
        for i in range(len(pboard[0,:])):
            if pboard[0,i] == 0:
                valid_moves.append(i)        
        
        return valid_moves
    #end getPossibleActions
    
    
    
    ######################################################################################################################
    # The function getId returns the int id of the player
    def getId(self):
       return self.id
    #end getPossibleActions

#end class

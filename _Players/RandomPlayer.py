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
        randi = np.random.randint(low=0, high=possibleCols.size)
        return possibleCols[randi]
    #end chooseCol
    
    
    
    ######################################################################################################################
    # The function getPossibleActions returns a np-vector of all collums that are not filled
    def getPossibleActions(self, pboard):
        print(np.nonzero(pboard[0]))
        x1 = np.where(pboard[0] == 0) #selects the column indices of where the first row is empty  
        print(x1)
        return x1    
    #end getPossibleActions
    
    
    
    ######################################################################################################################
    # The function getId returns the int id of the player
    def getId(self):
       return self.id
    #end getPossibleActions

#end class

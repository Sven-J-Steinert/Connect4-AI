# -*- coding: utf-8 -*-
import numpy as np
class RandomPlayer:
    
    ######################################################################################################################
    #The constructor
    def __init__(self, stateBoard):
        self.stateBoard = stateBoard
    #end __init__
    
    ######################################################################################################################
    # The function chooseCol returns a integer with the index of the choosen column
    def chooseCol(self, possibleCols):
        randi = np.random.randint(low=0, high=possibleCols.size)
        return possibleCols[randi]
    #end chooseCol

#end class

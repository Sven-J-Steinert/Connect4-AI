# Datafield


import numpy as np

class game:
    def __init__(
            self,
            board_width=6,
            board_height=7
            ):
        self.board_width = board_width
        self.board_height = board_height
        self.board = np.zeros((board_height,board_width))
        print(self.board)
        
        
    def playeraction(
            self,
            player_id,
            column
            ):
        if (column >self.board_width):
            return print("INVALID")
        
        for i in reversed( range(self.board_height)):
            if self.board[i,column] == 0:
                self.board[i,column] = player_id
                return

        print("INVALID")
        

    def display(self):
        print(self.board)
        
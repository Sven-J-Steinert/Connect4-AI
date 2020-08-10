import numpy as np
from tkinter import *
from tkinter import PhotoImage


class game:

    def __init__(
            self,
            board_width=6,
            board_height=7,
            old_game=None
            ):

        if old_game:
            print("Spiel übergeben")
            self.board = np.array(old_game.board)
            self.board_height = old_game.board_height
            self.board_width = old_game.board_width
        else:
            self.board_width = board_width
            self.board_height = board_height
            self.board = np.zeros((board_height,board_width))
            # print(self.board)
            # print(" ")

    ### Zug Funktion
    ### Erster Boolean: gültiger Zug
    ### Zweiter Parameter: gewonnen mit dem Zug
    ###
    def playAction(self, player_id, column):
        if (column > self.board_width):
            return (False, False)


        for i in reversed( range(self.board_height)):
            if self.board[i,column] == 0:
                self.board[i,column] = player_id
                return (True, self.check_win(player_id, x=column, y=i))


        return (False)



    ######################################################################################################################
    # The function setBoard is the set function for the gameboard. It may be used in case of reviewing the new state during learning
    def setBoard(self, newBoard):
        self.board = newBoard
    #end setBoard

    ######################################################################################################################
    # The function getBoard is the set function for the gameboard. It may be used in case of reviewing the new state during learning
    def getBoard(self):
        return self.board
    #end getBoard

    ######################################################################################################################
    # The function display prints the board to the terminal
    def display(self,gui=None,winner=None):
        if gui:
            window = Tk()
            window.title("Connect4 AI")
            canvas = Canvas(window, width = 400, height = 300)
            canvas.pack()

            self.icon_empty = PhotoImage(file='icons/empty.png')
            self.icon_player1 = PhotoImage(file='icons/player1.png')
            self.icon_player2 = PhotoImage(file='icons/player2.png')
            i=0
            u=0
            x=10
            y=10
            while u < self.board_height:
                while i < self.board_width:
                    if self.board[u,i]==0:
                        canvas.create_image(x,y, anchor=NW, image=self.icon_empty)
                    if self.board[u,i]==1:
                        canvas.create_image(x,y, anchor=NW, image=self.icon_player1)
                    if self.board[u,i]==-1:
                        canvas.create_image(x,y, anchor=NW, image=self.icon_player2)
                    x = x+55
                    i = i+1
                y = y + 50
                x = 10
                i = 0
                u = u + 1
            label_text=''
            if winner == 1:
                label_text = "positive (blue) wins"
            if winner == -1:
                label_text = "negative (orange) wins"
            self.label = Label(window, text=label_text)
            self.label.pack()
            mainloop()

        else:
            print(self.board)
            print(" ")
    # end dispaly



    ###
    ### Prüft ob ein Zug zu einem Sieg geführt hat
    ###
    def check_win(
            self,
            player_id,
            x,
            y
            ):
        sum_x = 1
        sum_y = 1
        sum_dp = 1
        sum_dn = 1
        self.sum_max = 1

        # row checking
        for ix in range(1,4):
            if (x+ix) > self.board_width-1:
                # print("out of board")
                break
            if self.board[y,x+ix] == player_id:
                sum_x +=1
            else:
                # print("zero on the right")
                break

        for ix in range(1,4):
            if (x-ix) < 0:
                # print("out of board")
                break
            if self.board[y,x-ix] == player_id:
                sum_x +=1
            else:
                # print("zero on the left")
                break
        if sum_x >= 4:
            return True

        # column checking
        for iy in range(1,4):
            if (y+iy) > self.board_height-1:
                # print("out of board")
                break
            if self.board[y+iy,x] == player_id:
                sum_y +=1
            else:
                # print("zero on the bottom")
                break

        for iy in range(1,4):
            if (y-iy) < 0:
                # print("out of board")
                break
            if self.board[y-iy,x] == player_id:
                sum_y +=1
            else:
                # print("zero on the top")
                break
        if sum_y >= 4:
            return True

        # pos diagonal checking
        # right
        for i in range(1,4):
            if (y-i) < 0 or (x+i) > self.board_width-1:
                # print("out of board dp right")
                break
            if self.board[y-i,x+i] == player_id:
                sum_dp +=1
            else:
                # print("zero on the dp right")
                break
        # left
        for i in range(1,4):
            if (y+i) > self.board_height-1 or (x-i) < 0:
                # print("out of board dp left")
                break
            if self.board[y+i,x-i] == player_id:
                sum_dp +=1
            else:
                # print("zero on the dp left")
                break

        if sum_dp >= 4:
            return True

        # neg diagonal checking
        # right
        for i in range(1,4):
            if (y+i) > self.board_height-1 or (x+i) > self.board_width-1:
                # print("out of board dn right")
                break
            if self.board[y+i,x+i] == player_id:
                sum_dn +=1
            else:
                # print("zero on the dn right")
                break
        # left
        for i in range(1,4):
            if (y-i) < 0 or (x-i) < 0:
                # print("out of board dn left")
                break
            if self.board[y-i,x-i] == player_id:
                sum_dn +=1
            else:
                # print("zero on the dn left")
                break

        if sum_dn >= 4:
            return True

        self.sum_max = max(sum_x , sum_y , sum_dp , sum_dn )

    ###
    ### Gibt alle gültigen Züge zurück
    ###
    def get_valid_moves(self):

        valid_moves = []

        for i in range(self.board_width):
            if self.board[0,i] == 0:
                valid_moves.append(i)

        return valid_moves

    ###
    ### Gibt das Spielfeld als numpy Matrix zurück
    ###
    def get_game_new_object(self):
        return game(old_game=self)

    def get_max_connected(self):
        return self.sum_max

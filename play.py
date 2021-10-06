from game import game
from trainer import Neural_Network
from _Players.RandomPlayer import RandomPlayer
from _Players.StrategicPlayer import StrategicPlayer
import time
import torch
from tkinter import *
from tkinter import PhotoImage

class GUI:
    def __init__(self, master):
            self.master = master
            self.icon_empty = PhotoImage(file='icons/empty.png')
            self.icon_player1 = PhotoImage(file='icons/player1.png')
            self.icon_player2 = PhotoImage(file='icons/player2.png')

            self.canvas = Canvas(master, width = 675, height = 580)
            self.canvas.pack()

            self.label = Label(master, text='Select enemy player:')
            self.label.pack()

            def enemy_type_1():
                self.enemy_type = 'RandomPlayer'

            def enemy_type_2():
                self.enemy_type = 'StrategicPlayer'

            def enemy_type_3():
                self.enemy_type = 'NN'

            self.button_enemy_1 = Button(master, text='Random Player', command = enemy_type_1())
            self.button_enemy_1.pack()
            self.button_enemy_2 = Button(master, text='Strategic Player', command = enemy_type_2())
            self.button_enemy_2.pack()
            self.button_enemy_3 = Button(master, text='Neural Network', command = enemy_type_3())
            self.button_enemy_3.pack()






    def start_game(self,enemy):
        if enemy == 'RandomPlayer':
            enemy = RandomPlayer(1)

        if enemy == 'StrategicPlayer':
            enemy = StrategicPlayer(1)

        if enemy == 'NN':
            NN = Neural_Network()
            NN = torch.load('all_time_high.pt')
            NN.eval()


        # Instanciation of the Game
        self.gameInstance = game(7, 6)
        self.winner = 0

        # the loop for playing the game until somebody won or the limit is reached
        for x in range(0, 3*7):
            # AI Player
            # Board data as input for Neural Network
            if enemy_type == 'RandomPlayer':
                print('RP')
                c = enemy.chooseCol(self.gameInstance) #the positive Player chooses his column

            if enemy_type == 'StrategicPlayer':
                print('SP')
                c = enemy.chooseCol(self.gameInstance) #the positive Player chooses his column

            if enemy_type == 'NN':
                print('NN')
                X = torch.tensor(self.gameInstance.getBoard().flatten(), dtype=torch.float)  # 7 X 6 tensor
                c = NN.forward(X)  # NN output

            move_return = self.gameInstance.playAction(1, c)  # the positive Player plays
            self.update()
            if not move_return[0]:
                self.winner = -1
                break
            if(move_return[1]):
                self.winner = 1
                break


            c = int(input())  # the negative Player chooses his column
            move_return = self.gameInstance.playAction(-1, c)  # the negative Player plays
            self.update()
            if not move_return[0]:
                self.winner = 1
                break
            if(move_return[1]):
                self.winner = -1
                break

            if self.winner == 0:
                self.label_text ="split - no winner"
            if self.winner == 1:
                self.label_text = "positive (blue) wins"
            if self.winner == -1:
                self.label_text = "negative (orange) wins"
            self.label['text'] = self.label_text
            # RESTART




    def update(self):
        i=0
        u=0
        x=10
        y=10
        while u < self.gameInstance.board_height:
            while i < self.gameInstance.board_width:
                if self.gameInstance.board[u,i]==0:
                    self.canvas.create_image(x,y, anchor=NW, image=self.icon_empty)
                if self.gameInstance.board[u,i]==1:
                    self.canvas.create_image(x,y, anchor=NW, image=self.icon_player1)
                if self.gameInstance.board[u,i]==-1:
                    self.canvas.create_image(x,y, anchor=NW, image=self.icon_player2)
                x = x+95
                i = i+1
            y = y + 92
            x = 10
            i = 0
            u = u + 1



def start():
    print('starting')
    root = Tk()
    root.title("Connect4 AI")
    window = GUI(root)
    Button(root, text="Quit", command=root.destroy).pack()
    root.mainloop()


while True:
    start()
    answer = input('Run again? ([y]/n): ')
    if answer == 'n':
        print('Goodbye')
        break

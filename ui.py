from game import game
from trainer import result, Neural_Network
from _Players.RandomPlayer import RandomPlayer
from _Players.StrategicPlayer import StrategicPlayer
import time
import torch
import os
import numpy as np

population_size = 100
batch_size = 100
generations = 5
surviving_rate = 0.5
mutation_rate = 0.1

against_own_AI = False

inputSize = 42
hiddenSize = 50
outputSize = 7

performance = [0] * population_size
survivor = [0] * int(population_size * surviving_rate)

all_time_high = 0

# RUN THIS AT FIRST STARTUP
# creates random starting set
#for i in range(0, population_size):
#    NN = Neural_Network()
#    NN.W1 = torch.randn(inputSize, hiddenSize)
#    NN.W2 = torch.randn(hiddenSize, outputSize)
#    torch.save(NN, 'data/' + str(i) + '_gen_x.pt')

# Generation loop
for z in range(0, generations):

    batch_wins = [0] * population_size

    # load and test one generation
    for a in range(0, population_size):

        NN = Neural_Network()
        NN.cuda()
        NN = torch.load('data/' + str(a) + '_gen_x.pt')
        NN.eval()


        winner = 0

        # Game loop
        for i in range(0, batch_size):

            # Instanciation of the Game
            gameInstance = game(7, 6)

            # Enemey player who chooses coloumn randomly
            #Pn1 = RandomPlayer(-1)
            Pn1 = StrategicPlayer(-1)

            # Turn loop
            for x in range(0, 3*7):

                # Random Player
                c_r = Pn1.chooseCol(gameInstance)  # the negative Player chooses his column
                move_return = gameInstance.playAction(-1, c_r)  # the negative Player plays
                if not move_return[0]:
                    winner = 1
                    break
                if(move_return[1]):
                    winner = -1
                    break

                # AI Player
                # Board data as input for Neural Network
                X = torch.tensor(gameInstance.getBoard().flatten(), dtype=torch.float)  # 42 X 1 tensor
                c = NN.forward(X)  # NN output
                move_return = gameInstance.playAction(1, c)  # the AI Player plays
                if not move_return[0]:
                    winner = -1
                    break
                if(move_return[1]):
                    winner = 1
                    break



            # after one game
            if winner == 0:
                print("split - no winner")

            if winner == 1:
                batch_wins[a] += 1

    # after one batch
    # evaluating routine for one generation

    for i in range(0, population_size):
        performance[i] = batch_wins[i]/(batch_size)  # winrate

    # sorted survivor array: last entry is highest
    survivor = sorted(range(len(performance)), key=lambda i: performance[i])[int(-1*surviving_rate * population_size):]

    if max(performance) >= all_time_high:
        all_time_high = max(performance)
        all_time_high_active = True
    else:
        all_time_high_active = False

    # performance info output
    print(str(max(performance)) + '  ' + str(all_time_high))

    # rename files to _old
    for i in range(0, population_size):
        os.rename('data/' + str(i) + '_gen_x.pt', 'data/' + str(i) + '_gen_x_old.pt')

    # Evolving loop
    for i in range(0, int(surviving_rate * population_size)):
        # load parent NN
        pNN = Neural_Network()
        pNN = torch.load('data/' + str(survivor[i]) + '_gen_x_old.pt')
        pNN.eval()

        # save all_time_high seperately
        if i == int((surviving_rate * population_size) -1) and all_time_high_active:
            torch.save(pNN, 'data/all_time_high.pt')

        # Mutate Genes
        NN.W1 = pNN.W1 + (mutation_rate * torch.randn(inputSize, hiddenSize))
        NN.W2 = pNN.W2 + (mutation_rate * torch.randn(hiddenSize, outputSize))
        torch.save(NN, 'data/' + str(i) + '_gen_x.pt')
        NN.W1 = pNN.W1 + (mutation_rate * torch.randn(inputSize, hiddenSize))
        NN.W2 = pNN.W2 + (mutation_rate * torch.randn(hiddenSize, outputSize))
        torch.save(NN, 'data/' + str(i+int(surviving_rate * population_size)) + '_gen_x.pt')

    # delete _old files
    for i in range(0, population_size):
        os.remove('data/' + str(i) + '_gen_x_old.pt')

    # one generation is done

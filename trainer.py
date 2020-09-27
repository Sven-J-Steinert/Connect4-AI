import torch
import torch.nn as nn
import torch.nn.functional as F


class Neural_Network(nn.Module):
    def __init__(self):
        super(Neural_Network, self).__init__()
        # neural network parameters
        # 7 input channels, 1 output channel, 5 hidden chanels
        self.inputSize = 42
        self.outputSize = 7
        self.hiddenSize = 12
        # second hidden layer

        # weights
        # self.W1 = torch.randn(self.inputSize, self.hiddenSize)  # 7 X 5 tensor
        # self.W2 = torch.randn(self.hiddenSize, self.outputSize)  # 5 X 1 tensor

    def forward(self, X):
        self.z = torch.matmul(X, self.W1)  # 3 X 3 ".dot" does not broadcast in PyTorch
        self.z2 = self.sigmoid(self.z)  # activation function
        self.z3 = torch.matmul(self.z2, self.W2)
        o = self.sigmoid(self.z3)  # final activation function
        values, indices = torch.max(o, 0)  # choosing the highest coloumn
        o = indices
        return o

    def sigmoid(self, s):
        return 1 / (1 + torch.exp(-s))

    def sigmoidPrime(self, s):
        # derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        self.o_error = y - o  # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o)  # derivative of sig to error
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += torch.matmul(torch.t(X), self.z2_delta)
        self.W2 += torch.matmul(torch.t(self.z2), self.o_delta)


    def saveWeights(self, model):
        # we will use the PyTorch internal storage functions
        torch.save(model, "NN")
        # you can reload model with all the weights and so forth with:
        # torch.load("NN")

    def loadWeights(self, ID):
        nn = Neural_Network()
        nn.load_state_dict(torch.load('data/' + str(ID) + '_model.pt'))
        nn.eval()

    def createRandom(self, x):
        for i in range(0, x):
            # weights
            # Save
            nn = Neural_Network()
            nn.W1 = torch.randn(self.inputSize, self.hiddenSize)
            nn.W2 = torch.randn(self.hiddenSize, self.outputSize)
            self.W1 = torch.randn(self.inputSize, self.hiddenSize)
            self.W2 = torch.randn(self.hiddenSize, self.outputSize)
            torch.save(self.state_dict(), 'data/' + str(i) + '_model.pt')


class result:

    def __init__(
            self,
            board,
            turns,
            max_connected,
            won,
            ):

        self.turns = turns
        self.total_turns = (6*7)/2
        self.won = won

        if self.won == 1:
            self.max_connected = 4
        else:
            self.max_connected = max_connected
        self.total_connected = 4

        self.board = board

        # max connected counter
        self.board_width = 6
        self.board_height = 7

        # self.Fitness = self.turns/self.total_turns + self.max_connected / self.total_connected + self.won
        # self.Fitness = self.max_connected / self.total_connected + self.won
        self.Fitness = self.won

    def display(self):
        print("Turns: ", self.turns)
        print("Winner:", self.won)
        print("max connected:", self.max_connected)
        print("Fitness: ",  self.Fitness)

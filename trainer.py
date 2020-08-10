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
        self.Fitness = self.max_connected / self.total_connected + self.won

    def display(self):
        print("Turns: ", self.turns)
        print("Winner:", self.won)
        print("max connected:", self.max_connected)
        print("Fitness: ",  self.Fitness)

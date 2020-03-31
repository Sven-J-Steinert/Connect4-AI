import numpy as np
#import tensorflow as tf
from game import game
from _Players.AZPlayer import AZPlayer
import pickle

class GameStore:
    
    def __init__(self):
        self.game_state_store = []
        self.game_mcts_store = []
        self.game_winner = []
        
    #Gibt ID für neuen Speicherstand zurück
    def store_new_game(self):
        self.game_state_store.append([])
        self.game_mcts_store.append([])
        return len(self.game_state_store)-1

    def store_move(self,id,state):
        self.game_state_store[id].append(state)
        
    def store_MCTS_probs(self,id,mcts_probs):
        self.game_mcts_store[id].append(mcts_probs)
        
    def store_winner(self,id,winner_id):
        self.game_winner.append(winner_id)
        
        
        
def main():
    
    self_play()
    
    return 0

def self_play():
    store = GameStore()
    
    # Play 25.000 games against it self and store moves
    for i in range(25000):
        print("Spiel: %d" %i)
        gameInstance = game(7,6)
        
        game_id = store.store_new_game()
        
        p1 = AZPlayer(1)
        p2 = AZPlayer(-1)
        
        #Jeder wirft maximal 7*6/2=21 Steine ein, dann ist das Spielfeld voll
        for moveCount in range(int(7*6/2)):
            
            action_return = gameInstance.playAction(p1.getId(),p1.chooseCol(gameInstance))
            store.store_move(game_id,gameInstance.board)
            if action_return[1]:
                print("Player 1 won")
                store.store_winner(game_id, p1.getId())
                break
            
            action_return = gameInstance.playAction(p2.getId(),p2.chooseCol(gameInstance))
            store.store_move(game_id,gameInstance.board)
            if action_return[1]:
                print("Player 2 won")
                store.store_winner(game_id, p2.getId())
                break
    
    with open("dumb.obj",'wb') as file:    
        pickle.dump(store, file)
    return 0

def retrain_network():
    
    return 0

def evaluate_network():
    
    return 0

class MCTS:
    
    #neue Namen?
    def __init__(self,root,cpuct):
        self.root = root
        self.tree={}
        self.cpuct = cpuct
        
        
    def __len__(self):
        return len(self.tree)
    
    def move_to_leaf(self):
        
        current_node = self.root
        
        done = 0
        value = 0
        
    def backFill(self,leaf,value,breadcrumbs):
        pass
    
    def addNode(self,leaf,value,breadcrumbs):
        pass
    
    
    
######
## Node Klasse
###### 
class Node:
    
    def __init__(self,state):
        self.state = state
        self.player_turn = state.player_turn
        self.id = state.id
        self.edges = []
        
        
    def is_leaf(self):
        return len(self.edges)==0
    
######
## Edge Klasse
###### 
class Edge:
    
    def __init__(self,inNode,outNode,prior,action):
        
        self.id = inNode.state.id + '|' + outNode.state.id
        self.inNode = inNode
        self.outNode = outNode
        self.player_turn = inNode.state.player_turn
        self.action = action
        
        self.stats = {
            'N':0,
            'W':0,
            'Q':0,
            'P':prior,
            }


if __name__=="__main__":
    main()
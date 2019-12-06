import os
import torch as T
import torch.nn as nn           #neural networks
import torch.nn.functional as F     #layers activation functions
import torch.optim as optim         #optimizer (Adam,gradient)
import numpy as np
import bot_help
class DeepQNetwork(nn.Module):
    def __init__(self, rows=25, cols=20):
        super(DeepQNetwork, self).__init__()
	self.rows = rows
	self.cols = cols
    def initBoard(self):
	board=[]
	for i in range(self.cols):
		board.append([0]*self.rows)
	return self.board
class Valid:  
    def isValidMove(self,gameId,gameState,action):
	try:
		if()
		
	except:
		return False
    def getMyPos(self,gameID,gameState):
	return(x,y)



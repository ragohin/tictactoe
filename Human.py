# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:02:12 2018

@author: ragoh
"""
from Player import *

#this class might not be necessary because we can just use playMove with the comp's game matrix
class Human(Player):
    def __init__(self, gameMatrix):
        super(Human, self).__init__()
        self.gameMatrix = gameMatrix
    def humanMove(self, location): #input human's move into the matrix, location is int 1-9 cooresponding to location on board
        if super(Human, self).isValidMove(location):
            self.gameMatrix[location] = 1
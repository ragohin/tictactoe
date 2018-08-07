# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:44:03 2018

@author: ragoh
"""
#COMPUTER IS X OR 1, HUMAN IS O OR -1
'''Things to add
1. error checks in playMove and isValidMove
'''

import operator
from Player import *

    
#moves for the computer
class Computer(Player):
    def __init__(self, gameMatrix = None):
        super(Computer, self).__init__()
        if gameMatrix == None:
            self.gameMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.gameMatrix = gameMatrix
        
    #ranking of moves are from 1-8 (8 being the best)
    def compMove(self):
        bestLocation = (9, 0) #this best move must be overwritten (best location of move, ranking of move in terms of best strategy)
        forks = []
        for location in range(len(self.gameMatrix)): #loop through matrix and check if any spot would result in one of these
            if super(Computer, self).isValidMove(location): #if spot is available
                if self.tryWin(self.gameMatrix.copy(), location, 'X'): #play space if it will result in win (3 in a row)
                    bestLocation = (location, 8)
                elif self.tryWin_Block(self.gameMatrix.copy(), location, 'O'): #play space if you have to block opponent's win
                    if bestLocation[1] < 7:
                        bestLocation = (location, 7)
                elif self.tryFork(self.gameMatrix.copy(), location, 'X'): #must be after at least 3 total game moves
                    if bestLocation[1] < 6:
                        bestLocation = (location, 6) 
                if self.tryFork(self.gameMatrix.copy(), location, 'O'): #if there is only one fork to block, return true
                    forks.append(location)
                    if bestLocation[1] < 5:
                        bestLocation = (location, 5)
                elif self.tryCenter(location):
                    if bestLocation[1] < 4:
                        bestLocation = (location, 4)
                if location != 4: #location isnt the center piece
                    if self.tryCorner_Opp(self.gameMatrix.copy(), location): #if opposite corner is taken by opponent, go there
                        if bestLocation[1] < 3:
                            bestLocation = (location, 3)
                    elif self.tryCorner(location): #location must be empty corner
                        if bestLocation[1] < 2:
                            bestLocation = (location, 2)
                    elif self.trySide(location): #location must be an open middle side space MAYBE THIS SHOULD JUST BE ELSE
                        if bestLocation[1] < 1:
                            bestLocation = (location, 1)
        if bestLocation[1] == 5:
            if len(forks) == 1: #if there is only one fork, simply block it (so that tryFork will become false)
                for win in self.wins:
                    if forks[0] in win:
                        for space in win: #try to play each space and see if one changes tryFork to false
                            matrixCopy = self.gameMatrix.copy()
                            super(Computer, self).playMove(space, 'X', matrixCopy)
                            if not self.tryFork(self.gameMatrix.copy(), bestLocation[0], 'O'):
                                bestLocation = (space, 6)
                                break
            #this works better than instructions on Wikipedia because not only does it create a 2 in a row that forces the oppoent to defend,
            #but it also block the max amount of human forks
            elif len(forks) > 1: #if there is one or more fork, block a fork that gives comp 2 in a row that forces the opponent to block, but doesnt give the human a fork
                numForksRemaining = {} #stores dictionary where key is a location that gives comp two in a row and value is the number of forks blocked
                for location in range(len(self.gameMatrix)):
                    matrixCopy = self.gameMatrix.copy()
                    TwoInRow = self.is2inRow(matrixCopy, location)
                    if TwoInRow != -1:
                        numForksRemaining[location] = 0
                        numForksRemaining[location] = self.countHumForks(matrixCopy, forks)
                bestLocation = (min(numForksRemaining.items(), key=operator.itemgetter(1))[0], 6)
        if bestLocation[1] > 0:
            super(Computer, self).playMove(bestLocation[0], 'X', self.gameMatrix)
            
    def is2inRow(self, matrixCopy, location): #if playing the current location gives the comp a 2 in a row (NOT NECESSARILY TWO NEXT TO EACHOTHER), it returns the space the human is forced to play, otherwise it returns -1
        super(Computer, self).playMove(location, 'X', matrixCopy)
        sum = 0
        for win in self.wins:    
            if location in win:
                sum = 0
                space2play = -1
                for space in win:
                    if matrixCopy[space] == 0:
                        space2play = space
                    sum += matrixCopy[space]
                if sum == 2 and space2play != -1:
                    return space2play
        return -1
    
    def countHumForks(self, matrixCopy, forks): #this will count the number of forks human can make
        counter = 0
        for fork in forks:
            matrixCopy2 = matrixCopy.copy()
            if self.tryFork(matrixCopy2, fork, 'O'):
                counter += 1
        return counter
    
    def tryWin(self, matrixCopy, location, CorH):
        super(Computer, self).playMove(location, CorH, matrixCopy)
        return (super(Computer, self).isWin(matrixCopy))[0]
    
    def tryWin_Block(self, matrixCopy, location, CorH):
        super(Computer, self).playMove(location, CorH, matrixCopy)
        return (super(Computer, self).isWin(matrixCopy))[0]
    
    def tryFork(self, matrixCopy, location, CorH):#CorH means try to find fork for the computer or the human (allows tryFork to be used in try_Fork_Block)
        super(Computer, self).playMove(location, CorH, matrixCopy)
        if not self.tryWin(matrixCopy, location, 'O'):
            winCounter = 0
            for loc in range(len(matrixCopy)): #loop through every possible space
                if super(Computer, self).isValidMove(loc, matrixCopy):
                    matrixCopy2 = matrixCopy.copy() #use a copy to test each move
                    super(Computer, self).playMove(loc, CorH, matrixCopy2) #play the space
                    if (super(Computer, self).isWin(matrixCopy2))[0]: #if winCounter reaches two, that means there is a fork (2 possible winning moves)
                        winCounter += 1
            if winCounter == 2: #should this be more than 2?
                return True
        return False
    
    def tryCenter(self, location):
        return location == 4
    
    def tryCorner_Opp(self, matrixCopy, location): 
        if (location == 0 or location == 2 or location == 6 or location == 8): #if its a corner
            if location == 0: #check to see if opponent is in each opposite corner
                return matrixCopy[8] == -1
            elif location == 2:
                return matrixCopy[6] == -1
            elif location == 6:
                return matrixCopy[2] == -1
            else:
                return matrixCopy[0] == -1
            
    def tryCorner(self, location):
        return (location == 0 or location == 2 or location == 6 or location == 8)#if its a corner
    
    def trySide(self, location):
        return (location == 1 or location == 3 or location == 5 or location == 7)
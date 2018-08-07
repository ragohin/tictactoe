# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:02:51 2018

@author: ragoh
"""

class Player(object):
    def __init__(self, gameMatrix = None):
        if gameMatrix == None:
            self.gameMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0] #3D matrix that will hold all of the game moves
        else:
            self.gameMatrix = gameMatrix
        self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]#indexes of possible 3 in a rows
    
    def getMatrix(self):
        return self.gameMatrix
    
    def isWin(self, mat = None): #check if there is a win in the matrix
        if mat == None:
            mat = self.gameMatrix
        if (abs(sum(mat[:3]))==3 or abs(sum(mat[3:6]))==3 or abs(sum(mat[6:9]))==3 #check rows
                or abs(sum(mat[::3]))==3 or abs(sum(mat[1::3]))==3 or abs(sum(mat[2::3]))==3 #check columns
                or abs(sum(mat[::4]))==3 or abs(sum(mat[2:7:2]))==3): #check diagonals
            if abs(sum(mat[:3]))==3:#check rows
                total = sum(mat[:3])
            elif abs(sum(mat[3:6]))==3:
                total = sum(mat[3:6])
            elif abs(sum(mat[6:9]))==3:
                total = sum(mat[6:9])
            elif abs(sum(mat[::3]))==3: #check columns
                total = sum(mat[::3])
            elif abs(sum(mat[1::3]))==3:
                total = sum(mat[1::3])
            elif abs(sum(mat[2::3]))==3: #check diagonals
                total = sum(mat[2::3])
            elif abs(sum(mat[::4]))==3:
                total = sum(mat[::4])
            elif abs(sum(mat[2:7:2]))==3:
                total = sum(mat[2:7:2])
            if total == 3:
                return (True, 'Computer')
            elif total == -3:
                return (True, 'Human')
        return (False, 'No Winner')
        
    def isCatsGame(self, gameMatrix = None):
        if gameMatrix == None:
            gameMatrix = self.gameMatrix
        return not (0 in gameMatrix)
        
    def isValidMove(self, location, gameMatrix = None): #checks to make sure space is open
        if gameMatrix == None:
            gameMatrix = self.gameMatrix
        return gameMatrix[location] == 0
    
    def playMove(self, location, playerType, gameMatrix = None): #playerType will be X (computer) or O (human)
        if gameMatrix == None:
            gameMatrix = self.gameMatrix
        while True:
            if self.isValidMove(location, gameMatrix):
                if playerType == 'X':
                    gameMatrix[location] = 1
                else:
                    gameMatrix[location] = -1
            else:
                break
    
    def humanMove(self, gameMatrix = None):
        if gameMatrix == None:
            gameMatrix = self.gameMatrix
        while True:
            try:
                displayBoard(gameMatrix)
                loc = int(input('Where would you like to play? (Enter number between 1 and 9) \n'))
                if self.isValidMove(loc-1, gameMatrix):
                    if loc>=1 and loc<=9:
                        self.playMove(loc-1, 'O', self.gameMatrix)
                        break
                    else:
                        displayBoard(gameMatrix)
                        print('Oops! Please enter a valid number between 1 and 9')
                else:
                    displayBoard(gameMatrix)
                    print('Oops! Please enter a valid number between 1 and 9')
            except ValueError:
                displayBoard(gameMatrix)
                print('Thats not a number! Try again!')

#INPUT: matrix of 9 elements(either 0, 1, or -1)
#OUTPUT: display of game board
def displayBoard(gameMatrix):
    row1 = ''
    row2 = ''
    row3 = ''
    tempGameMatrix = []
    for space in gameMatrix:
        if space == 1:
            tempGameMatrix.append('X')
        elif space == -1:
            tempGameMatrix.append('O')
        elif space == 0:
            tempGameMatrix.append(' ')
    gameMatrix = tempGameMatrix
    for space in range(len(gameMatrix)):
        if space<3:
            row1 = row1 + (gameMatrix[space] + ' ').join(' |')
        elif space>2 and space<6:
            row2 = row2 + (gameMatrix[space] + ' ').join(' |')
        elif space>5:
            row3 = row3 + (gameMatrix[space] + ' ').join(' |')
    print('|' + row1)
    print('|' + row2)
    print('|' + row3)
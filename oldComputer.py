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

    
#prints board as string
def displayBoard(gameMatrix):
    a = (' _____' *  3 )
    row1 = ''
    row2 = '' 
    row3 = ''
    currentPlay = ''
    for play in gameMatrix:
        if play == 0:
            currentPlay == ' '
        elif play == 1:
            currentPlay == 'X'
        else:
            currentPlay = 'O'
            
        if gameMatrix.index(play) < 3:
            row1 += currentPlay
        elif gameMatrix.index(play) > 2 and gameMatrix.index(play) < 6:
            row2 += currentPlay
        else:
            row3 += currentPlay
    b = '     '.join('||||')
    '|  ' + '  |'
    r1 = row1.join('||||')
    r2 = row2.join('||||')
    r3 = row3.join('||||')
    print('\n'.join((a, b, r1, a, b, r2, a, b, r3, a, )))
    
    
#maybe put these in a Game class
gameMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0] #3D matrix that will hold all of the game moves
catsGame = False
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]#indexes of possible 3 in a rows

#input: game matrix
#output: bool
def isWin(mat): #check if there is a win in the matrix
    return (abs(sum(mat[:3]))==3 or abs(sum(mat[3:6]))==3 or abs(sum(mat[6:9]))==3 #check rows
        or abs(sum(mat[::3]))==3 or abs(sum(mat[1::3]))==3 or abs(sum(mat[2::3]))==3 #check columns
        or abs(sum(mat[::4]))==3 or abs(sum(mat[2:7:2]))==3) #check diagonals

def playMove(gameMatrix, location, playerType): #playerType will be X (computer) or O (human)
    if isValidMove(gameMatrix, location):
        if playerType == 'X':
            gameMatrix[location] = 1
        else:
            gameMatrix[location] = -1
            
def isValidMove(gameMatrix, location): #checks to make sure space is open
    return gameMatrix[location] == 0

''' possible entirely separate Game class
class Game(object):
    def __init__(self):
        self.gameMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0] #3D matrix that will hold all of the game moves
        self.catsGame = False
        self.wins = {'row1': [0, 1, 2], 'row2': [3, 4, 5], 'row3': [6, 7, 8], 'col1': [0, 3, 6], #indexes of possible 3 in a rows
                    'col2': [1, 4, 7], 'col3': [2, 5, 8], 'dia1': [0, 4, 8], 'dia2': [2, 4, 6]}
        
    def displayBoard(self, gameMatrix):
        a = (' _____' *  3 )
        b = '     '.join('||||')
        print('\n'.join((a, b, b, a, b, b, a, b, b, a, )))
        

    #input: game matrix
    #output: bool
    def isWin(self): #check if there is a win in the matrix
        return (abs(sum(self.gameMatrix[:3]))==3 or abs(sum(self.gameMatrix[3:6]))==3 or abs(sum(self.gameMatrix[6:9]))==3 #check rows
            or abs(sum(self.gameMatrix[::3]))==3 or abs(sum(self.gameMatrix[1::3]))==3 or abs(sum(self.gameMatrix[2::3]))==3 #check columns
            or abs(sum(self.gameMatrix[::4]))==3 or abs(sum(self.gameMatrix[2:7:2]))==3) #check diagonals

    def playMove(self, location, playerType): #playerType will be X (computer) or O (human)
            #if isValidMove(gameMatrix, location):
            if playerType == 'X':
                self.gameMatrix[location] = 1
            else:
                self.gameMatrix[location] = -1
                
    def isValidMove(self, location): #checks to make sure space is open
        if self.gameMatrix[location] == 0:
            return True
        return False
'''

#not sure if want to keep simple class, playMove function can just be defined outside
class Simple(object):
    currentMove = 0
    '''def __init__(self, playerType):
        self.playerType = playerType
    
    def playMove(self, location, playerType): #playerType will be X (computer) or O (human)
        if isValidMove(location):
            gameMatrix[location] = playerType
            
    def isValidMove(self, location): #checks to make sure space is open
        if gameMatrix[location] == 0:
            return True
        return False'''
        
#moves for human player
class Human(object):
    def humanMove(self, location): #input human's move into the matrix, location is int 1-9 cooresponding to location on board
        if isValidMove(location):
            gameMatrix[location] = 1
    def isValidMove(self, location): #checks to make sure space is open
        if gameMatrix[location] == 0:
            return True
        return False
    
#moves for the computer
class Computer(object):
    def __init__(self, gameMatrix):
        self.gameMatrix = gameMatrix
    #ranking of moves are from 1-9 (9 being the best)
    def compMove(self):
        bestLocation = (10, 0) #this best move must be overwritten (best location of move, ranking of move in terms of best strategy)
        forks = []
        for location in range(len(self.gameMatrix)): #loop through matrix and check if any spot would result in one of these
            if isValidMove(self.gameMatrix, location): #if spot is available
                if self.tryWin(self.gameMatrix.copy(), location, 'X'): #play space if it will result in win (3 in a row)
                    bestLocation = (location, 9)
                elif self.tryWin_Block(self.gameMatrix.copy(), location, 'O'): #play space if you have to block opponent's win
                    if bestLocation[1] < 8:
                        bestLocation = (location, 8)
                elif self.tryFork(self.gameMatrix.copy(), location, 'X'): #must be after at least 3 total game moves
                    if bestLocation[1] < 7:
                        bestLocation = (location, 7) 
                if self.tryFork(self.gameMatrix.copy(), location, 'O'): #if there is only one fork to block, return true
                    forks.append(location)
                    if bestLocation[1] < 6:
                        bestLocation = (location, 6)
                        
                
                '''
                1. if one fork, block it
                2. block fork in a way that you have two in a row
                3. create a two in a row that forces the human to play (as long as it doesnt create a fork for them)
                '''
                '''elif self.tryCenter(location):
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
                            bestLocation = (location, 1)'''
        if bestLocation[1] == 6:
            if len(forks) == 1: #if there is only one fork, simply block it (so that tryFork will become false)
                for win in wins:
                    if forks[0] in win:
                        for space in win: #try to play each space and see if one changes tryFork to false
                            matrixCopy = self.gameMatrix.copy()
                            playMove(matrixCopy, space, 'X')
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
        if bestLocation[1] > 3:
            playMove(self.gameMatrix, bestLocation[0], 'X')
            
    def is2inRow(self, matrixCopy, location): #if playing the current location gives the comp a 2 in a row (NOT NECESSARILY TWO NEXT TO EACHOTHER), it returns the space the human is forced to play, otherwise it returns -1
        playMove(matrixCopy, location, 'X')
        sum = 0
        for win in wins:    
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
        playMove(matrixCopy, location, CorH)
        return isWin(matrixCopy)
    def tryWin_Block(self, matrixCopy, location, CorH):
        playMove(matrixCopy, location, CorH)
        return isWin(matrixCopy)
    def tryFork(self, matrixCopy, location, CorH):#CorH means try to find fork for the computer or the human (allows tryFork to be used in try_Fork_Block)
        playMove(matrixCopy, location, CorH)
        if not self.tryWin(matrixCopy, location, 'O'):
            winCounter = 0
            for loc in range(len(matrixCopy)): #loop through every possible space
                if isValidMove(matrixCopy, loc):
                    matrixCopy2 = matrixCopy.copy() #use a copy to test each move
                    playMove(matrixCopy2, loc, CorH) #play the space
                    if isWin(matrixCopy2): #if winCounter reaches two, that means there is a fork (2 possible winning moves)
                        winCounter += 1
            if winCounter == 2: #should this be more than 2?
                return True
        return False
    
    
    #NOTE: EFFICIENCY COULD BE IMPROVED WITH COMP LOOKING AHEAD AND FINDING SPOT THAT NOT ONLY BLOCKS OPPONENT'S
    #FORK, BUT ALSO PUTS COMP IN BEST POSITION TO WIN LATER (AS OF RIGHT NOW, COMP BLOCKS OPPONENTS FORK BY PLAYING
    #FIRST SPOT THAT BLOCKS FORK, BUT ISNT NECESSARILY THE BEST PLACE TO BLOCK IT)
    def tryForce(self, matrixCopy, location):
        playMove(matrixCopy, location, 'X')#otherwise create two in a row that forces human to defend as long as it doesnt create a fork for opponent
        #check if this is a two in a row
        forceHuman = []#places where human must play to block two in a row (possible edit, could use try_winBlock with human)
        for space in range(len(matrixCopy)):
            if self.tryWin_Block(matrixCopy, space, 'O'):
                forceHuman.append(space)
        for force in forceHuman:
            print('PENIS', force)
            matrixCopy2 = matrixCopy.copy()
            playMove(matrixCopy2, location, '0') #opponent forced to block human's win
            if (not self.tryFork(matrixCopy2, location, 'O')) and (not self.tryWin(matrixCopy2, location, 'O')): #if this doesnt create a fork nor a win for the human, return True
                return True #LOOK OUT THIS MIGHT BE WRONG
        return False
    
    def tryCenter(self, location):
        return location == 4
    def tryCorner_Opp(self, matrixCopy, location): 
        if (location == 0 or location == 2 or location == 6 or location == 8): #if its a corner
            if location == 0: #check to see if opponent is in each opposite corner
                if matrixCopy[8] == 'O':
                    return True
            elif location == 2:
                if matrixCopy[6] == 'O':
                    return True
            elif location == 6:
                if matrixCopy[2] == 'O':
                    return True
            elif location == 8:
                if matrixCopy[0] == 'O':
                    return True
    def tryCorner(self, location):
        return (location == 0 or location == 2 or location == 6 or location == 8)#if its a corner
    def trySide(self, location):
        return (location == 1 or location == 3 or location == 5 or location == 7)
        
            
    
    '''def tryWin(self, location):#checks each open spot to see if playing that spot would be a win
        
        for row in range(0,3): #check row for two in a row
            if sum(gameMatrix[row]) == 2: #if sum of row is 2, then it could possible have 2 in row
                if 0 in gameMatrix[row]: #if there is open spot in row
                    return gameMatrix[row].index(0)
        for column in range(0,3): #check columns for two in a row
            if sum(gameMatrix[column]) == 2:
                if 0 in gameMatrix[column]:
                    return gameMatrix[column].index(0)
        for :#check diagonal'''
        
            
    '''def find2inRow(self):
        sum = 0
        for row in range(0,3):
            if sum(gameMatrix[row]) == 2: #if sum of row is 2, then it could possible have 2 in row
                return gameMatrix[row].index(0)
        for column in range(0,3):'''

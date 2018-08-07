# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:15:10 2018

@author: ragoh
"""

import unittest
from playGame import *

'''
class simpleBoard(unittest.TestCase):
    board = [1, 1, 1, 0, -1, 0, -1, 0, 0]
    
    def test_isWin(self):
        self.assertTrue(isWin(board))'''


class test_isWin(unittest.TestCase):
    #test empty board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    def emptyBoard(self):
        self.assertFalse(isWin(board))
    
    #test board of one element
    board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    def lose1(self):
        self.assertFalse(isWin(board))
    
    #test board with two in a row
    board = [1, 0, 0, 1, 0, 0, 0, 0, 0]
    def lose2(self):
        self.assertFalse(isWin(board))
    
    #test three in a row horizontally
    board = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    def winH(self):
        self.assertTrue(isWin(board))
    
    #test three in a row vertically
    board = [0, 0, 1, 0, 0, 1, 0, 0, 1]
    def winV(self):
        self.assertTrue(isWin(board))
    
    #test three in a row diagonally
    board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    def winD(self):
        self.assertTrue(isWin(board))
    
    #test with human win
    board = [0, 0, 0, -1, -1, -1, 0, 0, 0]
    def winHum(self):
        self.assertTrue(isWin(board))

class test_playMove(unittest.TestCase):
    board = [0, 0, 0, 1, 1, 0, 0, 0, 0]
    playMove(board, 1, 'C') #move shouldn't be played
    playMove(board, 7, 'X')
    def win(self):
        self.assertTrue(isWin(board))
    






#test compMove methods
class test_tryWin(unittest.TestCase):
    board = [1, -1, 0, 1, 0, 0, 0, -1, 0]#try vertical win
    comp = Computer(board)
    comp.compMove()
    def win_vert(self):
        self.assertTrue(isWin(board))
    board = [-1, -1, 0, 0, 0, 0, 1, 0, 1]#try horizontal win
    comp = Computer(board)
    comp.compMove()
    def win_hor(self):
        self.assertTrue(isWin(board))
    board = [1, 0, 0, -1, 0, 0, -1, 0, 1]#try diagonal win
    comp = Computer(board)
    comp.compMove()
    def win_dia(self):
        self.assertTrue(isWin(board))
    
'''
class test_tryWin_Block(unittest.TestCase):
    
    
class test_tryFork(unittest.TestCase):

class test_tryFork_Block(unittest.TestCase)
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:15:10 2018

@author: ragoh
"""

import unittest
from Computer import *

'''
class simpleBoard(unittest.TestCase):
    board = [1, 1, 1, 0, -1, 0, -1, 0, 0]
    
    def test_isWin(self):
        self.assertTrue(isWin(board))'''


class test_isWin(unittest.TestCase):
    #test empty board
    def test_emptyBoard(self):
        self.assertFalse(isWin([0, 0, 0, 0, 0, 0, 0, 0, 0]))
 
    #test board of one element
    def test_lose1(self):
        self.assertFalse(isWin([1, 0, 0, 0, 0, 0, 0, 0, 0]))
    
    #test board with two in a row
    def test_lose2(self):
        self.assertFalse(isWin([1, 0, 0, 1, 0, 0, 0, 0, 0]))
    
    #test three in a row horizontally
    def test_winH(self):
        self.assertTrue(isWin([0, 0, 0, 0, 0, 0, 1, 1, 1]))
    
    #test three in a row vertically
    def test_winV(self):
        self.assertTrue(isWin([0, 0, 1, 0, 0, 1, 0, 0, 1]))
    
    #test three in a row diagonally
    def test_winD(self):
        self.assertTrue(isWin([1, 0, 0, 0, 1, 0, 0, 0, 1]))
    
    #test with human win
    def test_winHum(self):
        self.assertTrue(isWin([0, 0, 0, -1, -1, -1, 0, 0, 0]))


#tests playMove
class test_playMove(unittest.TestCase):
    def test_win(self):
        board = [0, 0, 1, 0, 1, 0, 0, 0, 0]
        playMove(board, 1, 'C') #move shouldn't be played
        playMove(board, 6, 'X')
        self.assertTrue(isWin(board))

    
#test compMove methods
class test_tryWin(unittest.TestCase): #test tryWin()
    def test_tryWin_vert(self):
        board = [1, -1, 0, 1, 0, 0, 0, -1, 0]#try vertical win
        comp = Computer(board)
        comp.compMove()
        self.assertTrue(isWin(board))
    def test_tryWin_hor(self):
        board = [-1, -1, 0, 0, 0, 0, 1, 0, 1]#try horizontal win
        comp = Computer(board)
        comp.compMove()
        self.assertTrue(isWin(board))
    def test_tryWin_dia(self):
        board = [1, 0, 0, -1, 0, 0, -1, 0, 1]#try diagonal win
        comp = Computer(board)
        comp.compMove()
        self.assertTrue(isWin(board))
  
class test_tryWin_Block(unittest.TestCase): #test tryWin_Block
    def test_tryWin_Block_vert(self): #block human's vertical win
        board = [-1, 0, 0, 0, 1, 0, -1, 0, 1]#try vertical win
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 0, 0, 1, 1, 0, -1, 0, 1])
    def test_tryWin_Block_hor(self): #block human's horizontal win
        board = [-1, 0, -1, 0, 1, 0, 0, 0, 1]#try horizontal win
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 1, -1, 0, 1, 0, 0, 0, 1])
    def test_tryWin__Block_dia(self): #block human's diagonal win
        board = [-1, 0, 0, 1, 0, 0, 1, 0, -1]#try diagonal win
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 0, 0, 1, 1, 0, 1, 0, -1])

#CANT THINK OF ANY MORE TEST CASES
class test_tryFork(unittest.TestCase): #test tryFork()
    def test_tryFork_1(self):
        board = [0, 0, -1, -1, 1, 0, 1, 0, 0]
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [0, 0, -1, -1, 1, 0, 1, 1, 0])
    def test_tryFork_3(self):
        board = [0, -1, 1, 0, -1, 0, 0, 1, 0]
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [0, -1, 1, 0, -1, 0, 0, 1, 1])


#I DONT THINK WELL EVER REACH THIS CASE BECAUSE COMP WONT ALLOW IT
class test_tryFork_Block(unittest.TestCase):
    def test_tryFork_noFork2Block(self): #if there is no fork, force opponent to block a 2 in a row
        board = [-1, 0, 0, 0, 1, 0, 0, 0, -1] #FIX THIS, IF X PLAYS THE CORNER, O HAS A FORK
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 1, 0, 0, 1, 0, 0, 0, -1])
    def test_tryFork_isFork2Block(self):
        board = [0, 0, 1, 0, -1, 0, -1, 1, 0] #two forks here, at 0 and 3
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [1, 0, 1, 0, -1, 0, -1, 1, 0])
        board = [-1, 1, 0, 0, -1, 0, 0, 0, 1] #two forks here, at 0 and 3
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 1, 0, 0, -1, 0, 1, 0, 1])
        board = [0, 1, -1, 0, 1, 0, 0, -1, 0]
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [0, 1, -1, 0, 1, 0, 0, -1, 1])
        board = [0, 0, 1, 1, -1, 0, -1, 0, 0]
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [0, 0, 1, 1, -1, 0, -1, 0, 1])
        board = [-1, 0, 0, 1, -1, 0, 0, 0, 1]
        comp = Computer(board)
        comp.compMove()
        self.assertEqual(board, [-1, 0, 1, 1, -1, 0, 0, 0, 1])

    

class test_tryCenter(unittest.TestCase):
    pass
    
class test_tryCorner_Opp(unittest.TestCase):
    pass
class test_tryCorner(unittest.TestCase):
    pass
class test_trySide(unittest.TestCase):
    pass
    

class test_is2inRow(unittest.TestCase):
    def test1(self):
        board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        comp = Computer(board)
        self.assertEqual(2, comp.is2inRow(board, 1))
    def test2(self):
        board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        comp = Computer(board)
        self.assertEqual(8, comp.is2inRow(board, 4))
    def test3(self):
        board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        comp = Computer(board)
        self.assertEqual(-1, comp.is2inRow(board, 5))
    def test4(self):
        board = [1, 0, -1, 0, 0, 0, -1, 0, 0]
        comp = Computer(board)
        self.assertEqual(8, comp.is2inRow(board, 4))
    def test5(self): #the two in a row dont have to be necessarily adjacent
        board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        comp = Computer(board)
        self.assertEqual(1, comp.is2inRow(board, 2))


    
    
    
    
        
    
if __name__ == '__main__':
    unittest.main()
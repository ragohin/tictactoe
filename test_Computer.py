# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:15:10 2018

@author: ragoh
"""

import unittest
from Computer import *

class test_isWin(unittest.TestCase):
    #test empty board
    def test_emptyBoard(self):
        self.assertFalse(Player.isWin(Player([0, 0, 0, 0, 0, 0, 0, 0, 0]))[0])
    #test board of one element
    def test_lose1(self):
        self.assertFalse(Player.isWin(Player([1, 0, 0, 0, 0, 0, 0, 0, 0]))[0])
    #test board with two in a row
    def test_lose2(self):
        self.assertFalse(Player.isWin(Player([1, 0, 0, 1, 0, 0, 0, 0, 0]))[0])
    #test three in a row horizontally
    def test_winH(self):
        self.assertTrue(Player.isWin(Player([0, 0, 0, 0, 0, 0, 1, 1, 1]))[0])
    #test three in a row vertically
    def test_winV(self):
        self.assertTrue(Player.isWin(Player([0, 0, 1, 0, 0, 1, 0, 0, 1]))[0])
    #test three in a row diagonally
    def test_winD(self):
        self.assertTrue(Player.isWin(Player([1, 0, 0, 0, 1, 0, 0, 0, 1]))[0])
    #test with human win
    def test_winHum(self):
        self.assertTrue(Player.isWin(Player([0, 0, 0, -1, -1, -1, 0, 0, 0]))[0])

#tests playMove
class test_playMove(unittest.TestCase):
    def test_win(self):
        p = Player([0, 0, 1, 0, 1, 0, 0, 0, 0])
        p.playMove(1, 'C') #move shouldn't be played
        p.playMove(6, 'X')
        self.assertTrue(p.isWin()[0])

#test compMove methods
class test_tryWin(unittest.TestCase): #test tryWin()
    def test_tryWin_vert(self):
        comp = Computer([1, -1, 0, 1, 0, 0, 0, -1, 0])#try vertical win
        comp.compMove()
        self.assertTrue(comp.isWin()[0])
    def test_tryWin_hor(self):
        comp = Computer([-1, -1, 0, 0, 0, 0, 1, 0, 1])#try horizontal win
        comp.compMove()
        self.assertTrue(comp.isWin()[0])
    def test_tryWin_dia(self):
        comp = Computer([1, 0, 0, -1, 0, 0, -1, 0, 1])#try diagonal win
        comp.compMove()
        self.assertTrue(comp.isWin()[0])

class test_tryWin_Block(unittest.TestCase): #test tryWin_Block
    def test_tryWin_Block_vert(self): #block human's vertical win
        comp = Computer([-1, 0, 0, 0, 1, 0, -1, 0, 1])#try vertical win
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 0, 0, 1, 1, 0, -1, 0, 1])
    def test_tryWin_Block_hor(self): #block human's horizontal win
        comp = Computer([-1, 0, -1, 0, 1, 0, 0, 0, 1])#try horizontal win
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 1, -1, 0, 1, 0, 0, 0, 1])
    def test_tryWin__Block_dia(self): #block human's diagonal win
        comp = Computer([-1, 0, 0, 1, 0, 0, 1, 0, -1])#try diagonal win
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 0, 0, 1, 1, 0, 1, 0, -1])

#CANT THINK OF ANY MORE TEST CASES
class test_tryFork(unittest.TestCase): #test tryFork()
    def test_tryFork_1(self):
        comp = Computer([0, 0, -1, -1, 1, 0, 1, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, 0, -1, -1, 1, 0, 1, 1, 0])
    def test_tryFork_3(self):
        comp = Computer([0, -1, 1, 0, -1, 0, 0, 1, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, -1, 1, 0, -1, 0, 0, 1, 1])

#I DONT THINK WELL EVER REACH THIS CASE BECAUSE COMP WONT ALLOW IT
class test_tryFork_Block(unittest.TestCase):
    def test_tryFork_noFork2Block(self): #if there is no fork, force opponent to block a 2 in a row
        comp = Computer([-1, 0, 0, 0, 1, 0, 0, 0, -1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 1, 0, 0, 1, 0, 0, 0, -1])
    def test_tryFork_isFork2Block(self):
        comp = Computer([0, 0, 1, 0, -1, 0, -1, 1, 0]) #two forks here, at 0 and 3
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, 0, 1, 0, -1, 0, -1, 1, 0])
        comp = Computer([-1, 1, 0, 0, -1, 0, 0, 0, 1]) #two forks here, at 0 and 3
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 1, 0, 0, -1, 0, 1, 0, 1])
        comp = Computer([0, 1, -1, 0, 1, 0, 0, -1, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, 1, -1, 0, 1, 0, 0, -1, 1])
        comp = Computer([0, 0, 1, 1, -1, 0, -1, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, 0, 1, 1, -1, 0, -1, 0, 1])
        comp = Computer([-1, 0, 0, 1, -1, 0, 0, 0, 1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 0, 1, 1, -1, 0, 0, 0, 1])

class test_tryCenter(unittest.TestCase):
    def test_empty(self):
        comp = Computer([0, 0, 0, 0, 0, 0, 0, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, 0, 0, 0, 1, 0, 0, 0, 0])
    def test_1stCompMove_1(self):
        comp = Computer([-1, 0, 0, 0, 0, 0, 0, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 0, 0, 0, 1, 0, 0, 0, 0])
    def test_1stCompMove_2(self):
        comp = Computer([0, 0, 0, 0, 0, 0, 0, -1, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [0, 0, 0, 0, 1, 0, 0, -1, 0])
    def test_lastMove(self):
        comp = Computer([1, 1, -1, -1, 0, 1, 1, -1, -1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, 1, -1, -1, 1, 1, 1, -1, -1])

class test_tryCorner_Opp(unittest.TestCase):
    def test_1(self):
        comp = Computer([-1, 0, 0, 0, 1, 0, 0, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [-1, 0, 0, 0, 1, 0, 0, 0, 1])
    def test_2(self):
        comp = Computer([0, 0, 0, 0, 1, 0, 0, 0, -1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, 0, 0, 0, 1, 0, 0, 0, -1])

class test_tryCorner(unittest.TestCase):
    def test_1(self):
        comp = Computer([0, 0, 0, 0, -1, 0, 0, 0, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, 0, 0, 0, -1, 0, 0, 0, 0])
    def test_2(self):
        comp = Computer([0, -1, 0, 0, 1, 0, 0, -1, 0])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, -1, 0, 0, 1, 0, 0, -1, 0])

class test_trySide(unittest.TestCase):
    def test_1(self):
        comp = Computer([1, -1, 1, 1, -1, 0, -1, 1, -1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, -1, 1, 1, -1, 1, -1, 1, -1])
    def test_2(self):
        comp = Computer([1, 0, -1, -1, -1, 1, 1, 1, -1])
        comp.compMove()
        self.assertEqual(comp.getMatrix(), [1, 1, -1, -1, -1, 1, 1, 1, -1])
    
class test_is2inRow(unittest.TestCase):
    def test1(self):
        comp = Computer([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(2, comp.is2inRow(comp.getMatrix(), 1))
    def test2(self):
        comp = Computer([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(8, comp.is2inRow(comp.getMatrix(), 4))
    def test3(self):
        comp = Computer([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(-1, comp.is2inRow(comp.getMatrix(), 5))
    def test4(self):
        comp = Computer([1, 0, -1, 0, 0, 0, -1, 0, 0])
        self.assertEqual(8, comp.is2inRow(comp.getMatrix(), 4))
    def test5(self): #the two in a row dont have to be necessarily adjacent
        comp = Computer([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(1, comp.is2inRow(comp.getMatrix(), 2))    

if __name__ == '__main__':
    unittest.main()
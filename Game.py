# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:01:53 2018

@author: ragoh
"""

from Player import *
from Computer import *

class Game(object):
    def __init__(self, comp_in):
        self.comp = comp_in #computer player in this game
        
    def playGame(self):
        while True:
            if not self.comp.isCatsGame() and not self.comp.isWin(self.comp.getMatrix())[0]:
                self.comp.compMove()
                displayBoard(self.comp.getMatrix())
            if not self.comp.isCatsGame() and not self.comp.isWin(self.comp.getMatrix())[0]:
                self.comp.humanMove()
            else:
                break
        if self.comp.isCatsGame():
            print('Cats game!')
        elif self.comp.isWin(self.comp.getMatrix())[0]:
            print(self.comp.isWin(self.comp.getMatrix())[1], 'wins!')

        

game = Game(Computer())
game.playGame()
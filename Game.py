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
            try:
                first = int(input('Would you like to make the first move? (1 for yes, 0 for no) \n'))
                if first == 1:
                    first = 'Human'
                    break
                elif first == 0:
                    first = 'Comp'
                    break
                else:
                    print('Invalid input!')
            except ValueError:
                print('Invalid input')
        while True:
            if not self.comp.isCatsGame() and not self.comp.isWin(self.comp.getMatrix())[0]:
                if first == 'Human':
                    self.comp.humanMove()
                else:
                    self.comp.compMove()
            if not self.comp.isCatsGame() and not self.comp.isWin(self.comp.getMatrix())[0]:
                if first == 'Human':
                    self.comp.compMove()
                else:
                    self.comp.humanMove()
            else:
                break
        if self.comp.isCatsGame():
            displayBoard(self.comp.getMatrix())
            print('Cats game!')
        elif self.comp.isWin(self.comp.getMatrix())[0]:
            displayBoard(self.comp.getMatrix())
            print(self.comp.isWin(self.comp.getMatrix())[1], 'wins!')

game = Game(Computer())
game.playGame()
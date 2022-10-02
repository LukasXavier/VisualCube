'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: horizontal3x3.py
    Purpose: concrete implementation of an ABCCubeNxN for a 3x3
'''

from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

class _3x3(ABCCubeNxN):
    '''
        a concrete implementation of a 3x3

        move(str): updates the internal model based on a WCA notation string
    '''
    # a structural relation between notation and the ABCCubeNxN `_move()` method
    MOVESET = {
        "x": {
            "filter": ["L'", "L", "M'", "M", "R", "R'"],
            "swap": ["L", "R'"],
            "layer": ["L", "M", "R"],
        },
        "y": {
            "filter": ["U", "U'", "E", "E'", "D'", "D"],
            "swap": ["U", "D'"],
            "layer": ["U", "E", "D"],
        },
        "z": {
            "filter": ["B'", "B", "S'", "S", "F", "F'"],
            "swap": ["B", "F'"],
            "layer": ["B", "S", "F"],
        },
    }

    def __init__(self) -> None:
        super().__init__(3)

    def move(self, notation: str) -> None:
        '''
            Takes in a single WCA notation and acts upon the internal model
        '''
        # handles X2 and Xw2 moves
        if (len(notation) > 1):
            if (notation[1] == '2'):
                self.move(notation[0])
                self.move(notation[0])
                return
            elif (len(notation) == 3 and notation[2] == '2'):
                self.move(notation[0])
                self.move(notation[0])
                return
        self._move(notation)

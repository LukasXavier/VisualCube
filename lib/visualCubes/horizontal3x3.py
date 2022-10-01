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
        rotate(str): WIP: unimplemented
    '''

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
            # WIP: need to implement middle slices to do handle Xw moves

        # handles F, F'
        if ("F" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_ZAxis(3,2,prime=notation=="F'"))
            self._face_rotate(FRONT, counter=notation=="F'")

        # handles U, U'
        elif ("U" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_YAxis(3,0))
            self._face_rotate(UP, counter=notation=="U'")
        
        # handles B, B'
        elif ("B" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_ZAxis(3,0,prime=notation=="B"))
            self._face_rotate(BACK, counter=notation=="B'")

        # handles D, D'        
        elif ("D" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_YAxis(3,2))
            self._face_rotate(DOWN, counter=notation=="D'")
        
        # handles L, L'
        elif ("L" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_XAxis(3,0,prime=notation=="L"))
            self._face_rotate(LEFT, counter=notation=="L'")
        
        # handles R, R'
        elif ("R" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_XAxis(3,2,prime=notation=="R'"))
            self._face_rotate(RIGHT, counter=notation=="R'")
        else:
            print(f"unimplemented notation: '{notation}'")

    def rotate(self, direction: str) -> None: ...
    '''
        WIP: unimplemented
    '''

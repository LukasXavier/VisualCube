'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: vertical3x3.py
    Purpose: display an unwrapped cube to visualize a 3x3 rubik's cube.

    WARNING: this class is deprecated and is only included as a reference
        there is no guarantee that this class will work as I continue to grow
        this project
'''

from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

@DeprecationWarning
class _3x3(ABCCubeNxN):
    '''
        a previous implementation of a 3x3 cube where the cube is unwrapped
        'vertically' 
    '''
    size = 50

    def __init__(self) -> None:
        self.faces = [[color for _ in range(9)] for color in NxN.COLORS]

    def move(self, notation: str) -> None:
        '''
        notation: a standard WCA notation for 3x3
        acts upon the cube preforming the input
        '''
        if (len(notation) > 1):
            if (notation[1] == '2'):
                self.move(notation[0])
                self.move(notation[0])
                return
        if (notation == 'F'):
            # rotates 'strip around' face       #piece index in 'cycle'
            self._swap_four(**NxN.SWAP['F'], t=[[6,0,2,8],[7,3,1,5],[8,6,0,2]])
            # rotates face
            self._face_rotate(FRONT)
        elif (notation == "F'"):
            self._swap_four(**NxN.SWAP["F'"], t=[[6,8,2,0],[7,5,1,3],[8,2,0,6]])
            self._face_rotate(FRONT, counter=True)
        elif (notation == 'U'):
            self._swap_four(**NxN.SWAP['U'], t=[[0,0,8,0],[1,1,7,1],[2,2,6,2]])
            self._face_rotate(UP)
        elif (notation == "U'"):
            self._swap_four(**NxN.SWAP["U'"], t=[[0,0,8,0],[1,1,7,1],[2,2,6,2]])
            self._face_rotate(UP, counter=True)
        elif (notation == 'B'):
            self._swap_four(**NxN.SWAP["F'"], t=[[0,6,8,2],[1,3,7,5],[2,0,6,8]])
            self._face_rotate(BACK)
        elif (notation == "B'"):
            self._swap_four(**NxN.SWAP['F'], t=[[0,2,8,6],[1,5,7,3],[2,8,6,0]])
            self._face_rotate(BACK, counter=True)
        elif (notation == "D"):
            self._swap_four(**NxN.SWAP["U'"], t=[[6,6,2,6],[7,7,1,7],[8,8,0,8]])
            self._face_rotate(DOWN)
        elif (notation == "D'"):
            self._swap_four(**NxN.SWAP['U'], t=[[6,6,2,6],[7,7,1,7],[8,8,0,8]])
            self._face_rotate(DOWN, counter=True)
        elif (notation == "L"):
            self._swap_four(**NxN.SWAP['R'], t=[[0,0,0,0],[3,3,3,3],[6,6,6,6]])
            self._face_rotate(LEFT)
        elif (notation == "L'"):
            self._swap_four(**NxN.SWAP["R'"], t=[[0,0,0,0],[3,3,3,3],[6,6,6,6]])
            self._face_rotate(LEFT, counter=True)
        elif (notation == "R"):
            self._swap_four(**NxN.SWAP["R'"], t=[[8,8,8,8],[5,5,5,5],[2,2,2,2]])
            self._face_rotate(RIGHT)
        elif (notation == "R'"):
            self._swap_four(**NxN.SWAP['R'], t=[[8,8,8,8],[5,5,5,5],[2,2,2,2]])
            self._face_rotate(RIGHT, counter=True)
        else:
            print(f"sus: '{notation}'")

    def rotate(self, direction: str) -> None: ...

    def _get_pos(self, face: int, pos: int) -> tuple[int, int]:
        if (face == LEFT):
            return (50 + (pos%3) * 55, 210 + (pos//3) * 55)
        elif (face == RIGHT):
            return (380 + (pos%3) * 55, 210 + (pos//3) * 55)
        else:
            return (215 + (pos%3) * 55, 45 + (face*165) + (pos//3) * 55)

    def _face_rotate(self, color: int, *, counter: bool = False) -> None:
        '''
        '''
        self._swap_four(color, t=([[0,6,8,2],[1,3,7,5]] if counter else [[0,2,8,6],[1,5,7,3]]))

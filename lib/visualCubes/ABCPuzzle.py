'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: ABCPuzzle.py
    Purpose: abstract base classes for all twisty puzzles

    WIP: currently only implements a NxN puzzle
'''

from typing import Callable
from ..graphics import Gui
from ..visualCubeLib import *
from abc import ABCMeta, abstractmethod


class ABCCubeNxN(metaclass=ABCMeta):
    '''
        the base class for NxN cubes to extend from
    '''

    def __init__(self, size: int) -> None:
        self.cube_size = size
        self.size = (160 - (5 * (size - 1))) / size
        self.faces = [[color for _ in range(size * size)] for color in NxN.COLORS]

    @abstractmethod
    def move(self, notation: str) -> None: ...
    '''
        expected that move takes in some WCA notation and acts upon the internal model
    '''

    @abstractmethod
    def rotate(self, direction: str) -> None: ...
    '''
        expected that rotate takes in some WCA rotation notation and acts upon the internal model
    '''

    def draw(self, gui: Gui) -> None:
        '''
            used to draw the NxN cube to the gui
        '''
        gui.clear()
        # draws each square of the internal model
        for i in range(len(self.faces)):
            for j in range(len(self.faces[0])):
                gui.rectangle(
                    pos=self._get_pos(i, j, (gui.get_width(), gui.get_height())),
                    width=self.size,
                    height=self.size,
                    fill=self.faces[i][j]
                )

    def _get_pos(self, face: int, pos: int, screen_size: tuple[int, int]) -> tuple[int ,int]:
        '''
            determines where to start drawing a specific square
        '''
        if (face == UP):
            return (210 + (pos%self.cube_size) * (self.size + 5),
                    50 + (pos//self.cube_size) * (self.size + 5))
        if (face == DOWN):
            return (210 + (pos%self.cube_size) * (self.size + 5),
                    380 + (pos//self.cube_size) * (self.size + 5))
        return (NxN.OFFSET[screen_size][face] + (pos%self.cube_size) * (self.size + 5),
                215 + (pos//self.cube_size) * (self.size + 5))

    def apply_alg(self, *, str_: str | None = None, s_list: list[str] | None = None) -> None:
        '''
            can take either a space separated string of WCA moves or a list of WCA moves
            then for each move acts upon the cube
        '''
        if (str_):
            for m in str_.split(" "):
                self.move(m)
        elif (s_list):
            for m in s_list:
                self.move(m)
    
    def _swap_four(self, color0: int, color1: int = None, color2: int = None, color3: int = None, *, t: list[list[int]]) -> None:
        '''
            since a cube's face is made up of 4 edges to rotate a 4 cycle swap occurs
            the method takes in a sequence of swaps to preform
        '''
        # for swapping face tiles we use the same color, otherwise all colors are specified by the caller
        # using the NxN.SWAP[] map
        if (color1 == None):
            color1, color2, color3 = color0, color0, color0
        for l in t:
            pool = [self.faces[color0][l[0]], self.faces[color1][l[1]], self.faces[color2][l[2]], self.faces[color3][l[3]]]
            self.faces[color0][l[0]], self.faces[color1][l[1]], self.faces[color2][l[2]], self.faces[color3][l[3]] = \
                pool[3], pool[0], pool[1], pool[2]

    def _face_rotate(self, color: int, *, counter: bool = False) -> None:
        '''
            cycles the inner tiles of a large cube's 'centers' (4x4 and up)
        '''
        from ..visualCubeLib import NxN
        self._swap_four(color, t=NxN.face_edge(self.cube_size, prime=counter))
        self._swap_four(color, t=NxN.face_corner(self.cube_size, prime=counter))

    @staticmethod
    # TODO: look at last character for a '2'.
    # TODO: look at last character for a 'w'.
    # TODO: look at first character for int.
    # NOTE: https://ruwix.com/the-rubiks-cube/notation/advanced/
    def _notation_filter(notation: str, move: Callable[[str], None]) -> bool:
        if (len(notation) == 2 and notation[1] != "'"):    # for cases like 'Rw', 'R2', 'r2'
            if (notation[1] == '2'):    # specifically for 'R2'/'r2' cases
                move(notation[0])
                move(notation[0])
                return True
            elif (notation[1] == 'w'):   # for cases like Rw, we recurse on 'r' and 'R'
                move(notation[0].lower())
                move(notation[0])
                return True
        if (len(notation) == 3): # handles 'Rw2', "Rw'"
            if (notation[2] == '2'):
                move(notation[:2])
                move(notation[:2])
                return True
            elif (notation[2] == "'"):   # handles the "Rw'" case by recursing on "r'" and "R'"
                move(f"{notation[0].lower()}'")
                move(f"{notation[0]}'")
                return True
        return False
        
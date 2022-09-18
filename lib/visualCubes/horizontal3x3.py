from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

class _3x3(ABCCubeNxN):
    cube_size = 3
    size = (160 - (5 * (cube_size-1)))/cube_size

    def __init__(self) -> None:
        self.faces = [[color for _ in range(3*3)] for color in NxN.COLORS]

    def move(self, notation: str) -> None:
        
        if (len(notation) > 1 and notation[1] == '2'):
            self.move(notation[0])
            self.move(notation[0])
            return

        if ("F" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_ZAxis(3,2,prime=notation=="F'"))
            self._face_rotate(FRONT, counter=notation=="F'")

        elif ("U" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_YAxis(3,0))
            self._face_rotate(UP, counter=notation=="U'")
        
        elif ("B" in notation):
            if ("B'" == notation):
                print(NxN.SWAP["B'"], NxN.horizontal_ZAxis(3,0))
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_ZAxis(3,0,prime=notation=="B"))
            self._face_rotate(BACK, counter=notation=="B'")
        
        elif ("D" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_YAxis(3,2))
            self._face_rotate(DOWN, counter=notation=="D'")
        
        elif ("L" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_XAxis(3,0,prime=notation=="L"))
            self._face_rotate(LEFT, counter=notation=="L'")
        
        elif ("R" in notation):
            self._swap_four(**NxN.SWAP[notation], t=NxN.horizontal_XAxis(3,2,prime=notation=="R'"))
            self._face_rotate(RIGHT, counter=notation=="R'")
        else:
            print(f"sus: '{notation}'")

    def rotate(self, direction: str) -> None: ...

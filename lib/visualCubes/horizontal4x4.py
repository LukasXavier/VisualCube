# COMMENT:

from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

class _4x4(ABCCubeNxN):

    def __init__(self):
        super().__init__(4)

    def move(self, notation: str) -> None:
        if self._notation_filter(notation, self.move): return
        if (notation in ['R', "R'", "r'", "r", "l'", "l", "L", "L'"]):
            swap = "R" if (notation in ["R", "r", "l'", "L'"]) else "R'"
            face = RIGHT if ("R" in notation) else LEFT if ("L" in notation) else None
            transform = NxN.horizontal_XAxis(
                4,
                ['L', 'l', 'r', 'R'].index(notation[0]),
                prime=notation in ["L", "l", "r'", "R'"]
            )

        elif (notation in ["U", "U'", "u'", "u", "d'", "d", "D'", "D"]):
            swap = "U" if (notation in ["U", "u", "d'", "D'"]) else "U'"
            face = UP if ("U" in notation) else DOWN if ("D" in notation) else None
            transform = NxN.horizontal_YAxis(
                4,
                ['U', 'u', 'd', 'D'].index(notation[0])
            )

        elif (notation in ["F", "F'", "f'", "f", "b'", "b", "B", "B'"]):
            swap = "F" if (notation in ["F", "f", "b'", "B'"]) else "F'"
            face = FRONT if ("F" in notation) else BACK if ("B" in notation) else None
            transform = NxN.horizontal_ZAxis(
                4,
                ['B', 'b', 'f', 'F'].index(notation[0]),
                prime=notation in ["B", "b", "f'", "F'"]
            )

        else:
            print(f"sus: |{notation}|")
            return
            
        self._swap_four(**NxN.SWAP[swap], t=transform)
        if (face != None):
            self._face_rotate(face, counter="'" in notation)

    def rotate(self, direction: str) -> None: ...

    def test(self):
        print(type(self.move))
from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

class _4x4(ABCCubeNxN):
    cube_size = 4
    size = (160 - (5 * (cube_size-1)))/cube_size

    def __init__(self):
        self.faces = [[color for _ in range(4*4)] for color in NxN.COLORS]

    def move(self, notation: str) -> None:
        if (len(notation) == 2 and notation[1] != "'"):    # for cases like 'Rw', 'R2', 'r2'
            if (notation[1] == '2'):    # specifically for 'R2'/'r2' cases
                self.move(notation[0])
                self.move(notation[0])
                return
            elif (notation[1] == 'w'):   # for cases like Rw, we recurse on 'r' and 'R'
                self.move(notation[0].lower())
                self.move(notation[0])
                return
        if (len(notation) == 3): # handles 'Rw2', "Rw'"
            if (notation[2] == '2'):
                self.move(notation[:2])
                self.move(notation[:2])
                return
            elif (notation[2] == "'"):   # handles the "Rw'" case by recursing on "r'" and "R'"
                self.move(f"{notation[0].lower()}'")
                self.move(f"{notation[0]}'")
                return
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
# COMMENT:

from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN


class _4x4(ABCCubeNxN):

    MOVESET = {
        "x": {
            "filter": ["L'", "L", "l'", "l", "r", "r'", "R", "R'"],
            "swap": ["L", "l", "r'", "R'"],
            "layer": ["L", "l", "r", "R"]
        },
        "y": {
            "filter": ["U", "U'", "u", "u'", "d'", "d", "D'", "D"],
            "swap": ["U", "u", "d'", "D'"],
            "layer": ["U", "u", "d", "D"]
        },
        "z": {
            "filter": ["B'", "B", "b'", "b", "f", "f'", "F", "F'"],
            "swap": ["B", "b", "f'", "F'"],
            "layer": ["B", "b", "f", "F"]
        },
    }

    def __init__(self):
        super().__init__(4)

    def move(self, notation: str) -> None:
        if self._notation_filter(notation, self.move): return
        self._move(notation)

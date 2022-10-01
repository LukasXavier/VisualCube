# COMMENT:

from ..visualCubeLib import *
from .ABCPuzzle import ABCCubeNxN

class _7x7(ABCCubeNxN):

    def __init__(self):
        super().__init__(7)

    def move(self, notation: str) -> None:
        ...

    def rotate(self, direction: str) -> None: ...

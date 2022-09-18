'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: test_horizontal3x3.py
    Purpose: checks that the NxN.horizontal_*() functions match expected outputs
'''

from lib.visualCubeLib import *
from Test.Tester import attempt
import sys

sys.path.append("..")

def run() -> None:
    '''
    a basic test runner that goes through each possible 'valid' input for a 3x3
    and checks it against a known answer, this is primarily for backwards
    compatibility as I expand the NxN class to make sure I don't break previously
    working code as I implement more cubes
    '''
    attempt(
        info="3x3 L",
        left=NxN.horizontal_XAxis(3, 0, prime=True),
        right=[[0,0,0,8],[3,3,3,5],[6,6,6,2]]
    )
    attempt(
        info="3x3 L'",
        left=NxN.horizontal_XAxis(3, 0),
        right=[[0,8,0,0],[3,5,3,3],[6,2,6,6]]
    )
    attempt(
        info="3x3 R",
        left=NxN.horizontal_XAxis(3, 2),
        right=[[2,6,2,2],[5,3,5,5],[8,0,8,8]]
    )
    attempt(
        info="3x3 R'",
        left=NxN.horizontal_XAxis(3, 2, prime=True),
        right=[[2,2,2,6],[5,5,5,3],[8,8,8,0]]
    )
    attempt(
        info="3x3 U",
        left=NxN.horizontal_YAxis(3, 0),
        right=[[0,0,0,0],[1,1,1,1],[2,2,2,2]]
    )
    attempt(
        info="3x3 U'",
        left=NxN.horizontal_YAxis(3, 0),
        right=[[0,0,0,0],[1,1,1,1],[2,2,2,2]]
    )
    attempt(
        info="3x3 D",
        left=NxN.horizontal_YAxis(3, 2),
        right=[[6,6,6,6],[7,7,7,7],[8,8,8,8]]
    )
    attempt(
        info="3x3 D'",
        left=NxN.horizontal_YAxis(3, 2),
        right=[[6,6,6,6],[7,7,7,7],[8,8,8,8]]
    )
    attempt(
        info="3x3 F",
        left=NxN.horizontal_ZAxis(3, 2),
        right=[[6,0,2,8],[7,3,1,5],[8,6,0,2]]
    )
    attempt(
        info="3x3 F'",
        left=NxN.horizontal_ZAxis(3, 2, prime=True),
        right=[[6,8,2,0],[7,5,1,3],[8,2,0,6]]
    )
    attempt(
        info="3x3 B",
        left=NxN.horizontal_ZAxis(3, 0, prime=True),
        right=[[0,6,8,2],[1,3,7,5],[2,0,6,8]]
    )
    attempt(
        info="3x3 B'",
        left=NxN.horizontal_ZAxis(3, 0),
        right=[[0,2,8,6],[1,5,7,3],[2,8,6,0]]
    )

    # _face_rotate 3x3
    attempt(
        info="3x3 face rotate clockwise",
        left=NxN.face_corner(3) + NxN.face_edge(3),
        right=[[0,2,8,6],[1,5,7,3]]
    )
    attempt(
        info="3x3 face rotate counterclockwise",
        left=NxN.face_corner(3, prime=True) + NxN.face_edge(3, prime=True),
        right=[[0,6,8,2],[1,3,7,5]]
    )

    print("\033[32mAll Horizontal 3x3 tests passed\033[m")

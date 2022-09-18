'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: test_horizontal4x4.py
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
    # X Axis tests
    attempt(
        info="4x4 L",
        left=NxN.horizontal_XAxis(4, 0, prime=True),
        right=[[0,0,0,15],[4,4,4,11],[8,8,8,7],[12,12,12,3]]
    )
    attempt(
        info="4x4 L'",
        left=NxN.horizontal_XAxis(4, 0),
        right=[[0,15,0,0],[4,11,4,4],[8,7,8,8],[12,3,12,12]]
    )
    attempt(
        info="4x4 l",
        left=NxN.horizontal_XAxis(4, 1, prime=True),
        right=[[1,1,1,14],[5,5,5,10],[9,9,9,6],[13,13,13,2]]
    )
    attempt(
        info="4x4 l'",
        left=NxN.horizontal_XAxis(4, 1),
        right=[[1,14,1,1],[5,10,5,5],[9,6,9,9],[13,2,13,13]]
    )
    attempt(
        info="4x4 r",
        left=NxN.horizontal_XAxis(4, 2),
        right=[[2,13,2,2],[6,9,6,6],[10,5,10,10],[14,1,14,14]]
    )
    attempt(
        info="4x4 r'",
        left=NxN.horizontal_XAxis(4, 2, prime=True),
        right=[[2,2,2,13],[6,6,6,9],[10,10,10,5],[14,14,14,1]]
    )
    attempt(
        info="4x4 R",
        left=NxN.horizontal_XAxis(4, 3),
        right=[[3,12,3,3],[7,8,7,7],[11,4,11,11],[15,0,15,15]]
    )
    attempt(
        info="4x4 R'",
        left=NxN.horizontal_XAxis(4, 3, prime=True),
        right=[[3,3,3,12],[7,7,7,8],[11,11,11,4],[15,15,15,0]]
    )
    # Y Axis tests
    attempt(
        info="4x4 U",
        left=NxN.horizontal_YAxis(4, 0),
        right=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    )
    attempt(
        info="4x4 U'",
        left=NxN.horizontal_YAxis(4, 0),
        right=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    )
    attempt(
        info="4x4 u",
        left=NxN.horizontal_YAxis(4, 1),
        right=[[4,4,4,4],[5,5,5,5],[6,6,6,6],[7,7,7,7]]
    )
    attempt(
        info="4x4 u'",
        left=NxN.horizontal_YAxis(4, 1),
        right=[[4,4,4,4],[5,5,5,5],[6,6,6,6],[7,7,7,7]]
    )
    attempt(
        info="4x4 d",
        left=NxN.horizontal_YAxis(4, 2),
        right=[[8,8,8,8],[9,9,9,9],[10,10,10,10],[11,11,11,11]]
    )
    attempt(
        info="4x4 d'",
        left=NxN.horizontal_YAxis(4, 2),
        right=[[8,8,8,8],[9,9,9,9],[10,10,10,10],[11,11,11,11]]
    )
    attempt(
        info="4x4 D",
        left=NxN.horizontal_YAxis(4, 3),
        right=[[12,12,12,12],[13,13,13,13],[14,14,14,14],[15,15,15,15]]
    )
    attempt(
        info="4x4 D'",
        left=NxN.horizontal_YAxis(4, 3),
        right=[[12,12,12,12],[13,13,13,13],[14,14,14,14],[15,15,15,15]]
    )
    # Z Axis tests
    attempt(
        info="4x4 B",
        left=NxN.horizontal_ZAxis(4, 0, prime=True),
        right=[[0,12,15,3],[1,8,14,7],[2,4,13,11],[3,0,12,15]]
    )
    attempt(
        info="4x4 B'",
        left=NxN.horizontal_ZAxis(4, 0),
        right=[[0,3,15,12],[1,7,14,8],[2,11,13,4],[3,15,12,0]]
    )
    attempt(
        info="4x4 b",
        left=NxN.horizontal_ZAxis(4, 1, prime=True),
        right=[[4,13,11,2],[5,9,10,6],[6,5,9,10],[7,1,8,14]]
    )
    attempt(
        info="4x4 b'",
        left=NxN.horizontal_ZAxis(4, 1),
        right=[[4,2,11,13],[5,6,10,9],[6,10,9,5],[7,14,8,1]]
    )
    attempt(
        info="4x4 f",
        left=NxN.horizontal_ZAxis(4, 2),
        right=[[8,1,7,14],[9,5,6,10],[10,9,5,6],[11,13,4,2]]
    )
    attempt(
        info="4x4 f'",
        left=NxN.horizontal_ZAxis(4, 2, prime=True),
        right=[[8,14,7,1],[9,10,6,5],[10,6,5,9],[11,2,4,13]]
    )
    attempt(
        info="4x4 F",
        left=NxN.horizontal_ZAxis(4, 3),
        right=[[12,0,3,15],[13,4,2,11],[14,8,1,7],[15,12,0,3]]
    )
    attempt(
        info="4x4 F'",
        left=NxN.horizontal_ZAxis(4, 3, prime=True),
        right=[[12,15,3,0],[13,11,2,4],[14,7,1,8],[15,3,0,12]]
    )

    # _face_rotate 4x4
    attempt(
        info="4x4 face rotate clockwise",
        left=NxN.face_corner(4) + NxN.face_edge(4),
        right=[[0,3,15,12],[5,6,10,9],[1,7,14,8],[2,11,13,4]]
    )
    attempt(
        info="4x4 face rotate counterclockwise",
        left=NxN.face_corner(4, prime=True) + NxN.face_edge(4, prime=True),
        right=[[0,12,15,3],[5,9,10,6],[1,8,14,7],[2,4,13,11]]
    )

    print("\033[32mAll Horizontal 4x4 tests passed\033[m")

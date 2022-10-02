'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: visualCubeLib.py
    Purpose: My intent is for this file to act as a pseudo '.h'
'''

# enums for cube face
UP = 0
FRONT = 1
DOWN = 2
BACK = 3
LEFT = 4
RIGHT = 5


class Color:
    '''
        Scoped enum for hex colors
    '''
    WHITE = '#ffffff'
    GREEN = '#006920'
    YELLOW = '#ffff00'
    BLUE = '#0069ff'
    ORANGE = '#ff6900'
    RED = '#d00000'


class Algs:
    '''
        Scoped const for named NxN algorithms
    '''
    T_PERM = "R U R' U' R' F R R U' R' U' R U R' F'"
    CUBE_IN_CUBE = "U' L' U' F' R2 B' R F U B2 U B' L U' F U R F'"
    BIG_2X2_CUBE_IN_CUBE = "Bw2 Rw' DW' Rw Dw Rw' Dw' Rw Uw Rw' Dw Rw Dw' Rw' Dw Rw Dw' Rw2"


class NxN:
    '''
        Similar to a namespace
    '''

    # color pallette used by all NxN cubes
    COLORS = [Color.WHITE, Color.GREEN, Color.YELLOW,
              Color.BLUE, Color.ORANGE, Color.RED]
    # a swap table for cycling 'pieces'
    SWAP = {
        "B": {"color0": UP, "color1": LEFT, "color2": DOWN, "color3": RIGHT},
        "B'": {"color0": UP, "color1": RIGHT, "color2": DOWN, "color3": LEFT},
        "L": {"color0": UP, "color1": FRONT, "color2": DOWN, "color3": BACK},
        "L'": {"color0": UP, "color1": BACK, "color2": DOWN, "color3": FRONT},
        "U": {"color0": FRONT, "color1": LEFT, "color2": BACK, "color3": RIGHT},
        "U'": {"color0": FRONT, "color1": RIGHT, "color2": BACK, "color3": LEFT},
    }
    # a pixel offset map
    OFFSET = {
        (800, 600): {LEFT: 45, FRONT: 210, RIGHT: 375, BACK: 540}
    }

    @staticmethod
    def horizontal_XAxis(cube_size: int, layer: int, *, prime: bool = False) -> list[list[int]]:
        '''
            takes in the cube size and which layer is being turned. and an optional prime/counter
            rotation boolean.
            returns a list of 4 indices to be cycled

            Cube layers go L -> M -> R
            prime == False => L', M', R
            prime == True  => L, M, R'
        '''
        res = []
        for t in range(cube_size):
            i = layer + (t * cube_size)
            j = cube_size * (cube_size - 1 - t) + cube_size - layer - 1
            res.append([i, j, i, i] if not prime else [i, i, i, j])
        return res

    @staticmethod
    def horizontal_YAxis(cube_size: int, layer: int) -> list[list[int]]:
        '''
            takes in the cube size and which layer is being turned
            returns a list of 4 indices to be cycled

            Cube layers go U -> E -> D
        '''
        r = cube_size * layer
        return [[i, i, i, i] for i in range(r, r + cube_size)]

    @staticmethod
    def horizontal_ZAxis(cube_size: int, layer: int, *, prime: bool = False) -> list[list[int]]:
        '''
            takes in the cube size and which layer is being turned. and an optional prime/counter
            rotation boolean.
            returns a list of 4 indices to be cycled

            Cube layers go B -> S -> F
            prime == False => B', S', F
            prime == True  => B, S, F'
        '''
        res = []
        for t in range(cube_size):
            i = t + (cube_size * layer)
            j = (cube_size - 1 - layer) + (cube_size * t)
            k = cube_size * cube_size - 1 - t - (layer * cube_size)
            l = (cube_size * (cube_size - 1 - t)) + layer
            res.append([i, j, k, l] if not prime else [i, l, k, j])
        return res

    @staticmethod
    def face_corner(cube_size: int, *, prime: bool = False) -> list[list[int]]:
        '''
            takes in the cube size and an optional prime/counter rotation boolean.
            returns a list of 4 indices to be cycled
        '''
        res = []
        for t in range(cube_size//2):
            i = (t * cube_size) + t
            j = (cube_size - 1) + (t * cube_size) - t
            k = ((cube_size * cube_size) - 1) - (t * cube_size) - t
            l = (cube_size * (cube_size - 1)) - (t * cube_size) + t
            res.append([i, j, k, l] if not prime else [i, l, k, j])
        return res

    @staticmethod
    def face_edge(cube_size: int, *, prime: bool = False) -> list[list[int]]:
        '''
            takes in the cube size and an optional prime/counter rotation boolean.
            returns a list of 4 indices to be cycled
        '''
        res = []
        for t in range((cube_size-1)//2):
            for r in range(cube_size-(2 * (t+1))):
                i = 1 + r + (t * cube_size) + t
                j = ((2+t) * cube_size) - t - 1 + (r * cube_size)
                k = (cube_size * cube_size) - 2 - r - (t * cube_size) - t
                l = ((cube_size - 2 - t) * cube_size) + t - (r * cube_size)
                res.append([i, j, k, l] if not prime else [i, l, k, j])
        return res

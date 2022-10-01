#! /usr/bin/env python3.10

'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: visualCube.py
    Dependencies: Python 3.10 [might work with older versions]
                  tkinter
    Purpose: construct the window (tkinter) and the cube and enter a mainloop.
             The user is able to interact with the window by sending WCA notation
             through the stdin
'''

from lib.graphics import Gui
from lib.visualCubeLib import *
from lib.visualCubes.horizontal7x7 import _7x7
from lib.visualCubes.horizontal3x3 import _3x3
from lib.visualCubes.horizontal4x4 import _4x4

def main():
    gui, cube = Gui((800, 600)), _4x4()
    cube.draw(gui)
    
    # cube.apply_alg(s_list=scramble(cube))
    
    # cube.apply_alg(str_=Algs.T_PERM)
    
    # cube.apply_alg(str_=Algs.CUBE_IN_CUBE)
    # cube.apply_alg(str_=Algs.BIG_2X2_CUBE_IN_CUBE)

    cube.draw(gui)

    while True:
        try:
            x = input()
            cube.move(x)
            cube.draw(gui)
        except(EOFError):
            print("Exited interactive mode")
            break
    gui.mainloop()

if __name__ == '__main__':
    main()

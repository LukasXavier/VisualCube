#! /usr/bin/env python3.10

'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: visualCubeLibValidator.py
    Purpose: a simple test runner
'''

import Test.test_horizontal3x3 as T_H3x3
import Test.test_horizontal4x4 as T_H4x4
from lib.visualCubeLib import *

if __name__ == '__main__':
    T_H3x3.run()
    T_H4x4.run()

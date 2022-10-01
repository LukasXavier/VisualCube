'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: Tester.py
    Purpose: checks for equality between two lists of lists of ints
'''

def attempt(*,info: str, left: list[list[int]], right: list[list[int]]) -> None:
    '''
    asserts that the left equals the right. if they are not equal print out the
    difference and exit with an error code of 1
    '''
    try:
        assert (left == right)
    except (AssertionError):
        print(f"\033[31mTest: {info} [failed]\n\033[mLeft:  {left}\nRight: {right}\033[m")
        exit(1)

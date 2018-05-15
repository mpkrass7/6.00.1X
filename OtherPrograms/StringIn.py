# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:27:22 2017

@author: pl89155
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        return isIn(char, aStr[0:int(len(aStr)/2)])


def isIn_True(char, aStr):
    if char == aStr[(len(aStr))//2]:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 0:
        return False
    else:
        if char > aStr[len(aStr)//2]:
            return isIn_True(char, aStr[len(aStr)//2:]) #Upper half of string
        else:
            return isIn_True(char, aStr[:len(aStr)//2]) #lower half of string
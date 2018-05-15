# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:39:34 2017

@author: pl89155
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    iterative power function
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for i in range(0, exp):
        if exp == 0:
            break
        else:
            result *= base
    return result

iterPower(2, 1)

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    recursive power function
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
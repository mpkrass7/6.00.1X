# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:42:10 2017

@author: pl89155
"""

def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
    return max

def gcdRecur(a,b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
       return gcdRecur(min(a,b), max(a,b) % min(a,b))

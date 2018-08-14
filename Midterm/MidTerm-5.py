# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:41:23 2017

@author: mpkra
"""

testList = [1, 2, 9, 6, 6, 3, 4, 5]
test = []


def square(x):
    return x*x
def isEven(x):
    return x % 2 == 0

def f(i):
    return i + 2
def g(i):
    return i > 5



def applyF_filterG(L,f,g):
    for i in reversed(range(len(L))):
        if not g(f(L[i])):
            del L[i]
    if len(L) == 0:
        return -1
    else:
        return max(L)
    
print(applyF_filterG(testList, f, g))
print(testList)    

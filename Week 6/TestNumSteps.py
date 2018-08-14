# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:24:49 2018

@author: mpkra
"""

def program1(x):
    total = 0
    for i in range(2):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

print(program1(0))
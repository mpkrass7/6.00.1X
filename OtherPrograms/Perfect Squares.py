# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:14:49 2018

@author: pl89155
"""

def countSquares(x):
    perfectSquares = []
    count = 1
    while count**2 <= x:
        perfectSquares.append(count**2)
        count += 1
    return perfectSquares, len(perfectSquares)
print(countSquares(1000000))
        
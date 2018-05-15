# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:34:01 2017

@author: pl89155
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(5, "Tower 1", "Tower 2", "Tower 3")
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:08:56 2017

@author: pl89155
"""

from math import *

def polysum(n, s): 

    def polyArea(n,s):
        return (.25*n*(s**2))/(tan(pi/n))
 
    def polyPerim(n, s):
        return s*n
    return round(polyArea(n, s) + (polyPerim(n,s)**2),4)

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:18:03 2017

@author: mpkra
"""

from math import *


def polysum(n, s):

    '''
    Input a float or an integer
    Takes 2 arguments: Number of sides (n) and side length (s).
    Returns the sum of the area and square of the perimeter
    of a regular polygon rounded to four decimal places.
    '''

    def polyArea(n, s):
        return (.25*n*(s**2))/(tan(pi/n))

    def polyPerim(n, s):
        return s*n

    return round(polyArea(n, s) + (polyPerim(n, s)**2), 4)

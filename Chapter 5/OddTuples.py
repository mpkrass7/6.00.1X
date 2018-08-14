# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:53:51 2017

@author: mpkra
"""


def oddTuples(aTup):
    """
    Input a Tuple
    Returns odd elements in tuple
    i.e. 1st, 3rd, 5th, etc..
    """
    oddTup = ()
    for i in range(0, len(aTup)):
        if i % 2 == 0:
            oddTup += aTup[i:i+1]
        print(oddTup)
    return oddTup


oddTuples(("Josh", "not", "is", "the", "a", "big", "butthole"))

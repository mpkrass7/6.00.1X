# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:47:43 2017

@author: pl89155
"""

def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    if str(x) in str(y):
        return True
    elif str(y) in str(x):
        return True
    else:
        return False



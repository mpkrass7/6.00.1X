# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:51:35 2018

@author: mpkra
"""


def sumDigits(s):
    total = 0
    for i in s:
        try:
            total += int(i)
        except ValueError:
            1
    return total


def findAnEven(L):
    for elem in L:
        try:
            if elem % 2 == 0:
                return elem
        except TypeError:
            1
    raise ValueError('No Even Numbers')


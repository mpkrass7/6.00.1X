# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:26:40 2017

@author: mpkra
"""


def getSublists(L, n):
    sublist = []
    counter = 0
    while counter < len(L) + 1 - n:
        print(sublist)
        sub = []
        for i in range(counter, n + counter):
            sub.append(L[i])
        counter += 1
        sublist.append(sub)
    return sublist


L = [1, 2, 3, 4, 5, 6, 7, 8]


def getSublists2(L, n):
    sublist = []
    counter = 0
    while counter < len(L) + 1 - n:
        print(sublist)
        sublist.append(L[counter:n + counter])
        counter += 1
    return sublist


getSublists2(L, 5)
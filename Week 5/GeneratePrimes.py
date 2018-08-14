# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:47:09 2018

@author: mpkra
"""


def genPrimes():
    primesList = []
    CurrentNum = 1
    while True:
        CurrentNum += 1
        count = 0
        for prime in primesList:
            if CurrentNum % prime == 0:
                count += 1
                break
        if count == 0:
            primesList.append(CurrentNum)
            yield CurrentNum


def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

primeGenerator = genPrimes()
primeGenerator.next()   
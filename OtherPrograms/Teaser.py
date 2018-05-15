# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:08:15 2018

@author: pl89155
"""

import math

def solveTeaser():
    step = 1
    guess = 9
    start = 0
    for i in range(1,10):
        for i in range(1, 10):  
            total = 0
            for i in range(start, guess, step):
                total += i**2
            print(start, i)
            print("Total:", total, "Mom:", round(math.sqrt(total),2), "Step:", step,\
                  "range:", (range(start, guess)))
            if math.sqrt(total) == int(math.sqrt(total)):
                print('max:', guess-step, 'step:', step, 'mom:', math.sqrt(total))
                return math.sqrt(total), step, range(start, guess-step)
            guess += 1
            start += 1
        guess = 9
        start = 0
        step += 1
        guess *= step
                       
print(solveTeaser())


def findDenoms(x):
    for i in range(2, x+1//2):
        if x/i == int(x/i):
            print("Divisible by", i)
            print("Result = ", x/i)

findDenoms(703)


def childrenAge(lastYear, thisYear, maxAge):
    for i in range(maxAge):
        for j in range(maxAge):
            for l in  range(maxAge):
                print(i, j, l)
                if (i * j * l) == thisYear and \
                (i - 1) * (j -1) * (l - 1) == lastYear:
                    return i, j, l
print(childrenAge(224, 360, 20))


def recurTest(x, y):
    while x > 7:
        print(y)
        recurTest(x-1, y)
        break



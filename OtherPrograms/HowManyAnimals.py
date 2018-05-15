# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:08:40 2017

@author: pl89155
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        print("Number of", i, "animals:", count)
how_many(animals)

def biggest(aDict):
    bigEntry = ''
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
        if count >= maxcount:
            maxcount = count
            bigEntry = i
        print("Number of", i, "animals:", count)
    print(maxcount, bigEntry)
    return maxcount

biggest(animals) 

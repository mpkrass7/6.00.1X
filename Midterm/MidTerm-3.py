# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:54:09 2017

@author: mpkra
"""

dic = {1:10, 2:20, 3:30, 4:30}
dic2 = {4:True, 2:True, 0:True}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    newDict = {}
    for i in d:
        if (d[i]) not in newDict:
            newDict[d[i]] = [i]
        else:
            newDict[d[i]].append(i)
            newDict[d[i]] = sorted(newDict[d[i]])
    return newDict
        
dict_invert(dic2)


testDict = {1:[10], 2:[20], 3:[30], 4:[30]}
test2 = {True:[4, 3, 2]}
testDict[4].append(50)
print(testDict)
test2[True] = sorted(test2[True])
print(test2)
sorted(test2[True]
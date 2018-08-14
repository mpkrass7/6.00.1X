# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:24:49 2017

@author: mpkra
"""

testList = [[1,'a', [], [['cat'],2],[[[3]],'dog'],4],5]
test2 = [1, 2, 3, [4, 5, 6, 7], 10]
endList = []

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    for i in aList:
        if type(i) == list:
            endList + flatten(i)
        else:
            endList.append(i)
    return endList
flatten(testList)
flatten([])
#
#test = []
#test.append(5)
#print(test)

#def flatten2(aList):
#    endList = []
#    for l in aList:
#        if type(l) == list:
#            endList += flatten2(l)
#        else:
#            endList.append(l)
#    return endList
#
#flatten2(testList)
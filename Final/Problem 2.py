# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:17:15 2018

@author: mpkra
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
#start by finding the longest increasing run
    def longest_direction(L, direction):
        countLongest, currentCount, longStart = 1, 1, 0
        currentList, longestList = [L[0]], [L[0]]
        for i in range(1, len(L)):
            if direction * L[i - 1] <= direction * L[i]:
                currentCount += 1
                currentList.append(L[i])
            if currentCount > countLongest:
                countLongest = currentCount
                longestList = currentList[:]
                longStart = i + 1 - len(longestList)
            if direction * L[i - 1] > direction * L[i]:
                currentCount = 1
                currentList = [L[i]]
        return(longestList, sum(longestList), longStart)

    if len(longest_direction(L, 1)[0]) == len(longest_direction(L, -1)[0]):
        if longest_direction(L, 1)[2] < longest_direction(L, -1)[2]:
            return longest_direction(L, 1)[1]
        else:
            return longest_direction(L, -1)[1]
    elif len(longest_direction(L, 1)[0]) > len(longest_direction(L, -1)[0]):
        return longest_direction(L, 1)[1]
    else:
        return longest_direction(L, -1)[1]

testList = [1, 2, 3, 2, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9]
testList2 = [1, 2, 4, 2, 1]
print(longest_run(testList2))

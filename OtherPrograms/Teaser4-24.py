# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:21:05 2018

@author: pl89155
"""

def solveTeaser(listLen):
    """listlen - a list of sequential numbers starting at 1
    returns the result of adding the first 2 numbers and appending 
    sum to end of the list"""

    steps = 0
    seq = list(range(1, listLen + 1))
#    print(seq)
    def recurSolve(seq, step):
#        print(seq)
        if len(seq) == 1:
           return(sum(seq), step)
        else:
           stepNum = step + 1
           seqCopy = seq[:]
           endSeq = seqCopy[0] + seqCopy[1]
           newSeq = seqCopy[2:]
           newSeq.append(endSeq)
#           print(newSeq)
           return recurSolve(newSeq, stepNum)
    
    return recurSolve(seq, steps)
    
print(solveTeaser(30))


def solveTeaserAgain(listLen):
    steps = 0
    seq = list(range(1, listLen + 1))
    for i in range(len(seq) - 1):
        firstTwo = sum(seq[:2])
        seq = seq[2:]
        seq.append(firstTwo)
        steps += 1
    return sum(seq), steps
    
print(solveTeaserAgain(30))

def solveTeaseraThirdTime(listLen):
    return ((len(list(range(1,listLen+1))) * len(list(range(1,listLen+2))))//2, listLen - 1) 

print(solveTeaseraThirdTime(30))

def solveTeaseraFourthTime(listLen):
    return(sum(list(range(1,listLen + 1))), listLen-1)

print(solveTeaseraFourthTime(30))


def solveMathRemain():
    x = 0
    while abs((x *.8 *.8) - 36) > .01:
        x += .015
    y = round(x,2)
    x = 0
    while 9/25 * x != 36:
        x += 1
    return "Amount to spend $36: " + str(x) + " Amount to have $36 remaining: "+ str(y)
print(solveMathRemain())
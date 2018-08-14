# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:10:57 2017

@author: mpkra
"""

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber == guess:
        return guess
    while guess != isMyNumber:
        print(guess)
        sign = guess - isMyNumber
        if sign < 0:
            guess *= 2
        elif sign > 0:
            guess -= 1
    print(guess)
    return guess

jumpAndBackpedal(275)

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    while isMyNumber(guess) != 0:
        sign = isMyNumber(guess)
        if sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess
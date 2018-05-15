# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:19:55 2017

@author: pl89155
"""

def isPalindrome(s):
    '''
    Check if a word is a palindrome. 
    Stips all punctuation and spacing
    Accepts words and numbers
    '''
    def toChars(s):
        s= s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return isPal(s[1:-1])
    return isPal(toChars(s))
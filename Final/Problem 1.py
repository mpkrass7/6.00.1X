# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    newStr = ''
    longest = max(len(s1), len(s2))
    for i in range(longest):
        try:
            newStr += s1[i]
#            print(newStr)
        except IndexError:
            newStr += s2[i:]
            break
        try:
            newStr += s2[i]
#            print(newStr)
        except IndexError:
            newStr += s1[i+1:]
            break
#    print(newStr)
    return newStr

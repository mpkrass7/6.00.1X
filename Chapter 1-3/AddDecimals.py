# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:21:36 2017

@author: mpkra
"""

s = '1.23,2.4,3.123'

startcount = 0
endcount = 0
total = 0

for i in s:
    if i != ',':
        endcount += 1
    else:
        total += float(s[startcount:endcount])
        endcount += 1
        startcount = endcount
total += float(s[startcount:endcount])
print(total)

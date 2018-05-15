# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#s = "abcababcde"
#
#string = ''
#count = 0
#keyindex = 0
#for i in range(len(s) - 1):
#    if s[i] <= s[i + 1]:
#        count += 1
#    else:
#        if count > maxcount:
#            maxcount = count
#            keyindex = i - maxcount
#            string = s[keyindex: keyindex + maxcount + 1]
#        count = 0
#if count > maxcount:
#    maxcount = count
#    keyindex = i + 1 - maxcount
#    string = s[keyindex: keyindex + maxcount + 1]
#print("Longest substring in alphabetical order is:", string)

s = "abcababcde"
count, maxcount, keyindex, string, topstring = 0, -1, 0, ''
for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
        string += s[i]
        print(string)
    else:
        string = s[i]
        print(string)
    if count > maxcount:
        maxcount = count
        topstring = string
        print(topstring)
        keyindex = i - maxcount
        string = s[keyindex: keyindex + maxcount + 1]
        count = 0 
print("The longest substring in alphabetical order is: " + topstring)
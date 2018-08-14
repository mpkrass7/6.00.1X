# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:39:09 2017

@author: mpkra
"""

integer = int(input("Enter an integer: "))

pwr = 5
root = 0
matches = 0
while pwr > 0:
    if root**pwr < abs(integer):
        root += 1
    elif root**pwr > abs(integer):
        root = 0
        pwr -= 1
    else:
        if integer < 0 and pwr % 2 != 0:
            root = -root
            print(root, "to the", pwr, "is", integer)
            root = -root
            matches += 1
        elif integer >= 0:
            print(root, "to the", pwr, "is", integer)
            matches += 1
        root += 1
if matches == 0:
    print("No root power combination between 1 and 6 exists ", end='')
    print("to get that integer")



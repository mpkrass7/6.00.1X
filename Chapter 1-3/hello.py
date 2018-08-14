# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:59:09 2017

@author: mpkra
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK


def hello():

    """Print "Hello World" and return None"""
    print("Hello World")


# main program starts here
hello()


def examineOdd(x, y, z):
    message = "the largest odd is"
    # Finds the maximum odd number
    if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
        if x >= y and x >= z:
            print(message, x)
        elif y >= x and y >= z:
            print(message, y)
        else:
            print(message, z)
    elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
        if x >= y:
            print(message, x)
        else:
            print(message, y)
    elif x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
        if y >= z:
            print(message, y)
        else:
            print(message, z)
    elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
        if x > z:
            print(message, x)
        else:
            print(message, z)
    elif x % 2 != 0:
        print(message, x)
    elif y % 2 != 0:
        print(message, y)
    elif z % 2 != 0:
        print(message, z)
    else:
        print("No odds")


examineOdd(7, 3, 5)
examineOdd(2, 5, 9)
examineOdd(2, 50, 22)
examineOdd(-5, -4, 8)

n = input('Enter an int: ')
print(int(n)**int(n))

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:00:28 2017

@author: pl89155
"""

nameHandle = open('kids', 'w')
for i in range(2):
    name = input("Enter your name: ")
    nameHandle.write(name + '\n')
nameHandle.close

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:07:33 2017

@author: mpkra
"""
varA = "roll"
varB = 3
if (type(varA) == str or type(varB) == str):
    print("string involved")
if (type(varA) == int and type(varB) == int):
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")

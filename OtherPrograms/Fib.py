# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:02:52 2017

@author: pl89155
"""

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)  
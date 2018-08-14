# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:51:44 2018

@author: mpkra
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()
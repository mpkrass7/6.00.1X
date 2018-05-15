# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:25:35 2018

@author: pl89155
"""
import random
import pylab

xvals = []
yvals = []
for i in range(1000):
    xvals.append(random.random())
    yvals.append(random.random())
xvals = pylab.array(xvals)
yvals = pylab.array(yvals)
zvals = xvals + yvals
pylab.hist(zvals)
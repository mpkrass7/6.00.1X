# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:00:46 2018

@author: mpkra
"""
import pylab as plt

sampleValues = []
linearGrowth = []
quadraticGrowth = []
cubicGrowth = []
exponentialGrowth = []

for i in range(0, 30):
    sampleValues.append(i)
    linearGrowth.append(i)
    quadraticGrowth.append(i**2)
    cubicGrowth.append(i**3)
    exponentialGrowth.append(1.5**i)

plt.plot(sampleValues, linearGrowth)
plt.plot(sampleValues, quadraticGrowth)
plt.plot(sampleValues, cubicGrowth)
plt.plot(sampleValues, exponentialGrowth)
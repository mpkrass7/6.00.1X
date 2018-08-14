# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:16:56 2017

@author: mpkra
"""

A = int(input("Enter integer 1: "))
B = int(input("Enter integer 2: "))
C = int(input("Enter integer 3: "))
D = int(input("Enter integer 4: "))
E = int(input("Enter integer 5: "))
F = int(input("Enter integer 6: "))
G = int(input("Enter integer 7: "))
H = int(input("Enter integer 8: "))
I = int(input("Enter integer 9: "))
J = int(input("Enter integer 10: "))
 
X = [A, B, C, D, E, F, G, H, I, J]
print(X)
iterations = len(X)
i = 0
maxOdd = 0
while iterations > 0:
    if X[i] % 2 == 0:
        X[i] = 0
    if X[i] > maxOdd:
        maxOdd = X[i]
    iterations -= 1
    i += 1
if maxOdd == 0:
    print("No Odd Numbers")
else:
    print("The largest odd is:", maxOdd)

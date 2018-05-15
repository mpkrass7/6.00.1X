# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:48:23 2018

@author: pl89155
"""

def primeMaker(n):
    count = 0
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        primes.append(3)
        for number in range(5, n + 1):
            print(number)
            for primeCheck in primes:
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
        return primes
    
def prime2Maker(n):
    count = 0
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        primes.append(3)
        for number in range(5, n + 1):
            print(number)
            for primeCheck in range(2, (number + 1) // 2):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
        return primes
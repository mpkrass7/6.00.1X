# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:48:41 2018

@author: mpkra
"""


def listPrimes(n):
    assert(type(n)) == int
    primes, count = [], 0
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        primes.append(3)
        for number in range(5, n + 1):
            count = 0
            for checkPrime in primes:
#                print("Checking", checkPrime, "on", number)
                if number % checkPrime == 0:
#                    print(number, "divides evenly by", checkPrime)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
        return primes

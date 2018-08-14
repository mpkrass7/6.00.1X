# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:45:12 2017

@author: mpkra
"""

# Test Case 1:
balance = 320000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
'''Remaining balance: 31.38'''


def CalculateBalance(b, r, mpr, count):
    minPay = mpr * b
    outstanding = b - minPay
    RemBalance = round(outstanding + (outstanding * (r/12)), 2)
    if count == 1:
        return RemBalance
    else:
        return CalculateBalance(RemBalance, r, mpr, count - 1)


def minMonthly(b, r):
    pay = 0
    endBalance = 1
    while endBalance > 0:
        pay += 10
        outstanding = b
        month = 0
        for i in range(0, 12):
            outstanding -= pay
            RemBalance = round(outstanding + (outstanding * (r/12)), 2)
            month += 1
            outstanding = RemBalance
        endBalance = RemBalance
    print("Lowest Payment:", pay)


minMonthly(balance, annualInterestRate)

balance = 999999
annualInterestRate = 0.18


def MonthlyMin(b, r):
    mi = r/12
    upper = (b * (1 + mi)**12)/12
    lower = b / 12
    epsilon = .01
    pay = round((upper + lower)/2, 2)

    def RemainBalanceCalc(b, r, p):
        month = 0
        print("Monthly payment:", p)
        for i in range(0, 12):
            b -= p
            RemBalance = round(b + (b * r), 3)
            month += 1
            print("Month", month, "remaining balance =", round(RemBalance, 2))
            b = RemBalance
        return RemBalance

    endBalance = RemainBalanceCalc(b, mi, pay)
    while abs(endBalance - epsilon) > .01:
        if endBalance > 0:
            lower = pay
            pay = round((upper + lower)/2, 3)
        else:
            upper = pay
            pay = round((upper + lower)/2, 3)
        endBalance = RemainBalanceCalc(b, mi, pay)
    print("Lowest Payment:", round(pay, 2))


MonthlyMin(balance, annualInterestRate)

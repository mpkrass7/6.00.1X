# -*- coding: utf-8 -*-
"""
Spyder Editor
test = 1

This is a temporary script file.
"""

x = -25
eps = .01
guesses = 0
low = min(0, x)
high = max(1.0, x)
ans = (high + low)/2
while abs(ans**3 - x) > eps:
    print('low =', low, 'high =,', high, 'ans =', ans)
    guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuess =', guesses)
print(ans, 'is close to square root of', x)

"""x = 0.0
for i in range(10):
    x += .1
    print(x)
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')"""

# find x so x**2 - 24 is within episolon of 0 (newton Rophson Square Root)

k = 1234567890
eps = .01
guesses = 0
low = min(0, k)
high = max(1.0, k)
ans = (high + low)/2
while abs(ans**2 - k) > eps:
    print('low =', low, 'high =,', high, 'ans =', ans)
    guesses += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Guess Count =', guesses)
print(ans, 'is close to square root of', x)

epsilon = 0.01
guess = k/2.0
NewtonCount = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2 * guess))
    NewtonCount += 1
print('Guess count:', NewtonCount)
print('Square root of', k, 'is about', guess)

print("Bisection search:", guesses, "Newton Raphson:", NewtonCount)
if NewtonCount < guesses:
    print("Newton Raphson is", guesses - NewtonCount, "guesses ", end='')
    print("more efficient than Bisection Search")
elif guesses < NewtonCount:
    print("Bisection Search is", NewtonCount - guesses, " guesses ", end='')
    print("more efficient than Newton Raphson")
else:
    print("Both methods required", NewtonCount, "guesses")

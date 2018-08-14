# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:52:45 2017

@author: mpkra
"""

# The output will place the subsequent string on the same line
# and will connect the two prints with the character given by end

print("Please think of a number between 0 and 100!")
guess, low, high, direct = 50, 0, 100, "o"
while True:
    print("Is your secret number " + str(guess) + "?")
    print("Enter 'h' to indicate the guess is too high. ", end='')
    print("Enter 'l' to indicate the guess is too low. ", end='')
    direct = input("Enter 'c' to indicate I guessed correctly. ")
    if direct == 'h':
        high = guess
        guess = int((guess + low) / 2)
    elif direct == 'l':
        low = guess
        guess = int((guess + high) / 2)
    elif direct == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(guess))

# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Fri Dec 15 11:13:08 2017)---
runfile('C:/Users/pl89155/.spyder-py3/temp.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Mon Dec 18 16:53:49 2017)---
s = "abcababcde"

string = ''
count = 0
maxcount = -1
keyindex = 0
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            keyindex = i - maxcount
            string = s[keyindex: keyindex + maxcount + 1]
        count = 0

if count > maxcount:
    maxcount = count
    keyindex = i + 1 - maxcount
    string = s[keyindex: keyindex + maxcount + 1]

print("Longest substring in alphabetical order is: " + string)
debugfile('C:/Users/pl89155/.spyder-py3/temp.py', wdir='C:/Users/pl89155/.spyder-py3')
s = "abcababcde"

string = ''
count = 0
maxcount = -1
keyindex = 0
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            keyindex = i - maxcount
            string = s[keyindex: keyindex + maxcount + 1]
        count = 0

if count > maxcount:
    maxcount = count
    keyindex = i + 1 - maxcount
    string = s[keyindex: keyindex + maxcount + 1]

print("Longest substring in alphabetical order is:", string)

## ---(Wed Dec 20 11:46:01 2017)---
def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    
    if x in y:
        return True
    else:
        return False
isIn("test", "email")
isIn("test", "testemail")
isIn("test", "etestemail")
isIn("testemail", "test")
def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    x, y = str(x), str(y)
    if x in y:
        return True
    elif y in x:
        return True
    else:
        return False
isIn(champ, champ you betcha!)
isIn(champ, champyoubetcha!)
def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    if str(x) in str(y):
        return True
    elif str(y) in str(x):
        return True
    else:
        return False
isIn(Else, Elseif)
isIn(chal, jaf)
isIn(123, 1234
)
"""

def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    if str(x) in str(y):
        return True
    elif y in x:
        return True
    else:
        return False
def isIn(x, y):
    """
    Input two Strings
    Returns true if one string is In another string
    """
    if str(x) in str(y):
        return True
    elif y in x:
        return True
    else:
        return False
isIn(1234, 123)
5*5
5+5
+5
5+5+5+5+5
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in exp:
        result *= base
        return base
iterPower(5, 2)
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(0, exp):
        result *= base
        return base
iterPower(5, 2)
range(0,5)
for i in range(0,5):
    print(i)
    
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(1, exp + 1):
        result *= base
        return base
    
iterPower(5,2)
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(0, exp + 1):
        result *= base
        return base
iterPower(5, 2)
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(1, exp):
        result *= base
        return result
    
iterPower(5,2)
iterPower(4,4)
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(1, exp):
        result *= base
    return result
iterPower(2, 5)
iterPower(5, 2)
debugfile('C:/Users/pl89155/.spyder-py3/Iteration and Recursion Powers.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Iteration and Recursion Powers.py', wdir='C:/Users/pl89155/.spyder-py3')
iterPower(5.213, 4)
runfile('C:/Users/pl89155/.spyder-py3/Iteration and Recursion Powers.py', wdir='C:/Users/pl89155/.spyder-py3')
iterPower(2, 4)
iterPower(2, 0)
iterPower(2, 1)
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    recursive power function
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
recurPower(4, 3)
recurPower(4, 1)
recurPower(4, 0)
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    recursive power function
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
recurPower(5,2)
recurPower(5,0)
recurPower(5,4)
recurPower(63,4)
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


Towers(5, "Tower 1", "Tower 2", "Tower 3")
debugfile('C:/Users/pl89155/.spyder-py3/Hanoi.py', wdir='C:/Users/pl89155/.spyder-py3')
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(0, min(a, b)):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(12, 8)
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(12, 8)
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(12, 6)
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(12, 1)
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(1234, 5125132)
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max = i
            print("New max is:", i)
    return max


gcdIter(1234, 2468)
def gcdRecur(a,b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
       return gcdRecur(min(a,b), max(a,b) % min(a,b))
gcdRecur(12, 8)
gcdRecur(12, 6)
gcdRecur(12, 10)
gcdRecur(10, 10)
gcdRecur(10, 17)
gcdRecur(10, 34)

## ---(Fri Dec 22 11:10:30 2017)---
def isPalindrome(s):
    def toChars(s):
        s= s.lower()
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return isPal(s[1:-1])
    return isPal(toChars(s))
def isPalindrome(s):
    def toChars(s):
        s= s.lower()
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return isPal(s[1:-1])
    return isPal(toChars(s))
isPalindrome('racecar')
def isPalindrome(s):
    def toChars(s):
        s= s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return isPal(s[1:-1])
    return isPal(toChars(s))
isPalindrome('racecar')
isPalindrome('rAcEcar')
isPalindrome('speedy')
isPalindrome('speedes')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) % 2 != 0:
        if char == aStr[len(aStr/2)]:
            return True
isIn('a', 'a')
string = 'abc'
string[1]
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) % 2 != 0:
        if char == aStr[ceiling(len(aStr/2))]:
            return True
isIn('a', 'a')
def ceiling(i):
    if i % 2 == 0:
        return i
    else:
        return int(i) + 1
ceiling(2.5)
ceiling(.5)
ceiling(.1)
ceiling(0)
ceiling(152423.164315)
string[ceiling(len(string/2))]
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) % 2 != 0:
        if char == aStr[ceiling(len(aStr)/2)]:
            return True
        else:
            return False
isIn('a', 'a')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) % 2 != 0:
        if char == aStr[int(len(aStr)/2)]:
            return True
        else:
            return False
isIn('a', 'a')
isIn('a', 'b')
isIn('a', 'c')
isIn('c', 'abcde')
isIn('c', 'abbce')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    else:
        print(aStr[0:aStr[int(len(aStr)/2)] + aStr[int(len(aStr)/2)]:len(aStr)])
        return isIn(char, aStr[0:aStr[int(len(aStr)/2)] + aStr[int(len(aStr)/2)]:len(aStr)])
isIn('a', 'a')
isIn('a', 'bab')
isIn('c', 'abc')
isIn('c', 'abccd')
isIn('c', 'abccde')
isIn('c', 'abccdee')
isIn('c', 'abccdeee')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print(aStr[int(len(aStr)/2):len(aStr)])
        return isIn(aStr[int(len(aStr)/2) + 1:len(aStr)-1])

isIn('e', 'abcde')
debugfile('C:/Users/pl89155/.spyder-py3/StringIn.py', wdir='C:/Users/pl89155/.spyder-py3')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print(aStr[int(len(aStr)/2):len(aStr)])
        return isIn(aStr[int(len(aStr)/2) + 1:len(aStr)-1])
    else:
        print(aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print(aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2) + 1:len(aStr)-1])
    else:
        print(aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print(aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2) + 1:len(aStr)-1])
    else:
        print(aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2) + 1:len(aStr)-1])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
debugfile('C:/Users/pl89155/.spyder-py3/StringIn.py', wdir='C:/Users/pl89155/.spyder-py3')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2) + 1:len(aStr)-1])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)-1])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)-1])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)-1])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('c', 'abcde')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('c', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('c', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:aStr[int(len(aStr)/2)]])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2)+1:len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2)+1:len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)-1])
        return isIn(char, aStr[0:int(len(aStr)/2)-1])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    print("char =", char)
    print("string =", aStr)
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)-1])
        return isIn(char, aStr[0:int(len(aStr)/2)-1])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)-1])
        return isIn(char, aStr[0:int(len(aStr)/2)-1])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('e', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('c', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('d', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('d', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('b', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('f', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('a', 'abcdef')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('a', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def ceiling(i):
        if i % 2 == 0:
            return i
        else:
            return int(i) + 1
    # Your code here
    if len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        print("string =", aStr[int(len(aStr)/2):len(aStr)])
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        print("string =", aStr[0:int(len(aStr)/2)])
        return isIn(char, aStr[0:int(len(aStr)/2)])

isIn('f', 'abcdefg')
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 1 and char != aStr:
        return False
    elif char == aStr[int(len(aStr)/2)] or char == aStr:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        return isIn(char, aStr[int(len(aStr)/2):len(aStr)])
    else:
        return isIn(char, aStr[0:int(len(aStr)/2)])
5//2
1//2
def isIn_True(char, aStr):
    if char == aStr[(len(aStr))//2]:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 0:
        return False
    else:
        if char > aStr[len(aStr)//2]:
            return isIn_True(char, aStr[len(aStr)//2:]) #Upper half of string
        else:
            return isIn_True(char, aStr[:len(aStr)//2]) #lower half of string
isIn_True('c', 'abcdef')
isIn_True('c', 'abcdefg')
isIn_True('f', 'abcdefg')
isIn_True('a', 'abcdefg')
isIn_True('a', 'abcdefghig')
from math import *

print(tan(3))
pi
from math import *

def polysum(n, s): 
    
    def polyArea(n,s):
        return (.25*n*(s**2))/(tan(pi/n))
    
    def polyPerim(n, s):
        return s*n
    return polyArea(n, s) + polyPerim(n,s)
polysum(5,2)
from math import *

def polysum(n, s): 
    
    def polyArea(n,s):
        return (.25*n*(s**2))/(tan(pi/n))
    
    def polyPerim(n, s):
        return s*n
    return round(polyArea(n, s) + (polyPerim(n,s)**2),4)
polysum(5,2)
def polyPerim(n, s):

## ---(Thu Dec 28 10:02:38 2017)---
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
fib(24)
fib(120)
fib(50)
fib(35)
fib(25)
fib(30)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(30)
fib(25)
nameHandle = open('kids', 'w')
for i in range(2):
    name = input("Enter your name: ")
    nameHandle.write(name + '\n')

nameHandle.close
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)

nameHandle.close
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
    
nameHandle.close
nameHandle = open('kids', 'w')
for i in range(2):
    name = input("Enter your name: ")
    nameHandle.write(name + '\n')

nameHandle.close

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)

nameHandle.close
-9**2
-9*-9
max(3)
max(3,4)
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals
animals['d']
animals['c']
animals['a']
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    for i in aDict:
        print(i)

how_many(animals)
runfile('C:/Users/pl89155/.spyder-py3/HowManyAnimals.py', wdir='C:/Users/pl89155/.spyder-py3')
def how_many(aDict):
    for i in aDict:
        for item in aDict[i]:
        print(item)

how_many(animals)
def how_many(aDict):
    for i in aDict:
        for item in aDict[i]:
            print(item)

how_many(animals)
def how_many(aDict):
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        print("Number of", i, "animals:", count)

how_many(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)

how_many(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)
        print(maxcount)

how_many(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)
    print(maxcount)

how_many(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)
    return maxcount

biggest(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)

biggest(animals)
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)
    for num in aDict:
        if num.values() == maxcount:
            return num.key

biggest(animals)
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def biggest(aDict):
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        if count >= maxcount:
            maxcount = count
        print("Number of", i, "animals:", count)
    for num in aDict:
        if num.values() == maxcount:
            return num.key

biggest(animals)
animals.values()
animals.values('a')
animals[a]
animals['a']
def biggest(aDict):
    bigEntry = ''
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
        if count >= maxcount:
            maxcount = count
            bigEntry = i
        print("Number of", i, "animals:", count)
    print(maxcount, bigEntry)
    return maxcount


biggest(animals)

## ---(Wed Jan  3 15:53:12 2018)---
count, maxcount, keyindex, topstring = 0, -1, 0, ''
for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            keyindex = i - maxcount
            string = s[keyindex: keyindex + maxcount + 1]
        count = 0 

print("The longest substring in alphabetical order is: " + topstring)
s = "abcababcde"
count, maxcount, keyindex, topstring = 0, -1, 0, ''
for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            keyindex = i - maxcount
            string = s[keyindex: keyindex + maxcount + 1]
        count = 0 

print("The longest substring in alphabetical order is: " + topstring)
s = "abcababcde"

string = ''
count = 0
maxcount = -1
keyindex = 0
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            keyindex = i - maxcount
            string = s[keyindex: keyindex + maxcount + 1]
        count = 0

if count > maxcount:
    maxcount = count
    keyindex = i + 1 - maxcount
    string = s[keyindex: keyindex + maxcount + 1]

print("Longest substring in alphabetical order is:", string)
s = 'abcabcdeab'
string = ''
topstring = ''
count = 0
maxcount = -1
keyindex = 0

for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
        string += s[i]
        print(string)
    else:
        string = s[i]
        print(string)
    if count > maxcount:
        maxcount = count
        topstring = string
        count = 0


print("Longest substring in alphabetical order is:", string)
s = 'abcabcdeab'
string = ''
topstring = ''
count = 0
maxcount = -1
keyindex = 0

for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
        string += s[i]
        print(string)
    else:
        count += 1
        string = s[i]
        print(string)
    if count > maxcount:
        maxcount = count
        topstring = string
        count = 0


print("Longest substring in alphabetical order is:", string)
debugfile('C:/Users/pl89155/.spyder-py3/longestConsecutiveString.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Fri Jan  5 13:10:48 2018)---
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
            print(item)
        print("Number of", i, "animals:", count)

how_many(animals)

def biggest(aDict):
    bigEntry = ''
    maxcount = 0
    for i in aDict:
        count = 0
        for item in aDict[i]:
            count += 1
        if count >= maxcount:
            maxcount = count
            bigEntry = i
        print("Number of", i, "animals:", count)
    print(maxcount, bigEntry)
    return maxcount


biggest(animals) 

animals.values('a')
animals.values('a')
biggest(animals)
animals.values('a')
animals.values()
s = "abcababcde"
count, maxcount, keyindex, string, topstring = 0, -1, 0, ''
for i in range(len(s)):
    if s[i-1] <= s[i]:
        count += 1
        string += s[i]
        print(string)
    else:
        string = s[i]
        print(string)
    if count > maxcount:
        maxcount = count
        topstring = string
        print(topstring)
        keyindex = i - maxcount
        string = s[keyindex: keyindex + maxcount + 1]
        count = 0 

print("The longest substring in alphabetical order is: " + topstring)
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers


normalize([0,0,0])
runfile('C:/Users/pl89155/.spyder-py3/Assert.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/6001x/ps4a.py', wdir='C:/Users/pl89155/.spyder-py3/6001x')
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
        print(score)
getWordScore("hand", 5)
runfile('C:/Users/pl89155/.spyder-py3/6001x/ps4a.py', wdir='C:/Users/pl89155/.spyder-py3/6001x')
getWordScore("hand", 5)
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    score *= len(word)
    if len(word) == n:
        score += 50
    print(score)
getWordScore("ratchet", 7
)
getWordScore("", 7
)
def displayHand(hand):
    """
    Displays the letters currently in the hand.
    
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()
displayHand("hand")
displayHand(5)
displayHand({'a':1, 'x':2, 'l':3, 'e':1})

## ---(Fri Jan 12 16:47:08 2018)---
print(range(0,10))
for i in range(0,10):
    print(i)
    
for i in range(1,10):
    print(i)
    
def primeMaker(n):
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        for number in range(2, n + 1):
            print(number)
            for primeCheck in range(2, int((number + 1)/2)):
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    break
            primes.append(number)
            print(primes)
        return primes
primeMaker(5)
primeMaker(23)
primeMaker(8)
def primeMaker(n):
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        for number in range(3, n + 1):
            print(number)
            for primeCheck in range(3, (number + 1)):
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    break
            primes.append(number)
            print(primes)
        return primes
primeMaker(8)
def primeMaker(n):
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        for number in range(3, n + 1):
            print(number)
            for primeCheck in range(3, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
primeMaker(8)
def primeMaker(n):
    count
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        for number in range(3, n + 1):
            print(number)
            for primeCheck in range(3, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
def primeMaker(n):
    count = 0
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2)
        for number in range(3, n + 1):
            print(number)
            for primeCheck in range(3, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
primeMaker(8)
def primeMaker(n):
    count = 0
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes.append(2, 3)
        for number in range(4, n + 1):
            print(number)
            for primeCheck in range(2, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
primeMaker(8)
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
        for number in range(4, n + 1):
            print(number)
            for primeCheck in range(2, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
primeMaker(8)
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
        for number in range(4, n + 1):
            print(number)
            for primeCheck in range(2, number):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
                print(primes)
        return primes
primeMaker(8)
primeMaker(9)
primeMaker(11)
primeMaker(213)
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
        for number in range(4, n + 1):
            print(number)
            for primeCheck in range(2, number + 1 // 2):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
        return primes
primeMaker(213)
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
        for number in range(4, n + 1):
            print(number)
            for primeCheck in range(2, (number + 1 // 2)):
                count = 0
                print("Checking", primeCheck, "on", number)
                if number % primeCheck == 0:
                    print(number, "divides by", primeCheck)
                    count += 1
                    break
            if count == 0:
                primes.append(number)
        return primes
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
        for number in range(4, n + 1):
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
primeMaker(213)
primeMaker(3)
primeMaker(4)
primeMaker(5)
primeMaker(6)
primeMaker(7)
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
primeMaker(7)
primeMaker(4)
primeMaker(5)
primeMaker(6)
primeMaker(7)
primeMaker(78)
def primeMaker(n):
    count = 0
    primes = []
    if n < 2:
        return primes
    elif n == 2:
        return [2]
    else:
        primes += 2
        primes += 3
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
                primes += number
        return primes
primeMaker(78)
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
primeMaker(78)
primeMaker(200)
primeMaker(500)
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
primeMaker(2)
primeMaker(3)
primeMaker(4)
primeMaker(5)
primeMaker(6)
primeMaker(7)
primeMaker(8)
primeMaker(9)
primeMaker(150)
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
prime2Maker(8)
prime2Maker(23)
prime2Maker(250)
primeMaker(250)
prime2Maker(10000)
prime2Maker(250)
primeMaker(250)
primeMaker(15)
primeMaker(32)
primeMaker(56)
primeMaker(123)

## ---(Fri Jan 19 16:08:02 2018)---
runfile('C:/Users/pl89155/.spyder-py3/ps6/ps6.py', wdir='C:/Users/pl89155/.spyder-py3/ps6')
get_story_string()
message = Message('I am the lord of hints')
message.valid_words
message.get_message_text()
def shift_dict(letters, shift):
    print(string.ascii_lowercase)
    
shift_dict('abc', 5)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    print(upperdict, lowerdict)
shift_dict('ab', 5)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        cypherDict[letter] = lowerdict[count + shift]
        count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 23 + shift]
        cypherDict[letter] = lowerdict[count + shift]
        count += 1
    print(cypherDict, upperdict, lowerdict)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 23 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 25 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def shift_dict(letters, shift):
    upperdict = string.ascii_lowercase
    lowerdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def shift_dict(letters, shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            count += 1
    count = 0
    for letter in upperdict:
        if count > 22:
            cypherDict[letter] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = upperdict[count + shift]
            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
A.lower()
"A".lower()
def shift_dict(letters, shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[letter.uppper()] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[letter.uppper()] = upperdict[count + shift]
            count += 1

#    count = 0
#    for letter in upperdict:
#        if count > 22:
#            cypherDict[letter] = upperdict[count - 26 + shift]
#            count += 1
#        else:
#            cypherDict[letter] = upperdict[count + shift]
#            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
test = string.ascii_lowercase
testList = []
for i in test:
    testList.append(i.upper())
    
test
testList
def shift_dict(letters, shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            UpCase = letter.upper()
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            UpCase = letter.upper()
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1

#    count = 0
#    for letter in upperdict:
#        if count > 22:
#            cypherDict[letter] = upperdict[count - 26 + shift]
#            count += 1
#        else:
#            cypherDict[letter] = upperdict[count + shift]
#            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def shift_dict(letters, shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1

#    count = 0
#    for letter in upperdict:
#        if count > 22:
#            cypherDict[letter] = upperdict[count - 26 + shift]
#            count += 1
#        else:
#            cypherDict[letter] = upperdict[count + shift]
#            count += 1
    print(cypherDict, upperdict, lowerdict)
shift_dict('rar', 3)
def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = []
    for i in phrase:
        if i in encryptor:
            newPhrase[0] += encryptor[i]
        else:
            newPhrase[0] += i
    print(newPhrase)
apply_shift('abc', 3)
runfile('C:/Users/pl89155/.spyder-py3/ps6/ps6.py', wdir='C:/Users/pl89155/.spyder-py3/ps6')
apply_shift('abc', 3)
def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = []
    for i in phrase:
        if i in encryptor:
            newPhrase.append(encryptor[i])
        else:
            newPhrase.append(i)
    print(newPhrase)
apply_shift('abc', 3)
apply_shift('abc!', 3)
test = 'abc'
test += 'def'
test
def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    print(newPhrase)
apply_shift('abc!', 3)
runfile('C:/Users/pl89155/.spyder-py3/ps6/ps6.py', wdir='C:/Users/pl89155/.spyder-py3/ps6')
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count > 22:
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift('Badel is actually named Al!", 7)
apply_shift("Badel is actually named Al!", 7)
runfile('C:/Users/pl89155/.spyder-py3/ps6/ps6.py', wdir='C:/Users/pl89155/.spyder-py3/ps6')
apply_shift("Badel is actually named Al!", 7)
apply_shift("Badel is actually named Al!", 3)
apply_shift("Badel is actually named Al!", 5)
apply_shift("Badel is actually named Al!", 4)
apply_shift("Badel is actually named Al!", 2)
apply_shift("Badel is actually named Al!", 1)
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count > (25 - shift):
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift("Badel is actually named Al!", 1)
apply_shift("Badel is actually named Al!", 3)
apply_shift("Badel is actually named Al!", 4)
apply_shift("Badel is actually named Al!", 20)
apply_shift("Badel is actually named Al!", 27)
apply_shift("Badel is actually named Al!", 26)
apply_shift("Badel is actually named Al!", 25)
apply_shift("Badel is actually named Al!", 0)
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count > (25 - (shift % 26)):
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift("Badel is actually named Al!", 0)
apply_shift("Badel is actually named Al!", 7)
apply_shift("Badel is actually named Al!", 3)
apply_shift("Badel is actually named Al!", 26)
apply_shift("Badel is actually named Al!", 27)
26 % 7
26 %% 2
26 % 2
26 % 26
26 % 25
26 % 27
25 % 26
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count % 26 > (25 - (shift % 26)):
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift("Badel is actually named Al!", 27)
apply_shift("Badel is actually named Al!", 5)
apply_shift("Badel is actually named Al!", 3)
apply_shift("Badel is actually named Al!", 25)
apply_shift("Badel is actually named Al!", 26)
apply_shift("Badel is actually named Al!", 27)
apply_shift("Badel is actually named Al!", 28)
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count % 26 > (25 - (shift % 26)):
            count = count % 26
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift("Badel is actually named Al!", 28)
apply_shift("Badel is actually named Al!", 26)
apply_shift("Badel is actually named Al!", 2)
apply_shift("Badel is actually named Al!", 25)
apply_shift("Badel is actually named Al!", 26)
def shift_dict(shift):
    lowerdict = string.ascii_lowercase
    upperdict = string.ascii_uppercase
    cypherDict = {}
    count = 0
    for letter in lowerdict:
        UpCase = letter.upper()
        if count > (25 - (shift % 26)):
            cypherDict[letter] = lowerdict[count - 26 + shift]
            cypherDict[UpCase] = upperdict[count - 26 + shift]
            count += 1
        else:
            cypherDict[letter] = lowerdict[count + shift]
            cypherDict[UpCase] = upperdict[count + shift]
            count += 1
    return cypherDict


def apply_shift(phrase, shift):
    encryptor = shift_dict(shift)
    newPhrase = ''
    for i in phrase:
        if i in encryptor:
            newPhrase += encryptor[i]
        else:
            newPhrase += i
    return newPhrase
apply_shift("Badel is actually named Al!", 26)
apply_shift("Badel is actually named Al!", 25)
apply_shift("Badel is actually named Al!", 0)
apply_shift("Badel is actually named Al!", 4)
apply_shift("Badel is actually named Al!", 3)
apply_shift("Badel is actually named Al!", 21)

## ---(Thu Feb  1 17:59:18 2018)---
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
for i in newList:
    i = float(i)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
print(newList)
for i in newList:
    i = float(i)
print(newList)
for i in range(len(newList)):
    newList[i] = float(newList[i])
BucketSize = sum(newList)/4
print(BucketSize)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList, 4)
makeBuckets(tempList, 5)
makeBuckets(tempList, 6)
makeBuckets(tempList, 123)
makeBuckets(tempList, 1000)
makeBuckets(tempList, 1)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
makeBuckets(tempList,8)
makeBuckets(tempList,15)
makeBuckets(tempList,3)
makeBuckets(tempList,1)
makeBuckets(tempList,2)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,2)
makeBuckets(tempList,3)
makeBuckets(tempList,4)
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,5)
makeBuckets(tempList,4)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,4)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,4)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,4)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,4)
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
makeBuckets(tempList,10)
makeBuckets(tempList,3)

## ---(Thu Feb 15 11:52:00 2018)---
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
testDict = {}
testDict["a"] = 2
print(testDict)
testDict["a"] = 3
print(testDict)
testDict["a"].append(2)
testDict["a"].append('2')
testDict["a"].append("2")
testDict["a"] = "test"
print(testDict)
testDict["a"].append("b")
testDict["a"] + "b"
testDict["a"] += "b"
print(testDict)
testDict["a"] += ["b"]
testDict = {}
testDict["a"] += ["b"]
testDict["a"] = ["b"]
print(testDict)
testDict["a"].append(["c"])
print(testDict)
testDict["a"].append("c")
print(testDict)
testDict = {}
testDict["a"] = ["b"]
print(testDict)
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
testTup = ('hi', 'there')
testTup[1]
testTup[0]
debugfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
test = []
test.append('hi','there')
test.append(('hi','there'))
print(test)
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Thu Feb 15 14:57:23 2018)---
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Tue Feb 20 09:30:32 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Wed Feb 21 15:23:47 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Fri Feb 23 12:11:10 2018)---
runfile('C:/Users/pl89155/.spyder-py3/TestProductCombos.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/TestBadelStuff.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Fri Feb 23 15:42:19 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Frequent Combinations.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Mon Feb 26 10:06:38 2018)---
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps2/ps2.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps2')

## ---(Fri Mar  9 09:07:52 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Fri Mar  9 16:40:30 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Thu Mar 15 08:26:29 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Thu Mar 15 18:26:54 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Fri Mar 16 16:50:23 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Brute Force.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/Perfect Squares.py', wdir='C:/Users/pl89155/.spyder-py3')
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
test = {'a': 3, 'b': 5}
'a' in test
3 in test
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
test['c'] = False
test['c']
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce()
virus.reproduce(0, [])
print(virus.reproduce(0, [])

)
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce(0, [])
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce(0, [])
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce(0, [])
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce(0, [])
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
virus.reproduce(0, [])
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
test = {'a': True, 'b': False}
test.keys()
list(test.keyes())
list(test.keys())
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')
test = 0
for i in range(150):
    test += 1
    
test
for i in range(150, 300):
    test += 1
    
test
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')

## ---(Mon Mar 26 08:34:08 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Mon Mar 26 17:23:54 2018)---
print(i for i in range(10) if i % 2 == 0)
i for i in range(10) if i % 2 == 0
print(list(i for i in range(10) if i % 2 == 0))
print(i) for i in range(10) if i % 2 == 0
(print(i) for i in range(10) if i % 2 == 0)
(print(list(i)) for i in range(10) if i % 2 == 0)
print(list(i for i in range(10) if i % 2 == 0))
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')
def recurTest(x, y):
    while x > 7:
        print(y)
        recurTest(x-1, y)
        
recurTest(10, 6)
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')
def recurTest(x, y):
    while x > 7:
        print(y)
        recurTest(x-1, y)
        break
    
recurTest(10, 7)

## ---(Wed Apr  4 10:25:31 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser.py', wdir='C:/Users/pl89155/.spyder-py3')
def childrenAge(lastYear, thisYear, maxAge):
    for i in range(maxAge):
        for j in range(maxAge):
            for l in  range(maxAge):
                if (i * j * l) == thisYear and \
                (i - 1) * (j -1) * (l - 1) == lastYear:
                    return i, j, l

print(childrenAge(224, 360, 20))
def childrenAge(lastYear, thisYear, maxAge):
    for i in range(maxAge):
        for j in range(maxAge):
            for l in  range(maxAge):
                print(i, j, l)
                if (i * j * l) == thisYear and \
                (i - 1) * (j -1) * (l - 1) == lastYear:
                    return i, j, l

print(childrenAge(224, 360, 20))
runfile('C:/Users/pl89155/.spyder-py3/6.00.2x ps3/ps3b.py', wdir='C:/Users/pl89155/.spyder-py3/6.00.2x ps3')

## ---(Wed Apr  4 15:25:27 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Test distributions.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Tue Apr 24 08:17:35 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
seq
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
seq
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
solveTeaser(30)
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
solveTeaser(30)
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
solveTeaser(30)
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
test = [1, 2, 3, 4]
test[0:1]
test[:1]
test[:2]
test[2:
]
test[0]+test[1]
test[2:].append(test[0]+test[1])
print(test[2:].append(test[0]+test[1]))
test[2:]
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Tue Apr 24 15:30:30 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')

## ---(Tue May 15 08:09:12 2018)---
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
55*.8
*.8
44*.8
55*.8*.8
56*.8*.8
57*.8*.8
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
56.24*.8*.8
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
99*9/25
100*9/25
runfile('C:/Users/pl89155/.spyder-py3/Teaser4-24.py', wdir='C:/Users/pl89155/.spyder-py3')
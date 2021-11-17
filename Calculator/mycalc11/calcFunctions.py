import math

def factorial(numStr):
    try:
        n = int(eval(numStr))
        r = math.factorial(n)
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        r = int(numStr, 2)
    except:
        r = 'Error!'
    return r

romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
]

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def romanToDec(numStr):
    try:
        result = 0
        i = 0
        for value, letters in romans:
            while (numStr[i:i + len(letters)] == letters):
                result += value
                i += len(letters)
                if i >= len(numStr):
                    return result
        return result
    except:
        return 'Error!'
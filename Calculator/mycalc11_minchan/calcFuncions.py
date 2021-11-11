from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
        if n >= 4000:
            return 'Error!'

        numberBreaks = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90:'XC',
            50:'L', 40:'XL', 10:'X', 9:'IX', 5: 'V', 4:'IV', 1:'I'
        }
        r =''
        for value in numberBreaks:
            while n>=value:
                r += letters[value]
                n -= value
    except:
        r = 'Error!'

    return r

def RomanTodec(numStr):
    try:
        n = str(numStr)
        r = 0
        letters = {
            'M' : 1000, 'CM' : 900 , 'D' : 500 , 'CD' : 400, 'C' : 100, 'XC' : 90,
            'L' : 50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1
        }

        index = 0
        while index != len(n):
            for value in letters.keys():
                if len(value) == 1: # 길이가 1일때
                    if n[index] == value:
                        r += letters[value]
                        index += 1
                        break

                elif len(value) == 2: # 길이가 2일때
                    if n[index] == value[0] and ((index+1)!=len(n)):
                        if n[index + 1] == value[1]:
                            r += letters[value]
                            index += 2
                            break
    except:
        r = 'Error!'

    return r

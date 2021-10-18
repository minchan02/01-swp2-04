import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def iterfibo(n):
    if n <= 1:
        return n

    f1 = 0
    s2 = 1

    for i in range(1, n):
        f1, s2 = s2, f1 + s2

    return s2


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %( nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

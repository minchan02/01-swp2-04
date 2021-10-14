import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n): # 변수를 2개만 사용해서 코드를 작성할 수도 있을 것 같습니다.
    if n <= 1:
        return n
    num1 = 0
    num2 = 1
    ans = 0
    for i in range(n - 1):
        ans = num1 + num2
        num1 = num2
        num2 = ans
    return ans

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

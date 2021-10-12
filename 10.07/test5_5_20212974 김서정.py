import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

#수정 전 코드
'''fibon = {0:0, 1:1}
def iterfibo(n):
    if n in fibon: #n == 1일때 0을 출력합니다.
        return fibon[n]
    fibon[n] = iterfibo(n-2) + iterfibo(n-1) #내부에서 자기 자신을 호출하고 있는 recursive형태인 것으로 보입니다. 확인 부탁드립니다.
    return fibon[n]'''

#수정 후 코드
def iterfibo(n):
    fibo1 = 0
    fibo2 = 1 
    fibon = 0
    if n <= 1:
        return 0
    for i in range(n - 1):
        fibon = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibon
    return fibon


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))


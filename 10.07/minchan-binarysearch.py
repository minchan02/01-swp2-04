import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target): # 재귀함수 L:리스트 l:탐색범위 왼쪽 끝 u : 오른쪽 끝 target: 탐색 값
    # 입력값에 되게 민감함 => 오류인건가...?
    if l > u: # 왼쪽 끝이 오른쪽 끝보다 더 커졌을 때
        return -1

    if L[(l+u)//2] == target:
        return None

    if L[(l+u)//2] > target:
        u = (l+u) // 2 - 1

    elif L[(l+u)//2] < target:
        l = (l+u) // 2 + 1

    return recbinsearch(L, l, u, target)

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

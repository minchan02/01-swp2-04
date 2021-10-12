import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        '''수정 전 코드
        if (target == nbrs[i]):''' # 괄호를 제거하는 것이 좋은 것 같네요. pycharm에서 제거하라고 이야기 합니다.
        # 수정 후 코드
        if target == nbrs[i]:
            return i
    return -1


def recbinsearch(L, l, u, target):
    while l < u:
        middle = int((l + u) // 2)
        if L[middle] == target:
            return middle
        elif L[middle] < target:
            l = middle + 1
            recbinsearch(L, l, u, target)
        else:
            u = middle - 1
            recbinsearch(L, l, u, target)
    return -1


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

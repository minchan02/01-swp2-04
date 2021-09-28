def solution(num):
    answer = 0
    n = str(num)
    for i in n:
        answer += int(i)
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54

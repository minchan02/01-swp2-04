def solution(lst):
    answer = []
    dic = {}
    for i in lst:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    if max(dic.values()) == 1: # 예외처리(최빈값 1일 경우)
        return answer

    for key in dic.keys():
        if dic[key] == max(dic.values()):
            answer.append(key)
    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]

def solution(n):
    answer = []
    listn = list(str(n))
    for i in range(len(listn)-1,-1,-1):
        answer.append(int(listn[i]))
    return answer
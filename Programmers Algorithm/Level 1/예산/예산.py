def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget = budget - i
        if budget >= 0:
            answer+=1
        else:
            break
    return answer
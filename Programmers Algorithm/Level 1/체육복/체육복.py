def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost1 = set(lost) - set(reserve)
    reserve1 = set(reserve) - set(lost)
    for i in reserve1:    
        if i-1 in lost1:
            lost1.remove(i-1)
        elif i+1 in lost1:
            lost1.remove(i+1)
    answer = n - len(lost1)
    return answer
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        for j in range(1, i):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 1:
            answer += i
        else:
            answer -= i
    return answer
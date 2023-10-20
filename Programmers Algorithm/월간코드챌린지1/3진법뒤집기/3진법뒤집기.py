def solution(n):
    answer = 0
    threenum = ''
    while(n != 0):
        threenum += str(n % 3)
        n = n // 3
    idx = 0
    for i in range(len(threenum)-1, -1, -1):
        answer += (3 ** i) * int(threenum[idx])
        idx += 1
        
    return answer
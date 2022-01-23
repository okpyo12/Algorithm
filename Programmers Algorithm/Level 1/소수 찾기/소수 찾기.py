def solution(n):
    answer = 0
    arr = [False, False] + [True] * (n-1)

    for i in range(2, int(n**0.5)+1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    for i in arr:
        if i == True:
            answer += 1
    return answer
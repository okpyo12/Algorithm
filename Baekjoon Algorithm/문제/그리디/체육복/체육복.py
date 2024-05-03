def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    for i in reserve:
        arr[i-1] += 1
    for i in lost:
        arr[i-1] -= 1
    for i in range(len(arr)):
        if arr[i] == 0:
            if i == 0:
                if arr[i+1] == 2:
                    arr[i+1] -= 1
                    answer += 1
            elif i == n-1:
                if arr[i-1] == 2:
                    arr[i-1] -= 1
                    answer += 1
            else:
                if arr[i-1] == 2:
                    arr[i-1] -= 1
                    answer += 1
                elif arr[i+1] == 2:
                    arr[i+1] -= 1
                    answer += 1
        else:
            answer += 1
    return answer
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
            continue
        else:
            if arr[i] != arr[i-1]:
                if answer[-1] != arr[i]:
                    answer.append(arr[i])
    return answer
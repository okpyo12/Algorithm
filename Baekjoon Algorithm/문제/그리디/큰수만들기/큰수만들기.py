def solution(number, k):
    answer = ''
    arr = []
    for i in number:
        if arr == []:
            arr.append(i)
        else:
            while True:
                if arr == []:
                    arr.append(i)
                    break
                if arr[-1] < i and k > 0:
                    del arr[-1]
                    k -= 1
                else:
                    arr.append(i)
                    break
    for i in range(k):
        del arr[-1]
    return ''.join(arr)
    
print(solution('333222111', 2))
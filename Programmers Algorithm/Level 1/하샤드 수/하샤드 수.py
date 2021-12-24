def solution(x):
    str_x = str(x)
    hasard = 0
    for i in range(len(str_x)):
        hasard += int(str_x[i])
    if x % hasard == 0:
        answer = True
    else:
        answer = False
    return answer
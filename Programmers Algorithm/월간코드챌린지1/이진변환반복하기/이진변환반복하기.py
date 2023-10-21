def solution(s):
    answer = []
    result = 0
    total = 0
    while len(s) > 1:
        result += 1
        cnt = 0
        for i in s:
            if i == '0':
                cnt += 1
                total += 1
        s = str(format(len(s)-cnt, 'b'))
    answer.append(result)
    answer.append(total)
    return answer
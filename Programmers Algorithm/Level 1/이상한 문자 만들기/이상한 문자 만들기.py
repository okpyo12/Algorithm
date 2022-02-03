def solution(s):
    answer = ""
    s = s.split(" ")
    for i in s:
        idx = 0
        for j in i:
            if idx % 2 == 0:
                answer += j.upper()
            else:
                answer += j.lower()
            idx += 1
        answer += " "
    return answer[:-1]
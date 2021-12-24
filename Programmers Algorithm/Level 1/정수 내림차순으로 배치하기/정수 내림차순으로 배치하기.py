def solution(n):
    answer = 0
    str_n = list(str(n))
    str_n.sort(reverse=True)
    answer = int("".join(str_n))
    return answer
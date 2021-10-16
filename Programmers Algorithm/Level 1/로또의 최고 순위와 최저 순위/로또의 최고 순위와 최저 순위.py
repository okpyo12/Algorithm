def solution(lottos, win_nums):
    answer = []
    rate = 7
    for i in lottos:
        if i == 0:
            rate -= 1
            continue
        for j in win_nums:
            if i == j:
                rate -= 1
                continue
    if rate == 7:
        rate = 6
    answer.append(rate)
    rate = 7
    for i in lottos:
        for j in win_nums:
            if i == j:
                rate -= 1
                continue
    if rate == 7:
        rate = 6
    answer.append(rate)
    return answer
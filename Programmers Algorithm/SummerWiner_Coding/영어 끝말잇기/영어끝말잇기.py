def solution(n, words):
    answer = []
    used = []
    last_word = words[0][0]
    idx = 1
    turn = 1
    for i in words:
        if i in used:
            answer.append(idx)
            answer.append(turn)
            break
        if i[0] != last_word:
            answer.append(idx)
            answer.append(turn)
            break
        if idx == n:
            idx = 1
            turn += 1
        else:
            idx += 1
        last_word = i[-1]
        used.append(i)
    if answer == []:
        return [0,0]
    return answer
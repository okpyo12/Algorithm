def solution(participant, completion):
    answer = ''
    result = 0
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)
    for i in range(len(sorted_completion)):
        if sorted_participant[i] != sorted_completion[i]:
            answer = sorted_participant[i]
            result += 1
            break

    if result == 0:
        answer = sorted_participant[-1]
    return answer

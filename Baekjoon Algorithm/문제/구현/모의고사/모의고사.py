def solution(answers):
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    dic = [['A',0], ['B',0], ['C',0]]
    
    for i in range(len(answers)):
        if answers[i] == A[i % 5]:
            dic[0][1] += 1
        if answers[i] == B[i % 8]:
            dic[1][1] += 1
        if answers[i] == C[i % 10]:
            dic[2][1] += 1
    dic.sort(key=lambda x: x[1])
    a = dic[-1][1]
    answer = []
    for i in dic:
        if i[1] == a:
            if i[0] == 'A':
                answer.append(1)
            elif i[0] == 'B':
                answer.append(2)
            else:
                answer.append(3)
    answer.sort()
    return answer
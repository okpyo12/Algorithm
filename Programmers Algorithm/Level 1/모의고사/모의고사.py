def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    cnt_a, cnt_b, cnt_c = 0,0,0
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            cnt_a += 1
        if answers[i] == b[i%8]:
            cnt_b += 1
        if answers[i] == c[i%10]:
            cnt_c += 1
    top = max(cnt_a, cnt_b, cnt_c)
    if top == cnt_a:
        answer.append(1)
    if top == cnt_b:
        answer.append(2)
    if top == cnt_c:
        answer.append(3)
    return answer

print(solution([1,3,2,4,2]))
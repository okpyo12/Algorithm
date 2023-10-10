from collections import deque

def solution(s):
    queue = deque(s)
    answer = 0
    for _ in range(len(queue)):
        if check(queue):
            answer += 1
        a = queue.popleft()
        queue.append(a)
        print(queue)
        print(answer)
    return answer

def check(queue):
    if len(queue) % 2 == 1:
        return 0
    arr = []
    for i in range(len(queue)):
        print(arr)
        if queue[i] == ']':
            if arr != []:
                if arr[-1] == '[':
                    arr.remove('[')
                    continue
                else:
                    return 0
        elif queue[i] == ')':
            if arr != []:
                if arr[-1] == '(':
                    arr.remove('(')
                    continue
                else:
                    return 0
        elif queue[i] == '}':
            if arr != []:
                if arr[-1] == '{':
                    arr.remove('{')
                    continue
                else:
                    return 0
        arr.append(queue[i])
    if arr != []:
        return 0
    return 1
    
print(solution("[](){}"))
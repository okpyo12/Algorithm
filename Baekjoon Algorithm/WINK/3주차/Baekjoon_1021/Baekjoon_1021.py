import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = deque(map(int, input().split()))
quearr = deque(i for i in range(1, N + 1))
answer = 0

for i in arr:
    cnt = 0
    for j in quearr:
        if i == j:
            break
        else:
            cnt += 1
    if cnt <= len(quearr) / 2:
        while True:
            temp = quearr.popleft()
            if i == temp:
                break
            quearr.append(temp)
            answer += 1
    else:
        while True:
            temp = quearr.pop()
            answer += 1
            if i == temp:
                break
            quearr.appendleft(temp)
print(answer)

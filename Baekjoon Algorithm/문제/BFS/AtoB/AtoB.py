import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

queue = deque()
queue.append((A,1))
r = 0

while queue:
    n, t = queue.popleft()
    if n > B:
        continue
    if n == B:
        print(t)
        break
    queue.append((n*2,t+1))
    queue.append((int(str(n)+"1"),t+1))
else:
    print(-1)
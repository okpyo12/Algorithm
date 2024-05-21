import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)

d = [-1]*(N+1)
d[X] = 0

queue = deque([X])

while queue:
    start = queue.popleft()

    for nx in arr[start]:
        if d[nx] == -1:
            d[nx] = d[start] + 1 
            queue.append(nx)

TorF = True

for i in range(1,N+1):
    if d[i] == K:
        print(i)
        TorF = False

if TorF:
    print(-1)
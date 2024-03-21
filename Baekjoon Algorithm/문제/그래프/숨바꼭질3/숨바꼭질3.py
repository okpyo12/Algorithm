import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 100000
dist = [0] * (MAX+1)

queue = deque([])
if N == 0:
    queue.append(1)
else:
    queue.append(N)

while queue:
    x = queue.popleft()
    if x == M:
        if N == 0:
            print(dist[x]+1)
            break
        else:
            print(dist[x])
            break
    for i in (x-1,x+1,x*2):
        if 0 <= i <= MAX and not dist[i]:
            if i != x*2:
                dist[i] = dist[x] + 1
                queue.append(i)
            else:
                dist[i] = dist[x]
                queue.appendleft(i)
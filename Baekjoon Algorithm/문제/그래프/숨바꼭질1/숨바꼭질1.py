import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 100000
dist = [0] * (MAX+1)

queue = deque([])
queue.append(N)

while queue:
    x = queue.popleft()
    if x == M:
        print(dist[x])
        break
    for i in (x-1,x+1,x*2):
        if 0 <= i <= MAX and not dist[i]:
            dist[i] = dist[x] + 1
            queue.append(i)
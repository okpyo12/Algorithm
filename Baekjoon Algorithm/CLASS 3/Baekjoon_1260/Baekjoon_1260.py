import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, sys.stdin.readline().split())
  graph[m1][m2] = graph[m2][m1] = 1

seen = [0] * (N+1)

def dfs(v):
    seen[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == 1 and seen[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    seen[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if graph[v][i]==1 and seen[i] == 0:
                queue.append(i)
                seen[i]=1

dfs(V)
seen = [0] * (N+1)
print()
bfs(V)
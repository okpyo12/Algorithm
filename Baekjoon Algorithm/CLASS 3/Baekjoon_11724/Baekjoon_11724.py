import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
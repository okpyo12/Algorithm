import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
T = int(input().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(x):
    queue = deque([1])

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    if sum(visited) == 0:
        return 0
    else:
        return sum(visited) - 1

print(bfs(1))
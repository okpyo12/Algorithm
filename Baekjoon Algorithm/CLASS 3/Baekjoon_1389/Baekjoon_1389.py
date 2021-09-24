import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    m1, m2 = map(int, sys.stdin.readline().split())
    graph[m1-1][m2-1] = 1
    graph[m2-1][m1-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif graph[i][k] and graph[k][j]:
                if graph[i][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 100000000
for i in range(N):
    sum = 0
    for j in range(N):
        sum += graph[i][j]
    if result > sum:
        result = sum
        p = i
print(p + 1)
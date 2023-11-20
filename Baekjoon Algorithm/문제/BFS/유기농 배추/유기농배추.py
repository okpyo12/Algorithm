import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    print(graph)
    
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1,-1,1,1,-2,-2,2,2]
dy = [-2,2,-2,2,-1,1,-1,1]

for i in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[-1]*l for _ in range(l)]
    graph[sx][sy] = 0

    queue = deque([])
    queue.append((sx,sy))

    TorF = False
    while queue:
        x, y = queue.popleft()
        cnt = graph[x][y]
        if x == ex and y == ey:
            print(cnt)
            break
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == -1:
                graph[nx][ny] = cnt + 1
                queue.append((nx,ny))
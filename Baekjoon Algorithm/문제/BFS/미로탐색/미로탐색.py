import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
vistied = [[0] * M for _ in range(N)]

vistied[0][0] = 1
dx, dy = [-1,1,0,0], [0,0,-1,1]
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if vistied[nx][ny] == 0 and graph[nx][ny] == '1':
                    vistied[nx][ny] = vistied[x][y] + 1
                    queue.append((nx, ny))
    return vistied[N-1][M-1]

print(bfs(0,0))
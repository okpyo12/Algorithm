import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
col, row = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y, c):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if c == "-":
                if graph[cx][ny] != 0 and graph[cx][ny] == c:
                    queue.append((cx,ny))
                    graph[cx][ny] = 0
            elif c == "|":
                if graph[nx][cy] != 0 and graph[nx][cy] == c:
                    queue.append((nx,cy))
                    graph[nx][cy] = 0
    return 1
        
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-':
            row += bfs(i,j,graph[i][j])
        elif graph[i][j] == '|':
            col += bfs(i,j,graph[i][j])
print(row + col)
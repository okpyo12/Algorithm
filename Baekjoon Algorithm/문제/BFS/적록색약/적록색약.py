import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
R_G_graph = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            R_G_graph[i][j] = 'R'
        else:
            R_G_graph[i][j] = graph[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
R_G_cnt = 0

def bfs(x, y):
    color = graph[x][y]
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 0 and graph[nx][ny] == color:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0
                    
    return color

def R_G_bfs(x, y):
    color = R_G_graph[x][y]
    queue = deque()
    queue.append([x,y])
    R_G_graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if R_G_graph[nx][ny] != 0 and R_G_graph[nx][ny] == color:
                    queue.append([nx, ny])
                    R_G_graph[nx][ny] = 0
                    
    return color

for i in range(N):
    for j in range(N):
        color = bfs(i,j)
        if color != 0:
            cnt += 1

print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        color = R_G_bfs(i,j)
        if color != 0:
            R_G_cnt += 1

print(R_G_cnt)
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    visited[x][y][0] = 1

    while queue:
        x, y, break_cnt = queue.popleft()

        if (x, y) == (N-1, M-1):
            return visited[x][y][break_cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and break_cnt == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                
                if arr[nx][ny] == 0 and visited[nx][ny][break_cnt] == 0:
                    visited[nx][ny][break_cnt] = visited[x][y][break_cnt] + 1
                    queue.append((nx, ny, break_cnt))
    return -1
    
print(bfs(0,0))
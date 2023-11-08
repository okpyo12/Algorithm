import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
arr = [[0]*M for _ in range(N)]
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = 1
dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    cnt = 0
    while queue:
        cx, cy = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx,ny))
                arr[nx][ny] = 0
    return cnt
        
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            tmp = bfs(i,j)
            result = tmp if tmp > result else result
print(result)
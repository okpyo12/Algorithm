import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
w,b = 0, 0

def bfs(x, y, c):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if arr[nx][ny] != 0 and arr[nx][ny] == c:
                queue.append((nx,ny))
                arr[nx][ny] = 0
    return cnt

for i in range(M):
    for j in range(N):
        if arr[i][j] != 0:
            if arr[i][j] == "W":
                w += (bfs(i,j, arr[i][j])**2)
            else:
                b += (bfs(i,j, arr[i][j]) ** 2)
print(w,b)
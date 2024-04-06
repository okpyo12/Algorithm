import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque(())
    queue.append((x,y))
    arr[x][y] = 1
    cnt = 0

    while queue:
        cnt += 1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = cnt
                    queue.append((nx, ny))
    return cnt

result = []
num = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            num += 1
            result.append(bfs(i,j))

result.sort()
print(num)
print(*result)

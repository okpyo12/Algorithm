import sys
from collections import deque
import copy

input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
result = 0
max_cnt = 0
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])

result = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result-1)
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    count = 0
    while queue:
        count += 1
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    return count
        
answer = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            answer = max(answer, bfs(i,j))
            cnt += 1

print(cnt)
print(answer)
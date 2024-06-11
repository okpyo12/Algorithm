import sys 
from collections import deque

input = sys.stdin.readline

L, W = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(L)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited = [[0] * W for _ in range(L)]
    visited[i][j]=1
    cnt=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=L or ny<0 or ny>=W:
                continue
            elif arr[nx][ny]=='L' and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                cnt=max(cnt,visited[nx][ny])
                queue.append((nx,ny))
    return cnt-1

result = 0
for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)
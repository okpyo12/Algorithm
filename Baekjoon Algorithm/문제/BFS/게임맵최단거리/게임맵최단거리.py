from collections import deque

def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            
            if x == n-1 and y == m-1:
                return maps[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == False:
                        queue.append((nx,ny))
                        maps[nx][ny] = maps[x][y] + 1
        return -1
    return bfs(0,0)
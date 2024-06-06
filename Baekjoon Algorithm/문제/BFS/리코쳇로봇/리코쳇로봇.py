from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(board):
    def bfs(x,y,N,M,visited):        
        queue = deque()
        queue.append((x,y))
        
        while queue:   
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x
                ny = y
                while True:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                
                    if 0 > nx or nx >= N or 0 > ny or ny >= M or board[nx][ny] == 'D':
                        nx = nx - dx[i]
                        ny = ny - dy[i]
                        break
                if visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
        return visited

    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                x, y = i, j
            if board[i][j] == 'G':
                target_x, target_y = i, j
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    arr = bfs(x,y,N,M,visited)
    for i in arr:
        print(i)
    if arr[target_x][target_y] == 0:
        return -1
    else:
        return arr[target_x][target_y]-1
    
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
#print(solution([".D.R", "....", ".G..", "...D"]))
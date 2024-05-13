from collections import deque

def solution(n, computers):    
    answer = 0
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False:
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = True
                    for k in range(n):
                        if visited[x][k] == False and computers[x][k] == 1:
                            visited[x][k] = True
                            queue.append([k,x])
                answer += 1
    return answer
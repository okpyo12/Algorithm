from collections import deque

def solution(land):
    answer = 0
    for i in range(len(land[0])):
        temp = copy(land)
        result = 0
        for j in range(len(land)):
            result += bfs(j,i,len(land), len(land[0]), temp)
        answer = max(answer, result)
    return answer

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def copy(land):
    temp = [[] for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[i])):
            temp[i].append(land[i][j])
    return temp

def bfs(x, y, N, M, land):
    queue = deque()
    queue.append((x,y))
    cnt = 0

    if land[x][y] == 1:
        land[x][y] = 0
        while queue:
            cnt += 1
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if land[nx][ny] == 1:
                        queue.append((nx,ny))
                        land[nx][ny] = 0
    return cnt
                    

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land))
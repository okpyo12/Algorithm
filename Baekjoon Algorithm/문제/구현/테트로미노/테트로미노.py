import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]
maxValue = 0

def dfs(i, j, dsum, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni,nj,dsum+arr[ni][nj], cnt + 1)
            visited[ni][nj] = False

def exce(i,j):
    global maxValue
    for n in range(4):
        temp = arr[i][j]
        for k in range(3):
            t = (n+k)%4
            ni = i + move[t][0]
            nj = j + move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                temp = 0
                break
            temp += arr[ni][nj]
        maxValue = max(maxValue, temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,arr[i][j], 1)
        visited[i][j] = False

        exce(i,j)

print(maxValue)
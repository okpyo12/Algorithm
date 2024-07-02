import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = 999999999

def dfs(start, now, value, cnt):
    global answer
    if cnt == N:
        if arr[now][start]:
            value += arr[now][start]
            answer = min(answer, value)
        return

    if value > answer:
        return
    
    for i in range(N):
        if not visited[i] and arr[now][i]:
            visited[i] = 1
            dfs(start, i, value + arr[now][i], cnt + 1)
            visited[i] = 0


for i in range(N):
    visited[i] = 1
    dfs(i,i,0,1)
    visited[i] = 0

print(answer)
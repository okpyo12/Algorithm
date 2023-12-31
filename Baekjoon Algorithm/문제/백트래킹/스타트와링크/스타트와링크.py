import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]
INF = 2147000000
result = INF

def dfs(L, idx):
    global result
    if L == N // 2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += arr[i][j]
        result = min(result, abs(power1 - power2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, idx+1)
            visited[i] = False

dfs(0,0)
print(result)
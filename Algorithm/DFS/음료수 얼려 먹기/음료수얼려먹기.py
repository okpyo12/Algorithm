import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    arr = input().rstrip()
    for j in arr:
        graph[i].append(int(j))

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)
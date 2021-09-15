import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

result = []
def bfs(j, k):
    if land[j][k] == 0:
        return True
    land[j][k] = 0

    bfs(j+1, k)
    bfs(j, k+1)
    bfs(j-1, k)
    bfs(j, k-1)
    
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = []
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr.append([X,Y])
    land = []
    for j in range(M+1):
        land.append([])
        for k in range(N+1):
            land[j].append(0)
    for j in arr:
        land[j[0]][j[1]] = 1
    cnt = 0
    for j in range(M):
        for k in range(N):
            if land[j][k] == 1:
                bfs(j, k)
                cnt += 1
    print(cnt)
                
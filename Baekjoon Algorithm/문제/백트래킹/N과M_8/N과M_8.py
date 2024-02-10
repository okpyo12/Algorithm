import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
q = []
def dfs(start):
    if len(q) == M:
        print(*q)
        return
    for i in range(start, N):
        q.append(arr[i])
        dfs(i)
        q.pop()

dfs(0)
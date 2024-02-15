import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []

def dfs():
    if len(temp) == M:
        print(*temp)
        return
    for i in range(N):
            temp.append(arr[i])
            dfs()
            temp.pop()

dfs()
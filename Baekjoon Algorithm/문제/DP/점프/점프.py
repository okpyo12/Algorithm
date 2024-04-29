import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if j + arr[i][j] < N:
            dp[i][j + arr[i][j]] += dp[i][j]

        if i + arr[i][j] < N:
            dp[i + arr[i][j]][j] += dp[i][j]
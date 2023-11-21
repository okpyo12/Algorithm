import sys

input = sys.stdin.readline

N = int(input())

dp = [99999999 for _ in range(N+5)]
dp[3] = dp[5] = 1

for i in range(6,N+1):
    dp[i] = min(dp[i-5] + 1, dp[i-3] + 1)

if dp[N] >= 99999999:
    print(-1)
else:
    print(dp[N])
import sys

input = sys.stdin.readline

T = int(input().rstrip())

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(T):
    n = int(input().rstrip())
    print(dp[n])
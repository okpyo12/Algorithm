import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [0 for _ in range(N + 1)]

dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[N])
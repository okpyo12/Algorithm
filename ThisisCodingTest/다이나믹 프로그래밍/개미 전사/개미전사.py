import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[N - 1])
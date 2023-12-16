import sys

input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

dp = [0] * N

if N > 1:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

    for i in range(2, N):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1], arr[i]+arr[i-1]+dp[i-3])

    print(max(dp))
else:
    print(arr[0])
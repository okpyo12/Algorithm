import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(len(arr)):
    dp[i] = arr[i]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
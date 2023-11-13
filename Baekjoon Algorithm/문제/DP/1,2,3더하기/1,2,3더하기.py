import sys

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    N = int(input().rstrip())
    dp = [1,2,4]
    if N <= 2:
        print(N)
        continue
    for j in range(3, N):
        dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3])
    print(dp[-1])
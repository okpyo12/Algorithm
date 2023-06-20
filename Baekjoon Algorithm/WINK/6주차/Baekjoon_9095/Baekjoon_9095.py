import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    num = input().rstrip()
    arr.append(int(num))

for i in arr:
    dp = [1, 2, 4]
    if i == 1:
        print(1)
        continue
    if i == 2:
        print(2)
        continue
    for j in range(3, i):
        dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3])
    print(dp[-1])

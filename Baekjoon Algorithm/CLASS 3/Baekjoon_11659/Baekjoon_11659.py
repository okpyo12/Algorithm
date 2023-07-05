import sys

input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))

pre_sum = [arr[0]]

for i in range(1, len(arr)):
    pre_sum.append(pre_sum[i-1] + arr[i])
pre_sum = [0] + pre_sum

for _ in range(M):
    a, b = map(int,input().split())
    print(pre_sum[b] - pre_sum[a-1])
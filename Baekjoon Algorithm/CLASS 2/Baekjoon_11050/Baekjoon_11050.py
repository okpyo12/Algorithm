import sys

N, K = map(int, sys.stdin.readline().split())
result = 1
for i in range(N, N-K, -1):
    result = result * i
for i in range(1, K+1):
    result = result//i
print(result)
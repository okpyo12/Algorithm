import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1):
    comb = combinations(arr, i)
    for j in comb:
        if S == sum(j):
            cnt += 1

print(cnt)
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

comb = combinations(arr, M)

for i in comb:
    print(*i)
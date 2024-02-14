import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

comb = combinations(arr, M)
for i in comb:
    print(*i)
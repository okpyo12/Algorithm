import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
comb = combinations(arr, 2)
result = []
for i in comb:
    if len(set(i)) != 1:
        result.append(i)

print(len(result))
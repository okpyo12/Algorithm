import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]

comb = permutations(arr, M)
for i in comb:
    print(*i)

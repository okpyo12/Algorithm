import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

perm = permutations(arr, M)

for i in perm:
    print(*i)
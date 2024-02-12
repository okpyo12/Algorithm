import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

arr = [i for i in range(1,N+1)]

perm = permutations(arr, N)
for i in perm:
    print(*i)
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

perm = permutations(A, len(A))
answer = 0
for i in perm:
    result = 0
    for j in range(len(i)-1):
        result += abs(i[j] - i[j+1])
    if answer < result:
        answer = result
print(answer)
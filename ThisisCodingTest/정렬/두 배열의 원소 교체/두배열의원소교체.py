import sys

input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

for i in range(K):
    if A[i] > B[-i]:
        continue
    else:
        A[i], B[-i] = B[-i], A[i]

print(sum(A))
import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for _ in range(N):
    a, b = input().split()
    arr.append([a,b])

arr = sorted(arr, key=lambda x: x[1])

for i in arr:
    print(i[0], end=' ')
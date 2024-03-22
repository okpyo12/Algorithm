import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
top = []
result = []

for i in range(N):
    while top:
        if top[-1][1] > arr[i]:
            result.append(top[-1][0] + 1)
            break
        else:
            top.pop()
    if not top:
        result.append(0)
    top.append([i, arr[i]])

print(*result)
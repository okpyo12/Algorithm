import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
print('<', end='')
idx = K-1
while arr:
    if (idx >= len(arr)):
        idx = 0
    if len(arr) == 1:
        print(arr[idx], end='')
    else:
        print(arr[idx], end=', ')
    del arr[idx]
    for i in range(K-1):
        if (idx >= len(arr)):
            idx = 0
        idx += 1
print('>')
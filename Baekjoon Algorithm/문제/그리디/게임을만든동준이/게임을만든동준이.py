import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

result = 0
level = 0
for i in range(N-1, -1, -1):
    if i == N-1:
        level = arr[N-1]
        continue
    else:
        if level > arr[i]:
            level = arr[i]
            continue
        else:
            level = level - 1
            result += arr[i] - level

print(result)
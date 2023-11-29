import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

num = 9999999999
result = [0] * (N)
idx = 0
for i in range(N):
    num = 9999999999
    for i in arr:
        if i <= num:
            num = i
    result[arr.index(num)] = idx
    idx += 1
    arr[arr.index(num)] = 9999999999

print(*result)

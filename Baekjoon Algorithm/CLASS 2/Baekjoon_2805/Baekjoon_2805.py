import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
low = 1
high = arr[-1]

while low <= high:
    result = 0
    mid = (low+high)//2
    for i in arr:
        if i > mid:
            result += i - mid

    if result >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)
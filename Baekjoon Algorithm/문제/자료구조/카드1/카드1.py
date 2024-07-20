import sys

input = sys.stdin.readline

N = int(input())
arr = [i for i in range(1,N+1)]

result = []

idx = 1
while True:
    if arr == []:
        break
    if idx % 2 == 1:
        result.append(arr[0])
        del arr[0]
    else:
        arr.append(arr[0])
        del arr[0]
    idx += 1

print(*result)
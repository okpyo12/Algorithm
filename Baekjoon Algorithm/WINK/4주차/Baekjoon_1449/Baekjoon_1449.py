import sys

input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(arr)

answer = 0

while arr:
    if len(arr) == 1:
        answer += 1
        break
    if arr[0] - 0.5 + L >= arr[1] + 0.5:
        del arr[1]
    else:
        answer += 1
        del arr[0]

print(answer)

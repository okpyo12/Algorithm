import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while left <= right and right <= N:
    if sum(arr[left:right]) == M:
        cnt += 1
        right += 1
    elif sum(arr[left:right]) > M:
        left += 1
    elif sum(arr[left:right]) < M:
        right += 1

print(cnt)
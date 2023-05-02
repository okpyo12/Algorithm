import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
temp = list(0 for _ in range(N))
idx = 1

for i in arr:
    cnt = 0
    for j in range(N):
        if cnt >= i:
            if temp[j] == 0:
                temp[j] = idx
                idx += 1
                break
        if temp[j] == 0:
            cnt += 1

for i in temp:
    print(i, end=" ")

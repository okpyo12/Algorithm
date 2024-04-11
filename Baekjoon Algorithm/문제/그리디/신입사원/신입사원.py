import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        paper, face = map(int, input().split())
        arr.append([paper,face])
    cnt = 0
    arr.sort()
    temp = 99999999
    for i in arr:
        if temp > i[1]:
            cnt += 1
            temp = i[1]
    print(cnt)
    
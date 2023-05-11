import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
answer = []

for _ in range(N):
    M, P = map(int, input().split())
    cnt = 1
    arr = deque(map(int, input().split()))
    while arr != deque([]):
        check = 0
        for j in range(len(arr)):
            if arr[0] < arr[j]:
                temp = arr.popleft()
                arr.append(temp)
                check = 1
                if P == 0:
                    P = len(arr) - 1
                else:
                    P = P - 1
                break
        if check == 0:
            if P == 0:
                answer.append(cnt)
                break
            arr.popleft()
            cnt = cnt + 1
            P = P - 1

for i in answer:
    print(i)
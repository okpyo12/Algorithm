import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [i for i in range(2,N+1)]

cnt = 0
TorF = 0
answer = 0
while True:
    prime = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            prime = arr[i]
            break
    for i in range(len(arr)):
        if cnt == K:
            TorF = 1
            break
        if arr[i] % prime == 0:
            answer = arr[i]
            arr[i] = -1
            cnt += 1
    if TorF == 1:
        break

print(answer)
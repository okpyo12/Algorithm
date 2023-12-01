import sys

input = sys.stdin.readline

N, L = map(int, input().split())

result = []
for i in range(L, 101):
    mid = N // i
    if i % 2 == 0:
        for j in range(1, i // 2):
            if mid-j >= 0:
                result.append(mid-j)
            else:
                continue
        result.append(mid)
        for j in range(1, i // 2 + 1):
            result.append(mid+j)
        if len(result) >= L:
            if sum(result) == N:
                break
            else:
                result = []
        else:
            result = []
    else:
        for j in range(1, i // 2 + 1):
            if mid-j >= 0:
                result.append(mid-j)
            else:
                continue
        result.append(mid)
        for j in range(1, i // 2 + 1):
            result.append(mid+j)
        if len(result) >= L:
            if sum(result) == N:
                break
            else:
                result = []
        else:
            result = []

result.sort()
if result == []:
    print(-1)
else:
    print(*result)

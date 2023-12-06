import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
min_num = min(N, M)
result = 0
for i in range(min_num, -1, -1):
    if result != 0:
        break
    for j in range(N):
        for k in range(M):
            if j+i < N and k+i < M:
                num = arr[j][k]
                if arr[j][k+i] == num and arr[j+i][k] == num and arr[j+i][k+i] == num:
                    result = (i+1)*(i+1)
print(result)
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dpu = [1 for _ in range(N)]
dpd = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        # print(i, j)
        if arr[i] > arr[j]:
            dpu[i] = max(dpu[i], dpu[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dpd[i] = max(dpd[i], dpd[j]+1)

result = []
for i in range(N):
    result.append(dpu[i]+dpd[i])

print(max(result)-1)
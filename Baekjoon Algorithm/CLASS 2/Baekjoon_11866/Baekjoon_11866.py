import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
result = []
for i in range(1, N+1):
    arr.append(i)
cnt = 0
while cnt < N:
    for i in range(K-1):
        arr.append(arr[0])
        del arr[0]
    result.append(arr[0])
    del arr[0]
    cnt += 1

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>')
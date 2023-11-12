import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, len(arr)):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])

print(max(arr[-1]))
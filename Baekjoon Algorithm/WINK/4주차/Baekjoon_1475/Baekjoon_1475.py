import sys

input = sys.stdin.readline

N = input().rstrip()

answer = 0
arr = [0 for _ in range(10)]

for i in N:
    arr[int(i)] += 1

total = 0
total += arr[6] + arr[9]
del arr[6]
del arr[8]

if total % 2 == 0:
    total = total // 2
else:
    total = total // 2 + 1
arr.append(total)

print(max(arr))

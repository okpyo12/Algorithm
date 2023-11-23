import sys

input = sys.stdin.readline

N = int(input().rstrip())

stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in range(len(stick)):
    if N >= stick[i]:
        cnt += 1
        N -= stick[i]
    if N == 0:
        break

print(cnt)
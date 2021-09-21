import sys

num = {str(i) for i in range(10)}
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M != 0:
        num -= set(map(str, input().split()))

min_cnt = abs(100 - N)
for i in range(1000001):
        i = str(i)
        for j in range(len(i)):
            if i[j] not in num:
                break
            elif j == len(i) - 1:
                min_cnt = min(min_cnt, abs(N - int(i)) + len(str(i)))
print(min_cnt)
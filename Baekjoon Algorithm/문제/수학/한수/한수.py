import sys

input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for i in range(N, 0, -1):
    num = 0
    if i < 10:
        cnt += 1
    else:
        gap = int(str(i)[0]) - int(str(i)[1])
        for j in range(len(str(i))-1):
            if int(str(i)[j]) - gap == int(str(i)[j+1]):
                num += 1
        if num == len(str(i)) - 1:
            cnt += 1
print(cnt)
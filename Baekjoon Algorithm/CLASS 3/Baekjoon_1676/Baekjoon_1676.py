import sys

N = int(sys.stdin.readline())

num  = 1
for i in range(1,N+1):
    num *= i

idx = -1
cnt = 0
for i in range(len(str(num))):
    if str(num)[idx] == '0':
        idx -= 1
        cnt += 1
    else:
        break
print(cnt)
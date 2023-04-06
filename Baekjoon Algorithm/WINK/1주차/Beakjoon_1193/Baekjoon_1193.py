import sys

input = sys.stdin.readline

N = int(input())
cnt = N
idx = 1

for i in range(1, N):
    cnt -= i
    if (cnt <= 0):
        cnt += i
        break
    idx += 1

if(idx % 2 ==0):
    print(str(cnt) + "/" + str(idx-cnt+1))
else:
    print(str(idx-cnt+1) + "/" + str(cnt))
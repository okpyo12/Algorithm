import sys

input = sys.stdin.readline

S = input().rstrip()

reuslt = 0
for i in S:
    i = int(i)
    if i == 0 or i == 1 or reuslt == 0 or reuslt == 1:
        reuslt += i
    else:
        reuslt = reuslt * i

print(reuslt)
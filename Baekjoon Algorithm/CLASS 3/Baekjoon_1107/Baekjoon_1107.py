import sys

N = str(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(str, sys.stdin.readline().split()))

num = ['0','1','2','3','4','5','6','7','8','9']
channel = 100
cnt = 0
for i in range(len(num)-len(arr)):
    for j in range(len(arr)):
        if num[i] == arr[j]:
            del num[i]

a = ''
for i in N:
    if i in num:
        cnt += 1
        a += i
    else:
        temp = []
        for j in num:
            temp.append()
        for j in range(len(temp)):

            temp[j] = temp[j] - i
        a += max(temp)
print(cnt)
import sys

N, M, B = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

time, height = 999999999999999, 0
for i in range(257):
    require, remain = 0, 0
    for j in arr:
        for k in j:
            if k > i:
                remain += k - i
            else:
                require += i - k

    if require > remain + B:
        continue

    if time >= remain * 2 + require:
        time = remain * 2 + require
        height = i

print(time, height)

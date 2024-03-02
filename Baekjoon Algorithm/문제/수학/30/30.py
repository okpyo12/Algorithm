import sys

input = sys.stdin.readline

N = input().rstrip()

if '0' in N:
    temp = list(map(int, N))
    if sum(temp) % 3 == 0:
        temp.sort(reverse=True)
        temp = list(map(str, temp))
        print(''.join(temp))
    else:
        print(-1)
else:
    print(-1)
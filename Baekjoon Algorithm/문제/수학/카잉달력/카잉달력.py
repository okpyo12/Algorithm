import sys

input = sys.stdin.readline

T = int(input())

def cal(N,M,x,y):
    while x <= N*M:
        if (x-y) % M == 0:
            return x
        x += N
    return -1

for i in range(T):
    N, M, x, y = map(int, input().split())
    print(cal(N,M,x,y))
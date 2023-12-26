import sys

input = sys.stdin.readline

N = int(input())

def top(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        top(N-1, a, c, b) 
        print(a, c)
        top(N-1, b, a, c)

print(2 ** N - 1)
top(N, 1, 2, 3)
import sys

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = []
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr.append([X,Y])
    print(arr)
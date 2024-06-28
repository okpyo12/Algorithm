import sys

input = sys.stdin.readline

N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

dic = {}

for i in range(N):
    dic[N_arr[i]] = 0

for i in M_arr:
    if i not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')
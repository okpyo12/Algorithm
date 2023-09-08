import sys

input = sys.stdin.readline

N = input().rstrip()
arr = list(map(int, input().split()))
M = input().rstrip()
num = list(map(int, input().split()))

for i in num:
    if i in arr:
        print("yes", end=' ')
    else:
        print("no", end=' ')
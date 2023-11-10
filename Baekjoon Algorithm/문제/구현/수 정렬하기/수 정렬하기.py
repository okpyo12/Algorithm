from re import I
import sys

N = int(sys.stdin.readline())

list = []
for _ in range(N):
    list.append(int(sys.stdin.readline().rstrip()))
list.sort()
for i in list:
    print(i)
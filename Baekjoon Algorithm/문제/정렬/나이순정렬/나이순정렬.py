import sys

input = sys.stdin.readline

N = int(input())
arr = []
idx = 0
for i in range(N):
    age, name = input().split()
    arr.append([int(age), name, idx])
    idx += 1

arr.sort(key = lambda x : (x[0],x[2]))

for i in arr:
    del i[-1]
    print(*i)
import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

def round45(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]

arr.sort()
rank = round45(n*0.15)
if n == 0:
    print(0)
else:
    print(round45(sum(arr[rank:n-rank])/len(arr[rank:n-rank])))
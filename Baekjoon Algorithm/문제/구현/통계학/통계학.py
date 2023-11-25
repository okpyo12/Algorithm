import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input().rstrip()))

arr.sort()
print(int(round(sum(arr)/N, 0)))
print(arr[len(arr)//2])

k = Counter(arr).most_common()
if len(k) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(arr[0])
print(arr[-1]-arr[0])
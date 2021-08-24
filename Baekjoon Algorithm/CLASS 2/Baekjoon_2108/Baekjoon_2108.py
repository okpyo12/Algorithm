import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(round(sum(arr)/N))

print(arr[N//2])

k = Counter(arr).most_common()
if len(k) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(arr[0])

print(arr[-1]-arr[0])
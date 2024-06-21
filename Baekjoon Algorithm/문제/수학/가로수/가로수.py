import sys
from math import gcd

input = sys.stdin.readline

N = int(input())

temp = [int(input()) for _ in range(N)]
arr = []

for i in range(1,len(temp)):
    arr.append(temp[i] - temp[i-1])

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

result = 0
for each in arr:
    result += each // g - 1
print(result)
import sys

input = sys.stdin.readline

N = int(input())
E = list(map(int, input().split()))
V = list(map(int, input().split()))

temp = 9999999999
result = 0

for i in range(len(E)):
    if temp > V[i]:
        temp = V[i]
    result += temp * E[i]

print(result)
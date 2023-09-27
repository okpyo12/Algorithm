import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
total = 0
for i in data:
    total += i
    if total >= N:
        total = 0
        result += 1

print(result)
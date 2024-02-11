import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    rope = int(input())
    arr.append(rope)

arr.sort()

result = 0
for i in range(len(arr)):
    result = max(result,arr[i]*(N-i))

print(result)
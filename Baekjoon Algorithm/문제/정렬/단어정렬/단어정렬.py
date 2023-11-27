import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = list(set(input().rstrip() for _ in range(N)))

arr = sorted(arr)
answer = sorted(arr, key=lambda x: len(x))

for i in answer:
    print(i)
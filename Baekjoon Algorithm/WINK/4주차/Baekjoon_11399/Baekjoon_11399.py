import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
answer = [0]

for i in range(N):
    answer.append(arr[i] + answer[i])

print(sum(answer))

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort(reverse=True)

result = 0
for i in arr:
    if K >= i:
        result += K // i
        K = K % i
    if K == 0:
        break

print(result)
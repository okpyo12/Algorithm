N = int(input())

arr = []
result = 0
arr += list(map(int, input()))
for i in range(N):
    result += int(arr[i])

print(result)
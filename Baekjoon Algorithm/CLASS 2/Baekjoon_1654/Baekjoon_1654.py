K, N = map(int, input().split())

arr = []

for i in range(K):
    num = int(input())
    arr.append(num)

arr.sort()
low = 1
high = max(arr)
result = 0
while low <= high:
    mid = (low+high)//2
    sum_num = 0
    for i in arr:
        sum_num += i//mid
    if sum_num < N:
        high = mid - 1
    elif sum_num >= N:
        low = mid + 1
        result = mid
    else:
        continue
print(result)
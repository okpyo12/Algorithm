import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()

def binary(arr):
    start = 0
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(N):
            if arr[i] >= mid:
                cnt += mid
            else:
                cnt += arr[i]
        
        if cnt <= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary(arr))
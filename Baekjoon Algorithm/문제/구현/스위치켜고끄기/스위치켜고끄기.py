import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def switch(num):
    if num == 0:
        return 1
    else:
        return 0
    
for i in range(M):
    gender, num = map(int, input().split())
    num -= 1
    if gender == 1:
        for j in range(num, len(arr), num+1):
            arr[j] = switch(arr[j])
    else:
        arr[num] = switch(arr[num])
        num_low = num
        num_high = num
        while True:
            num_low = num_low - 1
            num_high = num_high + 1
            if num_low < 0 or num_high >= len(arr):
                break
            if arr[num_low] == arr[num_high]:
                arr[num_low] = switch(arr[num_low])
                arr[num_high] = switch(arr[num_high])
            else:
                break

idx = 0 
for i in range(len(arr)):
    if idx == 19:
        print(arr[i])
        idx = 0
    else:
        if i == len(arr)-1:
            print(arr[i])
        else:
            print(arr[i], end=' ')
        idx += 1
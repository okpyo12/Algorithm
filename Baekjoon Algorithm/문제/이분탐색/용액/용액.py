import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()

left_idx = 0
right_idx = N - 1

ans = abs(arr[left_idx] + arr[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:
    tmp = arr[left_idx] + arr[right_idx]

    if abs(tmp) < ans:
        ans_left, ans_right = left_idx, right_idx
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(arr[ans_left], arr[ans_right])
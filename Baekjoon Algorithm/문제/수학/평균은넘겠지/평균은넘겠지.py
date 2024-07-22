import sys

input = sys.stdin.readline

C = int(input())

for i in range(C):
    arr = list(map(int, input().split()))
    cnt = 0
    avg = sum(arr[1:]) // arr[0]
    for j in arr[1:]:
        if j > avg:
            cnt += 1
    print(round(cnt/arr[0]*100, 3), end='')
    print('%')
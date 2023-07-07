import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr_sort = sorted(list(set(arr)))

dic = {arr_sort[i]: i for i in range(len(arr_sort))}

for co in arr:
    print(dic[co], end=' ')
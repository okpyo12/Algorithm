import sys

input = sys.stdin.readline

N = int(input())

arr = [input().rstrip() for i in range(N)]

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr.sort(key=lambda x : (len(x), sum_num(x), x))
for i in arr:
    print(i)
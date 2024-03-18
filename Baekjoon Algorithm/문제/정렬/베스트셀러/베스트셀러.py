import sys

input = sys.stdin.readline

N = int(input())

dic = {}
for i in range(N):
    book = input().rstrip()
    if book in dic:
        dic[book] = dic[book] + 1
    else:
        dic[book] = 1
arr = []
for i in dic:
    arr.append([i, dic[i]])
arr.sort()
arr.sort(key=lambda x: x[1], reverse=True)
print(arr[0][0])
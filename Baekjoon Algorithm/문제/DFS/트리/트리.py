import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
CN = int(input())

def dfs(del_node):
    arr[del_node] = -10
    for i in range(N):
        if del_node == arr[i]:
            dfs(i)
dfs(CN)
cnt = 0
for i in range(N):
    if arr[i] != -10 and i not in arr:
        cnt += 1
 
print(cnt)
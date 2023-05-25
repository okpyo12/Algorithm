import sys

input = sys.stdin.readline

N = int(input())
arr = []
dic = {}
visited = []

idx = 0
for i in range(int(N)):
    for j in range(int(N)):
        dic[idx] = set()
        idx += 1


def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


for _ in range(N):
    arr.append(list(map(int, input().rstrip())))

idx = -1
for i in range(N):
    for j in range(N):
        idx += 1
        if arr[i][j] == 1:
            if i == N - 1:
                if j != N - 1:
                    if arr[i][j + 1] == 1:
                        dic[idx].add(idx + 1)
                        dic[idx + 1].add(idx)
            elif j == N - 1:
                if arr[i + 1][j] == 1:
                    dic[idx].add(idx + N)
                    dic[idx + N].add(idx)
            else:
                if arr[i][j + 1] == 1:
                    dic[idx].add(idx + 1)
                    dic[idx + 1].add(idx)
                if arr[i + 1][j] == 1:
                    dic[idx].add(idx + N)
                    dic[idx + N].add(idx)

idx = -1
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        idx += 1
        if arr[i][j] == 1:
            if idx not in visited:
                a = len(visited)
                dfs(idx, dic)
                b = len(visited)
                if b - a == 0:
                    result.append(1)
                else:
                    result.append(b - a)
                cnt += 1

print(cnt)
result.sort()
for i in result:
    print(i)

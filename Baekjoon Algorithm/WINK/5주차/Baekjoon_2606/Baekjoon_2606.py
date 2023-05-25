import sys

input = sys.stdin.readline

N = input()
T = input()
dic = {}
visited = []

for i in range(int(N)):
    dic[i + 1] = set()

for _ in range(int(T)):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)


def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


dfs(1, dic)
print(len(visited) - 1)

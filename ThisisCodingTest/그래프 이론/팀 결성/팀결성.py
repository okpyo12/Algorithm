import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [0] * (N + 1)

for i in range(N+1):
    graph[i] = i

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

for i in range(M):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(graph, a, b)
    else:
        if find(graph, a) == find(graph, b):
            print("YES")
        else:
            print("NO")
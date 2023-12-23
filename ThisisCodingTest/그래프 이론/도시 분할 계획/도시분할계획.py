import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())

graph = []
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()
result = 0
last = 0

for edge in graph:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        print(a, b)
        union(parent, a, b)
        result += cost
        last = cost

print(result - last)
import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
s, e = map(int, input().split())
dp = [INF] * (N+1)
heap = []

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = w + wei

            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei, next_node))

Dijkstra(s)

print(dp[e])
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

result = []
dic = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    dic[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0
 
    visited = [False] * (N + 1)
    visited[start] = True
 
    while q:
        cur = q.popleft()
        for next in dic[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt
 
result = []
for start in range(1, len(dic)):
    result.append(bfs(start))
answer = []
for i in range(len(result)):
    if max(result) == result[i]:
        answer.append(i+1)

print(*answer)
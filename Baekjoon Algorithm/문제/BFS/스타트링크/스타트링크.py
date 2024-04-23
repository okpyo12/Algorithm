import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
arr = [0 for _ in range(F)]
arr[S-1] = 1

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        ux = x + U
        dx = x - D

        if 0 <= ux < F and arr[ux] == 0:
            arr[ux] = arr[x] + 1
            queue.append(ux)
        if 0 <= dx < F and arr[dx] == 0:
            arr[dx] = arr[x] + 1
            queue.append(dx)

bfs(S-1)
if arr[G-1] == 0:
    print('use the stairs')
else:
    print(arr[G-1]-1)
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
L = int(input())
turn = []
for i in range(L):
    X, C = input().split()
    turn.append([int(X),C])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
nd, hx, hy = 0, 0, 0
cnt, i = 0, 0
queue = deque()
queue.append((0,0))

while True:
    hx = hx + dx[nd]
    hy = hy + dy[nd]
    cnt += 1

    if hx < 0 or hx >= N or hy < 0 or hy >= N or (hx, hy) in queue:
        break
    queue.append((hx,hy))
    if arr[hx][hy] == 0:
        queue.popleft()
    else:
        arr[hx][hy] = 0
    if cnt == turn[i][0]:
        if turn[i][1] == 'L':
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4
        if i + 1 < len(turn):
            i += 1

print(cnt)
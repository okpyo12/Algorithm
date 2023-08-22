import sys

input = sys.stdin.readline

N = int(input())
contents = list(input().split())
x, y = 1, 1
move_types = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for content in contents:
    for i in range(len(move_types)):
        if content == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)
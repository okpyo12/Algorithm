import sys

input = sys.stdin.readline

data = input().rstrip()
x, y = int(data[1]), int(ord(data[0])) - int(ord('a')) + 1

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [-1,1,-1,1,-2,2,-2,2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)

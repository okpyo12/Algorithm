import sys

input = sys.stdin.readline

R, C = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]
answer = 0
alphabet = set()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not arr[nx][ny] in alphabet:
            alphabet.add(arr[nx][ny])
            dfs(nx, ny, count+1)
            alphabet.remove(arr[nx][ny])
alphabet.add(arr[0][0])

dfs(0,0,1)
print(answer)
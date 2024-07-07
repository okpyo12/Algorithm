import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr_be = [list(map(int,list(input().strip()))) for _ in range(N)]
arr_aft = [list(map(int,list(input().strip()))) for _ in range(N)]

def flip(x,y):
    for i in range(3):
        for j in range(3):
            arr_be[x+i][y+j] = 1 - arr_be[x+i][y+j]

if arr_be == arr_aft:
    print(0)
    exit()

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if arr_be[i][j] != arr_aft[i][j]:
            flip(i,j)
            cnt += 1
        if arr_be == arr_aft:
            print(cnt)
            exit()

print(-1)
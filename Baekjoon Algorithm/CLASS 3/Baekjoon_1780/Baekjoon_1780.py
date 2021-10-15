import sys

N = int(sys.stdin.readline())

a = 0
b = 0
c = 0
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def div(x, y, n):
    global a, b, c

    num_check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y, y+n):
            if(arr[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        div(x + k * n//3, y + l * n//3, n//3)
                return
    if num_check == -1:
        a += 1
    elif num_check == 0:
        b += 1
    else:
        c += 1

div(0,0,N)
print(a)
print(b)
print(c)
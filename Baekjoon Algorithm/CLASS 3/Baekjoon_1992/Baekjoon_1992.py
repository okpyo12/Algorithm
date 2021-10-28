import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def quard(x, y, n):
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        quard(x, y, n)  # 오른쪽 위
        quard(x, y + n, n)  # 왼쪽 위
        quard(x + n, y, n)  # 오른쪽 아래
        quard(x + n, y + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

quard(0, 0, N)
import sys

N, r, c = map(int, sys.stdin.readline().split())

cnt = 0

def Z(size, row, col):
    global cnt
    if row == r and col == c:
        print(int(cnt))
        sys.exit(0)

    if size == 0:
        cnt += 1
        return True
    
    if not (row <= r < row + size and col <= c < col + size):
        cnt += size**2
        return
    Z(size / 2, row, col)
    Z(size / 2, row, col + size / 2)
    Z(size / 2, row + size / 2, col)
    Z(size / 2, row + size / 2, col + size / 2)
Z(2**N, 0, 0)
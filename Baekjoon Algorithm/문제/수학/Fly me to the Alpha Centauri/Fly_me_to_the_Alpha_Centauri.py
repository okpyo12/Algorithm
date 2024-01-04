import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    idx = 0
    distance = y - x
    move = 1
    result = 0
    while distance > result:
        idx += 1
        result += move
        if idx % 2 == 0:
            move += 1  
    print(idx)
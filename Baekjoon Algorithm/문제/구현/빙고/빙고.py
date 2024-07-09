import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    answer += list(map(int, input().split()))

def check():
    bingo = 0
    for x in arr: 
        if x.count(0) == 5:
            bingo += 1

    for i in range(5): 
        y = 0
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        
        if y == 5:
            bingo += 1

    d1 = 0
    for i in range(5):
        if arr[i][i] == 0:
            d1 += 1
    
    if d1 == 5:
        bingo += 1

    d2 = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            d2 += 1
    
    if d2 == 5:
        bingo += 1

    return bingo 


cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if answer[i] == arr[x][y]:
                arr[x][y] = 0
                cnt += 1

    if cnt >= 12:
        result = check()
        if result >= 3:
            print(i+1)
            break
import sys

input = sys.stdin.readline

N = int(input())

answer = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True
    

def N_Queen(x):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                N_Queen(x+1)

N_Queen(0)
print(answer)
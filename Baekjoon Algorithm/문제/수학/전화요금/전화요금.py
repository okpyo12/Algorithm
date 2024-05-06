import sys

input = sys.stdin.readline

N = int(input())
result = 0
for i in range(N):
    start, time = input().split()

    H, M = map(int, start.split(':'))
    
    for i in range(int(time)):
        if 7 <= H < 19:
            result += 10
        else:
            result += 5
        M += 1
        if M == 60:
            H += 1
            M = 0
        if H == 24:
            H = 0

print(result)
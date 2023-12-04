import sys
import math

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    arr = []
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input().rstrip())
    for j in range(N):
        cx, cy, r = list(map(int, input().split()))
        arr.append([cx, cy, r])
    num = 0
    for j in arr:
        if j[2] > math.sqrt((j[0]-x1)**2 + (j[1]-y1)**2) and j[2] < math.sqrt((j[0]-x2)**2 + (j[1]-y2)**2):
            num += 1
        if j[2] < math.sqrt((j[0]-x1)**2 + (j[1]-y1)**2) and j[2] > math.sqrt((j[0]-x2)**2 + (j[1]-y2)**2):
            num += 1
    print(num)
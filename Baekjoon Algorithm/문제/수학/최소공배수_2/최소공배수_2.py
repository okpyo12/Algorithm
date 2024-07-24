import sys
import math

input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A,B))
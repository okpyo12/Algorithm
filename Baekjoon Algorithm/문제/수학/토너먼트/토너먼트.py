import sys

input = sys.stdin.readline

N, kim, lim = map(int, input().split())

r = 0
while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    r += 1

print(r)
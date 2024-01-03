import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())
words = list(input().split())
words.sort()

comb = combinations(words, L)

for i in comb:
    cnt = 0
    if 'a' in i:
        cnt += 1
    if 'e' in i:
        cnt += 1
    if 'i' in i:
        cnt += 1
    if 'o' in i:
        cnt += 1
    if 'u' in i:
        cnt += 1
    if L - cnt >= 2:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
            print(''.join(i))
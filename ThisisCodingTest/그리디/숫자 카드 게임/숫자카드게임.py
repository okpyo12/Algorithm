import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(N)]
result = 0
for card in cards:
    card.sort()
    result = max(result,card[0])
print(result)
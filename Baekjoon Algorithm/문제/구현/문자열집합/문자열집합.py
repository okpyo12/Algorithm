import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = []
for i in range(N):
    word = input().rstrip()
    S.append(word)

cnt = 0
for i in range(M):
    check = input().rstrip()
    if check in S:
        cnt += 1

print(cnt)
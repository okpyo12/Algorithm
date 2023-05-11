import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
answer = []

for _ in range(N):
    check = 0
    word = input().rstrip()
    arr = deque()
    for i in word:
        if i == "(":
            arr.append("(")
        else:
            if arr == deque([]):
                answer.append("NO")
                check = 1
                break
            else:
                arr.pop()
    if check == 0:
        if arr == deque([]):
            answer.append("YES")
        else:
            answer.append("NO")

for i in answer:
    print(i)

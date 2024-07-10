import sys

input = sys.stdin.readline

n = int(input())

answer = set()

for i in range(n):
    name, inout = input().split()
    if inout == 'enter':
        answer.add(name)
    else:
        answer.remove(name)

answer = list(answer)
answer.sort(reverse=True)

for i in answer:
    print(i)
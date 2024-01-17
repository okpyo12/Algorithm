import sys
from collections import deque

input = sys.stdin.readline

stick = input().rstrip()

queue = deque([])
sum = 0
before = ''
for i in stick:
    if i == ')':
        x = queue.pop()
        if before == ')':
            sum += 1
            continue
        if x == '(':
            sum += len(queue)
    else:
        queue.append(i)
    before = i

print(sum)
from collections import deque

N = int(input())

arr = []
deq = deque()
for i in range(N, 0, -1):
    deq.append(i)

while len(deq) > 1:
    deq.pop()
    deq.appendleft(deq[-1])
    deq.pop()

print(deq[0])
import sys
from collections import deque

input = sys.stdin.readline

N = input().rstrip()
name = []
dic = {}
left = deque()
right = deque()

for i in range(len(N)):
    name.append(N[i])
name.sort()
name_set = set(name)
TorF = 0
temp = []

for i in name_set:
    dic[i] = N.count(i)
    if dic[i] % 2 == 1:
        temp.append(i)
        name.remove(i)
        TorF += 1

if TorF >= 2:
    print("I'm Sorry Hansoo")
else:
    for i in range(len(name)):
        if i % 2 == 0:
            left.append(name[i])
        else:
            right.appendleft(name[i])
    if temp != []:
        left.append(temp[0])
    for j in right:
        left.append(j)

    print(''.join(left))
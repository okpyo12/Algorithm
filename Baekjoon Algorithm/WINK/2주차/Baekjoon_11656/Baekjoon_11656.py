import sys

input = sys.stdin.readline

word = input().rstrip()

temp = []
for i in range(len(word)):
    temp.append(word[i:])

temp = sorted(temp)

for i in temp:
    print(i)

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
idx = 1
for i in arr:
    if i == idx:
        idx += 1
    else:
        stack.append(i)
    while stack != [] and stack[-1] == idx:
        idx += 1
        stack.pop()

for i in range(len(stack)-1, -1, -1):
    if stack[i] == idx:
        idx += 1
    else:
        print("Sad")
        exit()
print("Nice")
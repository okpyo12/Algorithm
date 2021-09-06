import sys
K = int(input())

stack = []
for i in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))
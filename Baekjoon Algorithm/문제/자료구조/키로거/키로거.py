import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    L = input().rstrip()
    stack_left = []
    stack_right = []
    for j in L:
        if j == "<":
            if stack_left:
                stack_right.append(stack_left.pop())
        elif j == ">":
            if stack_right:
                stack_left.append(stack_right.pop())
        elif j == "-":
            if stack_left:
                stack_left.pop()
        else:
            stack_left.append(j)
    stack_left.extend(reversed(stack_right))
    print("".join(stack_left))
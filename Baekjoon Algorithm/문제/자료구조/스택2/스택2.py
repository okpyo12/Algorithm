import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    op = list(map(int, input().split()))
    if len(op) >= 2:
        stack.append(op[1])
    else:
        if op[0] == 2:
            if stack != []:
                print(stack[-1])
                del stack[-1]
            else:
                print(-1)
        elif op[0] == 3:
            print(len(stack))
        elif op[0] == 4:
            if stack != []:
                print(0)
            else:
                print(1)
        elif op[0] == 5:
            if stack != []:
                print(stack[-1])
            else:
                print(-1)
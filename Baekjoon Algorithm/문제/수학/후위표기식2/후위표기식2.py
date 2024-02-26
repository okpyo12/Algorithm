import sys

input = sys.stdin.readline

N = int(input())
arr = input().rstrip()
val = []
op = []
for i in range(N):
    a = int(input())
    val.append(a)
stack = []
for i in arr:
    if i == '*':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2*num1)
    elif i == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2+num1)
    elif i == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2-num1)
    elif i == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2/num1)
    else:
        stack.append(val[ord(i)-ord('A')])

print('%.2f' %stack[0])
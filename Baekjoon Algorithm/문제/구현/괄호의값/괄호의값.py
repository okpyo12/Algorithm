import sys

input = sys.stdin.readline

S = list(input().rstrip())
arr = []
total = 1
result = 0
for i in range(len(S)):
    if S[i] == '(':
        arr.append(S[i])
        total *= 2
    elif S[i] == '[':
        arr.append(i)
        total *= 3
    elif S[i] == ')':
        if not arr or arr[-1] == "[":
            result = 0
            break
        if S[i-1] == "(":
            result += total
        arr.pop()
        total //= 2
    elif S[i] == ']':
        if not arr or arr[-1] == "(":
            result = 0
            break
        if S[i-1] == "[":
            result += total
        arr.pop()
        total //= 3

if arr:
    print(0)
else:
    print(result)
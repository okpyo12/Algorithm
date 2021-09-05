T = int(input())

result = []
for _ in range(T):
    a = input()
    stack = []
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)
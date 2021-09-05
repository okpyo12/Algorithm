a = ''
result = []
while True:
    stack = []
    arr = []
    a = input()
    if a == '.':
        break
    for i in a:
        arr.append(i)
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
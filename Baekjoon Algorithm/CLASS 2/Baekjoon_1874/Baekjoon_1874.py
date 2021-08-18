n = int(input())

arr = []
stack = []
result = []
index = 0
possible = True
for i in range(n):
    a = int(input())
    arr.append(a)

for i in range(n):
    while index < arr[i]:
        index += 1
        stack.append(index)
        result.append('+')

    top = stack[-1]
    if top == arr[i]:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible == False:
    print('NO')
else:
    for i in result:
        print(i)
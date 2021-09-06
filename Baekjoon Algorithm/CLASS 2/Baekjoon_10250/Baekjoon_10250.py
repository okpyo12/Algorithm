T = int(input())

result = []
for i in range(T):
    H, W, N = map(int, input().split())

    a = N // H
    b = N % H
    if b == 0:
        b = H
        a -= 1
    if a > 8:
        result.append(str(b) + str(a+1))
    else:
        result.append(str(b) + '0' + str(a+1))

for i in result:
    print(i)
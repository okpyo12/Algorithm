N = int(input())
cnt = 1

for i in range(N, 0, -1):
    for j in range(i, 1, -1):
        print(" ", end='')
    for k in range(cnt):
        print('*', end='')
    cnt += 1
    print()
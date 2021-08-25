N = int(input())

reuslt = 0
for i in range(1, N+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if (s == N):
        reuslt = i
        break

print(reuslt)
T = int(input())

result = []
for _ in range(T):
    k = int(input())
    n = int(input())
    arr = []
    for i in range(k+1):
        num = 0
        arr2 = []
        for j in range(n+1):
            if i == 0:
                arr2.append(j)
            else:
                num += arr[i-1][j]
                arr2.append(num)
        arr.append(arr2)
    result.append(arr[-1][-1])

for i in range(T):
    print(result[i])
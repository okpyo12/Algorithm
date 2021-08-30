N, M = map(int, input().split())
arr = list(map(int, input().split()))

reuslt = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a = arr[i]+arr[j]+arr[k]
            if a > M:
                continue
            else:
                reuslt.append(a)

reuslt.sort()
print(reuslt[-1])
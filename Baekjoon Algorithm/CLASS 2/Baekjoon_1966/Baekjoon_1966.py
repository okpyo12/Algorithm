T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    idx = []
    cnt = 1
    for i in range(N):
        idx.append(i)
    idx[M] = 'target'
    while len(arr) != 0:
        if arr[0] == max(arr):
            result.append(arr[0])
            del arr[0]
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                cnt += 1
                del idx[0]
        else:
            arr.append(arr[0])
            del arr[0]
            idx.append(idx[0])
            del idx[0]
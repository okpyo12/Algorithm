T = int(input())

arr = []
result = 0
result_list = []
for i in range(T):
    arr.append(input())
    cnt = 0
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            result += 1
            if j >= 1:
                if arr[i][j-1] == 'O':
                    cnt += 1
                    result += cnt
                else:
                    cnt = 0
            else:
                continue
        else:
            cnt = 0
            continue
    result_list.append(result)
    result = 0

for i in range(T):
    print(result_list[i])
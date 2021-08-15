arr = []
while True:
    a = input()
    if a == '0':
        break
    else:
        arr.append(a)

for i in range(len(arr)):
    if int(len(arr[i])) % 2 == 1:
        temp = []
        cnt = len(arr[i])//2-1
        palindrome = True
        for j in range(len(arr[i])//2):
            temp.append(arr[i][j])
        for j in range(len(arr[i])//2+1, len(arr[i]), 1):
            if temp[cnt] == arr[i][j]:
                cnt += -1
                continue
            else:
                cnt += -1
                palindrome = False
        if palindrome == True:
            print('yes')
        else:
            print('no')
    else:
        temp = []
        cnt = len(arr[i])//2-1
        palindrome = True
        for j in range(len(arr[i]) // 2):
            temp.append(arr[i][j])
        for j in range(len(arr[i]) // 2, len(arr[i]), 1):
            if temp[cnt] == arr[i][j]:
                cnt += -1
                continue
            else:
                cnt += -1
                palindrome = False
        if palindrome == True:
            print('yes')
        else:
            print('no')
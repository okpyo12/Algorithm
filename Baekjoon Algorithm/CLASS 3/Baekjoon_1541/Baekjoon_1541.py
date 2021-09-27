import sys

a = sys.stdin.readline()

idx1 = 0
idx2 = 0
arr_num = []
arr_giho = []
for i in a:
    if i == '-' or i == '+':
        arr_giho.append(i)
        arr_num.append(a[idx1:idx2])
        idx1 = idx2+1
    idx2 += 1
arr_num.append(a[idx1:-1])

num = int(arr_num[0])
giho = '+'
for i in range(len(arr_giho)):
    if arr_giho[i] == '-':
        num -= int(arr_num[i+1])
        giho = '-'
    else:
        if giho == '+':
            num += int(arr_num[i+1])
        else:
            num -= int(arr_num[i+1])
print(num)
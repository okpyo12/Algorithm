import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    p = input().rstrip()
    n = int(input())
    ac = list(input().rstrip())
    if n == 0:
        if 'D' in p:
            print('error')
            continue
        else:
            print('[]')
            continue
    del ac[0]
    del ac[-1]
    temp = ''.join(ac)
    arr = list(map(int, temp.split(',')))
    TorF = 1
    flag = 0
    for j in range(len(p)):
        if p[j] == 'R':
            flag += 1
        if p[j] == 'D':
            if arr == []:
                TorF = 0
                break
            if arr[0] == '':
                TorF = 0
                del arr[0]
                break
            if len(p) != 0:
                if flag % 2 == 0:
                    del arr[0]
                else:
                    del arr[-1]
            else:
                TorF = 0
                break
    if TorF:
        if flag % 2 == 1:
            arr.reverse()
        if len(arr) == 0:
            print('[]')
        else:
            print('[',end='')
            for j in range(len(arr)-1):
                print(arr[j], end=',')
            print(arr[-1],end='')
            print(']')
    else:
        print('error')
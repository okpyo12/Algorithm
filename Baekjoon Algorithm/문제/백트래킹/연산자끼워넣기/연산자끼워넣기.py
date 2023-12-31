import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operator_num = list(map(int, input().split()))
operator = []

for i in range(4):
    if i == 0:
        for j in range(operator_num[i]):
            operator.append('+')
    elif i == 1:
        for j in range(operator_num[i]):
            operator.append('-')
    elif i == 2:
        for j in range(operator_num[i]):
            operator.append('*')
    elif i == 3:
        for j in range(operator_num[i]):
            operator.append('/')

result = []
permut = permutations(operator, N-1)

for i in permut:
    idx = 1
    total = arr[0]
    for j in i:
        if j == '+':
            total += arr[idx]
        if j == '-':
            total -= arr[idx]
        if j == '*':
            total *= arr[idx]
        if j == '/':
            if total < 0:
                total = -(-total // arr[idx])
            else:
                total //= arr[idx]
        idx += 1
    result.append(total)

result.sort()
print(result[-1])
print(result[0])
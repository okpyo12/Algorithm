import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(1, len(arr)):
    gcd_i = gcd(arr[0], arr[i])
    print(int(arr[0]/gcd_i), end='')
    print('/', end='')
    print(int(arr[i]/gcd_i))
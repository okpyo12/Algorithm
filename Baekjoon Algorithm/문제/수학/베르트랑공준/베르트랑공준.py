import sys
import math

input = sys.stdin.readline

arr = []
while True:
    num = int(input().rstrip())
    if num == 0:
        break
    arr.append(num)

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1
    
for i in arr:
    result = 0
    for j in range(i+1, i*2+1):
        result += isPrime(j)
    print(result)
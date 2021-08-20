import math

def isPrime(num):
    if num == 1: return False
    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0: return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i): print(i)
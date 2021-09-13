import sys

T = int(sys.stdin.readline())

zero = [1,0,1]
one = [0,1,1]

def fibonacci(num):
    if len(zero) <= num:
        for i in range(len(zero), num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num],one[num])

for i in range(T):
    N = int(sys.stdin.readline())
    fibonacci(N)